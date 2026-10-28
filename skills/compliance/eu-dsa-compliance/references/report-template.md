# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the DSA, and how to fix it.

## Severity

| Severity          | Meaning                                                               | Examples                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| High              | Likely infringement of an obligation at the service's tier            | No notice mechanism; restrictions without statements of reasons; profiling ads using special categories or to known minors; traders listed without traceability data; no complaint system |
| Medium            | Missing control or documentation that undermines a requirement        | Statements of reasons missing 17(3) elements; terms silent on automated moderation; ad label without targeting parameters; transparency report off-template                        |
| Low               | Weak practice that raises risk without a clear breach of a requirement | Contact page hard to find; recommender controls buried; vague moderation category labels                                                                                          |
| Needs information | Cannot be graded without evidence outside the artifact                | Recipient count or enterprise size unknown; Transparency Database submissions not shown; moderation staffing undocumented                                                         |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# DSA review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <service, repository and commit, PR, or document and version>
- Tier: <intermediary | hosting | online platform | marketplace | VLOP or VLOSE>, per service
- Size: <micro or small enterprise, or not; Art. 19 and 29 exemptions applied>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm tier
> classification, content illegality and risk assessment decisions with qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## DSA surface inventory

| Service | Surface | Location (code or document) | Triggered articles | Status |
| ------- | ------- | --------------------------- | ------------------ | ------ |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <Art. X(Y), with a one-line paraphrase; implementing act or guideline if relevant>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, text or organizational step>

## Not assessed

<Obligations out of scope, exempt, or blocked, with the reason or the evidence needed.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<DSA articles, implementing acts and Commission guidance cited, with links and the date checked.>
```

## Completion checklist

- [ ] Tier per service, territorial scope and size exemptions are stated
- [ ] The inventory covers every DSA surface found, with triggered articles and unknowns marked
- [ ] Every obligation at the tier is assessed, exempt, or listed as not assessed
- [ ] Every finding cites an article and concrete evidence, and has a fix
- [ ] Users and content appear only as categories and counts
- [ ] The not-legal-advice note is present and the status follows the severity rule
