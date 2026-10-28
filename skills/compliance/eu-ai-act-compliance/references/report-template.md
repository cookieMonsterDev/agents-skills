# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the AI Act, and how to fix it.

## Severity

| Severity          | Meaning                                                                         | Examples                                                                                                                                                           |
| ----------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| High              | Likely prohibited practice, or an applicable high-risk or GPAI obligation unmet | Emotion recognition on employees; Annex III system in use without human override or logs; unregistered high-risk system; GPAI model without a copyright policy     |
| Medium            | Missing control or documentation that undermines a requirement                  | Chatbot with no AI disclosure; generated media without machine-readable marking; instructions for use missing accuracy metrics; Art. 6(3) assessment undocumented |
| Low               | Weak practice that raises risk without a clear breach of a requirement          | Evaluation not split by group; log retention at the bare minimum; vague AI literacy measures                                                                       |
| Readiness         | Gap against an obligation not yet applicable on the review date                 | Annex III system lacking a QMS before 2 December 2027                                                                                                              |
| Needs information | Cannot be graded without evidence outside the artifact                          | Intended purpose undocumented; upstream provider contract not provided; conformity assessment records missing                                                      |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. Report readiness findings beside the status, each with its application date. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# AI Act review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <provider, deployer, importer, distributor, per system>
- Overall status: <Non-compliant | At risk | No issues found in scope>; <n> readiness findings

> This is a technical and documentary review, not legal advice. Confirm risk
> classification, conformity and incident decisions with the compliance owner or
> qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## AI system and model inventory

| System or model | Intended purpose | Role | Upstream model | Affected persons | Risk tier and reason | Applicable from |
| --------------- | ---------------- | ---- | -------------- | ---------------- | -------------------- | --------------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <Art. X(Y) or Annex, with a one-line paraphrase; guidance if relevant>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, document section or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, compliance lead or counsel, each tied to the finding it affects.>

## Sources

<AI Act articles, amendments and Commission documents cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, roles and AI-system status are stated
- [ ] The inventory covers every AI system and model found, each with a tier and reason
- [ ] Every finding cites an article and concrete evidence, and has a fix
- [ ] Each finding is graded against its obligation's application date on the review date
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal and confidential data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
