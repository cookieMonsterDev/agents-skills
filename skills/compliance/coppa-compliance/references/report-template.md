# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under COPPA, and how to fix it.

## Severity

| Severity          | Meaning                                                                                      | Examples                                                                                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely violation, or children's personal information collected or disclosed without consent | Ad SDK collecting advertising IDs from under-13 users for behavioral ads; collection before parental consent; disclosure to third parties without separate consent; deletion requests ignored |
| Medium            | Missing control or documentation that undermines a requirement                               | No written retention policy or security program; online notice missing required items; non-neutral age screen; consent method unfit for the disclosure practice                              |
| Low               | Weak practice that raises risk without a clear breach of a requirement                       | Optional fields that look required; long default log retention; unclear wording in a notice                                                                                                   |
| Needs information | Cannot be graded without evidence outside the artifact                                       | Audience composition unknown; vendor contract not provided; production SDK settings unavailable                                                                                                |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# COPPA review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, app version, or document and version>
- Audience status: <child-directed | mixed audience | general audience with actual knowledge | third party with actual knowledge>, with the evidence
- Role: <operator | service provider | third party>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm audience
> status, actual knowledge and safe harbor reliance with qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Children's personal information inventory

| Collection point | Items (§312.2) | Source | Purpose | Consent basis | Recipients | Integral? | Retention |
| ---------------- | -------------- | ------ | ------- | ------------- | ---------- | --------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <16 CFR 312.X(y) or 15 U.S.C. 650X, with a one-line paraphrase>
- **Evidence:** <file:line, screen, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, SDK setting, notice clause, consent step or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Rule sections, statute sections and FTC documents cited, with links and the date checked.>
```

## Completion checklist

- [ ] Audience status, role and the evidence for them are stated
- [ ] The inventory covers every collection point found, including SDKs, with unknowns marked
- [ ] Every finding cites a section and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal information appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
