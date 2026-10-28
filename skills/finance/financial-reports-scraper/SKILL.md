---
name: financial-reports-scraper
description: Official financial evidence for a ticker, CIK, ISIN or portfolio, collected from SEC EDGAR and iShares into a CSV with a coverage manifest. Use to download or refresh filings, XBRL company facts or ETF/ETC documents, or when fundamental-analysis or portfolio-analysis needs source evidence.
---

# Financial reports scraper

Acquire official evidence for a ticker or portfolio: one tidy CSV, a coverage and provenance manifest, and optional SEC filing snapshots. The CSV is the input contract for [fundamental-analysis](../fundamental-analysis/SKILL.md). The default `--period month` is an extraction window, not a monthly financial statement.

Run the scripts by path (`<skill-dir>` is this skill's folder) from the user's working directory. Outputs go to `--out-dir`, which defaults to `reports/` in the current directory; keep it outside the skill folder so collected data never lands in the skills repository.

## 1. Resolve the request

Resolve issuer and share-class identifiers and the information cutoff. Use `--tickers` or a portfolio CSV (`company_name,type,isin,ticker`, optionally `cik`; see [portfolio.example.csv](portfolio.example.csv)). Explicit CIKs skip the ticker-map download. iShares funds resolve by ISIN through `scripts/data/ishares_catalog.json`; a venue ticker alone is not enough.

Choose `--period`, explicit `--start`/`--end`, or `--history-years`. For fundamental analysis start with five years and extend when the selected scenario needs a longer history. Read the matching route:

- US-listed SEC registrant: [scenario-us-equity-edgar.md](references/scenario-us-equity-edgar.md)
- Foreign private issuer or home-market filer: [scenario-foreign-issuer.md](references/scenario-foreign-issuer.md)
- UCITS ETF: [scenario-ucits-etf.md](references/scenario-ucits-etf.md)
- Physically backed ETC: [scenario-precious-metals-etc.md](references/scenario-precious-metals-etc.md)

Other repositories route through [topic-map.md](references/topic-map.md) and remain explicit coverage gaps.

Done when each requested entity has a supported route or a named gap, and the cutoff and window are explicit.

## 2. Acquire

Install `requirements.txt` into a Python 3.9+ virtual environment. SEC access requires an identifying `SEC_USER_AGENT` (client name and a real contact email). Reuse a configured value; otherwise ask the user for one before any network call and never invent it. Read [compliance.md](references/compliance.md) for rate limits and access rules.

```bash
python3 <skill-dir>/scripts/run_report.py --tickers ACME --as-of 2026-09-15 --history-years 5 \
  --all-facts --download-filings --max-filings 32 --out-dir /absolute/path/to/new-run
```

The ticker and dates are illustrative. For an ordinary monthly portfolio extract, use `--portfolio /absolute/path/to/portfolio.csv --period month`. `--help` lists every flag. An existing bundle is never overwritten; use a new `--out-dir` for a rerun.

`--all-facts` keeps every supported standard taxonomy concept; core mode keeps balance-sheet, working-capital, debt/lease, cash-flow and dilution tags. Neither guarantees a complete statement. The EDGAR window and fallback rules are in the US equity scenario.

`--download-filings` saves bounded primary SEC filing HTML/PDF and readable text with hashes. Read [evidence-bundle.md](references/evidence-bundle.md) for limits, locators and validation. Fund literature is linked by URL, not downloaded.

Done when the CLI prints the CSV path and a companion manifest exists. Exit 0 means collection finished without recorded adapter or download errors; exit 1 means a partial bundle exists; exit 2 means an invocation or output failure. Neither exit 0 nor a wide window proves adequate analytical coverage.

## 3. Check and hand off

Check the CSV against [csv-schema.md](references/csv-schema.md): per-entity row counts, actual periods, errors, and omitted or failed documents in the manifest. Preserve leading zeros and raw concepts and units. A missing item stays unknown until the source statements and notes resolve it. A first-quarter YTD value equals the quarter; other YTD flows need explicit reconciliation before quarter or TTM calculations.

For a recoverable error, inspect the cause and retry the affected entity once in a new output directory, honoring `Retry-After`. Keep the partial evidence if the retry fails. One entity's failure does not discard another's data. Unsupported home markets stay explicit error rows; official filings are the only source, never an aggregator.

Hand the CSV and its manifest to `fundamental-analysis`, and point to downloaded filings when asked. For historical fund work, undated product-page links are discovery evidence, not proof of publication before the cutoff, and a year-only title never establishes a December 31 publication date.

Done when coverage and material gaps are stated and a downstream agent can locate the exact source artifacts. Custom XBRL tags and dimensional notes are not normalized automatically; the downloaded filings let the analyst investigate them. Automatic statement and segment extraction and more home-market adapters are outside the current implementation.

## Maintenance

Validate changes by running `python3 -m pytest tests -q` from this skill's folder, in its environment. Tests use synthetic fixtures only.
