# DEMO Synthetic Company — limited fundamental analysis example

**Entirely fictional training fixture. No real company, security or investment recommendation.**

Information cutoff: 2026-03-01. Reporting currency: USD. Status: completed limited numerical review; qualitative classification, resilience and valuation remain unassessed.

## Conclusion

The fictional series shows improving reported profitability and positive cash generation over 2023–2025. Revenue grows 10% in each observed year; net margin rises from 10% to 12%; CFO less gross PPE purchases rises from $90 to $130. These observations support an improving numerical trend within the fixture. They cannot establish a durable business, sustainable distributions or an attractive share price. The most consequential gaps are the underlying business/notes, financing terms and a dated market price. [Calculation workpaper](2026-03-01-DEMO-annual-workpaper.md)

## Evidence and coverage

The [synthetic scraper-format CSV](../tests/fixtures/synthetic-report.csv) contains 48 fictional facts for three calendar-year annual periods, ending 2023-12-31 through 2025-12-31. Their assigned filing dates precede the cutoff. SHA-256: `2de8ae7e31345c24e8338f22debe27dadc3da9575c2b699c63e8d484e7335629`.

The [JSON audit](2026-03-01-DEMO-annual-workpaper.json) preserves raw records, dates, tags, units, selected observations and metric formulas. All 48 facts are selected; there are no adapter-error rows. This is not evidence of complete filings: the fixture contains no filing documents, audit opinion, MD&A, segments, debt maturity schedule or market observations. The `example.invalid` locator is intentionally fictional and is not a retrieved source.

## Business and classification

“Steady compounder” names the demonstration playbook, not an established conclusion. Moderate consistent revenue growth suggests a question for that playbook, but industry, product economics, competitive position and durability are absent. Classification remains provisional. The [growth/income playbook](../references/scenario-growth-and-income.md) requires business evidence before confirming this category.

## Financial performance and accounting quality

Revenue is $1,000, $1,100 and $1,210; net income is $100, $121 and $145.20. Net income/revenue therefore gives 10%, 11% and 12% net margins. Diluted EPS rises from $1.00 to $1.21 to $1.452 while weighted-average diluted shares remain 100 in each period; within this fixture, share shrinkage does not explain the EPS increase. These are reported-basis calculations with no normalization adjustments. CSV records 2/18/34, 3/19/35, 9/25/41 and 10/26/42. [Audit](2026-03-01-DEMO-annual-workpaper.json)

CFO of $130/$150/$180 exceeds earnings in each period. Subtracting gross PPE purchases of $40/$45/$50 yields an FCF proxy of $90/$105/$130. The proxy is not FCFF or distributable cash: leases, intangible investment and other mandatory uses are not documented. CSV records 7/23/39 and 8/24/40. [Workpaper](2026-03-01-DEMO-annual-workpaper.md)

Inventory grows 20% in 2024 and approximately 16.7% in 2025, faster than 10% revenue growth. This warrants investigation of demand, stocking policy and obsolescence; it does not establish manipulation or impairment. Formula: current inventory/prior inventory minus one, using records 17/33/49. Notes and recognition policies are unavailable, so earnings quality remains unassessed. [Audit](2026-03-01-DEMO-annual-workpaper.json)

## Financial resilience and capital allocation

The latest current ratio is $450/$170, approximately 2.65; working capital is $280. Preliminary NCAV is $450 minus $340 total liabilities, or $110 before additional senior claims and realization costs. Cash is $100, but restrictions are unknown. CSV records 46/47/44/48. [Workpaper](2026-03-01-DEMO-annual-workpaper.md)

Debt components, covenants, maturities, restricted cash, distributions, acquisitions and management incentives are absent. No total-debt, net-debt, liquidity-runway or capital-allocation conclusion follows from these balances. A conservative value screen is incomplete: three years cannot establish a long earnings or dividend record, and the debt and valuation tests lack inputs.

## Valuation and downside

No company valuation range, margin of safety or price recommendation is supported. There is no price, documented normalized earning-power forecast, discount-rate rationale or complete capital-structure bridge. The calculator examples for [DCF](2026-03-01-synthetic-dcf.json), [earnings](2026-03-01-synthetic-earnings.json), [assets](2026-03-01-synthetic-asset.json), [liquidity](2026-03-01-synthetic-stress.json) and [costs](2026-03-01-synthetic-cost.json) contain independent fictional assumptions solely to demonstrate executable models; they are not valuations or forecasts of DEMO.

A company-specific downside case needs the cash-use schedule, refinancing constraints and evidence for operating sensitivity. Neither positive current cash generation nor preliminary NCAV guarantees survival or common-shareholder recovery.

## Counter-thesis and opportunity cost

The strongest counterargument is that a smooth three-year series omits the facts needed to assess durability: segment deterioration, cyclical peaks, working-capital reversals, recurring adjustments or future funding needs could reverse the apparent improvement. Inventory outgrowing revenue is the numerical question to investigate first.

The evidence does not establish an advantage over diversified low-cost ownership. No benchmark-performance or cost comparison is made because compatible current product and market inputs are absent. This follows the uncertainty and opportunity-cost questions in the [risk overlay](../references/risk-and-opportunity-cost.md).

## What would change the conclusion

- Official business and segment disclosures could support or reject the steady-compounder classification.
- Receivable/inventory notes, recognition policies and a working-capital bridge could clarify cash and earnings quality.
- Debt, covenant, liquidity and senior-claim disclosures could support a survival assessment.
- A dated price and defensible normalized earnings/FCFF or asset bridge could support conditional valuation.
- Longer earnings and dividend histories would make more value-screen criteria assessable.

The review is complete within its declared fictional, numerical scope. The missing evidence prevents stronger investment conclusions.
