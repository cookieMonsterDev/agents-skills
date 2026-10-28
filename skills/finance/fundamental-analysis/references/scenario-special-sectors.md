# Specialist businesses and non-company instruments

This is a routing boundary, not a complete sector valuation manual: it keeps the general industrial calculations from answering the wrong question. `analyze_report.py` cannot infer industry from the CSV; classify the business before interpreting ratios. Mark specialist metrics unassessed until their definitions and issuer disclosures are available.

## Banks and lenders

Read regulatory capital, asset quality, loan-loss allowances, funding/deposit mix, liquidity, duration mismatch and interest-rate sensitivity. Deposits and financing cash flows are integral to operations; generic industrial debt/EBITDA, working-capital and CFO-minus-capex conclusions are usually unhelpful. Use attributable earnings, tangible book and returns with capital adequacy evidence; excess-capital assumptions need regulatory and management constraints. Obtain current jurisdiction-specific definitions from the issuer/regulator.

## Insurers

Separate underwriting results from investment results; inspect reserves and development, reinsurance collectability, catastrophe exposure, asset/liability duration and solvency capital. Float is not unrestricted cash. Combined ratio and other specialist measures need their issuer-defined denominator and business scope. General return or asset models need claim and capital adjustments.

## REITs and property companies

Reconcile issuer FFO/AFFO to GAAP earnings using the applicable current definition; inspect maintenance capex, occupancy, lease expirations, tenant concentration, secured debt and maturities. Depreciation can make plain P/E misleading, while adjusted cash metrics can omit real recurring expenditure. Separate property value from debt/claims and avoid adding property value to capitalized rent income from the same properties.

## Regulated utilities

Inspect permitted versus earned returns, rate base, regulatory lag, funding of capex and allowed recovery, in addition to liquidity and debt. For a value screen, use utility-specific leverage criteria. Industrial current-ratio cutoffs are not universal here.

## ETFs and ETCs in a portfolio CSV

Retain these instruments in the coverage summary and route to the sibling scraper's fund/ETC references for documents. The company helper rejects non-stock targets. Assess mandate/index, exposure, fees, concentration, tracking, structure and relevant custody/collateral/counterparty terms from official documents; fund NAV, holdings weights and expenses are not company revenue, earnings or leverage.

Finish a requested company report without pretending to complete a fund analysis from company ratios. For a mixed portfolio request, provide separate limited fund/ETC assessments when official evidence is available. Explain missing coverage precisely.
