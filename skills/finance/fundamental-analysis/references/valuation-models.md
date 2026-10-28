# Explicit valuation and stress models

These helpers implement common analyst conventions. They operate offline and accept explicit sourced assumptions. They do not turn a reported metric into a forecast automatically.

## Run and provenance contract

From this skill's folder, using a bundled fixture:

```bash
python3 scripts/scenario_models.py dcf \
  --input tests/fixtures/dcf.json --output /absolute/path/to/run/acme-dcf-example.json
```

Executable synthetic assumptions for all five models are in `tests/fixtures/{dcf,earnings,asset,stress,cost}.json`. Copy an example to a new run folder and replace each fictional input/evidence string before real use. Use a new output name for each scenario; the CLI refuses overwrite. Values use decimal rates (`0.10` means 10%), base currency amounts and actual shares, not thousands/millions unless every amount and share count is consistently scaled and disclosed. Per-share amounts use the same share class and currency as price.

Every input file requires `currency`, ISO `as_of`, `rationale`, and `sources`, a mapping from **each top-level model input name** to its evidence or explicitly labeled assumption. An optional `label` names the case. Price comparisons require the optional positive `price` and its source entry, including timestamp, currency, exchange/share class and any ADR ratio. Dated market inputs need verification from a suitable primary exchange/issuer source. If unavailable, omit the price comparison. The script validates structure, not the truth or temporal availability of sources; the analyst verifies those.

Each output preserves assumptions, source explanations, formula and input hash. Link these outputs from the final Markdown. Run conservative/base/optimistic cases only when supported; avoid arbitrary symmetric percentage changes or invented probabilities.

## FCFF discounted cash flow: `dcf`

Inputs: `cash_flow_basis` exactly `FCFF`, annual `cash_flows` list in end-of-year order, `discount_rate`, `terminal_growth`, `net_debt`, `other_senior_claims`, `diluted_shares`.

Construct a reported-to-FCFF bridge: operating earnings after operating taxes, noncash adjustments, reinvestment and working capital, with interest/tax/shares treatment stated. CFO minus capex is only a proxy and cannot be relabeled FCFF without reconciliation. Use a discount rate appropriate for enterprise cash flow, then subtract net debt and other senior claims once. Account consistently for pensions, leases, non-operating assets, NCI, options and restricted/operating cash. Positive net debt reduces equity; negative net debt represents excess net cash, requiring evidence it is excess.

The model sums discounted FCFF plus a perpetuity at the final forecast year, then converts enterprise to equity and divides by the diluted share assumption. It requires positive final-year FCFF and discount rate greater than terminal growth. Negative earlier FCFF is allowed. State how funding deficits are financed and reflected in the bridge/shares.

Report terminal value as a share of enterprise value and sensitivity to discount rate, terminal growth and operating assumptions. Negative modeled equity is a shortfall signal, not a tradable negative share price. If the business has not approached a sustainable terminal state, extend the supported forecast or withhold this model. FCFE requires a separately documented cost-of-equity model; it is not supported by this FCFF helper.

## Earnings scenario: `earnings`

Inputs: positive `normalized_eps`, `growth_rate`, positive `terminal_pe`, positive `required_return`, integer `years`.

Formula: forecast EPS × terminal multiple, discounted to the cutoff. Explain EPS normalization, share dilution/buybacks embedded in growth and the choice of multiple. This is a terminal share-price scenario **excluding interim dividends**, not full shareholder total-return valuation. Growth and required return are decimal annual rates. Use a slowdown/multiple-compression case for growth companies and mid-cycle earnings for cyclicals. Negative EPS cannot produce a meaningful earnings multiple here.

## Recoverable assets: `asset`

Inputs: non-overlapping `assets` list of `name`, `carrying_value`, `recovery_fraction` from 0 to 1, `evidence`; then `total_liabilities`, `additional_senior_claims`, `realization_costs_and_taxes`, `diluted_shares`.

The model applies haircuts and deducts claims/costs once. Document appraisal date, restrictions, priority and likely realization timing. It does not discount delayed proceeds; adjust through a separately explained time-value bridge if material. Avoid mixing gross and already-net asset values. Common-equity NCAV and working capital have different liability deductions.

## Liquidity runway: `stress`

Inputs: `unrestricted_cash`, `available_committed_credit`, `one_off_obligations`, positive `monthly_cash_burn`, positive `horizon_months`.

The model deducts one-off obligations immediately, divides remaining liquidity by constant monthly burn, and shows the funding gap at the horizon. It is a simplified scenario, not a dated cash-flow schedule or default predictor. Verify credit draw conditions, cash restrictions and burn composition. If debt maturities or uneven seasonal cash needs matter, prepare a month-by-month schedule rather than claim this aggregate is sufficient. A positive-cash-generating base case needs no fabricated burn; use a supported adverse burn scenario or report that the model is inapplicable.

## Cost compounding: `cost`

Inputs: `initial_capital`, `gross_annual_return`, `active_annual_cost`, `benchmark_annual_cost`, integer `years`.

Compound each at the same gross return minus annual costs. Output the ending values and cost difference. This isolates costs; it excludes taxes, cash flows and differences in gross investment performance. It cannot substantiate a forecast of stock-versus-index outperformance.

## Review gate

Before using outputs, verify evidence timestamps against the cutoff, consistent units/currency/share class, numerator/denominator scope, sign conventions, non-overlapping adjustments and model suitability. Compare results with an independent method when evidence permits; disagreement is a question to resolve rather than a reason to average incompatible valuations.
