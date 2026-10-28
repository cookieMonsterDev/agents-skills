# Financial Reports Topic Map

Routing aid for official issuer numbers. Filings are the source of truth; aggregators are normalized copies.

## Skill adapters (this repo)

Identifier first, then one adapter:

| Entity | Identifier | Adapter | Scenario |
| ------ | ---------- | ------- | -------- |
| US equity | ticker → zero-padded 10-digit CIK | `edgar` | [scenario-us-equity-edgar.md](scenario-us-equity-edgar.md) |
| Foreign issuer with a US listing | CIK; 20-F / 6-K | `edgar` | [scenario-foreign-issuer.md](scenario-foreign-issuer.md) |
| iShares UCITS ETF | ISIN in `scripts/data/ishares_catalog.json` | `ishares` | [scenario-ucits-etf.md](scenario-ucits-etf.md) |
| iShares Physical ETC | ISIN in the same catalog | `ishares` | [scenario-precious-metals-etc.md](scenario-precious-metals-etc.md) |
| Anything else | local company number / LEI / ISIN | none (error row) | this map's Non-US section |

A miss gets a new catalog row or adapter; aggregators stay unofficial. Non-US work needs the local company number, LEI or ISIN, then the home-market repository.

## Getting Started

- [SEC EDGAR full-text search](https://www.sec.gov/edgar/search/)
- [EDGAR company search](https://www.sec.gov/edgar/searchedgar/companysearch)
- [Accessing EDGAR data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data)
- [EDGAR data APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Ticker to CIK map](https://www.sec.gov/files/company_tickers.json)
- [How to read a 10-K](https://www.sec.gov/answers/reada10k.htm)
- [Form 10-K](https://www.sec.gov/files/form10-k.pdf)
- [Form 10-Q](https://www.sec.gov/files/form10-q.pdf)
- [Form 8-K](https://www.sec.gov/files/form8-k.pdf)
- [Form 20-F (foreign private issuers)](https://www.sec.gov/files/form20-f.pdf)
- [Form 6-K (foreign current reports)](https://www.sec.gov/files/form6-k.pdf)
- [Regulation S-X (financial statement form and content)](https://www.ecfr.gov/current/title-17/chapter-II/part-210)
- [US GAAP Accounting Standards Codification](https://asc.fasb.org/)
- [IAS 1 Presentation of Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/)
- [IFRS 18 Presentation and Disclosure (replaces IAS 1 from 2027)](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/)

## Structured Filings (XBRL / iXBRL)

Use these when you want machine-readable line items rather than HTML. Company Facts covers standardized `us-gaap`, `ifrs-full`, `dei`, and `srt` tags only; company-specific extension tags live in the raw filing.

- [Company submissions (filing history)](https://data.sec.gov/submissions/CIK##########.json)
- [Company facts (all XBRL concepts)](https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json)
- [Company concept (one tag over time)](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/Revenues.json)
- [Frames (one tag across all filers)](https://data.sec.gov/api/xbrl/frames/us-gaap/Revenues/USD/CY2024.json)
- [DERA financial statement data sets (face statements)](https://www.sec.gov/dera/data/financial-statement-data-sets.html)
- [DERA financial statement and notes data sets](https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html)
- [FASB US GAAP XBRL taxonomy](https://xbrl.fasb.org/)
- [IFRS Accounting Taxonomy](https://www.ifrs.org/issued-standards/ifrs-taxonomy/)
- [ESMA ESEF (EU tagged annual reports)](https://www.esma.europa.eu/issuer-disclosure/electronic-reporting)
- [Extract statements with EdgarTools](https://edgartools.readthedocs.io/en/stable/guides/extract-statements/)

## Income Statement

Revenue, COGS, gross profit, operating expenses, operating income, interest, taxes, net income, EPS (basic and diluted).

- [Form 10-K Item 8 — financial statements](https://www.sec.gov/files/form10-k.pdf)
- [Regulation S-X Article 5 (commercial and industrial line items)](https://www.ecfr.gov/current/title-17/chapter-II/part-210/subpart-E)
- [ASC 220 Comprehensive Income](https://asc.fasb.org/220/tableOfContent)
- [ASC 260 Earnings Per Share](https://asc.fasb.org/260/tableOfContent)
- [IAS 33 Earnings per Share](https://www.ifrs.org/issued-standards/list-of-standards/ias-33-earnings-per-share/)
- [SEC company concept — Revenues](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/Revenues.json)
- [SEC company concept — NetIncomeLoss](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/NetIncomeLoss.json)
- [SEC company concept — OperatingIncomeLoss](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/OperatingIncomeLoss.json)

Common US-GAAP tags to try, in order: `RevenueFromContractWithCustomerExcludingAssessedTax`, `Revenues`, `SalesRevenueNet`, `CostOfGoodsAndServicesSold`, `GrossProfit`, `OperatingIncomeLoss`, `InterestExpense`, `IncomeTaxExpenseBenefit`, `NetIncomeLoss`, `EarningsPerShareBasic`, `EarningsPerShareDiluted`.

## Balance Sheet

Current and non-current assets, current and non-current liabilities, shareholders' equity.

- [ASC 210 Balance Sheet](https://asc.fasb.org/210/tableOfContent)
- [ASC 205 Presentation of Financial Statements](https://asc.fasb.org/205/tableOfContent)
- [IAS 1 — statement of financial position](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/)
- [SEC company concept — Assets](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/Assets.json)
- [SEC company concept — AssetsCurrent](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/AssetsCurrent.json)
- [SEC company concept — Liabilities](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/Liabilities.json)
- [SEC company concept — StockholdersEquity](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/StockholdersEquity.json)

Point-in-time (stock) facts use the period-end value. Frame queries for balance-sheet tags append `I` (instant), for example `CY2024Q4I`.

## Cash Flow Statement

Operating, investing, and financing activities, plus free cash flow (derived: operating cash flow minus capital expenditures).

- [ASC 230 Statement of Cash Flows](https://asc.fasb.org/230/tableOfContent)
- [IAS 7 Statement of Cash Flows](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/)
- [SEC company concept — NetCashProvidedByUsedInOperatingActivities](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/NetCashProvidedByUsedInOperatingActivities.json)
- [SEC company concept — PaymentsToAcquirePropertyPlantAndEquipment](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json)

Quarterly flow facts in 10-Q filings are often year-to-date. Derive the standalone quarter by subtracting the prior YTD value. There is no Q4 10-Q; Q4 flows are FY minus Q1–Q3.

## Statement of Changes in Equity

Share issuance, buybacks, dividends paid, retained earnings movement. Needed for dilution analysis.

- [Form 10-K Item 8 — statement of stockholders' equity](https://www.sec.gov/files/form10-k.pdf)
- [ASC 505 Equity](https://asc.fasb.org/505/tableOfContent)
- [IAS 1 — statement of changes in equity](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/)
- [SEC company concept — PaymentsForRepurchaseOfCommonStock](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/PaymentsForRepurchaseOfCommonStock.json)
- [SEC company concept — PaymentsOfDividends](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/PaymentsOfDividends.json)
- [SEC company concept — ProceedsFromIssuanceOfCommonStock](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/ProceedsFromIssuanceOfCommonStock.json)
- [SEC company concept — RetainedEarningsAccumulatedDeficit](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/RetainedEarningsAccumulatedDeficit.json)
- [DEF 14A proxy statement (share plans, votes, dilution)](https://www.sec.gov/files/def14a.pdf)

Aggregators often skip this statement. Prefer the 10-K HTML/iXBRL equity roll-forward, then reconcile issuance/buybacks/dividends against the cash-flow financing section.

## Notes to the Financial Statements

Accounting policies, debt maturity schedules, lease obligations, contingencies. Face statements are not enough here.

- [ASC 235 Notes to Financial Statements](https://asc.fasb.org/235/tableOfContent)
- [ASC 470 Debt](https://asc.fasb.org/470/tableOfContent)
- [ASC 842 Leases](https://asc.fasb.org/842/tableOfContent)
- [ASC 450 Contingencies](https://asc.fasb.org/450/tableOfContent)
- [IAS 8 Accounting Policies](https://www.ifrs.org/issued-standards/list-of-standards/ias-8-accounting-policies-changes-in-accounting-estimates-and-errors/)
- [IFRS 16 Leases](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/)
- [IAS 37 Provisions, Contingent Liabilities and Contingent Assets](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/)
- [IFRS 7 Financial Instruments: Disclosures](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-7-financial-instruments-disclosures/)
- [DERA financial statement and notes data sets](https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html)
- [EdgarTools notes and disclosures](https://edgartools.readthedocs.io/en/stable/guides/extract-statements/)
- [EDGAR full-text search](https://efts.sec.gov/LATEST/search-index)

Company Facts omits most narrative notes and many dimensional tables. For debt maturities, lease schedules, and contingencies, parse the filing HTML or the DERA notes dataset.

## Segment Reporting

Revenue and operating income by business line and geography.

- [ASC 280 Segment Reporting](https://asc.fasb.org/280/tableOfContent)
- [IFRS 8 Operating Segments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-8-operating-segments/)
- [Form 10-K Item 1 — business description](https://www.sec.gov/files/form10-k.pdf)
- [DERA financial statement and notes data sets](https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html)

Segment tables are usually dimensional XBRL in the notes, not top-level Company Facts tags. Cross-check the MD&A narrative against the note; they should describe the same operating view.

## MD&A

Management's explanation of the numbers, liquidity, capital resources, known trends, and guidance.

- [Regulation S-K Item 303 (MD&A)](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.300/section-229.303)
- [Form 10-K Item 7](https://www.sec.gov/files/form10-k.pdf)
- [Form 10-Q Item 2](https://www.sec.gov/files/form10-q.pdf)
- [Form 20-F Item 5 — operating and financial review](https://www.sec.gov/files/form20-f.pdf)
- [SEC Financial Reporting Manual Topic 9](https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-9)
- [2020 MD&A modernization (Release 33-10890)](https://www.sec.gov/files/rules/final/2020/33-10890.pdf)
- [KPI and metrics guidance (Release 33-10751)](https://www.sec.gov/files/rules/interp/2020/33-10751.pdf)
- [IFRS Practice Statement 1 — Management Commentary](https://www.ifrs.org/issued-standards/list-of-standards/management-commentary-practice-statement-1/)
- [Form 8-K Item 2.02 — earnings releases](https://www.sec.gov/files/form8-k.pdf)
- [EDGAR full-text search](https://efts.sec.gov/LATEST/search-index)

MD&A is prose plus tables. It is not in Company Facts. Pull the 10-K/10-Q HTML (or the 8-K Exhibit 99.1 earnings release for the first cut of the quarter).

## Share Count, EPS, and Dilution

Weighted-average and period-end shares outstanding. Needed for anything per share.

- [ASC 260 Earnings Per Share](https://asc.fasb.org/260/tableOfContent)
- [IAS 33 Earnings per Share](https://www.ifrs.org/issued-standards/list-of-standards/ias-33-earnings-per-share/)
- [dei:EntityCommonStockSharesOutstanding (cover page)](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/dei/EntityCommonStockSharesOutstanding.json)
- [WeightedAverageNumberOfSharesOutstandingBasic](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/WeightedAverageNumberOfSharesOutstandingBasic.json)
- [WeightedAverageNumberOfDilutedSharesOutstanding](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/WeightedAverageNumberOfDilutedSharesOutstanding.json)
- [EarningsPerShareBasic](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/EarningsPerShareBasic.json)
- [EarningsPerShareDiluted](https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/EarningsPerShareDiluted.json)
- [10-K Item 5 — market for common equity](https://www.sec.gov/files/form10-k.pdf)
- [DEF 14A — equity compensation and dilution](https://www.sec.gov/files/def14a.pdf)

Period-end shares (`EntityCommonStockSharesOutstanding`) are for per-share book value and market cap. Weighted-average basic/diluted shares are for EPS. Option and RSU overhang lives in the stock-based compensation note and the proxy, not on the face statements.

## Ratios, Valuation, and Growth

Margins, ROE, ROIC, current ratio, debt-to-equity, interest coverage, P/E, P/B, EV/EBITDA, and multi-period growth. Compute from the statements above, or take a vendor's precomputed series (see Aggregators) and audit it against the filing.

Market-price inputs (for P/E, P/B, EV) are not in the filing. Pair statement data with a quote source, and use diluted EPS plus diluted shares for per-share valuation.

## Aggregators and Quote Sources

Normalized three-statement APIs. Useful for screening and time series; always spot-check material figures against EDGAR or the home-market filing. This skill does not call them.

- [Financial Modeling Prep developer docs](https://site.financialmodelingprep.com/developer/docs)
- [Alpha Vantage documentation](https://www.alphavantage.co/documentation/)
- [Polygon stocks financials](https://polygon.io/docs/stocks/get_vx_reference_financials)
- [SimFin](https://simfin.com/)
- [Finnhub stock fundamentals](https://finnhub.io/docs/api/financials-reported)
- [Yahoo Finance (unofficial; `yfinance`)](https://github.com/ranaroussi/yfinance)
- [OpenFIGI identifier mapping](https://www.openfigi.com/api)

## Non-US Official Repositories

Foreign issuers listed in the US still file 20-F/6-K (or 40-F) on EDGAR. Home-market annual reports are often richer, especially for equity movements, segments, and management commentary.

- [ESMA ESEF / European tagged annual reports](https://www.esma.europa.eu/issuer-disclosure/electronic-reporting)
- [UK FCA National Storage Mechanism](https://data.fca.org.uk/#/nsm/nationalstoragemechanism)
- [UK Companies House search](https://find-and-update.company-information.service.gov.uk/)
- [Companies House public data API](https://developer.company-information.service.gov.uk/)
- [Canada SEDAR+](https://www.sedarplus.ca/home/)
- [Germany Unternehmensregister](https://www.unternehmensregister.de/)
- [Germany Bundesanzeiger](https://www.bundesanzeiger.de/)
- [France info-financière](https://www.info-financiere.fr/)
- [Japan EDINET](https://disclosure2.edinet-fsa.go.jp/)
- [Australia ASIC / company registers](https://asic.gov.au/)
- [Foreign private issuers overview (SEC)](https://www.sec.gov/divisions/corpfin/internatl/foreign-private-issuers-overview.shtml)

## Company Investor Relations

The IR site is the human-readable companion to the filing: annual report PDF, earnings slides, transcripts, and guidance. It is not a substitute for the 10-K/20-F.

Search `{company} investor relations annual report` or `{ticker} SEC filings`. Typical paths: `/investors`, `/investor-relations`, `/financials`, `/sec-filings`. Prefer the document that matches the EDGAR accession, not a marketing summary.

## iShares issuer literature

iShares UCITS ETFs and Physical ETCs are Irish-domiciled; their official documents live on the issuer's product pages, not EDGAR. Supported products are listed in `scripts/data/ishares_catalog.json`; see [scenario-ucits-etf.md](scenario-ucits-etf.md) and [scenario-precious-metals-etc.md](scenario-precious-metals-etc.md).
