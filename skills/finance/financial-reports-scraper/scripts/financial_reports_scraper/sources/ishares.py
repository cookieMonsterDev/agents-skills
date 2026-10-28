"""iShares / BlackRock issuer literature: product page, documents, holdings CSV."""

from __future__ import annotations

import csv
import io
import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from ..http import HttpError
from ..periods import Window, parse_date
from ..schema import fill_row, merge_entity
from .base import HttpClient

PRODUCT_URL = "https://www.ishares.com/uk/individual/en/products/{product_id}"
MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}

DOC_KINDS = (
    ("annual report", "annual_report"),
    ("semi-annual", "semiannual_report"),
    ("interim report", "interim_report"),
    ("factsheet", "factsheet"),
    ("fact sheet", "factsheet"),
    ("kiid", "kiid"),
    ("kid", "priips_kid"),
    ("prospectus", "prospectus"),
    ("reportable income", "reportable_income"),
)

FACT_CONCEPTS = {
    "net assets of share class": ("fund_metric", "net_assets_share_class"),
    "net assets of fund": ("fund_metric", "net_assets_fund"),
    "net assets": ("fund_metric", "net_assets"),
    "total expense ratio": ("fund_metric", "ter"),
    "shares outstanding": ("fund_metric", "shares_outstanding"),
    "isin": ("fund_metric", "isin"),
    "base currency": ("fund_metric", "base_currency"),
    "share class currency": ("fund_metric", "share_class_currency"),
    "use of income": ("fund_metric", "use_of_income"),
    "domicile": ("fund_metric", "domicile"),
    "benchmark index": ("fund_metric", "benchmark"),
    "number of holdings": ("fund_metric", "holdings_count"),
    "p/e ratio": ("fund_metric", "pe_ratio"),
    "p/b ratio": ("fund_metric", "pb_ratio"),
    "fiscal year end": ("fund_metric", "fiscal_year_end"),
    "tonnes in trust": ("fund_metric", "tonnes_in_trust"),
    "ounces in trust": ("fund_metric", "ounces_in_trust"),
    "daily metal entitlement per security": ("fund_metric", "metal_entitlement_per_security"),
    "ucits": ("fund_metric", "ucits"),
    "issuing company": ("fund_metric", "issuing_company"),
}


def load_catalog(path: Optional[Path] = None) -> dict[str, Any]:
    catalog_path = path or Path(__file__).resolve().parents[2] / "data" / "ishares_catalog.json"
    if not catalog_path.exists():
        return {}
    payload = json.loads(catalog_path.read_text(encoding="utf-8"))
    return {str(isin).upper(): meta for isin, meta in payload.items()}


def parse_ishares_date(text: str) -> Optional[date]:
    if not text:
        return None
    iso = parse_date(text)
    if iso:
        return iso
    iso_match = re.search(r"\b\d{4}-\d{2}-\d{2}\b", text)
    if iso_match:
        return parse_date(iso_match.group())
    match = re.search(
        r"(\d{1,2})[\/\-\s]+([A-Za-z]{3,9})[\/\-\s]+(\d{4})",
        text,
    )
    if match:
        day = int(match.group(1))
        month = MONTHS.get(match.group(2).lower())
        year = int(match.group(3))
        if month:
            try:
                return date(year, month, day)
            except ValueError:
                return None
    match = re.search(r"(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{4})", text)
    if match:
        day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
        try:
            return date(year, month, day)
        except ValueError:
            return None
    return None


def _as_of_in(text: str) -> Optional[date]:
    match = re.search(r"as of\s+(.+)$", text, re.I)
    if not match:
        return None
    return parse_ishares_date(match.group(1))


def _split_value(raw: str) -> tuple[str, str, str]:
    text = re.sub(r"\s+", " ", raw or "").strip()
    if not text:
        return "", "", ""
    if text.endswith("%"):
        number = text[:-1].replace(",", "").strip()
        return number, "percent", ""
    currency = ""
    match = re.match(r"^(USD|EUR|GBP|CHF|JPY|CAD|AUD)\s+(.*)$", text)
    if match:
        currency = match.group(1)
        text = match.group(2)
    number = text.replace(",", "")
    return text if not re.match(r"^-?\d+(\.\d+)?$", number) else number, currency or "", currency


def _doc_kind(label: str) -> str:
    lower = label.lower()
    for needle, kind in DOC_KINDS:
        if needle in lower:
            return kind
    if lower.endswith(".pdf") or "pdf" in lower:
        return "literature"
    return "literature"


def _year_from_label(label: str) -> str:
    match = re.search(r"(20\d{2})", label)
    return match.group(1) if match else ""


def parse_product_html(
    html: str,
    entity: dict[str, str],
    window: Window,
    page_url: str,
) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    rows: list[dict[str, str]] = []

    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            cells = [
                re.sub(r"\s+", " ", td.get_text(" ", strip=True))
                for td in tr.find_all(["th", "td"])
            ]
            if len(cells) != 2:
                continue
            label, raw_value = cells[0], cells[1]
            if not label or not raw_value:
                continue
            if label.lower() in {"type", "exchange"} and raw_value.lower() in {"fund", "ticker"}:
                continue
            key = re.sub(r"\s+", " ", re.sub(r"more info:?", "", label, flags=re.I)).strip().lower()
            key = re.sub(r"\s+as of .+$", "", key, flags=re.I).strip()
            mapped = FACT_CONCEPTS.get(key)
            if mapped is None and "holdings" in key and "%" in raw_value:
                mapped = ("segment", f"sector_weight_{re.sub(r'[^a-z0-9]+', '_', key)}")
            if mapped is None and cells[0].lower() in {
                "financials",
                "industrials",
                "health care",
                "information technology",
                "consumer staples",
                "consumer discretionary",
                "materials",
                "energy",
                "utilities",
                "communication",
                "consumer staples",
            }:
                mapped = ("segment", f"sector_weight_{cells[0].lower().replace(' ', '_')}")
            if mapped is None:
                # Sector table: first cell is sector name, second is weight.
                if raw_value.endswith("%") and cells[0][0].isalpha() and len(cells) == 2:
                    mapped = ("segment", f"sector_weight_{re.sub(r'[^a-z0-9]+', '_', cells[0].lower())}")
                else:
                    continue
            statement, concept = mapped
            as_of = _as_of_in(label) or _as_of_in(raw_value)
            value_text = re.sub(r"\s+as of\s+.+$", "", raw_value, flags=re.I).strip()
            value, unit, currency = _split_value(value_text)
            if concept == "isin":
                value = raw_value.strip().upper()
                unit, currency = "", ""
            reason = "listed"
            if as_of:
                reason = (
                    "period_in_window"
                    if window.contains(as_of)
                    else ("asof_latest" if as_of <= window.cutoff else "listed")
                )
                if as_of > window.cutoff:
                    continue
            rows.append(
                _row(
                    entity,
                    window,
                    record_kind="fact",
                    inclusion_reason=reason,
                    source_url=page_url,
                    form="product_page",
                    filed_at="",
                    period_end=as_of.isoformat() if as_of else "",
                    statement=statement,
                    concept=concept,
                    concept_local=label,
                    value=value,
                    unit=unit or ("percent" if raw_value.endswith("%") else ""),
                    currency=currency,
                    notes=raw_value + "; publication_date_unknown; product-page observation only",
                )
            )

    for anchor in soup.find_all("a"):
        href = (anchor.get("href") or "").strip()
        label = re.sub(r"\s+", " ", anchor.get_text(" ", strip=True))
        if not href:
            continue
        lower = href.lower()
        abs_url = urljoin(page_url, href)
        if "datatype=fund" in lower or "filetype=csv" in lower:
            continue
        if not (lower.endswith(".pdf") or "literature" in lower or "gls-download" in lower):
            if "annual report" not in label.lower() and "factsheet" not in label.lower() and "kiid" not in label.lower():
                continue
        kind = _doc_kind(label or Path(urlparse(abs_url).path).name)
        year = _year_from_label(label)
        doc_date = parse_ishares_date(label)
        if doc_date and doc_date > window.cutoff:
            continue
        in_window = window.contains(doc_date) if doc_date else False
        rows.append(
            _row(
                entity,
                window,
                record_kind="document",
                inclusion_reason="period_in_window" if in_window else ("asof_latest" if doc_date else "listed"),
                source_url=abs_url,
                form=kind,
                filed_at="",
                period_end=doc_date.isoformat() if doc_date else "",
                fiscal_year=year,
                statement="document",
                concept=kind,
                concept_local=label or kind,
                notes=abs_url + "; publication_date_unknown; label year is not a publication date",
            )
        )
    return rows


def parse_holdings_csv(
    text: str,
    entity: dict[str, str],
    window: Window,
    source_url: str,
) -> list[dict[str, str]]:
    # iShares holdings files often start with title rows before the header.
    lines = text.splitlines()
    header_index = None
    for index, line in enumerate(lines[:30]):
        lower = line.lower()
        if "isin" in lower and ("weight" in lower or "ticker" in lower or "name" in lower):
            header_index = index
            break
    if header_index is None:
        raise ValueError("No recognized holdings CSV header in first 30 lines")
    blob = "\n".join(lines[header_index:])
    reader = csv.DictReader(io.StringIO(blob))
    rows: list[dict[str, str]] = []
    as_of = None
    for line in lines[: header_index + 1]:
        found = parse_ishares_date(line)
        if found:
            as_of = found
    if as_of and as_of > window.cutoff:
        return [_row(entity, window, record_kind="error", inclusion_reason="adapter_error", source_url=source_url,
                     concept="holdings_after_cutoff", notes=f"Holdings dated {as_of} are after cutoff {window.cutoff}; historical snapshot needed")]
    for item in reader:
        name = _first(item, "Name", "Issuer Name", "Security Name")
        ticker = _first(item, "Issuer Ticker", "Ticker")
        isin = _first(item, "ISIN")
        weight = _first(item, "Weight (%)", "Weight", "Weight(%)")
        if not name and not isin:
            continue
        rows.append(
            _row(
                entity,
                window,
                record_kind="holding",
                inclusion_reason="listed" if as_of is None else (
                    "period_in_window" if window.contains(as_of) else "asof_latest"
                ),
                source_url=source_url,
                form="holdings",
                filed_at="",
                period_end=as_of.isoformat() if as_of else "",
                statement="holdings",
                concept="weight_percent",
                concept_local=name or isin,
                taxonomy="ishares",
                value=weight.replace("%", "").replace(",", "").strip(),
                unit="percent",
                notes=f"holding_ticker={ticker};holding_isin={isin};publication_date_unknown",
            )
        )
    return rows


def _first(row: dict[str, str], *names: str) -> str:
    lookup = {re.sub(r"\s+", " ", (key or "")).strip().lower(): value for key, value in row.items()}
    for name in names:
        value = lookup.get(name.lower())
        if value:
            return str(value).strip()
    return ""


def _row(entity: dict[str, str], window: Window, **values: Any) -> dict[str, str]:
    payload = {
        "as_of_date": window.as_of_iso,
        "window_start": window.start_iso,
        "window_end": window.end_iso,
        "grain": window.grain,
        "source": "ishares",
        "taxonomy": "ishares",
        "entity_name": entity.get("entity_name", ""),
        "entity_type": entity.get("entity_type", ""),
        "ticker": entity.get("ticker", ""),
        "isin": entity.get("isin", ""),
    }
    payload.update(values)
    row = fill_row(payload)
    merge_entity(row, entity)
    return row


def holdings_urls_from_html(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    urls: list[str] = []
    for tag in soup.find_all(["a", "form"]):
        href = tag.get("href") or tag.get("action") or ""
        if "datatype=fund" in href.lower() or ("filetype=csv" in href.lower() and "fund" in href.lower()):
            urls.append(urljoin(page_url, href))
    for match in re.findall(r"[^\"']+dataType=fund[^\"']*", html):
        urls.append(urljoin(page_url, match.replace("&amp;", "&")))
    # de-dupe
    seen: set[str] = set()
    out: list[str] = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


class IsharesAdapter:
    name = "ishares"

    def __init__(self, client: HttpClient, catalog: Optional[dict[str, Any]] = None):
        self.client = client
        self.catalog = catalog if catalog is not None else load_catalog()

    def collect(self, entity: dict[str, str], window: Window) -> list[dict[str, str]]:
        isin = (entity.get("isin") or "").upper()
        meta = self.catalog.get(isin)
        if not meta:
            return [
                _row(
                    entity,
                    window,
                    record_kind="error",
                    inclusion_reason="adapter_error",
                    concept="unknown_product",
                    notes=(
                        f"ISIN {isin or entity.get('ticker')} is not in "
                        "scripts/data/ishares_catalog.json"
                    ),
                )
            ]
        product_id = str(meta.get("product_id", "")).strip()
        page_url = PRODUCT_URL.format(product_id=product_id)
        try:
            html = self.client.get_text(page_url)
        except HttpError as exc:
            return [
                _row(
                    entity,
                    window,
                    record_kind="error",
                    inclusion_reason="adapter_error",
                    concept="http_error",
                    notes=str(exc),
                    source_url=page_url,
                )
            ]
        rows = parse_product_html(html, entity, window, page_url)
        holding_failure = None
        for url in holdings_urls_from_html(html, page_url)[:2]:
            try:
                text = self.client.get_text(url)
                holdings = parse_holdings_csv(text, entity, window, url)
                if not holdings:
                    raise ValueError("Holdings CSV contained no observations")
            except (HttpError, ValueError) as exc:
                holding_failure = (url, str(exc))
                continue
            rows.extend(holdings)
            holding_failure = None
            break
        if holding_failure:
            rows.append(_row(entity, window, record_kind="error", inclusion_reason="adapter_error", concept="holdings_download_failed",
                             source_url=holding_failure[0], notes=holding_failure[1]))
        if not rows:
            rows.append(
                _row(
                    entity,
                    window,
                    record_kind="error",
                    inclusion_reason="adapter_error",
                    concept="empty_product_page",
                    notes="parsed no facts or documents",
                    source_url=page_url,
                )
            )
        return rows
