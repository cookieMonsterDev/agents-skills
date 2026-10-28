# Cyclicals and turnarounds

Use this playbook when normalized earning power or survival matters more than extrapolating the latest results. Apply the survival and room-for-error overlay in [risk-and-opportunity-cost.md](risk-and-opportunity-cost.md).

## Cyclical: where are earnings relative to the cycle?

Gather a full cycle including a downturn if accessible: volume, realized prices, input costs, inventories, utilization, capacity additions, margins, working capital and capex. Distinguish a cyclical upswing from structural market-share gain. Explain missing cycle history instead of treating five good years as representative.

Run `analyze_report.py` over annual history. Choose normalized earnings from documented mid-cycle assumptions or a justified historical window; arithmetic averaging alone can mask changed capacity, acquisitions or business mix. Reconcile normalized earnings to reported figures. Run `scenario_models.py earnings` with normalized positive EPS and several terminal multiples, or a documented FCFF model. Stress trough liquidity with `scenario_models.py stress` and actual maturities/covenants.

A low P/E at peak earnings may indicate unusually high current earnings. A high or unavailable P/E at the trough does not by itself establish overvaluation. Past cycle lengths are examples, not forecasts; current supply/demand evidence determines the scenario.

Complete with cycle-position evidence, normalized earning power, peak/trough comparisons, balance-sheet capacity through a downturn and the indicators that would contradict the proposed recovery. Keep any commodity/price assumptions dated and sourced.

## Turnaround: can the equity survive to benefit?

Gather unrestricted cash, committed and usable credit, burn, debt maturity schedule, covenant headroom, secured claims, lease/pension/other obligations and restructuring costs. Verify actual contractual callability; neither “bank debt” nor “funded debt” establishes it. Separate company survival from survival of existing shareholders' ownership percentage.

Build a recovery mechanism: profitable units, cost actions already implemented, asset disposals, customer retention or capacity rationalization. Track announced versus achieved milestones. Include financing cost, creditor priority and dilution in the common-equity bridge. State what depends on discretionary refinancing, new equity or asset sales.

Run `stress` for liquidity under at least a slower-recovery case. Choose dated obligations and a time bucket fine enough to detect near-term shortfalls; the static helper assumes immediate one-off obligations and a constant monthly burn. Avoid counting a maturity or lease payment both in burn and one-off obligations. Credit counts only to the extent drawable under scenario covenants. Use an `asset` downside or supported earnings/FCFF recovery case as relevant.

Complete with a dated liquidity bridge, the next binding funding constraint, measurable recovery milestones and residual equity outcomes after financing. If missing covenants or maturity data controls the result, conclude that survival is unassessed. Neither zero financial debt nor current net cash guarantees survival or a share-price floor.
