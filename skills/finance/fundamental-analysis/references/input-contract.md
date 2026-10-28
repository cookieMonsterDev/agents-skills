# Scraper handoff and period policy

## Acquisition

The required sibling is `../financial-reports-scraper/` relative to this skill root. Acquire with the command in its SKILL.md step 2 (five years, `--all-facts`, `--download-filings`), using the user's cutoff; that step also covers its environment and SEC contact. Its `scripts/financial_reports_scraper/schema.py` owns the CSV columns, and its [evidence-bundle.md](../../financial-reports-scraper/references/evidence-bundle.md) describes the manifest and snapshots.

`analyze_report.py` imports that schema locally, validates all required headers, and leaves the input unchanged. Extra columns are allowed. It calculates one ticker at a time; for a portfolio enumerate stocks and run separately, retaining identifiers. Conflicting CIKs or ISINs under one ticker require an identifier-filtered copy with provenance.

Fetch history long enough for the fiscal periods the analysis needs, and check the returned coverage: a window guarantees neither five complete annual periods nor a full archive. The analyzer independently rechecks `filed_at` and `period_end` against the cutoff, including in older CSVs.

Companyfacts lacks custom tags and dimensional notes even with `--all-facts`, and snapshots are raw sources, not normalized prose or segment tables. Follow material exhibits or official filing links as needed. Keep manually extracted evidence in a separate source ledger with section/page, date, unit, scope and calculation bridge, leaving the CSV untouched and custom tags distinct from standard ones.

When a `.manifest.json` sits beside the CSV, the analyzer verifies the CSV hash, rejects a mismatching bundle, and carries the manifest location and snapshot list into the workpaper JSON. Check document hashes before citing local copies. A partial bundle or snapshot limit is a visible evidence gap, even if some metrics calculate successfully. CSV-only inputs remain supported.

## Intake outcomes

- `fact`: numeric candidate. Source rows retain accession, form, filed date, economic dates, concept, unit, URL, and raw notes.
- `filing` / `document`: document locator, never a numerical zero.
- `holding`: fund exposure; route separately from company financial statements.
- `error`: failed/incomplete acquisition; show it in limitations and follow the scraper retry policy. A successful CSV write can still contain failed adapters.
- Header-only CSV, wrong schema, mixed issuer identities or non-stock targets: fail with a specific diagnostic.

CSV record numbers in the audit count parsed records starting at 2 after the header, not physical text lines when a cell contains newlines. SHA-256 binds all record citations to the exact input file.

## Selection rules implemented by the helper

1. Require valid publication/end dates, finite values, supported filing forms, explicit reporting currency and an exact unit (`USD`, `USD/shares`, or `shares`, for example). Unknown or incompatible rows remain in the rejection audit. Missing values never become zero.
2. Classify by actual start/end: annual 350–380 days, standalone quarter 75–105, interim YTD 150–200 or 240–290. Instant facts have no start. These are conservative duration buckets, not proof of comparability; verify odd fiscal years against the filing. A first-quarter YTD period is indistinguishable from the quarter and belongs to `quarter`.
3. Keep annual facts by default; `--period quarter` or `ytd` selects those durations. Exact period matches link income and cash flow; balance facts must share that end date. No nearest-date filling, Q4/TTM derivation or automatic annualization. Review unmatched instants in the audit.
4. Within a concept, unit and exact economic interval choose the latest publication available by cutoff. Collapse exact duplicates. Conflicting values at that latest date invalidate the metric. Multiple mapped concepts with different values also invalidate it; reconcile with the filing before using either.
5. Compute growth only between comparable year-apart intervals with similar durations and a positive prior denominator. Negative-to-positive changes require narrative and absolute changes. The output's null/reason is part of the result.

The JSON retains selected and excluded rows, formulas, units and source-record identifiers. The Markdown workpaper surfaces the selected evidence. Check the audit's rejection reasons before treating a small workpaper as complete coverage.

For current analysis, the latest-known comparative values can mix publication vintages. Check restatement/accounting-policy consistency across selected periods; a cutoff filter alone cannot establish a coherent accounting basis. Historical analysis also needs price and qualitative sources that were available by that cutoff.

Primary implementation reference: [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), checked 2026-09-15. Units and reported fiscal boundaries govern comparison; calendar frames and `fy`/`fp` labels do not replace them.
