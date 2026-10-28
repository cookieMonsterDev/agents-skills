# Survival, uncertainty and opportunity cost

Apply this overlay to every full thesis. It adds questions about resilience and the alternative use of capital; it does not provide company valuation formulas.

## Room for error

Identify dependencies whose joint failure could damage the business: a concentrated customer/supplier, refinancing, covenant headroom, input prices, litigation, regulation, key staff, or a financing-dependent growth plan. Separate the evidence that a dependency exists from the assumed severity of a scenario.

Use a downside case that tests several plausible stresses together, justified by the business. State the timing of cash needs and whether survival depends on refinancing, share issuance, optional asset sales or unproven cost savings. Include dilution and senior claims when translating business survival to equity value. The historical worst outcome is not a bound on future loss.

Use `scenario_models.py stress` when the needed cash/credit/burn/obligation inputs are supported. Otherwise explain the missing schedule or covenant rather than inventing runway. Low/base/high cases are conditional scenarios, not probabilities unless a probability model is justified. Label the stress test as an analyst convention, not a prescribed cash-buffer rule. State the thesis's most fragile input and an observable falsification condition.

## Opportunity cost

State what evidence supports taking company-specific exposure relative to a diversified, low-cost benchmark. A well-run business is not automatically attractively priced or likely to outperform. The analysis can conclude that the advantage is unproven.

For a numerical benchmark comparison, align horizon, currency, total-return convention, dividends, fees and dates. Separate historical returns from prospective scenarios. Taxes need the relevant jurisdiction and user circumstances; avoid assumed tax rates. Portfolio sizing or suitability requires additional user context and is not implied by this report workflow.

Use `scenario_models.py cost` only to illustrate compounding of a documented fee difference under the same assumed gross return. It excludes tax and cash flows and does not forecast relative investment performance. Fetch current official fund fees if applying it to real products. Historical cost levels and realized market returns are not current inputs.
