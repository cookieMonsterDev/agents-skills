#!/usr/bin/env python3
"""Auditable, offline calculations on financial-reports-scraper CSVs. Python 3.9+."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRAPER = ROOT.parent / "financial-reports-scraper"

# Only equivalent consolidated meanings belong in one group. Parent profit/equity,
# total debt and current debt are intentionally not inferred from broader totals.
TAGS = {
    "revenue": ("us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax", "us-gaap:Revenues", "us-gaap:SalesRevenueNet", "ifrs-full:Revenue"),
    "net_income": ("us-gaap:NetIncomeLoss", "ifrs-full:ProfitLoss"),
    "gross_profit": ("us-gaap:GrossProfit", "ifrs-full:GrossProfit"),
    "operating_income": ("us-gaap:OperatingIncomeLoss",),
    "interest_expense": ("us-gaap:InterestExpense",),
    "cfo": ("us-gaap:NetCashProvidedByUsedInOperatingActivities", "ifrs-full:CashFlowsFromUsedInOperatingActivities"),
    "capex": ("us-gaap:PaymentsToAcquirePropertyPlantAndEquipment", "ifrs-full:PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
    "dividends": ("us-gaap:PaymentsOfDividends",),
    "buybacks": ("us-gaap:PaymentsForRepurchaseOfCommonStock",),
    "sbc": ("us-gaap:ShareBasedCompensation",),
    "eps": ("us-gaap:EarningsPerShareDiluted", "ifrs-full:DilutedEarningsLossPerShare"),
    "diluted_shares": ("us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding",),
    "assets": ("us-gaap:Assets", "ifrs-full:Assets"),
    "liabilities": ("us-gaap:Liabilities", "ifrs-full:Liabilities"),
    "equity": ("us-gaap:StockholdersEquity", "ifrs-full:EquityAttributableToOwnersOfParent"),
    "total_equity": ("us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "ifrs-full:Equity"),
    "current_assets": ("us-gaap:AssetsCurrent", "ifrs-full:CurrentAssets"),
    "current_liabilities": ("us-gaap:LiabilitiesCurrent", "ifrs-full:CurrentLiabilities"),
    "cash": ("us-gaap:CashAndCashEquivalentsAtCarryingValue", "ifrs-full:CashAndCashEquivalents"),
    "inventory": ("us-gaap:InventoryNet", "ifrs-full:Inventories"),
    "receivables": ("us-gaap:AccountsReceivableNetCurrent",),
    "goodwill": ("us-gaap:Goodwill", "ifrs-full:Goodwill"),
    "long_term_debt_noncurrent": ("us-gaap:LongTermDebtNoncurrent",),
    "long_term_debt_reported": ("us-gaap:LongTermDebt",),
    "shares_outstanding": ("dei:EntityCommonStockSharesOutstanding", "us-gaap:CommonStockSharesOutstanding"),
}
INSTANT = {"assets", "liabilities", "equity", "total_equity", "current_assets", "current_liabilities", "cash", "inventory", "receivables", "goodwill", "long_term_debt_noncurrent", "long_term_debt_reported", "shares_outstanding"}
TAG_TO_METRIC = {tag: metric for metric, tags in TAGS.items() for tag in tags}
FORMS = {"10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A", "40-F", "40-F/A", "6-K", "6-K/A"}


def iso(value):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value or ""):
        raise ValueError("expected ISO date YYYY-MM-DD")
    return date.fromisoformat(value)


def classify(start, end):
    if not start:
        return "instant"
    days = (iso(end) - iso(start)).days + 1
    if 350 <= days <= 380:
        return "annual"
    if 75 <= days <= 105:
        return "quarter"
    if 150 <= days <= 200 or 240 <= days <= 290:
        return "ytd"
    return "other"


def schema_columns():
    """Load the sibling contract without importing its network dependencies."""
    import runpy
    schema = SCRAPER / "scripts/financial_reports_scraper/schema.py"
    if not schema.is_file():
        raise ValueError(f"Required financial-reports-scraper dependency missing: {schema}")
    return runpy.run_path(str(schema))["COLUMNS"]


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        if len(headers) != len(set(headers)):
            raise ValueError("Duplicate CSV column names")
        missing = set(schema_columns()) - set(headers)
        if missing:
            raise ValueError("Not a scraper CSV; missing columns: " + ", ".join(sorted(missing)))
        rows = []
        for number, row in enumerate(reader, 2):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f"Malformed CSV record {number}")
            rows.append({**{k: v.strip() for k, v in row.items()}, "csv_record": number})
    if not rows:
        raise ValueError("CSV has a header but no observations")
    return rows


def analyze(path, ticker, as_of, currency, period="annual", period_end=None):
    iso(as_of)
    if period not in {"annual", "quarter", "ytd"}:
        raise ValueError("period must be annual, quarter or ytd")
    if period_end:
        iso(period_end)
        if period_end > as_of:
            raise ValueError("period-end must be on or before as-of")
    if not re.fullmatch(r"[A-Z]{3}", currency):
        raise ValueError("Currency must be a three-letter uppercase code")
    rows = read_csv(path)
    input_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest_path = path.with_suffix(".manifest.json")
    acquisition_manifest = None
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict) or manifest.get("csv_sha256") != input_hash:
            raise ValueError("Acquisition manifest does not match the input CSV hash; reconcile the evidence bundle")
        acquisition_manifest = {"path": str(manifest_path.resolve()), "status": manifest.get("status"),
                                "error_count": manifest.get("error_count"), "document_directory": manifest.get("document_directory"),
                                "download_requested": manifest.get("download_requested"),
                                "documents": manifest.get("documents", [])}
    selected = [r for r in rows if r["ticker"].upper() == ticker.upper()]
    if not selected:
        raise ValueError(f"Ticker {ticker} is absent; available: {sorted({r['ticker'] for r in rows})}")
    identities = {(r["cik"], r["isin"]) for r in selected if r["cik"] or r["isin"]}
    ciks = {r["cik"] for r in selected if r["cik"]}
    isins = {r["isin"] for r in selected if r["isin"]}
    if len(ciks) > 1 or len(isins) > 1:
        raise ValueError("Ticker identifies multiple issuers/share classes; split the input by identifier")
    audit, candidates, issues = [], [], []
    if acquisition_manifest and acquisition_manifest["status"] == "partial":
        issues.append(f"Acquisition bundle is partial; inspect {manifest_path.name} for adapter/document failures.")
    if acquisition_manifest and any(d.get("status") == "not_downloaded_limit" for d in acquisition_manifest["documents"]):
        issues.append("Some source filings were not downloaded because of the snapshot limit; inspect manifest locators as needed.")
    kinds = Counter(r["record_kind"] for r in selected)
    types = {r["entity_type"].lower() for r in selected}
    if types - {"stock"}:
        raise ValueError(f"Company calculations require entity_type=stock; found {sorted(types)}. Read scenario-special-sectors.md")
    for row in selected:
        record = dict(row)
        audit.append(record)
        record["status"] = "excluded"
        metric = TAG_TO_METRIC.get(row["taxonomy"] + ":" + row["concept"])
        reason = None
        if row["record_kind"] == "error":
            issues.append(f"Adapter error at CSV record {row['csv_record']}: {row['notes']}")
            reason = "adapter_error"
        elif row["record_kind"] != "fact":
            reason = "non_fact"
        elif not metric:
            reason = "unmapped_concept"
        else:
            try:
                iso(row["filed_at"])
                iso(row["period_end"])
                grain = classify(row["period_start"], row["period_end"])
                value = float(row["value"])
                if not math.isfinite(value):
                    raise ValueError("nonfinite")
            except (ValueError, TypeError):
                reason = "invalid_value_or_date"
            if not reason:
                expected_unit = "shares" if metric in {"diluted_shares", "shares_outstanding"} else currency + "/shares" if metric == "eps" else currency
                if row["filed_at"] > as_of or row["period_end"] > as_of:
                    reason = "unavailable_at_cutoff"
                elif row["form"] not in FORMS:
                    reason = "unsupported_form"
                elif row["unit"] != expected_unit or row["currency"] not in {"", currency}:
                    reason = "unit_or_currency_mismatch"
                elif (metric in INSTANT) != (grain == "instant"):
                    reason = "instant_duration_mismatch"
                elif grain not in {"instant", period}:
                    reason = "different_duration"
                elif period_end and row["period_end"] != period_end:
                    reason = "different_period_end"
                else:
                    record.update(metric=metric, number=value, period_kind=grain, status="candidate")
                    candidates.append(record)
        if reason:
            record["reason"] = reason

    # First select latest publication per exact concept and economic interval.
    groups = defaultdict(list)
    for r in candidates:
        key = (r["metric"], r["taxonomy"], r["concept"], r["period_start"], r["period_end"], r["unit"])
        groups[key].append(r)
    chosen = defaultdict(list)
    for key, group in groups.items():
        latest = max(r["filed_at"] for r in group)
        top = [r for r in group if r["filed_at"] == latest]
        for r in group:
            r.update(status="excluded", reason="superseded_publication")
        context_key = (key[0], key[3], key[4])
        if len({r["number"] for r in top}) > 1:
            for r in top:
                r.update(status="excluded", reason="conflicting_latest_values")
            chosen[context_key].append(None)
            issues.append(f"Conflicting latest values: {key[0]} {key[3]} to {key[4]}")
        else:
            for r in top:
                r.update(reason="duplicate")
            winner = min(top, key=lambda r: r["csv_record"])
            winner.update(status="candidate", reason="latest_publication")
            chosen[context_key].append(winner)
    observations = {}
    for key, group in chosen.items():
        valid = [r for r in group if r is not None]
        if None in group or len({r["number"] for r in valid}) > 1:
            issues.append(f"Metric unavailable pending concept reconciliation: {key}")
            for r in valid:
                r.update(status="excluded", reason="competing_concepts")
            continue
        winner = min(valid, key=lambda r: TAGS[key[0]].index(r["taxonomy"] + ":" + r["concept"]))
        for r in valid:
            r.update(status="excluded", reason="equivalent_alias")
        winner.update(status="selected", reason="latest_consistent_value")
        observations[key] = winner

    intervals = sorted({(s, e) for m, s, e in observations if s})
    periods = []
    for start, end in intervals:
        facts = {m: r for (m, s, e), r in observations.items() if e == end and s in {"", start}}
        metrics = compute_metrics(facts)
        periods.append({"start": start, "end": end, "kind": period, "facts": facts, "metrics": metrics})
    # Exactly one like-length prior-year interval; no annualization or TTM inference.
    for current in periods:
        prior = [p for p in periods if 350 <= (iso(current["end"]) - iso(p["end"])).days <= 380
                 and abs((iso(current["end"]) - iso(current["start"])).days - (iso(p["end"]) - iso(p["start"])).days) <= 10]
        if len(prior) == 1:
            previous = prior[0]
            for name in ("revenue", "net_income", "eps", "inventory", "receivables", "diluted_shares"):
                a, b = previous["facts"].get(name), current["facts"].get(name)
                current["metrics"][name + "_growth"] = derived([a, b], lambda x, y: y / x - 1 if x > 0 and y >= 0 else None, f"current {name} / prior {name} - 1", "fraction")
    if not intervals:
        issues.append(f"No usable {period} duration facts; widen scraper history or review conflicts. Balance facts remain in the audit.")
    if any(p["end"] < as_of for p in periods):
        issues.append("Reporting periods precede the cutoff; review the latest filing and intervening events for staleness.")
    rejection_counts = Counter(r.get("reason", "") for r in audit if r["status"] == "excluded")
    return {"schema_version": 1, "status": "computed_evidence_requires_analyst_review", "ticker": ticker.upper(), "as_of": as_of,
            "currency": currency, "period_kind": period, "input": str(path.resolve()),
            "input_sha256": input_hash, "acquisition_manifest": acquisition_manifest, "row_counts": dict(kinds),
            "identifiers": sorted(identities), "issues": issues, "rejection_counts": dict(rejection_counts), "periods": periods, "audit": audit}


def derived(facts, function, formula, unit):
    ids = [f["csv_record"] for f in facts if f]
    result = {"value": None, "formula": formula, "unit": unit, "source_records": ids}
    if any(f is None for f in facts):
        result["reason"] = "missing_or_ambiguous_input"
    else:
        value = function(*(f["number"] for f in facts))
        if value is None or not math.isfinite(value):
            result["reason"] = "not_meaningful_for_denominator_or_sign"
        else:
            result["value"] = value
    return result


def compute_metrics(facts):
    result = {}
    for name, numerator, denominator in (
        ("net_margin", "net_income", "revenue"),
        ("gross_margin", "gross_profit", "revenue"),
        ("operating_margin", "operating_income", "revenue"),
        ("cfo_margin", "cfo", "revenue"),
        ("cash_conversion", "cfo", "net_income"),
        ("current_ratio", "current_assets", "current_liabilities"),
        ("liabilities_to_assets", "liabilities", "assets"),
        ("interest_coverage_proxy", "operating_income", "interest_expense"),
    ):
        result[name] = derived([facts.get(numerator), facts.get(denominator)], lambda a, b: a / b if b > 0 else None, f"{numerator} / {denominator}", "ratio")
    result["fcf_proxy"] = derived([facts.get("cfo"), facts.get("capex")], lambda a, b: a - b if b >= 0 else None, "cfo - nonnegative gross PPE purchases (not FCFF or FCFE)", "reporting_currency")
    result["net_current_assets"] = derived([facts.get("current_assets"), facts.get("current_liabilities")], lambda a, b: a - b, "current_assets - current_liabilities", "reporting_currency")
    result["ncav_before_senior_claims"] = derived([facts.get("current_assets"), facts.get("liabilities")], lambda a, b: a - b, "current_assets - total_liabilities; preferred/NCI and realization costs still unadjusted", "reporting_currency")
    return result


def markdown(result):
    lines = [f"# {result['ticker']} — computed financial evidence", "", "Status: analyst review pending. This is a calculation workpaper, not a completed investment analysis.", "",
             f"Information cutoff: {result['as_of']}. Currency: {result['currency']}. Duration: {result['period_kind']}.",
             f"Input: `{result['input']}`. SHA-256: `{result['input_sha256']}`.", "", "## Coverage", ""]
    lines += [f"- {k}: {v} records" for k, v in result["row_counts"].items()]
    if result.get("acquisition_manifest"):
        lines.append(f"- Acquisition manifest and source-document locators: {result['acquisition_manifest']['path']}")
    lines += ["", "## Data limitations", ""] + [f"- {x}" for x in result["issues"]]
    lines += ["- Missing/ambiguous values stay unavailable. Facts use actual start/end dates; publication dates enforce the cutoff.", "- All source records, rejected observations, formulas and units are in the companion JSON."]
    lines += [f"- Excluded {count} record(s): {reason}." for reason, count in sorted(result["rejection_counts"].items())]
    for p in result["periods"]:
        lines += ["", f"## {p['start']} to {p['end']}", "", "Reported facts:", ""]
        for name, f in sorted(p["facts"].items()):
            lines.append(f"- {name}: {f['number']:,.6g} {f['unit']} (CSV record {f['csv_record']}; {f['taxonomy']}:{f['concept']}; filed {f['filed_at']}; accession {f['accession']}; {f['source_url']})")
        lines += ["", "Derived metrics:", ""]
        for name, m in p["metrics"].items():
            value = f"{m['value']:,.6g}" if m["value"] is not None else "unavailable: " + m["reason"]
            lines.append(f"- {name}: {value}; {m['formula']}; unit {m['unit']}; records {m['source_records']}.")
    lines += ["", "## Analyst completion", "", "Apply the relevant scenario reference and report-template.md: business/category evidence, notes and MD&A, normalized earnings, valuation assumptions, downside, counter-thesis, opportunity cost, and unresolved questions. Save the completed analysis as a separate Markdown report.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--as-of", required=True, help="Information availability cutoff, YYYY-MM-DD")
    parser.add_argument("--currency", required=True, help="Explicit reporting currency, e.g. USD")
    parser.add_argument("--period", choices=["annual", "quarter", "ytd"], default="annual")
    parser.add_argument("--period-end", help="Optional exact economic period end")
    parser.add_argument("--out-dir", type=Path, default=Path("reports"), help="Directory for the workpaper (default: reports/ in the current directory)")
    args = parser.parse_args(argv)
    try:
        result = analyze(args.input, args.ticker, args.as_of, args.currency, args.period, args.period_end)
        slug = re.sub(r"[^A-Za-z0-9_.-]", "_", args.ticker.upper())
        stem = f"{args.as_of}-{slug}-{args.period}" + (f"-{args.period_end}" if args.period_end else "") + "-workpaper"
        paths = [args.out_dir / (stem + suffix) for suffix in (".json", ".md")]
        if any(p.exists() for p in paths):
            raise ValueError("Output exists; choose a new --out-dir to preserve the previous run")
        args.out_dir.mkdir(parents=True, exist_ok=True)
        paths[0].write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        paths[1].write_text(markdown(result), encoding="utf-8")
        print(paths[1])
        print(paths[0])
        return 0
    except (ValueError, OSError, csv.Error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
