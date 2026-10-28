from datetime import date
import hashlib
import json
from pathlib import Path
import sys

import pytest
import requests

from financial_reports_scraper import cli
from financial_reports_scraper.evidence import snapshot_filings
from financial_reports_scraper.http import HttpError, PoliteClient
from financial_reports_scraper.periods import resolve_window
from financial_reports_scraper.pipeline import run_report
from financial_reports_scraper.portfolio import make_entity
from financial_reports_scraper.schema import fill_row
from financial_reports_scraper.sources.edgar import EdgarAdapter, FACTS_URL, SUBMISSIONS_URL, flatten_companyfacts, flatten_submissions
from financial_reports_scraper.sources.ishares import IsharesAdapter, parse_holdings_csv, parse_product_html, parse_ishares_date


class Client:
    def __init__(self, payloads=None, body=b"<html><body><h1>Item 7. MD&amp;A</h1><p>Liquidity and debt</p></body></html>"):
        self.payloads = payloads or {}
        self.body = body
        self.urls = []

    def get_json(self, url):
        self.urls.append(url)
        if url not in self.payloads:
            raise HttpError(url, 404, "fixture absent")
        return self.payloads[url]

    def get_bytes(self, url):
        self.urls.append(url)
        return self.body


def facts(observations):
    return {"cik": 1, "entityName": "Example", "facts": {"us-gaap": {"Revenues": {"units": {"USD": observations}}}}}


def obs(start="2024-01-01", end="2024-12-31", filed="2025-02-01", value=100):
    return {"start": start, "end": end, "filed": filed, "val": value, "form": "10-K", "accn": "0000000001-25-000001"}


def submissions(filing_date="2025-02-01", report_date="2024-12-31", accession="0000000001-25-000001"):
    return {"form": ["10-K"], "filingDate": [filing_date], "reportDate": [report_date], "accessionNumber": [accession], "primaryDocument": ["annual.htm"]}


@pytest.mark.parametrize("field", ["as_of", "start", "end"])
def test_malformed_dates_fail_instead_of_using_today(field):
    with pytest.raises(ValueError, match="invalid"):
        resolve_window(**{field: "2025-99-03"})


def test_cutoff_excludes_future_publications_and_future_periods():
    window = resolve_window(as_of="2025-01-15", start="2024-01-01", end="2025-12-31")
    rows = flatten_companyfacts(facts([obs(), obs(end="2025-03-31", filed="2025-01-01")]), {}, window)
    assert rows == []
    rows = flatten_submissions({"filings": {"recent": submissions()}}, {}, window)
    assert rows == []


def test_latest_prefers_economic_period_over_comparison_order():
    window = resolve_window(as_of="2025-07-01")
    # Current observation first; old comparative last, even with a newer publication.
    rows = flatten_companyfacts(facts([obs(value=100), obs(start="2023-01-01", end="2023-12-31", filed="2025-03-01", value=70)]), {}, window)
    assert len(rows) == 1
    assert rows[0]["value"] == "100"


def test_latest_keeps_different_duration_types_and_tied_conflicts():
    window = resolve_window(as_of="2025-07-01")
    rows = flatten_companyfacts(facts([obs(), obs(value=101), obs(start="2025-01-01", end="2025-03-31", filed="2025-05-01", value=30)]), {}, window)
    assert {r["value"] for r in rows} == {"100", "101", "30"}


def test_invalid_facts_are_visible_as_errors():
    rows = flatten_companyfacts(facts([obs(value="nan"), obs(value=None)]), {}, resolve_window(as_of="2025-07-01"))
    assert len(rows) == 1
    assert rows[0]["record_kind"] == "error"
    assert "2 malformed" in rows[0]["notes"]


def test_explicit_cik_avoids_ticker_map_and_reads_old_submissions():
    cik = "0000000001"
    main = {"cik": cik, "filings": {"recent": submissions(), "files": [
        {"name": "CIK0000000001-submissions-001.json", "filingFrom": "2020-01-01", "filingTo": "2023-12-31"},
        {"name": "CIK0000000001-submissions-002.json", "filingFrom": "2010-01-01", "filingTo": "2015-12-31"}]}}
    history_url = "https://data.sec.gov/submissions/CIK0000000001-submissions-001.json"
    client = Client({SUBMISSIONS_URL.format(cik=cik): main, history_url: submissions("2022-02-01", "2021-12-31", "0000000001-22-000001"), FACTS_URL.format(cik=cik): facts([obs()])})
    rows = EdgarAdapter(client).collect(make_entity(cik=cik, ticker="DEMO"), resolve_window(start="2021-01-01", end="2025-03-01", as_of="2025-03-01"))
    filings = [r for r in rows if r["record_kind"] == "filing"]
    assert {r["period_end"] for r in filings} == {"2021-12-31", "2024-12-31"}
    assert history_url in client.urls
    assert not any("company_tickers" in url or "002.json" in url for url in client.urls)


def test_latest_primary_filing_survives_empty_month():
    payload = {"filings": {"recent": submissions()}}
    rows = flatten_submissions(payload, make_entity(cik="1", ticker="DEMO"), resolve_window(as_of="2025-07-01"), include_latest=True)
    assert rows[0]["inclusion_reason"] == "asof_latest"
    assert rows[0]["form"] == "10-K"


def test_year_only_document_is_not_given_an_invented_publication_date():
    rows = parse_product_html('<a href="annual.pdf">Annual Report 2024</a>', {}, resolve_window(as_of="2025-03-01"), "https://www.ishares.com/fund")
    assert rows[0]["filed_at"] == rows[0]["period_end"] == ""
    assert rows[0]["fiscal_year"] == "2024"
    assert rows[0]["inclusion_reason"] == "listed"


def test_future_holdings_and_invalid_dates():
    text = 'Fund holdings as of,"2025-04-01"\nName,ISIN,Weight (%)\nExample,XX0000000000,4\n'
    rows = parse_holdings_csv(text, {}, resolve_window(as_of="2025-03-01"), "https://example.test")
    assert not any(r["record_kind"] == "holding" for r in rows)
    assert rows[0]["concept"] == "holdings_after_cutoff"
    assert parse_ishares_date("31 February 2025") is None
    with pytest.raises(ValueError, match="header"):
        parse_holdings_csv("unrelated HTML", {}, resolve_window(), "url")


def test_product_value_asof_suffix_preserves_number_not_publication_claim():
    rows = parse_product_html('<table><tr><td>Net Assets</td><td>USD 1,000 as of 1 March 2025</td></tr></table>', {}, resolve_window(as_of="2025-03-01"), "https://example.test")
    assert rows[0]["value"] == "1000"
    assert rows[0]["period_end"] == "2025-03-01"
    assert rows[0]["filed_at"] == ""


def test_holdings_download_failure_not_silenced():
    class FundClient:
        def get_text(self, url):
            if "holdings" in url:
                raise HttpError(url, 503, "unavailable")
            return '<a href="annual.pdf">Annual Report 2024</a><a href="holdings?fileType=csv&amp;dataType=fund">Holdings</a>'
    rows = IsharesAdapter(FundClient(), {"IE123": {"product_id": "1"}}).collect(make_entity(isin="IE123", entity_type="etf"), resolve_window())
    assert any(r["concept"] == "holdings_download_failed" for r in rows)


def test_partial_entity_failure_preserves_other_entities(tmp_path):
    class Adapter:
        def collect(self, entity, window):
            if entity["ticker"] == "FAIL":
                raise HttpError("url", 0, "timeout")
            return [fill_row({"ticker": entity["ticker"], "entity_type": "stock", "record_kind": "fact", "concept": "Assets", "value": 10})]
    path = run_report([make_entity(ticker="FAIL"), make_entity(ticker="OK")], resolve_window(), Client(), out_dir=tmp_path, adapters={"edgar": Adapter()})
    manifest = json.loads(path.with_suffix(".manifest.json").read_text())
    assert manifest["status"] == "partial"
    assert manifest["error_count"] == 1
    assert {c["ticker"] for c in manifest["coverage"]} == {"FAIL", "OK"}
    assert "OK" in path.read_text()
    with pytest.raises(FileExistsError):
        run_report([make_entity(ticker="OK")], resolve_window(), Client(), out_dir=tmp_path, adapters={"edgar": Adapter()})


def test_full_bundle_feeds_analyzer_and_preserves_documents(tmp_path):
    cik = "0000000001"
    client = Client({SUBMISSIONS_URL.format(cik=cik): {"filings": {"recent": submissions()}}, FACTS_URL.format(cik=cik): facts([obs()])})
    path = run_report([make_entity(cik=cik, ticker="DEMO", entity_type="stock")], resolve_window(as_of="2025-03-01", start="2024-01-01", end="2025-03-01"), client, out_dir=tmp_path, download_filings=True)
    manifest = json.loads(path.with_suffix(".manifest.json").read_text())
    assert manifest["csv_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    doc = manifest["documents"][0]
    assert doc["status"] == "downloaded"
    directory = tmp_path / manifest["document_directory"]
    assert hashlib.sha256((directory / doc["raw_path"]).read_bytes()).hexdigest() == doc["sha256"]
    assert "Liquidity and debt" in (directory / doc["text_path"]).read_text()
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "fundamental-analysis/scripts"))
    from analyze_report import analyze
    result = analyze(path, "DEMO", "2025-03-01", "USD")
    assert result["periods"][0]["facts"]["revenue"]["number"] == 100


def test_download_limit_and_failure_are_recorded(tmp_path):
    row = fill_row({"record_kind": "filing", "form": "10-K", "source_url": "https://www.sec.gov/Archives/edgar/data/1/a.htm", "accession": "a"})
    other = dict(row, source_url="https://www.sec.gov/Archives/edgar/data/1/b.htm", accession="b")
    entries = snapshot_filings([row, other], Client(body=b""), tmp_path, 1)
    assert [e["status"] for e in entries] == ["error", "not_downloaded_limit"]


def test_cli_history_and_partial_exit(tmp_path, monkeypatch):
    captured = {}
    def run(entities, window, client, **kwargs):
        captured.update(window=window, options=kwargs)
        path = tmp_path / "result.csv"
        path.with_suffix(".manifest.json").write_text('{"error_count": 1}')
        return path
    monkeypatch.setattr(cli, "run_report", run)
    result = cli.main(["--tickers", "DEMO", "--as-of", "2025-03-01", "--history-years", "5", "--download-filings", "--user-agent", "test test@example.test"])
    assert result == 1
    assert captured["window"].start == date(2020, 3, 1)
    assert captured["options"]["download_filings"] is True
    assert cli.main(["--tickers", "DEMO", "--history-years", "0"]) == 2


def test_custom_history_option_and_invalid_datetime(tmp_path, monkeypatch):
    captured = {}
    def run(entities, window, client, **kwargs):
        captured["window"] = window
        path = tmp_path / "result.csv"
        path.with_suffix(".manifest.json").write_text('{"error_count": 0}')
        return path
    monkeypatch.setattr(cli, "run_report", run)
    assert cli.main(["--tickers", "DEMO", "--period", "custom", "--history-years", "5", "--as-of", "2025-03-01", "--user-agent", "test test@example.test"]) == 0
    assert captured["window"].start == date(2020, 3, 1)
    with pytest.raises(ValueError, match="invalid"):
        resolve_window(as_of="2025-03-01Tgarbage")


class Session:
    def __init__(self, responses):
        self.headers = {}
        self.responses = iter(responses)
    def get(self, *args, **kwargs):
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


class Response:
    def __init__(self, code, retry=None):
        self.status_code = code
        self.headers = {"Retry-After": retry} if retry else {}
        self.reason = "fixture"


def test_http_retry_after_and_network_failure(monkeypatch):
    sleeps = []
    monkeypatch.setattr("financial_reports_scraper.http.time.sleep", sleeps.append)
    client = PoliteClient("test test@example.test", session=Session([Response(429, "4"), Response(200)]), sec_interval=0)
    assert client.get("https://data.sec.gov/test").status_code == 200
    assert 4 in sleeps
    assert client._bucket("https://notsec.gov/test") != "sec"
    client = PoliteClient("test test@example.test", session=Session([requests.Timeout("timeout")]), sec_interval=0)
    with pytest.raises(HttpError, match="timeout"):
        client.get("https://data.sec.gov/test", retries=1)


def test_long_retry_after_is_reported_without_early_retry(monkeypatch):
    monkeypatch.setattr("financial_reports_scraper.http.time.sleep", lambda _: pytest.fail("should not sleep"))
    client = PoliteClient("test test@example.test", session=Session([Response(503, "120")]), sec_interval=0)
    with pytest.raises(HttpError, match="retry later"):
        client.get("https://data.sec.gov/test")
