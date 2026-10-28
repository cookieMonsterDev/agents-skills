# Scenario: iShares UCITS ETF

Use when the holding is an iShares UCITS ETF (Irish domicile, ISIN `IE…`). These are funds, not 10-K issuers. Official reports are the **annual / interim reports, KIID/KID, prospectus, factsheet**, and **holdings** published by BlackRock/iShares.

## Current catalog

| Name | ISIN | Product page |
| ---- | ---- | ------------ |
| iShares Core MSCI Europe (Dist) | IE00B1YZSC51 | https://www.ishares.com/uk/individual/en/products/251860 |
| iShares MSCI EM Asia (Acc) | IE00B5L8K969 | https://www.ishares.com/uk/individual/en/products/253723 |

Product ids live in `scripts/data/ishares_catalog.json`. A new iShares ISIN needs a row there.

## What the adapter writes

- `record_kind=fact` — TER, AUM, shares outstanding, P/E, P/B, sector weights (`taxonomy=ishares`).
- `record_kind=document` — literature PDF URLs (`annual_report`, `factsheet`, `kiid`, `prospectus`). Files stay at the issuer; the CSV stores the link.
- `record_kind=holding` — weight % per position when a holdings CSV is linked from the product page.

`scripts/run_report.py --portfolio portfolio.example.csv --period month` covers this path for catalogued funds.

## Failure modes

- Unknown ISIN → `concept=unknown_product`. Add the product id; do not scrape a random aggregator.
- A linked holdings CSV that fails retrieval/parsing becomes an error row while facts/documents are retained. If no holdings link exists, no holdings coverage is implied. Holdings dated after the cutoff are rejected.
- Ticker `AEB` / `IBIS2` is venue-specific; **ISIN** is the key, not the broker ticker.

Report years and holdings observation dates are not publication dates. The adapter leaves unknown publication dates empty; a current product page with undated literature cannot establish a historical snapshot. Check the manifest's retrieval time and obtain contemporaneous evidence for historical analysis.
