from __future__ import annotations

from pathlib import Path

from financial_reports_scraper.portfolio import load_portfolio, resolve_entities
from financial_reports_scraper.schema import pad_cik, validate_rows, fill_row

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_load_portfolio_skips_blank_and_normalizes():
    entities = load_portfolio(FIXTURES / "portfolio.csv")
    assert [e["ticker"] for e in entities] == ["AAPL", "AEB"]
    assert entities[0]["entity_type"] == "stock"
    assert entities[1]["entity_type"] == "etf"
    assert entities[1]["isin"] == "IE00B1YZSC51"


def test_resolve_entities_requires_input():
    try:
        resolve_entities()
    except ValueError as exc:
        assert "no entities" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_cik_padding_and_schema_validation():
    assert pad_cik(320193) == "0000320193"
    row = fill_row({"cik": 320193, "record_kind": "fact", "inclusion_reason": "listed"})
    assert row["cik"] == "0000320193"
    assert validate_rows([row]) == []
    bad = dict(row)
    bad["cik"] = "320193"
    assert validate_rows([bad])
