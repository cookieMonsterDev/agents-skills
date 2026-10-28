# Accounting quality and metric validity

Use the generated evidence to choose where to read deeper. Investigate material audit qualifications, restatements, going-concern language, changes in recognition/estimates, related parties, contingent liabilities, acquisitions, pensions, leases and taxes in the actual filing. A CSV cannot establish a clean audit opinion or absence of these risks.

## Reconcile the economics

- Explain revenue changes through volume, price/mix, acquisitions/disposals, FX and recognition where disclosed. Compare receivables and inventory with sales; rising balances are a question to investigate, not proof of manipulation.
- Reconcile reported earnings to any normalized estimate, item by item with tax and attribution effects. Track recurring “one-time” costs. Preserve share-based compensation as an economic cost and inspect dilution, repurchases, issuance and conversions.
- Compare cash from operations with earnings and working-capital changes. CFO boosted by payables, receivable sales or advance collections may reverse. Reconcile IFRS/US GAAP interest/dividend classification differences before cross-company cash comparisons.
- Gross PPE purchases are a cash outflow, represented nonnegative in the supported payment tags. `FCF proxy = CFO - PPE purchases`; acquisitions, lease principal and intangible investment may remain outside that proxy. A missing capex tag leaves FCF unavailable; it does not mean capex is zero. Verify signs before mapping a new concept.
- Retain reported basic/diluted EPS and its accounting scope. Consolidated profit and profit attributable to common shareholders differ; basic, diluted, weighted-average and point-in-time shares serve different purposes. ADR ratios, currency conversions and share splits need explicit reconciliation.

## Calculation boundaries

The helper computes margins, cash conversion, current ratio, liabilities/assets, operating-income/interest coverage proxy, FCF proxy, working capital and preliminary NCAV when exact inputs exist. It deliberately leaves total debt, net debt, EBITDA, ROE and ROIC for a documented bridge: their definitions need evidence that the core CSV does not guarantee.

- Margins: same interval and scope numerator/revenue, with positive revenue. Negative earnings can produce a meaningful negative margin.
- Cash conversion: CFO/positive net income; losses make the ratio unhelpful. Show the actual loss and cash flow instead.
- Interest coverage proxy: operating income/positive interest expense. Explain departures from EBIT and whether interest is net, gross or capitalized; a missing/zero expense is not infinite safety.
- ROE: attributable common earnings/average common equity on aligned opening/closing dates. Negative or tiny equity requires explanation. ROIC: define NOPAT, operating assets/liabilities, cash and lease treatment before calculation. Neither is automatic in the helper.
- Total debt: reconcile short-term borrowings, current maturities, noncurrent borrowings and any leases treated as debt without overlapping tags. `LongTermDebt` alone is not total debt; liabilities are not interchangeable with debt. Review cash restrictions and operating cash needs before a net-debt bridge.
- Balance check: assets minus liabilities minus **total** equity including NCI. Parent equity alone need not balance. Allow disclosed rounding, then inspect unexplained differences.
- P/E: positive normalized or reported attributable EPS, clearly named, with matching price/share basis. P/B: positive attributable book equity/share; intangible intensity and impairments affect its meaning.
- Working capital: current assets minus current liabilities. Preliminary NCAV: current assets minus **all** liabilities; subtract preferred and other senior equity claims not already deducted before calling it common-equity value.

Losses, mixed currencies, changing fiscal calendars, scope changes and competing tags are interpretation gates. Keep the metric unavailable until the basis is reconciled. When two issuers' accounting differs, compare explicitly normalized measures or describe the limitation.

## Source grounding

These operational formulas are common analytical conventions, not regulatory definitions.

Current guidance checked 2026-09-15: [SEC non-GAAP interpretations, Q102.07](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures) explains that free cash flow lacks a uniform definition and needs calculation/reconciliation; [SEC financial-statement guide](https://www.sec.gov/about/reports-publications/investorpubsbegfinstmtguide) identifies notes and MD&A as necessary context. Recheck current guidance for legal/accounting assertions in a live report.
