from __future__ import annotations

from pathlib import Path

from financial_reports_scraper.periods import resolve_window
from financial_reports_scraper.portfolio import make_entity
from financial_reports_scraper.sources.ishares import (
    holdings_urls_from_html,
    parse_holdings_csv,
    parse_product_html,
)
from financial_reports_scraper.sources.router import choose_adapter

FIXTURES = Path(__file__).resolve().parent / "fixtures"
CATALOG = {
    "IE00B1YZSC51": {"product_id": "251860"},
    "IE00B4ND3602": {"product_id": "258441"},
}


def test_router_ishares_vs_edgar():
    etf = make_entity(
        entity_name="iShares Core MSCI Europe",
        entity_type="etf",
        isin="IE00B1YZSC51",
        ticker="AEB",
    )
    stock = make_entity(entity_name="Apple Inc.", entity_type="stock", ticker="AAPL")
    other_etf = make_entity(entity_name="Some Other ETF", entity_type="etf", isin="LU0000000000")
    assert choose_adapter(etf, CATALOG) == "ishares"
    assert choose_adapter(stock, CATALOG) == "edgar"
    assert choose_adapter(other_etf, CATALOG) is None


def test_parse_product_page_facts_and_documents():
    html = (FIXTURES / "ishares_product.html").read_text(encoding="utf-8")
    window = resolve_window(period="month", as_of="2026-09-10")
    entity = make_entity(
        entity_name="iShares Core MSCI Europe",
        entity_type="etf",
        isin="IE00B1YZSC51",
        ticker="AEB",
    )
    rows = parse_product_html(html, entity, window, "https://www.ishares.com/uk/individual/en/products/251860")
    concepts = {r["concept"]: r for r in rows if r["record_kind"] == "fact"}
    assert concepts["ter"]["value"] == "0.12"
    assert concepts["isin"]["value"] == "IE00B1YZSC51"
    assert concepts["net_assets_fund"]["currency"] == "EUR"
    assert concepts["net_assets_fund"]["value"] == "11976345768"
    assert concepts["sector_weight_financials"]["value"] == "25.87"
    docs = [r for r in rows if r["record_kind"] == "document"]
    assert any(r["concept"] == "annual_report" for r in docs)
    assert holdings_urls_from_html(html, "https://www.ishares.com/uk/individual/en/products/251860")


def test_parse_holdings_csv_emits_weight_rows():
    text = (FIXTURES / "holdings.csv").read_text(encoding="utf-8")
    window = resolve_window(period="month", as_of="2026-09-10")
    entity = make_entity(isin="IE00B1YZSC51", ticker="AEB", entity_type="etf")
    rows = parse_holdings_csv(text, entity, window, "https://example.test/holdings.csv")
    assert len(rows) == 2
    nestle = next(r for r in rows if "NESTLE" in r["concept_local"])
    assert nestle["value"] == "3.10"
    assert nestle["record_kind"] == "holding"
    assert "CH0038863350" in nestle["notes"]
