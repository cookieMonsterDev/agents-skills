# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the CCPA, and how to fix it.

## Severity

| Severity          | Meaning                                                                            | Examples                                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely violation, or personal information sold, shared or exposed against a right | Ad pixels firing despite GPC or an opt-out; sale or sharing of under-16 data without opt-in; no notice at collection; deletion that leaves live copies at vendors |
| Medium            | Missing control or documentation that undermines a requirement                     | Vendor contract without the Regs. §7051 terms; privacy policy missing required items or older than 12 months; asymmetric cookie banner; no retention rule       |
| Low               | Weak practice that raises risk without a clear breach of a requirement             | Overly precise geolocation; vague category names; long log retention                                                                                            |
| Needs information | Cannot be graded without evidence outside the artifact                             | Revenue or consumer counts unknown; vendor contract not provided; production tag configuration not visible                                                      |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# CCPA review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <business, service provider, contractor or third party, per activity>
- Applicability: <threshold met, exemptions considered>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm applicability,
> sale and sharing classifications and risk-assessment conclusions with privacy counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal information inventory

| Activity | Categories (sensitive marked) | Source | Purpose | Recipients and role | Sold or shared | Retention |
| -------- | ----------------------------- | ------ | ------- | ------------------- | -------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <§1798.X or Regs. §7X, with a one-line paraphrase>
- **Evidence:** <file:line, document section, quoted clause, or observed request>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Statute and regulation sections cited, with links and the date checked.>
```

## Completion checklist

- [ ] Roles, applicability and exemptions are stated
- [ ] The inventory covers every personal-information category found, with unknowns marked
- [ ] Every recipient is classified as service provider, contractor or third party, or marked unknown
- [ ] Every finding cites a section and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal information appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
