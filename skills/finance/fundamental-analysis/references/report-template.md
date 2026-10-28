# Completing the Markdown report

Use this structure for full analysis; shorten to the requested scope when the user asks a specific question. Preserve the evidence and limitation sections even in a short report. Replace prompts with findings, including explicit “unassessed” outcomes. An unfinished workpaper must retain its analyst-review-pending status.

```markdown
# {Company} ({ticker/share class}) — {scenario} fundamental analysis

Information cutoff: {date}. Reporting currency: {currency}. Analysis date: {date}.
Scope/status: {full, focused, or limited by named missing evidence}.

## Conclusion
State the operating assessment and any supportable valuation conclusion separately.
Give the decisive evidence, strongest counterargument and main uncertainty.

## Evidence and coverage
Link source CSV + SHA-256, workpaper and assumptions/calculation outputs.
List actual annual/interim periods, available filing dates, and accounting basis.
Identify missing documents, adapter errors, rejected facts and reconciliations.
State price timestamp/source/share class or explain why price judgment is absent.

## Business and classification
Explain how the company earns cash, its segments/customers and competitive position.
Name the business profile (or hybrid) and the evidence selecting it.

## Financial performance and accounting quality
Explain comparable growth, margins, cash conversion, reinvestment and per-share results.
Reconcile normalization and capital-structure measures to reported amounts.
Address notes, auditor opinion, material estimates and earnings-quality concerns.

## Financial resilience and capital allocation
Assess liquidity, maturities, covenants, contingent claims and funding needs.
Evaluate reinvestment, acquisitions, dividends, buybacks, issuance and incentives.
Distinguish supported conclusions from missing specialist evidence.

## Valuation and downside
Explain the model, sources and assumptions and give conditional ranges/sensitivities.
Show enterprise-to-common-equity bridge if applicable and avoid double counting.
Label screen thresholds, heuristics and analytical assumptions as analyst choices.
State margin of safety and upside separately only with positive defensible value.
Assess survival, refinancing and dilution under the adverse case.

## Counter-thesis and opportunity cost
Present the strongest evidence against the thesis and fragile assumptions.
Explain whether a company-specific advantage over a diversified alternative is supported.

## What would change the conclusion
List observable operating, financial or valuation developments and their implications.
Give exact outstanding evidence needs; do not schedule monitoring without a request.

## Sources and calculation trail
Link official filing sections/pages/accessions and dated market inputs near claims.
Map calculated figures to workpaper metric + source CSV records or manual bridges.
```

## Completion checklist

- Issuer/share class, currency, information cutoff and actual period coverage are explicit.
- Every material factual assertion has a filing/document locator; every derived number has a formula and inputs.
- Unavailable, conflicting and inapplicable data are visible; missing debt/capex/notes is not interpreted as absence.
- Selected scenario requirements are addressed; specialist boundaries are respected.
- Reported, adjusted, assumed and interpreted statements are distinguishable. Current accounting or market claims use current primary evidence.
- Financial statement scope, reporting units, currencies, dates, restatements, share class and dilution are reconciled before comparisons.
- A valuation conclusion uses supported assumptions, downside and sensitivity; otherwise it is withheld with a precise reason.
- Synthetic examples are labeled fictional, and no real-company recommendation is inferred from fixtures.
- The completed Markdown is saved with its run outputs (outside the skill folder), links its evidence, and is distinct from the generated workpaper. It contains no unresolved template prompts.

Review example: [synthetic limited analysis](../examples/2026-03-01-DEMO-steady-compounder-analysis.md). It demonstrates how to finish an honest limited report when quantitative facts exist but qualitative/price evidence does not.
