"""SEC EDGAR: ticker map, submissions, company facts. Filings are the source of truth."""

from __future__ import annotations

import json
import math
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

from ..http import HttpError
from ..periods import Window, parse_date
from ..schema import (
    ALLOWED_TAXONOMIES,
    CORE_CONCEPTS,
    fill_row,
    merge_entity,
    pad_cik,
    statement_for,
)
from .base import HttpClient

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
FILING_URL = "https://www.sec.gov/Archives/edgar/data/{cik_int}/{accn_nodash}/{primary}"

KEEP_FORMS = {
    "10-K",
    "10-K/A",
    "10-Q",
    "10-Q/A",
    "8-K",
    "8-K/A",
    "20-F",
    "20-F/A",
    "6-K",
    "6-K/A",
    "40-F",
    "40-F/A",
    "11-K",
    "DEF 14A",
    "S-1",
    "S-3",
}


def _cache_path() -> Path:
    return Path(__file__).resolve().parents[2] / ".cache" / "company_tickers.json"


def load_ticker_map(
    client: HttpClient, cache_path: Optional[Path] = None, max_age_hours: int = 24
) -> dict[str, str]:
    path = cache_path or _cache_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        age_hours = (datetime.now(timezone.utc).timestamp() - path.stat().st_mtime) / 3600
        if age_hours < max_age_hours:
            payload = json.loads(path.read_text(encoding="utf-8"))
            return _index_tickers(payload)
    payload = client.get_json(TICKER_MAP_URL)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return _index_tickers(payload)


def _index_tickers(payload: dict[str, Any]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in payload.values():
        ticker = str(row.get("ticker", "")).upper()
        cik = pad_cik(row.get("cik_str"))
        if ticker and cik:
            mapping[ticker] = cik
    return mapping


def resolve_cik(entity: dict[str, str], ticker_map: dict[str, str]) -> str:
    if entity.get("cik"):
        return pad_cik(entity["cik"])
    ticker = (entity.get("ticker") or "").upper()
    return ticker_map.get(ticker, "")


def _inclusion(filed: Optional[date], period_end: Optional[date], window: Window) -> Optional[str]:
    if filed is None or filed > window.cutoff or (period_end and period_end > window.cutoff):
        return None
    if window.contains(filed):
        return "filed_in_window"
    if window.contains(period_end):
        return "period_in_window"
    return None


def duration_kind(start: Optional[date], end: date) -> str:
    if start is None:
        return "instant"
    days = (end - start).days + 1
    for lower, upper, label in ((75, 105, "quarter"), (150, 200, "half_year_ytd"), (240, 290, "nine_month_ytd"), (350, 380, "annual")):
        if lower <= days <= upper:
            return label
    return "other_duration"


def flatten_companyfacts(
    payload: dict[str, Any],
    entity: dict[str, str],
    window: Window,
    *,
    core_only: bool = True,
) -> list[dict[str, str]]:
    facts_root = payload.get("facts") or {}
    window_rows: list[dict[str, str]] = []
    latest_by_key = {}
    invalid_count = 0
    entity_cik = pad_cik(payload.get("cik") or entity.get("cik"))
    entity_name = str(payload.get("entityName") or entity.get("entity_name") or "")

    for taxonomy, concepts in facts_root.items():
        if taxonomy not in ALLOWED_TAXONOMIES:
            continue
        if not isinstance(concepts, dict):
            continue
        for concept, body in concepts.items():
            if core_only and concept not in CORE_CONCEPTS.get(taxonomy, {}):
                continue
            units = (body or {}).get("units") or {}
            label = (body or {}).get("label") or concept
            for unit, observations in units.items():
                for obs in observations or []:
                    filed = parse_date(obs.get("filed"))
                    period_end = parse_date(obs.get("end"))
                    period_start = parse_date(obs.get("start"))
                    try:
                        valid_number = not isinstance(obs.get("val"), bool) and math.isfinite(float(obs.get("val")))
                    except (TypeError, ValueError, OverflowError):
                        valid_number = False
                    if not filed or not period_end or (obs.get("start") and not period_start) or (period_start and period_start > period_end) or not valid_number:
                        invalid_count += 1
                        continue
                    if filed > window.cutoff or period_end > window.cutoff:
                        continue
                    row = fill_row(
                        {
                            "as_of_date": window.as_of_iso,
                            "window_start": window.start_iso,
                            "window_end": window.end_iso,
                            "grain": window.grain,
                            "record_kind": "fact",
                            "entity_name": entity_name,
                            "entity_type": entity.get("entity_type") or "stock",
                            "ticker": entity.get("ticker", ""),
                            "isin": entity.get("isin", ""),
                            "cik": entity_cik,
                            "source": "edgar",
                            "source_url": FACTS_URL.format(cik=entity_cik),
                            "accession": obs.get("accn") or "",
                            "form": obs.get("form") or "",
                            "filed_at": filed.isoformat() if filed else "",
                            "period_start": period_start.isoformat() if period_start else "",
                            "period_end": period_end.isoformat() if period_end else "",
                            "fiscal_year": obs.get("fy") if obs.get("fy") not in (None, "") else "",
                            "fiscal_period": obs.get("fp") or "",
                            "statement": statement_for(taxonomy, concept) or "",
                            "concept": concept,
                            "concept_local": label,
                            "taxonomy": taxonomy,
                            "value": obs.get("val"),
                            "unit": unit,
                            "currency": unit if isinstance(unit, str) and unit.isalpha() and len(unit) == 3 else "",
                            "notes": obs.get("frame") or "",
                        }
                    )
                    merge_entity(row, entity)
                    reason = _inclusion(filed, period_end, window)
                    if reason:
                        row["inclusion_reason"] = reason
                        window_rows.append(row)
                    if filed <= window.cutoff:
                        key = (taxonomy, concept, unit, duration_kind(period_start, period_end))
                        rank = (period_end, period_start or date.min, filed)
                        previous = latest_by_key.get(key)
                        if previous is None or rank >= previous[0]:
                            asof = dict(row)
                            asof["inclusion_reason"] = "asof_latest"
                            tied = previous[1] if previous and rank == previous[0] else []
                            latest_by_key[key] = (rank, tied + [asof])

    present = {(r["taxonomy"], r["concept"], r["unit"], duration_kind(parse_date(r["period_start"]), parse_date(r["period_end"]))) for r in window_rows}
    asof_rows = [
        row
        for key, (_, values) in latest_by_key.items()
        if key not in present
        for row in values
    ]
    if invalid_count:
        window_rows.append(_error_row(entity, window, f"Skipped {invalid_count} malformed companyfacts observations (dates or numeric values); inspect source JSON"))
    return window_rows + asof_rows


def flatten_submissions(
    payload: dict[str, Any],
    entity: dict[str, str],
    window: Window,
    *,
    include_latest: bool = False,
) -> list[dict[str, str]]:
    cik = pad_cik(payload.get("cik") or entity.get("cik"))
    name = str(payload.get("name") or entity.get("entity_name") or "")
    tickers = payload.get("tickers") or []
    ticker = entity.get("ticker") or (tickers[0] if tickers else "")
    recent = (payload.get("filings") or {}).get("recent") or {}
    forms = recent.get("form") or []
    rows: list[dict[str, str]] = []
    latest = {}

    def _col(key: str, index: int) -> str:
        values = recent.get(key) or []
        if index < len(values) and values[index] is not None:
            return str(values[index])
        return ""

    for index in range(len(forms)):
        form = _col("form", index)
        if KEEP_FORMS and form not in KEEP_FORMS:
            continue
        filed = parse_date(_col("filingDate", index))
        report = parse_date(_col("reportDate", index))
        if not filed or filed > window.cutoff or (report and report > window.cutoff):
            continue
        reason = _inclusion(filed, report, window)
        accession = _col("accessionNumber", index)
        primary = _col("primaryDocument", index)
        accn_nodash = accession.replace("-", "")
        cik_int = str(int(cik)) if cik else ""
        source_url = ""
        if cik_int and accn_nodash and primary:
            source_url = FILING_URL.format(
                cik_int=cik_int, accn_nodash=accn_nodash, primary=primary
            )
        row = fill_row(
                {
                    "as_of_date": window.as_of_iso,
                    "window_start": window.start_iso,
                    "window_end": window.end_iso,
                    "grain": window.grain,
                    "record_kind": "filing",
                    "inclusion_reason": reason or "asof_latest",
                    "entity_name": name,
                    "entity_type": entity.get("entity_type") or "stock",
                    "ticker": ticker,
                    "isin": entity.get("isin", ""),
                    "cik": cik,
                    "source": "edgar",
                    "source_url": source_url,
                    "accession": accession,
                    "form": form,
                    "filed_at": filed.isoformat() if filed else "",
                    "period_end": report.isoformat() if report else "",
                    "concept": "filing",
                    "concept_local": _col("primaryDocDescription", index) or form,
                    "notes": _col("fileNumber", index),
                }
        )
        if reason:
            rows.append(row)
        if form in {"10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A", "40-F", "40-F/A"}:
            rank = (report or date.min, filed)
            if form not in latest or rank > latest[form][0]:
                latest[form] = (rank, row)
    if include_latest:
        present = {r["accession"] for r in rows}
        rows.extend(r for _, r in latest.values() if r["accession"] not in present)
    return rows


def _error_row(entity: dict[str, str], window: Window, notes: str) -> dict[str, str]:
    row = fill_row(
        {
            "as_of_date": window.as_of_iso,
            "window_start": window.start_iso,
            "window_end": window.end_iso,
            "grain": window.grain,
            "record_kind": "error",
            "inclusion_reason": "adapter_error",
            "source": "edgar",
            "concept": "http_error",
            "notes": notes,
        }
    )
    merge_entity(row, entity)
    return row


class EdgarAdapter:
    name = "edgar"

    def __init__(
        self,
        client: HttpClient,
        ticker_map: Optional[dict[str, str]] = None,
        core_only: bool = True,
    ):
        self.client = client
        self._ticker_map = ticker_map
        self.core_only = core_only

    def _map(self) -> dict[str, str]:
        if self._ticker_map is None:
            self._ticker_map = load_ticker_map(self.client)
        return self._ticker_map

    def collect(self, entity: dict[str, str], window: Window) -> list[dict[str, str]]:
        try:
            cik = pad_cik(entity.get("cik")) or resolve_cik(entity, self._map())
        except (HttpError, OSError, ValueError) as exc:
            return [_error_row(entity, window, f"Ticker resolution failed: {exc}")]
        if not cik:
            row = fill_row(
                {
                    "as_of_date": window.as_of_iso,
                    "window_start": window.start_iso,
                    "window_end": window.end_iso,
                    "grain": window.grain,
                    "record_kind": "error",
                    "inclusion_reason": "adapter_error",
                    "source": "edgar",
                    "concept": "unresolved_cik",
                    "notes": f"no CIK for ticker {entity.get('ticker')!r}",
                }
            )
            merge_entity(row, entity)
            return [row]
        entity = dict(entity)
        entity["cik"] = cik
        entity["entity_type"] = entity.get("entity_type") or "stock"
        rows: list[dict[str, str]] = []
        try:
            submissions = self.client.get_json(SUBMISSIONS_URL.format(cik=cik))
            recent = (submissions.get("filings") or {}).get("recent") or {}
            merged = {k: list(v) for k, v in recent.items() if isinstance(v, list)}
            # Include prior annual/interim context around a narrow historical window.
            history_floor = min(window.start, window.cutoff - timedelta(days=550))
            for entry in (submissions.get("filings") or {}).get("files", []):
                start = parse_date(entry.get("filingFrom"))
                end = parse_date(entry.get("filingTo"))
                if (start and start > window.cutoff) or (end and end < history_floor):
                    continue
                name = entry.get("name", "")
                if not re.fullmatch(r"CIK\d{10}-submissions-\d+\.json", name):
                    rows.append(_error_row(entity, window, f"Unsupported submissions history filename: {name}"))
                    continue
                try:
                    old = self.client.get_json("https://data.sec.gov/submissions/" + name)
                    count = len(old.get("form", []))
                    prior_count = len(merged.get("form", []))
                    for key in set(merged) | set(old):
                        merged[key] = merged.get(key, [""] * prior_count) + list(old.get(key, [""] * count))
                except (HttpError, ValueError, TypeError) as exc:
                    rows.append(_error_row(entity, window, f"Historical submissions {name}: {exc}"))
            combined = {**submissions, "filings": {"recent": merged}}
            rows.extend(flatten_submissions(combined, entity, window, include_latest=True))
        except HttpError as exc:
            rows.append(_error_row(entity, window, str(exc)))
        try:
            facts = self.client.get_json(FACTS_URL.format(cik=cik))
            rows.extend(
                flatten_companyfacts(facts, entity, window, core_only=self.core_only)
            )
        except HttpError as exc:
            rows.append(_error_row(entity, window, str(exc)))
        for row in rows:
            merge_entity(row, entity)
        return rows
