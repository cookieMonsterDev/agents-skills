# Evidence bundle and handoff

The canonical output name remains `{as_of}-report-{window_start}-{window_end}.csv`. The CSV columns are unchanged. Each run also writes `{same_stem}.manifest.json`. Optional SEC snapshots are in `{same_stem}-documents/`.

The writer refuses to replace any existing bundle path before network collection starts. Pick a new `--out-dir` when retrying or changing the entity set for the same date window. Exact duplicate rows collapse, while different values or provenance remain distinct. A partially written bundle after a filesystem failure should be inspected and retried into a new directory.

## Manifest

`schema_version=1` records the CSV filename/hash, actual UTC retrieval timestamp, information cutoff, collection status and per-entity identifiers, row counts, observed intervals and errors. `collected` means no errors were recorded; `partial` identifies an adapter or document error. Neither guarantees all needed disclosures exist. Period coverage can include a lone metric rather than a complete statement; check the actual concept set before analysis.

`documents` records filing URL, accession, form and publication date, along with one of:

- `downloaded`: raw local filename, SHA-256, byte count, retrieval timestamp, and text filename/hash for HTML.
- `error`: explicit retrieval/write failure.
- `not_downloaded_limit`: the locator was collected but the configured snapshot budget was reached.

Document filenames are relative to `document_directory`; that directory is relative to the CSV/manifest's parent. A false `download_requested` and empty document list mean snapshots were not requested, not that no filings exist. The analysis helper verifies the CSV hash when this sidecar is present; legacy CSV-only reports remain supported.

## Source snapshots

`--download-filings` retrieves only collected primary SEC Archives filings. The default maximum is 12 per run, across all entities; adjust with `--max-filings` based on coverage needs. Annual/interim statements are prioritized, then event/proxy reports, newest first within each group. A cap can omit older years or entire entities; inspect per-entity coverage and omitted entries before claiming a complete multi-company document set. For a wider company analysis, 32 is a starting budget, not a completeness guarantee.

Raw HTML/PDF preserves tables and context. HTML text removes executable/style/hidden-XBRL blocks and separates visible text with newlines. It is a reading aid, not structured note extraction; cite the raw document's section/page/table for material facts. PDF files remain intact for page-aware reading. Snapshots above 25 MiB or empty responses are recorded as errors. Attachments/exhibits referenced by a primary filing are not recursively downloaded; follow material exhibit links as needed.

## Boundaries

The historical cutoff filters SEC filing dates and economic periods, while the retrieval timestamp documents when bytes were acquired. Current iShares pages can expose undated links or facts. Their observation dates and report years are distinct from publication dates, so `filed_at` stays empty when publication is unverified. A historical portfolio analysis needs separately verified contemporaneous fund documents.

Primary design reference, verified 2026-09-15: [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces). The main submissions endpoint exposes recent history and references older JSON files; Companyfacts contains standard entity-wide concepts, not every custom or dimensional disclosure.
