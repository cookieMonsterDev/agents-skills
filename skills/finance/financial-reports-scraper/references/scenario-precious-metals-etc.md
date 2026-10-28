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

The `ishares` adapter already maps those labels when they appear on the product page. Holdings of an ETC are the bullion, not a stock book — do not expect a 400-line equity holdings CSV.

## Failure modes

- Treating the ETC as a stock and sending it to EDGAR (no CIK). Router must keep `entity_type=etc` on the iShares path.
- Using a broker ticker (`LSEETF`) instead of the ISIN.
- Valuing the ETC with P/E. Use metal entitlement and spot, not earnings.
