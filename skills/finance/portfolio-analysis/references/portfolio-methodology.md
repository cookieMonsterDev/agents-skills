# Portfolio review methodology

## Valuation and performance

Keep statement date, research cutoff, quote timestamps and FX dates separate.
Account NAV is not the same as invested securities value. Review cash, accrued
interest/dividends, margin debt and other liabilities before explaining residuals.
If the export is incomplete, do not renormalize the visible subset to 100% and
call it the whole portfolio. A subset allocation must name its denominator.
Analyze different account snapshots separately until their dates/currencies align.

Position weights use market value / validated NAV. Report signed and gross
exposures for shorts/leverage; market value alone does not measure derivative
exposure. Do not report HHI/effective holdings as meaningful diversification for
leveraged or incomplete books. For a fully valued long-only book, top issuer
weights and an optional sum-of-squared-weights concentration measure are useful,
but broad funds require look-through interpretation.

TWR needs valuations around external flows; money-weighted return needs complete
dated flows and endpoint values with a well-defined IRR. Neither is established
by the sum of trades, change in NAV or unrealized gain/cost. Without suitable
history, label performance, volatility, correlations and drawdowns unassessed.
Benchmarks must match exposure, currency, period and income reinvestment.

## Look-through diversification

Use dated issuer fund holdings and verified classifications. Underlying exposure
is direct issuer weight plus the sum of (fund portfolio weight × underlying weight).
Use fractions consistently (40% × 5% = 2%, not 200%). Explain coverage dates and
unclassified residuals; do not normalize missing holdings away. Pairwise overlap
may use sum of min(weight in fund A, weight in fund B) on comparable holdings.
Identify issuer/share-class mapping assumptions and avoid counting parent funds
again in look-through totals. Recursive fund-of-funds analysis needs cycle guards.

Distinguish trading, fund base, hedging and economic exposure currencies; distinguish
domicile, listing venue and underlying geography. For bond funds discuss duration,
credit, issuer concentration and currency. For ETCs assess collateral, custody,
issuer/counterparty structure and commodity sensitivity. For ETFs assess index
concentration, tracking difference, TER and securities lending where material.
Do not imply generic company fundamentals complete a fund review.

## Costs and contribution efficiency

Review expense ratios and tracking difference without adding overlapping cost
measures. Quantify trade commissions, spread, FX and taxes only with evidence.
Compare fees to gross traded value in the same currency; missing fees are unknown.
With a documented fixed commission C and fee ceiling f (a fraction), a hypothetical
minimum order size is C/f, before spread/FX and subject to the actual fee schedule.
This can motivate less frequent contributions, but assess time out of market and
cash needs. A contribution-first rebalance can reduce turnover and tax realization.

## Recommendations and allocation

Separate company/fund quality, price attractiveness and suitability in this
portfolio. A strong business can be too expensive or too concentrated; a sound
fund can duplicate existing exposure. Base decisions on the thesis and role,
not on whether the user's purchase currently shows a gain/loss.

For each action give the problem, evidence, proposed change, expected benefit,
downside/tradeoff, confidence and review trigger. Candidate additions need a
verified identity, accessibility/share class, evidence and opportunity-cost
comparison; an asset-class role is preferable to an unsupported ticker pick.
For an exit/trim, consider thesis impairment versus concentration and execution
costs. Include hold/no-action alternatives and explain uncertain conclusions.

Target ranges reflect objectives, time horizon, loss capacity and liquidity.
Do not hard-code a universal stock/bond split or single-position cap. With missing
preferences, show clearly labeled scenarios and their assumptions, with no claim
that one is personalized. For a selected long-only scenario, midpoint weights
including cash must sum to 100%; lower bounds must sum to at most 100% and upper
bounds to at least 100%. Account for leverage separately.

With verified holdings/prices, cash and contributions, desired value is target
weight × post-contribution NAV. Compare to existing value, fund underweights with
new cash where appropriate, and retain required liquidity. Check rounding, lot
sizes, minimum orders, fees and available cash before any indicative quantities.
Recommendations never execute trades. Verify jurisdiction-specific tax/account
rules from current authoritative sources only after the jurisdiction is known;
otherwise identify tax uncertainty without guessing liability.

## Scenario analysis

Use transparent assumptions such as equity drawdown, rate/duration shock or
currency move. A weighted linear shock is an illustration, not a forecast or VaR;
explain covariance, nonlinearity and derivative gaps. Avoid spurious precision or
estimated failure probabilities without a defensible model. State what evidence
would change the allocation or thesis. Monitoring triggers are report content;
creating a recurring monitor requires a separate user request.
