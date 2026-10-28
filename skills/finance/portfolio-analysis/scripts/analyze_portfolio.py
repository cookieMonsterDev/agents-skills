#!/usr/bin/env python3
"""Normalize declarations and write offline workpapers, not investment advice."""

import argparse
from collections import defaultdict
import csv
from datetime import datetime, timezone
from decimal import Decimal
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

from adapters import ibkr

ADAPTERS = {"ibkr": ibkr.parse}
ZERO = Decimal(0)


def summarize(account):
    positions = account["positions"]
    base = account["base_currency"]
    valued = account["positions_complete"] and base and all(p["market_value_base"] is not None for p in positions)
    cash = account["cash_balances"]
    # BASE_SUMMARY already includes other currencies; never add it to them.
    base_summary = [c for c in cash if c["currency"] == "BASE_SUMMARY"]
    cash_value = base_summary[0]["ending_cash"] if base and base_summary else None
    if cash_value is None and base and len(cash) == 1 and cash[0]["currency"] == base:
        cash_value = cash[0]["ending_cash"]
    securities = sum((p["market_value_base"] for p in positions), ZERO) if valued else None
    nav = account["reported_nav"]["value"] if account["reported_nav"] and base else None
    residual = nav - securities - cash_value if nav is not None and securities is not None and cash_value is not None else None
    tolerance = max(Decimal("0.01"), abs(nav) * Decimal("0.0001")) if nav is not None else None
    reconciled = residual is not None and abs(residual) <= tolerance
    eligible = bool(reconciled and nav > 0 and all(p["asset_category"] == "STK" for p in positions))
    reasons = []
    if not valued:
        reasons.append("Ending positions, values or base currency are incomplete.")
    if cash_value is None:
        reasons.append("Base-currency ending cash unavailable; request BASE_SUMMARY or review dated FX externally.")
    if nav is None:
        reasons.append("Reported ending NAV unavailable.")
    if residual is not None and not reconciled:
        reasons.append("NAV does not reconcile to positions plus cash; investigate accruals/liabilities/omissions.")
    if nav is not None and nav <= 0:
        reasons.append("Nonpositive NAV: conventional allocation weights withheld.")
    if any(p["asset_category"] != "STK" for p in positions):
        reasons.append("Non-stock instruments need exposure-specific valuation; automated weights withheld.")
    weights = [{"instrument_id": p["instrument_id"], "currency": p["currency"],
                "weight_pct": p["market_value_base"] / nav * 100} for p in positions] if eligible else []
    activity = defaultdict(lambda: {"net_traded_quantity": ZERO, "gross_traded_value": ZERO, "gross_value_complete": True})
    commissions, flows = defaultdict(Decimal), defaultdict(Decimal)
    for trade in account["trades"]:
        key = (trade["instrument_id"], trade["currency"])
        activity[key]["net_traded_quantity"] += trade["quantity"]
        if trade["proceeds"] is None:
            activity[key]["gross_value_complete"] = False
        else:
            activity[key]["gross_traded_value"] += abs(trade["proceeds"])
        if trade["commission"] is not None:
            commissions[trade["commission_currency"] or "UNKNOWN"] += trade["commission"]
    for row in account["cash_transactions"]:
        flows[(row["currency"], row["type"])] += row["amount"]
    return {"securities_value_base": securities, "cash_value_base": cash_value, "reported_nav_base": nav,
            "reconciliation_residual": residual, "reconciliation_tolerance": tolerance,
            "weights_available": eligible, "weights": weights, "limitations": reasons,
            "cash_weight_pct": cash_value / nav * 100 if eligible else None,
            "gross_security_exposure_pct": sum((abs(p["market_value_base"]) for p in positions), ZERO) / nav * 100 if eligible else None,
            "activity_status": "observed execution totals" if account["activity_complete"] else "provisional; manual review required",
            "trade_activity": [{"instrument_id": key[0], "currency": key[1], **value} for key, value in activity.items()],
            "commissions_signed_by_currency": dict(commissions),
            "commission_fields_complete": all(t["commission"] is not None and t["commission_currency"] for t in account["trades"]),
            "cash_activity": [{"currency": key[0], "type": key[1], "amount": value} for key, value in flows.items()]}


def safe(value):
    return str(value if value is not None else "unavailable").replace("|", "\\|").replace("\n", " ").replace("\r", " ").replace("<", "&lt;").replace(">", "&gt;")


def workpaper(data):
    lines = ["# Portfolio declaration workpaper", "", "Status: offline data review only; research and recommendations are not yet completed.",
             "", f"Source SHA-256: `{data['source_sha256']}`", "", "Account identifiers are replaced with run-local labels.",
             "", "The snapshot date is not a current market valuation. Section presence does not prove the export is unfiltered."]
    for account in data["accounts"]:
        metrics = account["metrics"]
        lines += ["", f"## {account['account']} · {account['from_date']} to {account['as_of']}", "",
                  f"Base currency: {safe(account['base_currency'])}. Activity: {metrics['activity_status']}.", "",
                  f"Ending NAV: {safe(metrics['reported_nav_base'])}; securities: {safe(metrics['securities_value_base'])}; cash: {safe(metrics['cash_value_base'])}.",
                  f"NAV reconciliation residual: {safe(metrics['reconciliation_residual'])}. Weights available: {metrics['weights_available']}.", "",
                  "### Data limitations", ""]
        lines += [f"- {safe(w)}" for w in account["warnings"] + metrics["limitations"]]
        lines += ["", f"Ignored rows: {safe(account['ignored_rows'])}.", "", "### Reported ending positions", "",
                  "| Instrument | ISIN | Units | Currency | Value | Value in base |", "| --- | --- | ---: | --- | ---: | ---: |"]
        for p in account["positions"]:
            lines.append("| " + " | ".join(safe(p[k]) for k in ("ticker", "isin", "quantity", "currency", "market_value", "market_value_base")) + " |")
        if not account["positions"]:
            lines += ["", "No ending position rows supplied; this does not establish an empty portfolio."]
        lines += ["", "### Trading activity (not holdings)", "", "| Instrument ID | Currency | Net traded units | Gross traded value |", "| --- | --- | ---: | ---: |"]
        for row in metrics["trade_activity"]:
            lines.append(f"| {safe(row['instrument_id'])} | {safe(row['currency'])} | {row['net_traded_quantity']} | {row['gross_traded_value'] if row['gross_value_complete'] else 'unavailable'} |")
        fees = "; ".join(f"{safe(currency)} {amount}" for currency, amount in metrics['commissions_signed_by_currency'].items()) or "none reported"
        lines += ["", f"Reported signed commissions (negative = charge): {fees}. Commission fields complete: {metrics['commission_fields_complete']}.", "",
                  "### Cash activity (not ending cash)", "", "| Currency | Type | Amount |", "| --- | --- | ---: |"]
        for row in metrics["cash_activity"]:
            lines.append(f"| {safe(row['currency'])} | {safe(row['type'])} | {row['amount']} |")
    lines += ["", "## Next steps", "", "Verify export coverage, resolve identities in research-universe.csv, acquire official evidence with financial-reports-scraper, then apply fundamental-analysis and the portfolio report template. Unknown holdings/context require conditional recommendations.", ""]
    return "\n".join(lines)


def research_universe(data):
    entities = {}
    for account in data["accounts"]:
        rows = account["positions"] if account["positions_complete"] else account["positions"] + account["trades"]
        for row in rows:
            if row["type"] not in ("stock", "etf", "etc") or not row["quantity"]:
                continue
            key = row["isin"] or (row["ticker"], row["exchange"], row["currency"])
            entities[key] = {k: row[k] for k in ("company_name", "type", "isin", "ticker", "exchange")}
    return list(entities.values())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--format", choices=sorted(ADAPTERS), default="ibkr")
    parser.add_argument("--out-dir", type=Path, required=True, help="New directory; existing runs are never overwritten")
    args = parser.parse_args(argv)
    try:
        if args.out_dir.exists():
            raise ValueError("Output directory already exists; select a new run directory")
        data = ADAPTERS[args.format](args.input)
        data["generated_at"] = datetime.now(timezone.utc).isoformat()
        for account in data["accounts"]:
            account["metrics"] = summarize(account)
        args.out_dir.mkdir(parents=True, exist_ok=False)
        (args.out_dir / "portfolio.json").write_text(json.dumps(data, indent=2, default=str) + "\n", encoding="utf-8")
        (args.out_dir / "workpaper.md").write_text(workpaper(data), encoding="utf-8")
        with (args.out_dir / "research-universe.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["company_name", "type", "isin", "ticker", "exchange"])
            writer.writeheader()
            writer.writerows(research_universe(data))
    except (ValueError, OSError, ET.ParseError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(args.out_dir.resolve() / "workpaper.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
