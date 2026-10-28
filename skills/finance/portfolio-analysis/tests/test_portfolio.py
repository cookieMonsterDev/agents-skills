"""Synthetic accounting regressions; no private broker data is bundled."""

from decimal import Decimal as D
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from adapters.ibkr import parse
from analyze_portfolio import summarize, research_universe


def statement(body, account="PRIVATE-ACCOUNT", end="20260930"):
    return f'<FlexStatement accountId="{account}" fromDate="20260901" toDate="{end}">{body}</FlexStatement>'


def trade(identity="t1", qty="2", extra="", **overrides):
    attrs = dict(tradeID=identity, conid="123", symbol="FUND", isin="IE0000000001", description="Synthetic fund",
                 currency="EUR", assetCategory="STK", subCategory="ETF", quantity=qty,
                 tradeDate="20260915", levelOfDetail="EXECUTION", buySell="BUY", proceeds="-20",
                 ibCommission="-1", ibCommissionCurrency="EUR", netCash="-21", ibOrderID="same-order")
    attrs.update(overrides)
    return '<Trade ' + ' '.join(f'{k}="{v}"' for k, v in attrs.items()) + ' ' + extra + '/>'


def snapshot(value="90", currency="EUR", fx="1", **overrides):
    attrs = dict(conid="123", symbol="FUND", isin="IE0000000001", description="Synthetic fund",
                 assetCategory="STK", subCategory="ETF", currency=currency, position="9",
                 positionValue=value, fxRateToBase=fx, levelOfDetail="SUMMARY", reportDate="20260930")
    attrs.update(overrides)
    return '<OpenPosition ' + ' '.join(f'{k}="{v}"' for k, v in attrs.items()) + '/>'


def balances(nav="100", cash="10"):
    return (f'<CashReport><CashReportCurrency currency="BASE_SUMMARY" endingCash="{cash}"/>'
            f'<CashReportCurrency currency="EUR" endingCash="{cash}"/></CashReport>'
            f'<EquitySummaryInBase total="{nav}" reportDate="20260930"/>')


class ParserTests(unittest.TestCase):
    def read(self, body, wrap=True):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "input.xml"
            path.write_text(statement(body) if wrap else body)
            return parse(path)

    def account(self, body):
        account = self.read(body)["accounts"][0]
        account["metrics"] = summarize(account)
        return account

    def test_activity_is_not_holdings(self):
        a = self.account('<Trades>' + trade(qty="2.125") + '</Trades>')
        self.assertFalse(a["positions_complete"])
        self.assertFalse(a["metrics"]["weights_available"])
        self.assertIsNone(a["metrics"]["reported_nav_base"])
        self.assertEqual(a["metrics"]["trade_activity"][0]["net_traded_quantity"], D("2.125"))
        self.assertIsNone(a["base_currency"])

    def test_summary_and_lots_are_not_added(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + snapshot(levelOfDetail="LOT") + '</OpenPositions>' + balances())
        self.assertEqual(len(a["positions"]), 1)
        self.assertEqual(a["metrics"]["weights"][0]["weight_pct"], D(90))
        self.assertEqual(a["metrics"]["cash_value_base"], D(10))
        self.assertEqual(a["metrics"]["reconciliation_residual"], D(0))

    def test_identical_duplicate_removed_but_partial_fills_kept(self):
        a = self.account('<Trades>' + trade() + trade() + trade(identity="t2", qty="3") + trade(identity="sum", levelOfDetail="ORDER", qty="5") + '</Trades>')
        self.assertEqual(len(a["trades"]), 2)
        self.assertEqual(a["metrics"]["trade_activity"][0]["net_traded_quantity"], D(5))
        self.assertEqual(a["metrics"]["commissions_signed_by_currency"]["EUR"], D(-2))

    def test_basecurrency_cash_and_daily_nav_reconcile(self):
        a = self.account(
            '<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + '</OpenPositions>'
            '<CashReport><CashReportCurrency currency="BASE_SUMMARY" levelOfDetail="BaseCurrency" '
            'endingCash="10" toDate="20260930"/>'
            '<CashReportCurrency currency="EUR" endingCash="4"/>'
            '<CashReportCurrency currency="USD" endingCash="7"/></CashReport>'
            '<EquitySummaryInBase>'
            '<EquitySummaryByReportDateInBase reportDate="20260901" total="70"/>'
            '<EquitySummaryByReportDateInBase reportDate="20260930" total="100"/>'
            '</EquitySummaryInBase><ChangeInNAV endingValue="100"/>')
        self.assertEqual(a["metrics"]["cash_value_base"], D(10))
        self.assertEqual(a["metrics"]["reported_nav_base"], D(100))
        self.assertEqual(a["metrics"]["reconciliation_residual"], D(0))
        self.assertEqual(a["metrics"]["weights"][0]["weight_pct"], D(90))
        self.assertEqual(a["metrics"]["cash_weight_pct"], D(10))
        self.assertEqual(len(a["reported_nav"]["source_refs"]), 2)
        self.assertEqual(a["warnings"], [])

    def test_daily_nav_without_change_in_nav(self):
        a = self.account(
            '<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + '</OpenPositions>'
            '<CashReportCurrency currency="BASE_SUMMARY" levelOfDetail="BaseCurrency" endingCash="10"/>'
            '<EquitySummaryInBase><EquitySummaryByReportDateInBase '
            'reportDate="20260930" total="100"/></EquitySummaryInBase>')
        self.assertTrue(a["metrics"]["weights_available"])
        self.assertEqual(a["metrics"]["reported_nav_base"], D(100))

    def test_daily_nav_requires_ending_date(self):
        for attrs in ('reportDate="20260901"', ''):
            with self.subTest(attrs=attrs):
                a = self.account('<AccountInformation currency="EUR"/>'
                                 '<EquitySummaryInBase><EquitySummaryByReportDateInBase '
                                 + attrs + ' total="100"/></EquitySummaryInBase>')
                self.assertIsNone(a["reported_nav"])
                self.assertFalse(a["metrics"]["weights_available"])

    def test_daily_nav_conflict_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Conflicting ending NAV"):
            self.read('<EquitySummaryInBase><EquitySummaryByReportDateInBase '
                      'reportDate="20260930" total="100"/></EquitySummaryInBase>'
                      '<ChangeInNAV endingValue="120"/>')

    def test_basecurrency_cash_validation(self):
        row = '<CashReportCurrency currency="BASE_SUMMARY" levelOfDetail="BaseCurrency" endingCash="10"/>'
        with self.assertRaisesRegex(ValueError, "Duplicate cash"):
            self.read(row + row)
        with self.assertRaisesRegex(ValueError, "BASE_SUMMARY"):
            self.read(row.replace('currency="BASE_SUMMARY"', 'currency="USD"'))
        a = self.account('<AccountInformation currency="EUR"/>'
                         + row.replace('/>', ' toDate="20260901"/>'))
        self.assertIsNone(a["metrics"]["cash_value_base"])

    def test_conflicting_duplicate_fails(self):
        with self.assertRaisesRegex(ValueError, "Conflicting duplicate"):
            self.read(trade() + trade(qty="3"))

    def test_multicurrency_value_uses_position_fx(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot(value="100", currency="USD", fx="0.9") + '</OpenPositions>' + balances())
        self.assertEqual(a["metrics"]["securities_value_base"], D(90))
        self.assertTrue(a["metrics"]["weights_available"])

    def test_missing_fx_and_missing_value_remain_unknown(self):
        for row in (snapshot(currency="USD", fx=""), snapshot(value="")):
            a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + row + '</OpenPositions>' + balances())
            self.assertIsNone(a["metrics"]["securities_value_base"])
            self.assertFalse(a["metrics"]["weights_available"])

    def test_foreign_cash_not_converted_with_trade_fx(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + '</OpenPositions><CashReportCurrency currency="USD" endingCash="10"/><EquitySummaryInBase total="100"/>')
        self.assertIsNone(a["metrics"]["cash_value_base"])
        self.assertFalse(a["metrics"]["weights_available"])

    def test_nav_residual_blocks_weights(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + '</OpenPositions>' + balances(nav="120"))
        self.assertEqual(a["metrics"]["reconciliation_residual"], D(20))
        self.assertFalse(a["metrics"]["weights_available"])

    def test_cash_only_and_zero_nav(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions/>' + balances(cash="100"))
        self.assertEqual(a["metrics"]["cash_weight_pct"], D(100))
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions/>' + balances(nav="0", cash="0"))
        self.assertFalse(a["metrics"]["weights_available"])

    def test_stale_position_and_lot_only_block_weights(self):
        for row in (snapshot(reportDate="20260915"), snapshot(levelOfDetail="LOT")):
            a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + row + '</OpenPositions>' + balances())
            self.assertFalse(a["positions_complete"])
            self.assertFalse(a["metrics"]["weights_available"])

    def test_lot_for_missing_summary_blocks_weights(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot() + snapshot(conid="456", levelOfDetail="LOT") + '</OpenPositions>' + balances())
        self.assertFalse(a["positions_complete"])
        self.assertFalse(a["metrics"]["weights_available"])

    def test_missing_currency_and_commissions_stay_incomplete(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot(currency="") + '</OpenPositions>' + balances() + trade(ibCommission=""))
        self.assertFalse(a["metrics"]["weights_available"])
        self.assertFalse(a["metrics"]["commission_fields_complete"])

    def test_order_only_activity_is_provisional(self):
        a = self.account(trade(levelOfDetail="ORDER"))
        self.assertFalse(a["activity_complete"])

    def test_duplicate_balances_and_conflicting_nav_fail(self):
        for body in ('<OpenPositions>' + snapshot() * 2 + '</OpenPositions>',
                     '<CashReportCurrency currency="EUR" endingCash="10"/>' * 2,
                     '<EquitySummaryInBase total="100"/><ChangeInNAV endingValue="120"/>'):
            with self.assertRaises(ValueError):
                self.read(body)

    def test_short_position_has_signed_weight_and_gross_exposure(self):
        a = self.account('<AccountInformation currency="EUR"/><OpenPositions>' + snapshot(value="-90", position="-9") + '</OpenPositions>' + balances(cash="190"))
        self.assertEqual(a["metrics"]["weights"][0]["weight_pct"], D(-90))
        self.assertEqual(a["metrics"]["cash_weight_pct"], D(190))
        self.assertEqual(a["metrics"]["gross_security_exposure_pct"], D(90))

    def test_corrections_and_corporate_actions_mark_provisional(self):
        a = self.account(trade(origTradeID="original") + '<CorporateActions><CorporateAction/></CorporateActions>')
        self.assertFalse(a["activity_complete"])

    def test_sell_signs_and_currency_buckets(self):
        a = self.account(trade() + trade(identity="t2", qty="-1", buySell="SELL", currency="USD", proceeds="15", ibCommissionCurrency="USD"))
        self.assertEqual(len(a["metrics"]["trade_activity"]), 2)
        self.assertEqual(a["metrics"]["commissions_signed_by_currency"], {"EUR": D(-1), "USD": D(-1)})
        with self.assertRaisesRegex(ValueError, "direction"):
            self.read(trade(qty="-2"))

    def test_unsupported_instrument_retained_not_sent_to_scraper(self):
        data = self.read('<OpenPositions>' + snapshot(assetCategory="OPT", subCategory="", symbol="CALL") + '</OpenPositions>')
        self.assertEqual(data["accounts"][0]["positions"][0]["type"], "unsupported")
        self.assertEqual(research_universe(data), [])

    def test_research_list_uses_positions_when_available(self):
        data = self.read('<OpenPositions>' + snapshot() + '</OpenPositions>' + trade(conid="456", isin="DIFFERENT", symbol="CLOSED"))
        self.assertEqual([r["ticker"] for r in research_universe(data)], ["FUND"])

    def test_cash_transactions_do_not_establish_cash_balance(self):
        a = self.account('<CashTransaction transactionID="c1" dateTime="20260915;120000" currency="EUR" amount="100" type="Deposits/Withdrawals" levelOfDetail="DETAIL"/>')
        self.assertEqual(a["metrics"]["cash_activity"][0]["amount"], D(100))
        self.assertIsNone(a["metrics"]["cash_value_base"])

    def test_namespace_multiple_accounts_and_private_identifiers(self):
        xml = '<FlexQueryResponse xmlns="urn:test"><FlexStatements>' + statement(trade()) + statement(trade(), account="SECOND-PRIVATE") + '</FlexStatements></FlexQueryResponse>'
        data = self.read(xml, wrap=False)
        self.assertEqual(len(data["accounts"]), 2)
        encoded = json.dumps(data, default=str)
        self.assertNotIn("PRIVATE-ACCOUNT", encoded)
        self.assertNotIn("SECOND-PRIVATE", encoded)

    def test_repeated_accounts_fail(self):
        with self.assertRaisesRegex(ValueError, "repeated account"):
            self.read('<FlexStatements>' + statement("") * 2 + '</FlexStatements>', wrap=False)

    def test_bad_numeric_and_out_of_period_trade_fail(self):
        for attrs in ({"quantity": "NaN"}, {"quantity": "not-money"}, {"tradeDate": "20261001"}):
            with self.assertRaises(ValueError):
                self.read(trade(**attrs))

    def test_dtd_and_utf16_dtd_fail(self):
        text = '<!DOCTYPE x [<!ENTITY e "unsafe">]>' + statement("")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "input.xml"
            for encoding in ("utf-8", "utf-16"):
                p.write_bytes(text.encode(encoding))
                with self.assertRaisesRegex(ValueError, "DTD/entity"):
                    parse(p)

    def test_cli_outputs_preserve_runs_and_no_private_id(self):
        with tempfile.TemporaryDirectory() as td:
            path, out = Path(td) / "input.xml", Path(td) / "out"
            path.write_text(statement(trade()))
            command = [sys.executable, str(SCRIPTS / "analyze_portfolio.py"), "--input", str(path), "--out-dir", str(out)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list(out.iterdir())), 3)
            for file in out.iterdir():
                self.assertNotIn("PRIVATE-ACCOUNT", file.read_text())
            original = (out / "portfolio.json").read_bytes()
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)
            self.assertEqual((out / "portfolio.json").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
