"""Behavioral checks for financial selection, invalid inputs and scraper compatibility."""
import csv
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analyze_report as analysis
import scenario_models as models


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "input.csv"
        with (ROOT / "tests/fixtures/synthetic-report.csv").open(newline="") as f:
            self.rows = list(csv.DictReader(f))

    def run_analysis(self, **kwargs):
        with self.path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=analysis.schema_columns())
            w.writeheader()
            w.writerows(self.rows)
        options = dict(ticker="DEMO", as_of="2026-03-01", currency="USD")
        options.update(kwargs)
        return analysis.analyze(self.path, **options)

    def fact(self, concept="Revenues", year=2025):
        return next(r for r in self.rows if r["concept"] == concept and r["period_end"] == f"{year}-12-31")

    def test_known_financial_arithmetic_and_provenance(self):
        r = self.run_analysis()
        p = r["periods"][-1]
        self.assertEqual(len(r["periods"]), 3)
        self.assertAlmostEqual(p["metrics"]["net_margin"]["value"], .12)
        self.assertAlmostEqual(p["metrics"]["revenue_growth"]["value"], .10)
        self.assertEqual(p["metrics"]["fcf_proxy"]["value"], 130)
        self.assertEqual(p["metrics"]["ncav_before_senior_claims"]["value"], 110)
        self.assertEqual(len(p["metrics"]["fcf_proxy"]["source_records"]), 2)
        self.assertEqual(r["input_sha256"], hashlib.sha256(self.path.read_bytes()).hexdigest())
        self.assertEqual(len(r["audit"]), len(self.rows))

    def test_future_filing_is_excluded_even_when_period_is_in_window(self):
        r = self.run_analysis(as_of="2026-01-01")
        self.assertEqual(r["periods"][-1]["end"], "2024-12-31")
        self.assertGreater(r["rejection_counts"]["unavailable_at_cutoff"], 0)

    def test_latest_restatement_at_cutoff(self):
        duplicate = dict(self.fact(), filed_at="2026-04-01", value="1300")
        self.rows.append(duplicate)
        self.assertEqual(self.run_analysis()["periods"][-1]["facts"]["revenue"]["number"], 1210)
        self.assertEqual(self.run_analysis(as_of="2026-05-01")["periods"][-1]["facts"]["revenue"]["number"], 1300)

    def test_same_publication_conflict_quarantines_metric(self):
        self.rows.append(dict(self.fact(), value="1300"))
        r = self.run_analysis()
        self.assertNotIn("revenue", r["periods"][-1]["facts"])
        self.assertIsNone(r["periods"][-1]["metrics"]["net_margin"]["value"])

    def test_conflict_cannot_fall_back_to_alias(self):
        self.rows.append(dict(self.fact(), value="1300"))
        self.rows.append(dict(self.fact(), concept="SalesRevenueNet"))
        self.assertNotIn("revenue", self.run_analysis()["periods"][-1]["facts"])

    def test_duplicate_and_equivalent_alias_do_not_double_count(self):
        self.rows += [dict(self.fact()), dict(self.fact(), concept="SalesRevenueNet")]
        r = self.run_analysis()
        self.assertEqual(r["periods"][-1]["facts"]["revenue"]["number"], 1210)
        self.assertEqual(r["rejection_counts"]["duplicate"], 1)
        self.assertEqual(r["rejection_counts"]["equivalent_alias"], 1)

    def test_conflicting_alias_is_not_summed(self):
        self.rows.append(dict(self.fact(), concept="SalesRevenueNet", value="50"))
        self.assertNotIn("revenue", self.run_analysis()["periods"][-1]["facts"])

    def test_currency_mismatch(self):
        self.fact()["unit"] = "EUR"
        r = self.run_analysis()
        self.assertNotIn("revenue", r["periods"][-1]["facts"])
        self.assertEqual(r["rejection_counts"]["unit_or_currency_mismatch"], 1)

    def test_eps_requires_per_share_unit(self):
        self.fact("EarningsPerShareDiluted")["unit"] = "USD"
        self.assertNotIn("eps", self.run_analysis()["periods"][-1]["facts"])

    def test_invalid_numbers_and_dates(self):
        for value in ("", "NaN", "Infinity", "1,210", "garbage"):
            with self.subTest(value=value):
                self.fact()["value"] = value
                self.assertNotIn("revenue", self.run_analysis()["periods"][-1]["facts"])
        self.fact()["value"] = "1210"
        self.fact()["filed_at"] = "2026-99-01"
        self.assertNotIn("revenue", self.run_analysis()["periods"][-1]["facts"])

    def test_missing_capex_is_not_zero(self):
        self.rows.remove(self.fact("PaymentsToAcquirePropertyPlantAndEquipment"))
        self.assertIsNone(self.run_analysis()["periods"][-1]["metrics"]["fcf_proxy"]["value"])

    def test_negative_capex_requires_sign_review(self):
        self.fact("PaymentsToAcquirePropertyPlantAndEquipment")["value"] = "-50"
        self.assertIsNone(self.run_analysis()["periods"][-1]["metrics"]["fcf_proxy"]["value"])

    def test_losses_are_not_attractive_ratios(self):
        self.fact("NetIncomeLoss")["value"] = "-10"
        r = self.run_analysis()["periods"][-1]
        self.assertLess(r["metrics"]["net_margin"]["value"], 0)
        self.assertIsNone(r["metrics"]["cash_conversion"]["value"])
        self.assertIsNone(r["metrics"]["net_income_growth"]["value"])

    def test_balance_dates_do_not_forward_fill(self):
        self.fact("AssetsCurrent")["period_end"] = "2025-12-30"
        self.assertIsNone(self.run_analysis()["periods"][-1]["metrics"]["current_ratio"]["value"])

    def test_ytd_and_quarter_not_mixed_with_annual(self):
        self.rows.append(dict(self.fact(), period_start="2025-10-01", value="300"))
        self.rows.append(dict(self.fact(), period_start="2025-01-01", period_end="2025-09-30", value="910"))
        self.assertEqual(self.run_analysis()["periods"][-1]["facts"]["revenue"]["number"], 1210)
        self.assertEqual(self.run_analysis(period="quarter")["periods"][-1]["facts"]["revenue"]["number"], 300)
        self.assertEqual(self.run_analysis(period="ytd")["periods"][-1]["facts"]["revenue"]["number"], 910)

    def test_fiscal_labels_do_not_define_period(self):
        self.fact()["fiscal_year"] = "2040"
        self.fact()["fiscal_period"] = "Q3"
        self.assertEqual(self.run_analysis()["periods"][-1]["start"], "2025-01-01")

    def test_quarter_growth_matches_previous_year_not_previous_quarter(self):
        base = dict(self.fact())
        self.rows = [dict(base, period_start="2024-01-01", period_end="2024-03-31", value="100"),
                     dict(base, period_start="2024-10-01", period_end="2024-12-31", value="150"),
                     dict(base, period_start="2025-01-01", period_end="2025-03-31", value="110")]
        p = self.run_analysis(period="quarter")["periods"][-1]
        self.assertAlmostEqual(p["metrics"]["revenue_growth"]["value"], .1)

    def test_incomplete_debt_never_becomes_total_debt(self):
        self.rows.append(dict(self.fact("Assets"), concept="LongTermDebt", value="40"))
        p = self.run_analysis()["periods"][-1]
        self.assertNotIn("net_debt", p["metrics"])
        self.assertIn("long_term_debt_reported", p["facts"])

    def test_nonstock_target_is_routed(self):
        for r in self.rows:
            r["entity_type"] = "etf"
        with self.assertRaisesRegex(ValueError, "scenario-special-sectors"):
            self.run_analysis()

    def test_portfolio_is_filtered_by_ticker(self):
        self.rows.append(dict(self.fact(), ticker="ELSE", entity_type="etf"))
        r = self.run_analysis()
        self.assertEqual(len(r["audit"]), len(self.rows) - 1)

    def test_conflicting_cik_is_rejected(self):
        self.rows.append(dict(self.fact(), cik="0000000002"))
        with self.assertRaisesRegex(ValueError, "multiple issuers"):
            self.run_analysis()

    def test_errors_are_visible_not_financial_zeros(self):
        self.rows.append(dict(self.fact(), record_kind="error", notes="adapter unavailable"))
        r = self.run_analysis()
        self.assertTrue(any("adapter unavailable" in x for x in r["issues"]))
        self.assertEqual(r["periods"][-1]["facts"]["revenue"]["number"], 1210)

    def test_documents_only_give_limited_workpaper(self):
        self.rows = [dict(self.fact(), record_kind="filing", value="")]
        r = self.run_analysis()
        self.assertEqual(r["periods"], [])
        self.assertTrue(any("No usable" in x for x in r["issues"]))

    def test_empty_and_wrong_schema(self):
        self.rows = []
        with self.assertRaisesRegex(ValueError, "no observations"):
            self.run_analysis()
        self.path.write_text("ticker,value\nDEMO,10\n")
        with self.assertRaisesRegex(ValueError, "missing columns"):
            analysis.read_csv(self.path)

    def test_cli_outputs_and_refuses_overwrite(self):
        self.run_analysis()
        args = ["--input", str(self.path), "--ticker", "DEMO", "--as-of", "2026-03-01", "--currency", "USD", "--out-dir", self.temp.name]
        self.assertEqual(analysis.main(args), 0)
        output = Path(self.temp.name) / "2026-03-01-DEMO-annual-workpaper.md"
        original = output.read_bytes()
        self.assertEqual(analysis.main(args), 2)
        self.assertEqual(output.read_bytes(), original)

    def test_manifest_hash_and_partial_download_warning(self):
        self.run_analysis()
        sidecar = self.path.with_suffix(".manifest.json")
        manifest = {"csv_sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(), "status": "partial",
                    "error_count": 1, "download_requested": True, "documents": [{"status": "not_downloaded_limit"}]}
        sidecar.write_text(json.dumps(manifest))
        result = self.run_analysis()
        self.assertEqual(result["acquisition_manifest"]["error_count"], 1)
        self.assertTrue(any("partial" in x for x in result["issues"]))
        self.assertTrue(any("snapshot limit" in x for x in result["issues"]))
        manifest["csv_sha256"] = "incorrect"
        sidecar.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "does not match"):
            self.run_analysis()

    @unittest.skipUnless(all(importlib.util.find_spec(name) for name in ("dateutil", "requests", "bs4", "lxml", "pandas")), "Integration test requires the sibling scraper's requirements/environment")
    def test_scraper_flattener_output_accepted_without_conversion(self):
        sys.path.insert(0, str(analysis.SCRAPER / "scripts"))
        from financial_reports_scraper.sources.edgar import flatten_companyfacts
        from financial_reports_scraper.periods import resolve_window
        payload = json.loads((analysis.SCRAPER / "tests/fixtures/companyfacts_mini.json").read_text())
        window = resolve_window(start="2024-01-01", end="2026-09-01", as_of="2026-09-01")
        self.rows = flatten_companyfacts(payload, {"ticker": "AAPL", "entity_type": "stock"}, window, core_only=False)
        r = self.run_analysis(ticker="AAPL", as_of="2026-09-01")
        self.assertEqual(r["periods"][0]["facts"]["revenue"]["number"], 391035000000)
        self.assertIsNone(r["periods"][0]["metrics"]["fcf_proxy"]["value"])


class ModelTests(unittest.TestCase):
    def fixture(self, name):
        return json.loads((ROOT / f"tests/fixtures/{name}.json").read_text())

    def test_dcf_independently_computed(self):
        r = models.calculate("dcf", self.fixture("dcf"))
        pv = 100 / 1.1 + 110 / 1.1**2 + 120 / 1.1**3
        terminal = (120 * 1.02 / .08) / 1.1**3
        value = (pv + terminal - 100) / 100
        self.assertAlmostEqual(r["value_per_share"], value)
        self.assertAlmostEqual(r["terminal_value_fraction"], terminal / (pv + terminal))
        self.assertAlmostEqual(r["margin_of_safety"], (value - 10) / value)
        self.assertAlmostEqual(r["price_upside"], value / 10 - 1)

    def test_dcf_invalid_basis_and_terminal_assumptions(self):
        for key, value in [("cash_flow_basis", "CFO-capex"), ("terminal_growth", .1), ("diluted_shares", 0), ("cash_flows", [100, -1])]:
            data = self.fixture("dcf")
            data[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                models.calculate("dcf", data)

    def test_earnings(self):
        r = models.calculate("earnings", self.fixture("earnings"))
        self.assertAlmostEqual(r["value_per_share"], 2 * 1.05**5 * 12 / 1.1**5)
        self.assertIn("dividends excluded", r["limitation"])

    def test_asset_and_liquidity(self):
        r = models.calculate("asset", self.fixture("asset"))
        self.assertEqual(r["value_per_share"], 10)
        r = models.calculate("stress", self.fixture("stress"))
        self.assertEqual(r["runway_months"], 12)
        self.assertEqual(r["horizon_funding_gap"], 60)

    def test_negative_asset_equity_has_no_margin_of_safety(self):
        data = self.fixture("asset")
        data["total_liabilities"] = 400
        r = models.calculate("asset", data)
        self.assertLess(r["residual_equity"], 0)
        self.assertIsNone(r["margin_of_safety"])

    def test_cost(self):
        r = models.calculate("cost", self.fixture("cost"))
        self.assertAlmostEqual(r["cost_difference"], 10000 * (1.059**20 - 1.05**20))

    def test_unexplained_inputs_and_nonfinite_are_rejected(self):
        data = self.fixture("earnings")
        del data["sources"]["growth_rate"]
        with self.assertRaisesRegex(ValueError, "Missing sources"):
            models.calculate("earnings", data)
        for value in (float("inf"), float("nan"), True, "2", -1):
            data = self.fixture("earnings")
            data["normalized_eps"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                models.calculate("earnings", data)

    def test_cli_model_output_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "result.json"
            args = ["asset", "--input", str(ROOT / "tests/fixtures/asset.json"), "--output", str(output)]
            self.assertEqual(models.main(args), 0)
            original = output.read_bytes()
            self.assertEqual(models.main(args), 2)
            self.assertEqual(output.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
