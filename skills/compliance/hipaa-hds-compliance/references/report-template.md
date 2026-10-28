# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under HIPAA or HDS, and how to fix it.

## Severity

| Severity          | Meaning                                                                         | Examples                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely violation, or health data exposed or disclosed without a permission      | PHI sent to a tracking or AI vendor with no BAA; unencrypted ePHI on public storage; no audit logging of ePHI access; French health data hosted by an uncertified provider or outside the EEA |
| Medium            | Missing control or documentation that undermines a requirement                  | No current risk analysis; BAA missing breach reporting terms; addressable encryption skipped without documentation; hosting contract missing reversibility; PHI in logs                     |
| Low               | Weak practice that raises risk without a clear breach of a requirement          | Long session timeouts; broad but logged support access; vague notice wording                                                                                                                  |
| Needs information | Cannot be graded without evidence outside the artifact                          | BAA not provided; certificate scope unknown; hosting region unknown; risk analysis not shared                                                                                                 |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# HIPAA and HDS review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Regimes: <HIPAA, HDS, or both, with the reason each applies>
- Roles: <covered entity, business associate or subcontractor; HDS controller and hosts with activities>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm role, breach,
> certification and contract decisions with the privacy or security official or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Health data inventory

| Flow | Data categories | Individuals | Purpose and permission | Storage, host and region | Recipients and BAA or HDS status | Transfers | Retention |
| ---- | --------------- | ----------- | ---------------------- | ------------------------ | -------------------------------- | --------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <45 CFR section or CSP article or HDS requirement, with a one-line paraphrase>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, privacy or security official, or counsel, each tied to the finding it affects.>

## Sources

<Sections, articles and guidance cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, regimes and roles are stated
- [ ] The inventory covers every health-data category found, with unknowns marked
- [ ] Every vendor or host receiving health data has a BAA or HDS status, or a finding
- [ ] Every finding cites a section or article and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Health data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
