# DEMO — computed financial evidence

Status: analyst review pending. This is a calculation workpaper, not a completed investment analysis.

Information cutoff: 2026-03-01. Currency: USD. Duration: annual.
Input: `tests/fixtures/synthetic-report.csv`. SHA-256: `2de8ae7e31345c24e8338f22debe27dadc3da9575c2b699c63e8d484e7335629`.

## Coverage

- fact: 48 records

## Data limitations

- Reporting periods precede the cutoff; review the latest filing and intervening events for staleness.
- Missing/ambiguous values stay unavailable. Facts use actual start/end dates; publication dates enforce the cutoff.
- All source records, rejected observations, formulas and units are in the companion JSON.

## 2023-01-01 to 2023-12-31

Reported facts:

- assets: 800 USD (CSV record 11; us-gaap:Assets; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- capex: 40 USD (CSV record 8; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- cash: 100 USD (CSV record 16; us-gaap:CashAndCashEquivalentsAtCarryingValue; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- cfo: 130 USD (CSV record 7; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- current_assets: 350 USD (CSV record 14; us-gaap:AssetsCurrent; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- current_liabilities: 150 USD (CSV record 15; us-gaap:LiabilitiesCurrent; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- diluted_shares: 100 shares (CSV record 10; us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- eps: 1 USD/shares (CSV record 9; us-gaap:EarningsPerShareDiluted; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- equity: 500 USD (CSV record 13; us-gaap:StockholdersEquity; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- gross_profit: 400 USD (CSV record 4; us-gaap:GrossProfit; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- interest_expense: 10 USD (CSV record 6; us-gaap:InterestExpense; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- inventory: 50 USD (CSV record 17; us-gaap:InventoryNet; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- liabilities: 300 USD (CSV record 12; us-gaap:Liabilities; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- net_income: 100 USD (CSV record 3; us-gaap:NetIncomeLoss; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- operating_income: 150 USD (CSV record 5; us-gaap:OperatingIncomeLoss; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)
- revenue: 1,000 USD (CSV record 2; us-gaap:Revenues; filed 2024-02-15; accession SYNTHETIC-2023; https://example.invalid/demo/fictional-annual-report)

Derived metrics:

- net_margin: 0.1; net_income / revenue; unit ratio; records [3, 2].
- gross_margin: 0.4; gross_profit / revenue; unit ratio; records [4, 2].
- operating_margin: 0.15; operating_income / revenue; unit ratio; records [5, 2].
- cfo_margin: 0.13; cfo / revenue; unit ratio; records [7, 2].
- cash_conversion: 1.3; cfo / net_income; unit ratio; records [7, 3].
- current_ratio: 2.33333; current_assets / current_liabilities; unit ratio; records [14, 15].
- liabilities_to_assets: 0.375; liabilities / assets; unit ratio; records [12, 11].
- interest_coverage_proxy: 15; operating_income / interest_expense; unit ratio; records [5, 6].
- fcf_proxy: 90; cfo - nonnegative gross PPE purchases (not FCFF or FCFE); unit reporting_currency; records [7, 8].
- net_current_assets: 200; current_assets - current_liabilities; unit reporting_currency; records [14, 15].
- ncav_before_senior_claims: 50; current_assets - total_liabilities; preferred/NCI and realization costs still unadjusted; unit reporting_currency; records [14, 12].

## 2024-01-01 to 2024-12-31

Reported facts:

- assets: 870 USD (CSV record 27; us-gaap:Assets; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- capex: 45 USD (CSV record 24; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- cash: 100 USD (CSV record 32; us-gaap:CashAndCashEquivalentsAtCarryingValue; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- cfo: 150 USD (CSV record 23; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- current_assets: 400 USD (CSV record 30; us-gaap:AssetsCurrent; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- current_liabilities: 160 USD (CSV record 31; us-gaap:LiabilitiesCurrent; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- diluted_shares: 100 shares (CSV record 26; us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- eps: 1.21 USD/shares (CSV record 25; us-gaap:EarningsPerShareDiluted; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- equity: 550 USD (CSV record 29; us-gaap:StockholdersEquity; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- gross_profit: 440 USD (CSV record 20; us-gaap:GrossProfit; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- interest_expense: 10 USD (CSV record 22; us-gaap:InterestExpense; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- inventory: 60 USD (CSV record 33; us-gaap:InventoryNet; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- liabilities: 320 USD (CSV record 28; us-gaap:Liabilities; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- net_income: 121 USD (CSV record 19; us-gaap:NetIncomeLoss; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- operating_income: 181.5 USD (CSV record 21; us-gaap:OperatingIncomeLoss; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)
- revenue: 1,100 USD (CSV record 18; us-gaap:Revenues; filed 2025-02-15; accession SYNTHETIC-2024; https://example.invalid/demo/fictional-annual-report)

Derived metrics:

- net_margin: 0.11; net_income / revenue; unit ratio; records [19, 18].
- gross_margin: 0.4; gross_profit / revenue; unit ratio; records [20, 18].
- operating_margin: 0.165; operating_income / revenue; unit ratio; records [21, 18].
- cfo_margin: 0.136364; cfo / revenue; unit ratio; records [23, 18].
- cash_conversion: 1.23967; cfo / net_income; unit ratio; records [23, 19].
- current_ratio: 2.5; current_assets / current_liabilities; unit ratio; records [30, 31].
- liabilities_to_assets: 0.367816; liabilities / assets; unit ratio; records [28, 27].
- interest_coverage_proxy: 18.15; operating_income / interest_expense; unit ratio; records [21, 22].
- fcf_proxy: 105; cfo - nonnegative gross PPE purchases (not FCFF or FCFE); unit reporting_currency; records [23, 24].
- net_current_assets: 240; current_assets - current_liabilities; unit reporting_currency; records [30, 31].
- ncav_before_senior_claims: 80; current_assets - total_liabilities; preferred/NCI and realization costs still unadjusted; unit reporting_currency; records [30, 28].
- revenue_growth: 0.1; current revenue / prior revenue - 1; unit fraction; records [2, 18].
- net_income_growth: 0.21; current net_income / prior net_income - 1; unit fraction; records [3, 19].
- eps_growth: 0.21; current eps / prior eps - 1; unit fraction; records [9, 25].
- inventory_growth: 0.2; current inventory / prior inventory - 1; unit fraction; records [17, 33].
- receivables_growth: unavailable: missing_or_ambiguous_input; current receivables / prior receivables - 1; unit fraction; records [].
- diluted_shares_growth: 0; current diluted_shares / prior diluted_shares - 1; unit fraction; records [10, 26].

## 2025-01-01 to 2025-12-31

Reported facts:

- assets: 950 USD (CSV record 43; us-gaap:Assets; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- capex: 50 USD (CSV record 40; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- cash: 100 USD (CSV record 48; us-gaap:CashAndCashEquivalentsAtCarryingValue; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- cfo: 180 USD (CSV record 39; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- current_assets: 450 USD (CSV record 46; us-gaap:AssetsCurrent; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- current_liabilities: 170 USD (CSV record 47; us-gaap:LiabilitiesCurrent; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- diluted_shares: 100 shares (CSV record 42; us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- eps: 1.452 USD/shares (CSV record 41; us-gaap:EarningsPerShareDiluted; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- equity: 610 USD (CSV record 45; us-gaap:StockholdersEquity; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- gross_profit: 484 USD (CSV record 36; us-gaap:GrossProfit; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- interest_expense: 10 USD (CSV record 38; us-gaap:InterestExpense; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- inventory: 70 USD (CSV record 49; us-gaap:InventoryNet; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- liabilities: 340 USD (CSV record 44; us-gaap:Liabilities; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- net_income: 145.2 USD (CSV record 35; us-gaap:NetIncomeLoss; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- operating_income: 217.8 USD (CSV record 37; us-gaap:OperatingIncomeLoss; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)
- revenue: 1,210 USD (CSV record 34; us-gaap:Revenues; filed 2026-02-15; accession SYNTHETIC-2025; https://example.invalid/demo/fictional-annual-report)

Derived metrics:

- net_margin: 0.12; net_income / revenue; unit ratio; records [35, 34].
- gross_margin: 0.4; gross_profit / revenue; unit ratio; records [36, 34].
- operating_margin: 0.18; operating_income / revenue; unit ratio; records [37, 34].
- cfo_margin: 0.14876; cfo / revenue; unit ratio; records [39, 34].
- cash_conversion: 1.23967; cfo / net_income; unit ratio; records [39, 35].
- current_ratio: 2.64706; current_assets / current_liabilities; unit ratio; records [46, 47].
- liabilities_to_assets: 0.357895; liabilities / assets; unit ratio; records [44, 43].
- interest_coverage_proxy: 21.78; operating_income / interest_expense; unit ratio; records [37, 38].
- fcf_proxy: 130; cfo - nonnegative gross PPE purchases (not FCFF or FCFE); unit reporting_currency; records [39, 40].
- net_current_assets: 280; current_assets - current_liabilities; unit reporting_currency; records [46, 47].
- ncav_before_senior_claims: 110; current_assets - total_liabilities; preferred/NCI and realization costs still unadjusted; unit reporting_currency; records [46, 44].
- revenue_growth: 0.1; current revenue / prior revenue - 1; unit fraction; records [18, 34].
- net_income_growth: 0.2; current net_income / prior net_income - 1; unit fraction; records [19, 35].
- eps_growth: 0.2; current eps / prior eps - 1; unit fraction; records [25, 41].
- inventory_growth: 0.166667; current inventory / prior inventory - 1; unit fraction; records [33, 49].
- receivables_growth: unavailable: missing_or_ambiguous_input; current receivables / prior receivables - 1; unit fraction; records [].
- diluted_shares_growth: 0; current diluted_shares / prior diluted_shares - 1; unit fraction; records [26, 42].

## Analyst completion

Apply the relevant scenario reference and report-template.md: business/category evidence, notes and MD&A, normalized earnings, valuation assumptions, downside, counter-thesis, opportunity cost, and unresolved questions. Save the completed analysis as a separate Markdown report.
