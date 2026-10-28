from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from financial_reports_scraper.periods import resolve_window
from financial_reports_scraper.portfolio import make_entity
from financial_reports_scraper.sources.edgar import flatten_companyfacts, flatten_submissions

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _payload(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_flatten_keeps_filed_in_window_and_asof_for_the_rest():
    window = resolve_window(period="month", as_of="2026-09-10")
    entity = make_entity(entity_name="Apple Inc.", ticker="AAPL", entity_type="stock")
    rows = flatten_companyfacts(_payload("companyfacts_mini.json"), entity, window)
    assets = [r for r in rows if r["concept"] == "Assets"]
    reasons = {r["inclusion_reason"] for r in assets}
    # 2026-08-15 filing is inside 2026-08-10..2026-09-10
    assert "filed_in_window" in reasons
    filed_row = next(r for r in assets if r["inclusion_reason"] == "filed_in_window")
    assert filed_row["value"] == "331000000000"
    assert filed_row["cik"] == "0000320193"
    assert filed_row["period_end"] == "2026-06-27"

    shares = [r for r in rows if r["concept"] == "EntityCommonStockSharesOutstanding"]
    # 2026-08-01 is before the window start, so only as-of latest
    assert any(r["inclusion_reason"] == "asof_latest" for r in shares)
    latest_shares = next(r for r in shares if r["inclusion_reason"] == "asof_latest")
    assert latest_shares["value"] == "14900000000"


def test_flatten_submissions_keeps_forms_in_window_only():
    window = resolve_window(period="month", as_of="2026-09-10")
    entity = make_entity(ticker="AAPL")
    rows = flatten_submissions(_payload("submissions_mini.json"), entity, window)
    forms = {r["form"] for r in rows}
    assert forms == {"8-K", "10-Q"}
    ten_q = next(r for r in rows if r["form"] == "10-Q")
    assert "0000320193-26-000066" in ten_q["accession"]
    assert ten_q["source_url"].endswith("aapl-10q.htm")
    assert date.fromisoformat(ten_q["filed_at"]) == date(2026, 8, 15)
