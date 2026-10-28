# Scenario: iShares Physical Gold ETC

Use when the holding is an **ETC** (exchange-traded commodity), not an ETF. iShares Physical Gold (`IE00B4ND3602`) is a series of secured metal-linked **debt securities** issued by iShares Physical Metals plc. It is not a UCITS fund and it does not file a 10-K.

Official page: https://www.ishares.com/uk/individual/en/products/258441

## What matters

Face-statement equity metrics (revenue, EPS, book value) do not apply. The extract should carry:

- Metal in trust (tonnes / ounces)
- Daily metal entitlement per security
- TER
- Shares (securities) outstanding
- Base currency, ISIN, issuing company
- Annual report / prospectus / KID PDF links for iShares Physical Metals plc

The `ishares` adapter already maps those labels when they appear on the product page. An ETC's holdings are its bullion, so expect metal-in-trust facts rather than an equity holdings table.

## Failure modes

- Routing the ETC to EDGAR as a stock (it has no CIK). Keep `entity_type=etc` so the router stays on the iShares path.
- Keying on a broker ticker (`LSEETF`). Key on the ISIN.
- Valuing the ETC with P/E. Value it from metal entitlement and spot.
