"""Coverage manifest and optional, bounded SEC primary filing snapshots."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from .http import HttpError
from .periods import parse_date
from .sources.edgar import duration_kind

DOCUMENT_FORMS = {"10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A", "40-F", "40-F/A", "6-K", "6-K/A", "8-K", "8-K/A", "DEF 14A"}


def snapshot_filings(rows, client, directory: Path, max_filings: int):
    filings = {r["source_url"]: r for r in rows if r["record_kind"] == "filing" and r["form"] in DOCUMENT_FORMS and r["source_url"]}
    # Annual/interim statements before event/proxy reports; newest first within each group.
    ordered = sorted(filings.values(), key=lambda r: r["filed_at"], reverse=True)
    ordered.sort(key=lambda r: r["form"].split("/")[0] not in {"10-K", "10-Q", "20-F", "40-F"})
    entries = []
    for index, row in enumerate(ordered):
        entry = {k: row[k] for k in ("ticker", "cik", "accession", "form", "filed_at", "source_url")}
        if index >= max_filings:
            entries.append({**entry, "status": "not_downloaded_limit"})
            continue
        url = row["source_url"]
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "www.sec.gov" or not parsed.path.startswith("/Archives/edgar/data/"):
            entries.append({**entry, "status": "error", "error": "Expected official SEC Archives URL"})
            continue
        try:
            body = client.get_bytes(url)
            if not body or len(body) > 25 * 1024 * 1024:
                raise ValueError("Empty filing or filing exceeds 25 MiB snapshot limit")
            directory.mkdir(parents=True, exist_ok=True)
            stem = re.sub(r"[^A-Za-z0-9_.-]", "_", row["cik"] + "-" + row["accession"])
            is_pdf = body.lstrip().startswith(b"%PDF")
            raw_path = directory / (stem + (".pdf" if is_pdf else ".html"))
            with raw_path.open("xb") as stream:
                stream.write(body)
            entry.update(status="downloaded", raw_path=raw_path.name, sha256=hashlib.sha256(body).hexdigest(), bytes=len(body), retrieved_at=datetime.now(timezone.utc).isoformat())
            if not is_pdf:
                soup = BeautifulSoup(body, "lxml")
                for node in soup.find_all(["script", "style", "noscript", "ix:hidden"]):
                    node.decompose()
                text = soup.get_text("\n", strip=True)
                text_path = directory / (stem + ".txt")
                with text_path.open("x", encoding="utf-8") as stream:
                    stream.write(text + "\n")
                entry["text_path"] = text_path.name
                entry["text_sha256"] = hashlib.sha256(text_path.read_bytes()).hexdigest()
            else:
                entry["text_status"] = "PDF preserved; use a PDF reader for page-aware extraction"
            entries.append(entry)
        except (HttpError, OSError, ValueError) as exc:
            entries.append({**entry, "status": "error", "error": str(exc)})
    return entries


def write_manifest(path, frame, window, documents, requested_downloads):
    records = frame.fillna("").to_dict("records")
    coverage = []
    for (ticker, cik, isin), group in frame.groupby(["ticker", "cik", "isin"], dropna=False, sort=True):
        periods = {}
        for row in group.to_dict("records"):
            end = parse_date(row["period_end"])
            if row["record_kind"] == "fact" and end:
                kind = duration_kind(parse_date(row["period_start"]), end)
                periods.setdefault(kind, set()).add((row["period_start"], row["period_end"]))
        coverage.append({"ticker": ticker, "cik": cik, "isin": isin,
                         "row_counts": {str(k): int(v) for k, v in group["record_kind"].value_counts().items()},
                         "periods": {k: [list(pair) for pair in sorted(v)] for k, v in periods.items()},
                         "errors": [r["notes"] for r in group.to_dict("records") if r["record_kind"] == "error"]})
    errors = sum(r["record_kind"] == "error" for r in records) + sum(d["status"] == "error" for d in documents)
    payload = {"schema_version": 1, "status": "partial" if errors else "collected", "error_count": errors,
               "retrieved_at": datetime.now(timezone.utc).isoformat(), "information_cutoff": window.cutoff.isoformat(),
               "csv": path.name, "csv_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
               "coverage": coverage, "download_requested": requested_downloads,
               "document_directory": path.stem + "-documents", "documents": documents,
               "limitations": ["Coverage lists available observations, not proof of complete statements or comparable accounting.",
                               "Companyfacts excludes custom tags and dimensional notes; read source filings for those.",
                               "iShares listed/undated records describe retrieved pages, not verified historical availability.",
                               "Filing text is a reading aid; raw HTML/PDF is authoritative for tables and layout."]}
    destination = path.with_suffix(".manifest.json")
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2, allow_nan=False)
        stream.write("\n")
    return destination
