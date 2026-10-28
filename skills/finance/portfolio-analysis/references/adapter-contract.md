# Adapter contract, version 1

`scripts/adapters/ibkr.py:parse(path)` returns a dictionary; register additional
parsers in `ADAPTERS` in `scripts/analyze_portfolio.py`. Keep broker field names
inside adapters. A new format must not weaken the common accounting rules.

Amounts and quantities are Python Decimal during calculation and decimal strings
in JSON. Unknowns are null, never zero. Dates are ISO dates. A true observed zero
is retained. Never add different currencies or valuation dates implicitly.

Top level: `schema_version`, `adapter`, `source_sha256`, `accounts`, `limitations`.
The CLI adds UTC `generated_at` and account `metrics`.

Each account contains:

- `account`: run-local pseudonym; `from_date`, `as_of`, `base_currency`.
- `sections`: raw section names/counts; `warnings`; `ignored_rows` with reason/count.
- `positions_complete`: structural coverage flag, conditional on export filters;
  `activity_complete`: whether observed execution totals avoid known ambiguities.
- `positions`: source_ref, instrument fields, quantity, market_value (local),
  fx_rate_to_base, market_value_base, cost_basis (local), unrealized_pnl (local), as_of.
- `trades`: source_ref, instrument fields, signed quantity, fx_rate_to_base, date,
  side, proceeds, commission, commission_currency, net_cash. Local currency unless
  explicitly qualified; net cash and commission may overlap and are never summed
  into a reconstructed balance by this implementation.
- `cash_transactions`: source_ref, date, currency, amount, original type.
- `cash_balances`: source_ref, currency, ending_cash, as_of. `BASE_SUMMARY` means
  aggregate account-base cash, never a tradable currency.
- `reported_nav`: null or {value, source_refs}, denominated in account base.

Instrument fields: instrument_id (broker ID preferred), isin, ticker, company_name,
type (`stock`, `etf`, `etc`, `unsupported`), asset_category, sub_category, exchange,
currency. Preserve identity per listing for valuations; deduplicate issuer research
by ISIN when available. Do not merge ADRs and local shares by company name.

## Derived metrics

`securities_value_base` requires structurally complete valued ending positions.
`reconciliation_residual = reported_nav - securities_value_base - cash_value_base`.
Tolerance is max(0.01 base units, 0.01% of absolute NAV), a disclosed analytical
convention. No cash/NAV is invented from trades. Automated weights require
positive NAV, reconciled cash/positions, and stock-category instruments; funds
reported by IBKR as STK are included. Signed weights expose shorts; gross exposure
sums absolute security values. Analysts must verify the export is unfiltered.

Activity aggregates keep currency partitions. Signed commissions can include
rebates; `commission_fields_complete` flags omitted commission amounts/currencies
in retained trades, and does not attest complete transaction history. Missing
commissions do not establish zero cost. Incomplete gross trade
values have a false completeness flag. No TWR, IRR, volatility, VaR, tax basis,
look-through classifications or target weights are calculated by the helper.
`research-universe.csv` is scraper-compatible discovery input, subject to identity
review; unsupported instruments are retained in JSON, not exported to the scraper.

## Adding a broker

Implement `parse(Path)`, retain source hashes/row locators, distinguish snapshot
balances from flows, and explicitly represent unsupported rows. Add the adapter
to the CLI registry and an input reference linked from SKILL.md. Test synthetic
samples with multiple currencies/accounts, missing balances, duplicate IDs,
summary/detail overlap, malformed data and source date mismatches. Add no raw
user statements to fixtures. Reject an unsupported format rather than guessing
that arbitrary XML/CSV is compatible with IBKR.

Changes that alter accounting meaning require a schema version increment and
corresponding analytics/report changes. New optional evidence fields can be
added without changing existing meanings.
