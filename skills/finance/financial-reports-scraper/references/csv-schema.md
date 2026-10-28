# CSV schema

Tidy long form: one observation per row. `scripts/financial_reports_scraper/schema.py` is the source of truth for column order.

| Column | Meaning |
| ------ | ------- |
| `as_of_date` | Extract as-of (usually today) |
| `window_start` / `window_end` | Inclusive window |
| `grain` | `month` (default), `quarter`, `year`, or `custom` |
| `record_kind` | `fact`, `filing`, `document`, `holding`, `error` |
| `inclusion_reason` | `filed_in_window`, `period_in_window`, `asof_latest`, `listed`, `adapter_error` |
| `entity_name` | Issuer or fund name |
| `entity_type` | `stock`, `etf`, `etc` |
| `ticker` | Exchange ticker as given |
| `isin` | ISIN when known |
| `cik` | 10-digit string, leading zeros kept |
| `lei` | LEI when known |
| `source` | `edgar` or `ishares` |
| `source_url` | JSON endpoint, filing HTML, or literature PDF |
| `accession` | EDGAR accession |
| `form` | `10-K`, `10-Q`, `8-K`, `20-F`, `annual_report`, `factsheet`, … |
| `filed_at` | Verified filing/publication date; blank when unknown, including iShares page observations |
| `period_start` / `period_end` | Duration start (blank for instants) and period end |
| `fiscal_year` / `fiscal_period` | EDGAR `fy` / `fp` (`FY`, `Q1`…) |
| `statement` | `income`, `balance`, `cash_flow`, `equity`, `shares`, `fund_metric`, `holdings`, `segment`, `document` |
| `concept` | Tag or metric name (`Assets`, `ter`, `weight_percent`) |
| `concept_local` | Human label |
| `taxonomy` | `us-gaap`, `ifrs-full`, `dei`, `srt`, `ishares` |
| `value` | Numeric or identifier string; empty for documents |
| `unit` | `USD`, `shares`, `percent`, … |
| `currency` | ISO currency when the unit is money |
| `notes` | Frame, file number, holding identifiers, error text |

Filename: `{as_of}-report-{window_start}-{window_end}.csv` (ISO dates).

The matching `.manifest.json` records retrieval time, CSV hash, errors and actual coverage; optional source documents are described in [evidence-bundle.md](evidence-bundle.md). `as_of_date` is the requested cutoff label, not the HTTP retrieval timestamp. SEC rows also satisfy `filed_at <= min(window_end, as_of_date)` and an economic-end cutoff.

For iShares, an observation's `period_end` or title's `fiscal_year` is not its publication date. Undated document links use `listed`, and a year-only title leaves both `filed_at` and `period_end` empty. Current pages alone cannot substantiate historical availability.
