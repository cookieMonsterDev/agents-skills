from __future__ import annotations

import json
from pathlib import Path

from financial_reports_scraper.http import HttpError
from financial_reports_scraper.periods import resolve_window
from financial_reports_scraper.pipeline import run_report
from financial_reports_scraper.portfolio import make_entity
from financial_reports_scraper.schema import COLUMNS
from financial_reports_scraper.sources.edgar import EdgarAdapter, FACTS_URL, SUBMISSIONS_URL
from financial_reports_scraper.sources.ishares import IsharesAdapter, load_catalog

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class FakeClient:
    def __init__(self, json_by_url, text_by_url=None):
        self.json_by_url = json_by_url
        self.text_by_url = text_by_url or {}

    def get_json(self, url):
        if url not in self.json_by_url:
            raise HttpError(url, 404, "missing")
        return self.json_by_url[url]

    def get_text(self, url):
        if url not in self.text_by_url:
            raise HttpError(url, 404, "missing")
        return self.text_by_url[url]


def test_pipeline_writes_named_csv(tmp_path):
    window = resolve_window(period="month", as_of="2026-09-10")
    facts = json.loads((FIXTURES / "companyfacts_mini.json").read_text(encoding="utf-8"))
    submissions = json.loads((FIXTURES / "submissions_mini.json").read_text(encoding="utf-8"))
    html = (FIXTURES / "ishares_product.html").read_text(encoding="utf-8")
    holdings = (FIXTURES / "holdings.csv").read_text(encoding="utf-8")
    cik = "0000320193"
    client = FakeClient(
        json_by_url={
            SUBMISSIONS_URL.format(cik=cik): submissions,
            FACTS_URL.format(cik=cik): facts,
        },
        text_by_url={
            "https://www.ishares.com/uk/individual/en/products/251860": html,
            "https://www.ishares.com/uk/individual/en/products/251860/holdings.ajax?fileType=csv&fileName=IMEU_holdings&dataType=fund": holdings,
        },
    )
    entities = [
        make_entity(entity_name="Apple Inc.", ticker="AAPL", entity_type="stock"),
        make_entity(
            entity_name="iShares Core MSCI Europe",
            entity_type="etf",
            isin="IE00B1YZSC51",
            ticker="AEB",
        ),
    ]
    path = run_report(
        entities,
        window,
        client,
        out_dir=tmp_path,
        adapters={
            "edgar": EdgarAdapter(client, ticker_map={"AAPL": cik}),
            "ishares": IsharesAdapter(client, catalog=load_catalog()),
        },
    )
    assert path.name == "2026-09-10-report-2026-08-10-2026-09-10.csv"
    text = path.read_text(encoding="utf-8")
    header = text.splitlines()[0]
    assert header.split(",") == COLUMNS
    assert "AAPL" in text
    assert "IE00B1YZSC51" in text
    assert "0000320193" in text
    assert "annual_report" in text
