# Scenario: US equity via EDGAR

Use when the entity is a US-listed stock (or any name with a CIK) and you need face-statement numbers plus the filing index for a window.

## Identifiers

1. Ticker → CIK via `https://www.sec.gov/files/company_tickers.json`.
2. Pad CIK to 10 digits (`320193` → `0000320193`).

## Fetch (the `edgar` adapter)

| Resource | URL |
| -------- | --- |
| Submissions | `https://data.sec.gov/submissions/CIK##########.json` |
| Company facts | `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` |
| Filing HTML | `https://www.sec.gov/Archives/edgar/data/{cik_int}/{accession_nodash}/{primary}` |

`scripts/run_report.py --tickers AAPL --period month` runs this path.

## Window rules

- First require valid filing/end dates on or before `min(window.end, window.as_of)`. Then keep facts whose `filed` or `end` date falls in the window (`filed_in_window` / `period_in_window`).
- When a concept/unit/duration class has no window hit, retain its latest economic period and latest publication for that period (`asof_latest`). Annual, quarter, six/nine-month YTD and instant values remain separate; conflicting ties survive for downstream reconciliation.
- Keep supported filing forms in the window plus latest annual/interim locators for context. Follow older submissions JSON files overlapping the requested history or the preceding 550-day context range. This supports narrow historical windows without pretending to provide an unlimited archive.
- Default facts are core face-statement tags in `schema.py`. `--all-facts` keeps every `us-gaap` / `ifrs-full` / `dei` / `srt` tag.

For analysis use `--history-years 5 --download-filings`; review the manifest and snapshot limit as described in [evidence-bundle.md](evidence-bundle.md). Core mode now includes inventory, receivables, goodwill, debt components, leases and share compensation where tagged. Do not sum overlapping debt tags or assume absence means zero.

## Failure modes

- HTTP 403: inspect identifying User-Agent and fair-access restrictions; it is not proof of a missing email. See [compliance.md](compliance.md).
- Unresolved ticker: not in the SEC map (wrong venue ticker, or not a US filer).
- Empty month: fallback facts and annual/interim locators may provide context. An adapter returning no evidence becomes an explicit error, including for an issuer without XBRL coverage.
- Quarterly cash-flow tags are often YTD; do not treat a 10-Q operating-cash number as a standalone quarter without subtracting prior YTD.
