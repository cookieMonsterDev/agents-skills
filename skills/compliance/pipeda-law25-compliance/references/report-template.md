# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under PIPEDA or Law 25, and how to fix it.

## Severity

| Severity          | Meaning                                                                       | Examples                                                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely contravention, or personal information exposed or used without consent | Profiling or geolocation on by default; sensitive information without express consent; deletion that leaves live copies; communication outside Québec with no PIA or agreement           |
| Medium            | Missing control or documentation that undermines a requirement                | No retention rule for a store; policy missing the person in charge or outside-Québec notice; service contract without s. 18.3 terms; no incident register; personal information in logs |
| Low               | Weak practice that raises risk without a clear contravention                  | Overly precise identifiers; long default log retention; vague purpose wording                                                                                                           |
| Needs information | Cannot be graded without evidence outside the artifact                        | Consent form undocumented; vendor contract or PIA not provided; hosting region unknown                                                                                                   |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# PIPEDA and Law 25 review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Regimes: <PIPEDA, Law 25, or both, per activity; provincial or health laws flagged>
- Roles: <accountable organization or service provider, per activity>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm consent,
> breach-harm and cross-border decisions with the privacy officer or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal information inventory

| Activity | Information categories | Individuals | Purpose | Consent or exception | Storage and providers | Outside Québec / Canada | Retention |
| -------- | ---------------------- | ----------- | ------- | -------------------- | --------------------- | ----------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <PIPEDA s. or Principle, and/or Québec s., with a one-line paraphrase; OPC or CAI guidance if relevant>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, privacy officer or counsel, each tied to the finding it affects.>

## Sources

<Sections, regulations and guidance cited, with links and the date checked; the
status of Bill C-36 when a finding mentions reform.>
```

## Completion checklist

- [ ] Regimes, roles and the provincial or sector laws flagged are stated
- [ ] The inventory covers every personal-information category found, with unknowns marked
- [ ] Every finding cites a section or principle and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal information appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
