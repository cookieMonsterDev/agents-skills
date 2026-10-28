# IBKR Activity Flex input

Supported: local Activity Flex XML with `FlexQueryResponse`, `FlexStatements`, or
`FlexStatement` root, including XML namespaces. One statement period per account
per run. The parser rejects repeated accounts rather than double-counting
overlapping snapshots. It accepts UTF-8/UTF-16 and rejects DTD/entity declarations.
PDF, CSV, tax forms and Trade Confirmation exports need separate adapters.

## Recommended export

Export all instruments/accounts intended for analysis, with no symbol or asset
filters, using the same end date. Include:

- Account Information: account ID and base currency.
- Open Positions at SUMMARY detail: account ID, report date, conid, symbol,
  description, ISIN/security ID, asset/subcategory, listing exchange, currency,
  position, position value, FX rate to base, cost basis and unrealized P&L.
- Cash Report: currency, ending cash, report/to date; include BASE_SUMMARY for a
  multi-currency total. The portfolio export labels this row
  `currency="BASE_SUMMARY" levelOfDetail="BaseCurrency"`; it is supported alongside
  legacy rows with SUMMARY or omitted detail. Trade-date and settled cash are
  different measures.
- Net Asset Value (NAV) in Base: `EquitySummaryInBase` with dated
  `EquitySummaryByReportDateInBase` children (`total`), a legacy summary carrying
  `total` directly, or Change in NAV (`endingValue`). If NAV
  includes accruals/liabilities beyond positions and cash, investigate the
  reconciliation residual; the helper intentionally withholds allocation weights.
- Trades at EXECUTION detail: transaction/trade ID, trade date, signed quantity,
  proceeds, net cash, commission and its currency, identifiers and buy/sell.
- Cash Transactions at DETAIL level: ID, type, amount, currency, date.
- Corporate Actions, Transfers and stock grants when applicable for analyst review.

Actual field names are configurable by IBKR exports. Missing optional values
remain null; invalid supplied numbers/dates fail parsing rather than becoming
zero. Row dates omitted in ending balance sections inherit the statement end
date. Non-ending dated rows are skipped and positions marked incomplete.

## Accounting choices

Use summary positions, not summary plus tax lots. Use executions, not execution
plus order totals. Identical duplicate trade/cash IDs are dropped; conflicting
duplicates fail. Order IDs are not execution IDs: multiple partial fills can
legitimately share one order. Duplicate position summaries/cash currencies fail.
Model-level rows are omitted with warnings; supply an account-level export.

`positionValue * fxRateToBase` converts a supplied position value to base currency.
Do not calculate market value from trade prices, or assume `quantity * price`
works for bonds, options and futures. Trade-date FX is not closing FX for cash.
BASE_SUMMARY cash is already aggregated and must not be added to currency rows.
The helper uses only that summary or a single matching base-currency cash row;
other cash conversion requires separately verified ending FX.
Daily NAV rows require a date matching the statement end; earlier or undated
daily observations are skipped. They are never summed or treated as separate
account statements. If ending NAV appears in multiple supported sections, the
values must agree. A BaseCurrency cash row must identify currency as BASE_SUMMARY.

Signed trade quantities are **net traded units during the statement window**.
They are not ending holdings without opening positions and all transfers,
corporate actions, grants and corrections. The helper does not reconstruct lots,
tax basis, realized returns or current holdings from activity. Corrections and
nonstandard trades mark activity provisional. Corporate actions/transfers/grants
are inventoried but not normalized; inspect the source if material.

An activity-only declaration with trades and cash transactions produces an
activity workpaper and research list, with all portfolio weights unavailable.
A full portfolio export adds ending positions, Cash Report and NAV; reconcile
these before using allocation weights. Both export shapes remain supported.
Do not silently infer account inception from its first deposit. Dividends received
are not total return or dividend yield.

## Primary semantics references

- [IBKR Cash Report, Flex](https://www.ibkrguides.com/reportingreference/reportguide/cash%20reportfq.htm): ending cash, currency summary and settlement distinction.
- [IBKR Change in NAV, Flex](https://ibkrguides.com/reportingreference/reportguide/changeinnav_fq.htm): ending value and components beyond transactions.
- [IBKR Cash Transactions, Flex](https://ibkrguides.com/reportingreference/reportguide/cash%20transactionsfq.htm): transaction currency and FX rate direction.
- [IBKR Open Position Summary](https://ibkrguides.com/reportingreference/reportguide/openpositionsummary.htm): end-period position market values.

Checked when authored on 2026-10-01; recheck official field definitions when adding
an unfamiliar export variant. These references describe semantics, not a complete
machine-readable XML schema.
