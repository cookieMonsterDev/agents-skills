"""Canonical tidy row. Code is the source of truth; references/csv-schema.md is the agent cache."""

from __future__ import annotations

from typing import Any, Iterable, Mapping, MutableMapping, Optional

COLUMNS = [
    "as_of_date",
    "window_start",
    "window_end",
    "grain",
    "record_kind",
    "inclusion_reason",
    "entity_name",
    "entity_type",
    "ticker",
    "isin",
    "cik",
    "lei",
    "source",
    "source_url",
    "accession",
    "form",
    "filed_at",
    "period_start",
    "period_end",
    "fiscal_year",
    "fiscal_period",
    "statement",
    "concept",
    "concept_local",
    "taxonomy",
    "value",
    "unit",
    "currency",
    "notes",
]

RECORD_KINDS = ("fact", "filing", "document", "holding", "error")
INCLUSION_REASONS = (
    "filed_in_window",
    "period_in_window",
    "asof_latest",
    "listed",
    "adapter_error",
)

# Face-statement tags we always try to keep, even on a thin monthly window.
CORE_CONCEPTS = {
    "dei": {
        "EntityCommonStockSharesOutstanding": "shares",
    },
    "us-gaap": {
        "RevenueFromContractWithCustomerExcludingAssessedTax": "income",
        "Revenues": "income",
        "SalesRevenueNet": "income",
        "CostOfGoodsAndServicesSold": "income",
        "GrossProfit": "income",
        "OperatingIncomeLoss": "income",
        "InterestExpense": "income",
        "IncomeTaxExpenseBenefit": "income",
        "NetIncomeLoss": "income",
        "EarningsPerShareBasic": "income",
        "EarningsPerShareDiluted": "income",
        "Assets": "balance",
        "AssetsCurrent": "balance",
        "Liabilities": "balance",
        "LiabilitiesCurrent": "balance",
        "StockholdersEquity": "balance",
        "LongTermDebt": "balance",
        "LongTermDebtCurrent": "balance",
        "LongTermDebtNoncurrent": "balance",
        "ShortTermBorrowings": "balance",
        "OperatingLeaseLiabilityCurrent": "balance",
        "OperatingLeaseLiabilityNoncurrent": "balance",
        "FinanceLeaseLiabilityCurrent": "balance",
        "FinanceLeaseLiabilityNoncurrent": "balance",
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest": "balance",
        "MinorityInterest": "balance",
        "Goodwill": "balance",
        "FiniteLivedIntangibleAssetsNet": "balance",
        "IndefiniteLivedIntangibleAssetsExcludingGoodwill": "balance",
        "InventoryNet": "balance",
        "AccountsReceivableNetCurrent": "balance",
        "AccountsPayableCurrent": "balance",
        "ShortTermInvestments": "balance",
        "CashAndCashEquivalentsAtCarryingValue": "balance",
        "NetCashProvidedByUsedInOperatingActivities": "cash_flow",
        "NetCashProvidedByUsedInInvestingActivities": "cash_flow",
        "NetCashProvidedByUsedInFinancingActivities": "cash_flow",
        "PaymentsToAcquirePropertyPlantAndEquipment": "cash_flow",
        "PaymentsForRepurchaseOfCommonStock": "cash_flow",
        "PaymentsOfDividends": "cash_flow",
        "ProceedsFromIssuanceOfCommonStock": "cash_flow",
        "ShareBasedCompensation": "cash_flow",
        "DepreciationDepletionAndAmortization": "cash_flow",
        "PaymentsToAcquireBusinessesNetOfCashAcquired": "cash_flow",
        "RetainedEarningsAccumulatedDeficit": "equity",
        "WeightedAverageNumberOfSharesOutstandingBasic": "shares",
        "WeightedAverageNumberOfDilutedSharesOutstanding": "shares",
    },
    "ifrs-full": {
        "Revenue": "income",
        "ProfitLoss": "income",
        "Assets": "balance",
        "Equity": "balance",
        "EquityAttributableToOwnersOfParent": "balance",
        "NoncontrollingInterests": "balance",
        "CurrentAssets": "balance",
        "CurrentLiabilities": "balance",
        "CashAndCashEquivalents": "balance",
        "Inventories": "balance",
        "Goodwill": "balance",
        "IntangibleAssetsOtherThanGoodwill": "balance",
        "Liabilities": "balance",
        "CashFlowsFromUsedInOperatingActivities": "cash_flow",
        "CashFlowsFromUsedInInvestingActivities": "cash_flow",
        "CashFlowsFromUsedInFinancingActivities": "cash_flow",
        "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities": "cash_flow",
        "GrossProfit": "income",
        "BasicEarningsLossPerShare": "income",
        "DilutedEarningsLossPerShare": "income",
    },
}

ALLOWED_TAXONOMIES = frozenset({"us-gaap", "ifrs-full", "dei", "srt"})


def empty_row() -> dict[str, str]:
    return {column: "" for column in COLUMNS}


def pad_cik(value: Any) -> str:
    if value is None or value == "":
        return ""
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(10)


def format_value(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if value != value:  # NaN
            return ""
        if value == int(value) and abs(value) < 1e16:
            return str(int(value))
        return repr(value)
    return str(value).strip()


def fill_row(values: Mapping[str, Any]) -> dict[str, str]:
    row = empty_row()
    for key, raw in values.items():
        if key not in row:
            continue
        if key == "cik":
            row[key] = pad_cik(raw)
        elif key == "value":
            row[key] = format_value(raw)
        elif raw is None:
            row[key] = ""
        else:
            row[key] = str(raw).strip()
    return row


def merge_entity(row: MutableMapping[str, str], entity: Mapping[str, Any]) -> None:
    for key in ("entity_name", "entity_type", "ticker", "isin", "lei"):
        if not row.get(key) and entity.get(key):
            row[key] = str(entity[key]).strip()
    if not row.get("cik"):
        row["cik"] = pad_cik(entity.get("cik"))


def validate_rows(rows: Iterable[Mapping[str, str]]) -> list[str]:
    problems: list[str] = []
    for index, row in enumerate(rows):
        missing = [column for column in COLUMNS if column not in row]
        if missing:
            problems.append(f"row {index}: missing {missing}")
            continue
        kind = row.get("record_kind", "")
        if kind and kind not in RECORD_KINDS:
            problems.append(f"row {index}: bad record_kind {kind!r}")
        reason = row.get("inclusion_reason", "")
        if reason and reason not in INCLUSION_REASONS:
            problems.append(f"row {index}: bad inclusion_reason {reason!r}")
        cik = row.get("cik", "")
        if cik and (len(cik) != 10 or not cik.isdigit()):
            problems.append(f"row {index}: cik must be 10 digits, got {cik!r}")
    return problems


def statement_for(taxonomy: str, concept: str) -> Optional[str]:
    return CORE_CONCEPTS.get(taxonomy, {}).get(concept)
