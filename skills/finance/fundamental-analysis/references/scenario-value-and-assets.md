# Value screens, margin of safety and asset-backed value

Use when asked to screen for conservative or neglected value, or to value identifiable assets. A screen filters research candidates; it does not decide a purchase.

## Conservative value screen

Before screening, write down each criterion, its threshold and why it fits this company and today's conditions. Thresholds are analyst policy: state them in the report and never present them as an authoritative standard. For each criterion record pass, fail, unknown or not applicable, with the inputs, dates, evidence and reason. A history shorter than the criterion requires is unknown, never a pass.

Typical criteria to choose from, adapted to the business:

- Size: a minimum revenue or asset base, stated in current currency with the reason for the level chosen.
- Financial condition: current ratio and long-term debt relative to working capital for industrials; debt relative to equity for regulated utilities, where an industrial liquidity test does not apply unchanged.
- Earnings stability: positive earnings over a stated number of years.
- Distribution record: uninterrupted dividends over a stated number of years, when income matters to the thesis.
- Growth: per-share earnings growth between multi-year endpoint averages, listing the actual years and a consistent per-share basis.
- Price: maximum P/E on multi-year average earnings and maximum P/B, optionally with a combined P/E × P/B ceiling. Positive earnings and book value are prerequisites; negative multiples are inapplicable.

Use `analyze_report.py` for available annual evidence, current ratio and working capital, then source longer histories and total-debt definitions manually.

## Neglected-value screen

For a deliberately more permissive screen (for example lower liquidity requirements, a shorter clean-earnings record, a current dividend, and price near net tangible assets), state the chosen thresholds and earnings comparison interval with their rationale.

Investigate why value is neglected, whether earning power is deteriorating and what evidence could close the price/value gap. Greater investigative effort is part of this lens; it does not make a weak company safe by definition.

## Asset play and NCAV

Identify ownership, encumbrances, carrying values, independent realizable-value evidence, costs/taxes, liabilities and additional senior claims. Explain the catalyst and time to realization. Distinguish restricted cash, operating cash and genuinely distributable excess cash. Asset value and the value of earnings produced by that same asset cannot both be added without a separation bridge.

The helper's `ncav_before_senior_claims = current assets - total liabilities` is preliminary. Subtract preferred/NCI and other senior equity claims not already included, and consider burn and realization costs. Working capital subtracts only current liabilities and is not NCAV. A purchase rule based on a fixed discount to NCAV is a convention that assumes diversification across many such opportunities, not a single-stock safety test.

Use `scenario_models.py asset` for explicit recovery haircuts. It accepts non-overlapping asset components, all liabilities, additional claims and realization costs. Accounting book value is not an appraisal. For assets worth more than carrying value, document an independent valuation separately; the conservative helper only models recovery fractions from zero to one. An illustrative haircut is an assumption, not market evidence.

Complete with an asset-to-common-equity bridge, conservative/base recovery assumptions, dilution where relevant, a realization mechanism and the impediments to shareholders receiving value.

## Margin of safety

Use a defensible conservative value, not a price multiple selected to meet a desired answer. The helper reports the modern convention `(value - price) / value` for positive value and separately reports `(value / price) - 1` as upside. Match enterprise/equity and aggregate/per-share units before comparison. A discount on uncertain estimates can disappear when assumptions change; show the sensitivity and the strongest argument that this is a value trap.
