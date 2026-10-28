"""Conservative IBKR Activity Flex XML ingestion using Python's standard library."""

from collections import Counter
from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import xml.etree.ElementTree as ET


def number(value):
    if value is None or value == "":
        return None
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("Invalid numeric field") from exc
    if not result.is_finite():
        raise ValueError("Non-finite numeric field")
    return result


def date(value):
    if not value:
        return None
    value = value.split(";")[0]
    for fmt in ("%Y%m%d", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    raise ValueError("Unsupported date field")


def instrument(a):
    isin = a.get("isin") or (a.get("securityID") if a.get("securityIDType") == "ISIN" else "")
    category, sub = a.get("assetCategory", ""), a.get("subCategory", "")
    kind = {"ETF": "etf", "ETC": "etc"}.get(sub, "stock" if category == "STK" and sub in ("", "COMMON", "ADR", "REIT") else "unsupported")
    key = a.get("conid") or isin or "|".join(a.get(k, "") for k in ("symbol", "listingExchange", "currency", "assetCategory"))
    return {"instrument_id": key, "isin": isin or "", "ticker": a.get("symbol", ""),
            "company_name": a.get("description", ""), "type": kind,
            "asset_category": category, "sub_category": sub,
            "exchange": a.get("listingExchange", ""), "currency": a.get("currency", "")}


def parse(path):
    with path.open("rb") as handle:
        raw = handle.read(50_000_001)
    if len(raw) > 50_000_000:
        raise ValueError("XML exceeds the 50 MB local parser limit")
    # Decode before checking so UTF-16 cannot bypass the DTD/entity guard.
    encoding = "utf-16" if raw.startswith((b"\xff\xfe", b"\xfe\xff")) or b"\x00" in raw[:100] else "utf-8-sig"
    xml = raw.decode(encoding)
    if "<!DOCTYPE" in xml.upper() or "<!ENTITY" in xml.upper():
        raise ValueError("DTD/entity declarations are not supported")
    root = ET.fromstring(xml)
    for node in root.iter():
        node.tag = node.tag.rsplit("}", 1)[-1]
    if root.tag not in ("FlexQueryResponse", "FlexStatements", "FlexStatement"):
        raise ValueError("Expected IBKR Activity Flex XML")
    statements = list(root.iter("FlexStatement"))
    if not statements:
        raise ValueError("No FlexStatement found")
    result = {"schema_version": 1, "adapter": "ibkr-flex", "source_sha256": hashlib.sha256(raw).hexdigest(),
              "accounts": [], "limitations": ["Export filters/completeness must be verified by the analyst; presence of a section does not prove full account coverage."]}
    seen_accounts = set()
    for index, statement in enumerate(statements, 1):
        account_id = statement.get("accountId")
        if not account_id or account_id in seen_accounts:
            raise ValueError("Missing/repeated account statement; export one period per account")
        seen_accounts.add(account_id)
        start, end = date(statement.get("fromDate")), date(statement.get("toDate"))
        if not start or not end or start > end:
            raise ValueError("Missing/invalid statement period")
        infos = list(statement.iter("AccountInformation"))
        currencies = {n.get("currency") or n.get("baseCurrency") for n in infos} - {None, ""}
        if statement.get("baseCurrency"):
            currencies.add(statement.get("baseCurrency"))
        if len(currencies) > 1:
            raise ValueError("Conflicting account base currencies")
        base = next(iter(currencies), statement.get("baseCurrency") or None)
        account = {"account": f"account-{index}", "from_date": start, "as_of": end, "base_currency": base,
                   "sections": dict(Counter(n.tag for n in statement)), "positions": [], "trades": [],
                   "cash_transactions": [], "cash_balances": [], "reported_nav": None,
                   "positions_complete": statement.find("OpenPositions") is not None,
                   "activity_complete": True, "warnings": [], "ignored_rows": dict()}
        warnings = account["warnings"]
        ignored = Counter()
        if not base:
            warnings.append("Base currency missing; transaction FX rates do not identify it.")
        if not account["positions_complete"]:
            warnings.append("Open Positions missing: net traded units are activity, not ending holdings.")
        for section in ("CorporateActions", "Transfers", "StockGrantActivities"):
            if any(len(n) for n in statement.iter(section)):
                warnings.append(f"{section} present but not normalized; review source for ownership/cash changes.")
                account["activity_complete"] = False
        seen, position_keys, cash_keys, navs = {}, set(), set(), []
        lot_keys = set()
        for tag, accepted in (("OpenPosition", {"SUMMARY"}), ("Trade", {"EXECUTION"}),
                              ("CashTransaction", {"DETAIL"}),
                              ("CashReportCurrency", {"SUMMARY", "BASECURRENCY"}),
                              ("EquitySummaryInBase", {"SUMMARY"}),
                              ("EquitySummaryByReportDateInBase", {"SUMMARY"}),
                              ("ChangeInNAV", {"SUMMARY"})):
            for ordinal, node in enumerate(statement.iter(tag), 1):
                a = node.attrib
                if a.get("accountId", account_id) != account_id:
                    raise ValueError("Row account does not match statement account")
                ref = f"FlexStatement[{index}]/{tag}[{ordinal}]"
                detail = a.get("levelOfDetail", "").upper()
                if detail and detail not in accepted:
                    ignored[f"{tag}:{detail}"] += 1
                    if tag == "OpenPosition" and detail == "LOT":
                        lot = instrument(a)
                        lot_keys.add((lot["instrument_id"], lot["currency"]))
                    if tag == "OpenPosition" and detail != "LOT":
                        account["positions_complete"] = False
                    continue
                if a.get("model"):
                    warnings.append(f"{ref}: model-level row omitted; use an account-level export.")
                    if tag == "OpenPosition":
                        account["positions_complete"] = False
                    if tag in ("Trade", "CashTransaction"):
                        account["activity_complete"] = False
                    continue
                row_date = date(a.get("reportDate") or a.get("toDate"))
                if tag == "EquitySummaryByReportDateInBase" and not row_date:
                    ignored[f"{tag}:missing-date"] += 1
                    continue
                if tag in ("OpenPosition", "CashReportCurrency", "EquitySummaryInBase",
                           "EquitySummaryByReportDateInBase", "ChangeInNAV") and row_date and row_date != end:
                    ignored[f"{tag}:non-ending-date"] += 1
                    if tag == "OpenPosition":
                        account["positions_complete"] = False
                    continue
                item = {"source_ref": ref}
                if tag in ("OpenPosition", "Trade"):
                    item.update(instrument(a))
                    if not a.get("conid") and not item["isin"] and not a.get("symbol"):
                        raise ValueError(f"{ref}: instrument identifier missing")
                    item["quantity"] = number(a.get("position" if tag == "OpenPosition" else "quantity"))
                    if item["quantity"] is None:
                        raise ValueError(f"{ref}: quantity missing")
                    item["fx_rate_to_base"] = number(a.get("fxRateToBase"))
                    if item["fx_rate_to_base"] is not None and item["fx_rate_to_base"] <= 0:
                        raise ValueError(f"{ref}: FX rate must be positive")
                if tag == "OpenPosition":
                    key = (item["instrument_id"], item["currency"])
                    if key in position_keys:
                        raise ValueError("Duplicate position summary; refusing to double-count")
                    position_keys.add(key)
                    item["market_value"] = number(a.get("positionValue"))
                    rate = Decimal(1) if item["currency"] == base else item["fx_rate_to_base"]
                    item["market_value_base"] = (item["market_value"] * rate if base and item["currency"] and rate is not None and item["market_value"] is not None else None)
                    item["cost_basis"] = number(a.get("costBasisMoney"))
                    item["unrealized_pnl"] = number(a.get("fifoPnlUnrealized"))
                    item["as_of"] = end
                    account["positions"].append(item)
                elif tag in ("Trade", "CashTransaction"):
                    identity = a.get("tradeID") or a.get("transactionID") or a.get("ibExecID")
                    if identity:
                        key = (tag, identity)
                        if key in seen:
                            if seen[key] != a:
                                raise ValueError("Conflicting duplicate transaction identifier")
                            ignored[f"{tag}:duplicate"] += 1
                            continue
                        seen[key] = dict(a)
                    else:
                        warnings.append(f"{ref}: no transaction ID; duplicate detection unavailable.")
                        account["activity_complete"] = False
                    item["date"] = date(a.get("tradeDate") or a.get("dateTime") or a.get("reportDate"))
                    if not item["date"] or not start <= item["date"] <= end:
                        raise ValueError(f"{ref}: missing or out-of-period transaction date")
                    if tag == "Trade":
                        item.update({"side": a.get("buySell"), "proceeds": number(a.get("proceeds")),
                                     "commission": number(a.get("ibCommission")),
                                     "commission_currency": a.get("ibCommissionCurrency", ""),
                                     "net_cash": number(a.get("netCash"))})
                        if (item["side"] == "BUY" and item["quantity"] < 0) or (item["side"] == "SELL" and item["quantity"] > 0):
                            raise ValueError("Trade direction conflicts with signed quantity")
                        if (a.get("origTradeID", "") not in ("", "0") or a.get("transactionType", "ExchTrade") not in ("ExchTrade", "Trade") or item["side"] not in ("BUY", "SELL")):
                            account["activity_complete"] = False
                            warnings.append(f"{ref}: correction/nonstandard trade requires manual review.")
                        account["trades"].append(item)
                    else:
                        item.update({"currency": a.get("currency", ""), "amount": number(a.get("amount")), "type": a.get("type", "unknown")})
                        if item["amount"] is None:
                            raise ValueError(f"{ref}: cash amount missing")
                        account["cash_transactions"].append(item)
                elif tag == "CashReportCurrency":
                    currency = a.get("currency", "")
                    if detail == "BASECURRENCY" and currency != "BASE_SUMMARY":
                        raise ValueError(f"{ref}: BaseCurrency cash requires BASE_SUMMARY currency")
                    if currency in cash_keys:
                        raise ValueError("Duplicate cash balance currency")
                    cash_keys.add(currency)
                    account["cash_balances"].append({"source_ref": ref, "currency": currency, "ending_cash": number(a.get("endingCash")), "as_of": end})
                elif tag in ("EquitySummaryInBase", "EquitySummaryByReportDateInBase"):
                    if a.get("total"):
                        navs.append((number(a["total"]), ref))
                elif tag == "ChangeInNAV" and a.get("endingValue"):
                    navs.append((number(a["endingValue"]), ref))
        if lot_keys - position_keys:
            account["positions_complete"] = False
            warnings.append("Some instruments have only tax lots; re-export SUMMARY Open Positions.")
        for tag, field in (("Trade", "trades"), ("CashTransaction", "cash_transactions")):
            if list(statement.iter(tag)) and not account[field]:
                account["activity_complete"] = False
                warnings.append(f"No supported {tag} detail rows retained; inspect ignored rows.")
        if len({n[0] for n in navs}) > 1:
            raise ValueError("Conflicting ending NAV observations")
        if navs:
            account["reported_nav"] = {"value": navs[0][0], "source_refs": [n[1] for n in navs]}
        if not account["cash_balances"]:
            warnings.append("Ending Cash Report missing; cash transactions are not cash balances.")
        account["ignored_rows"] = dict(ignored)
        result["accounts"].append(account)
    return result
