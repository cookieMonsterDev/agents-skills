#!/usr/bin/env python3
"""Calculate explicit analyst assumptions; no market-data fetch or inferred forecasts."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path


def number(data, key, minimum=None, strict=False):
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} must be a finite JSON number")
    if minimum is not None and (value <= minimum if strict else value < minimum):
        raise ValueError(f"{key} must be {'>' if strict else '>='} {minimum}")
    return value


def years(data):
    value = number(data, "years", 1)
    if int(value) != value or value > 100:
        raise ValueError("years must be an integer from 1 to 100")
    return int(value)


def provenance(data):
    for key in ("currency", "as_of", "rationale"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} is required")
    from analyze_report import iso
    iso(data["as_of"])
    sources = data.get("sources")
    if not isinstance(sources, dict) or not sources or any(not isinstance(v, str) or not v.strip() for v in sources.values()):
        raise ValueError("sources must map input names to evidence/assumption explanations")
    uncovered = set(data) - {"currency", "as_of", "rationale", "sources", "label"} - set(sources)
    if uncovered:
        raise ValueError("Missing sources/assumption explanations for: " + ", ".join(sorted(uncovered)))


def calculate(model, data):
    provenance(data)
    result = {"model": model, "label": data.get("label", "analyst scenario"), "currency": data["currency"], "as_of": data["as_of"], "assumptions": data}
    if model == "dcf":
        if data.get("cash_flow_basis") != "FCFF":
            raise ValueError("DCF requires explicitly normalized FCFF; CFO-minus-capex is insufficient")
        flows = data.get("cash_flows")
        if not isinstance(flows, list) or not 1 <= len(flows) <= 100:
            raise ValueError("cash_flows must contain 1–100 annual FCFF projections")
        flows = [number({"flow": x}, "flow") for x in flows]
        rate = number(data, "discount_rate", 0, strict=True)
        growth = number(data, "terminal_growth", -1, strict=True)
        if rate <= growth or flows[-1] <= 0:
            raise ValueError("DCF requires discount_rate > terminal_growth and positive terminal-year FCFF")
        shares = number(data, "diluted_shares", 0, strict=True)
        net_debt = number(data, "net_debt")
        senior = number(data, "other_senior_claims", 0)
        pv_flows = sum(flow / (1 + rate) ** t for t, flow in enumerate(flows, 1))
        pv_terminal = flows[-1] * (1 + growth) / (rate - growth) / (1 + rate) ** len(flows)
        enterprise = pv_flows + pv_terminal
        equity = enterprise - net_debt - senior
        result.update(pv_forecast_fcff=pv_flows, pv_terminal=pv_terminal, enterprise_value=enterprise,
                      equity_value=equity, value_per_share=equity / shares,
                      terminal_value_fraction=pv_terminal / enterprise if enterprise > 0 else None,
                      formula="PV(FCFF) + PV(terminal FCFF/(r-g)) - net debt - other senior claims; divide by diluted shares")
    elif model == "earnings":
        eps = number(data, "normalized_eps", 0, strict=True)
        growth = number(data, "growth_rate", -1, strict=True)
        multiple = number(data, "terminal_pe", 0, strict=True)
        rate = number(data, "required_return", 0, strict=True)
        n = years(data)
        future_eps = eps * (1 + growth) ** n
        result.update(terminal_eps=future_eps, terminal_price=future_eps * multiple,
                      value_per_share=future_eps * multiple / (1 + rate) ** n,
                      formula="normalized EPS × (1+growth)^years × terminal P/E / (1+required return)^years",
                      limitation="Terminal share-price scenario only; interim dividends excluded. Not a full total-return valuation.")
    elif model == "asset":
        assets = data.get("assets")
        if not isinstance(assets, list) or not assets:
            raise ValueError("assets must be nonempty: [{name, carrying_value, recovery_fraction, evidence}]")
        recoveries = []
        for asset in assets:
            if not isinstance(asset, dict) or not asset.get("name") or not asset.get("evidence"):
                raise ValueError("Each asset needs name and evidence")
            value = number(asset, "carrying_value", 0)
            recovery = number(asset, "recovery_fraction", 0)
            if recovery > 1:
                raise ValueError("recovery_fraction must be <=1; document independent appraisal outside this haircut model")
            recoveries.append(value * recovery)
        liabilities = number(data, "total_liabilities", 0)
        senior = number(data, "additional_senior_claims", 0)
        costs = number(data, "realization_costs_and_taxes", 0)
        shares = number(data, "diluted_shares", 0, strict=True)
        residual = sum(recoveries) - liabilities - senior - costs
        result.update(recoverable_assets=sum(recoveries), residual_equity=residual, value_per_share=residual / shares,
                      formula="sum(carrying value × recovery fraction) - total liabilities - additional senior claims - realization costs/taxes; divide by diluted shares",
                      limitation="Negative residual indicates a modeled shortfall. Realizable equity depends on legal priority, timing and a catalyst.")
    elif model == "stress":
        cash = number(data, "unrestricted_cash", 0)
        credit = number(data, "available_committed_credit", 0)
        obligations = number(data, "one_off_obligations", 0)
        burn = number(data, "monthly_cash_burn", 0, strict=True)
        months = number(data, "horizon_months", 0, strict=True)
        buffer = cash + credit - obligations
        result.update(liquidity_after_one_off_obligations=buffer, runway_months=max(0, buffer) / burn,
                      horizon_funding_gap=max(0, months * burn - buffer),
                      formula="(unrestricted cash + available committed credit - one-off obligations) / monthly cash burn",
                      limitation="Static liquidity stress; verify covenant availability and obligation dates. Include each cash use once. Does not predict default.")
    elif model == "cost":
        capital = number(data, "initial_capital", 0, strict=True)
        gross = number(data, "gross_annual_return", -1, strict=True)
        active_cost = number(data, "active_annual_cost", 0)
        benchmark_cost = number(data, "benchmark_annual_cost", 0)
        n = years(data)
        if gross - max(active_cost, benchmark_cost) <= -1:
            raise ValueError("Net annual return must exceed -100%")
        active = capital * (1 + gross - active_cost) ** n
        benchmark = capital * (1 + gross - benchmark_cost) ** n
        result.update(active_ending_value=active, benchmark_ending_value=benchmark, cost_difference=benchmark - active,
                      formula="initial capital × (1 + same assumed gross return - annual cost)^years",
                      limitation="Cost-only illustration: same gross return, no cash flows, no taxes. Not an outperformance forecast or a stock-selection rule.")
    else:
        raise ValueError(f"Unknown model {model}")
    if "price" in data:
        price = number(data, "price", 0, strict=True)
        intrinsic = result.get("value_per_share")
        if intrinsic is None:
            raise ValueError("price is only applicable to dcf, earnings and asset")
        result["margin_of_safety"] = (intrinsic - price) / intrinsic if intrinsic > 0 else None
        result["price_upside"] = intrinsic / price - 1
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", choices=["dcf", "earnings", "asset", "stress", "cost"])
    parser.add_argument("--input", required=True, type=Path, help="JSON assumptions with per-input sources")
    parser.add_argument("--output", required=True, type=Path, help="New JSON output path; refuses overwrite")
    args = parser.parse_args(argv)
    try:
        if args.output.exists():
            raise ValueError("Output exists; choose a new output path")
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Input must be a JSON object")
        result = calculate(args.model, data)
        result["input_sha256"] = hashlib.sha256(args.input.read_bytes()).hexdigest()
        encoded = json.dumps(result, indent=2, allow_nan=False) + "\n"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(args.output)
        return 0
    except (ValueError, TypeError, OverflowError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
