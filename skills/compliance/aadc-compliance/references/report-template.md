# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, which code requires it, and how to fix it.

## Severity

| Severity          | Meaning                                                                                  | Examples                                                                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely breach of a binding, in-force requirement, or a design that exposes children to harm | Child profiles public and contactable by strangers by default; precise location shared by default; profiling-based ads to known minors; no age assurance on a high-risk feature |
| Medium            | Missing control or documentation that undermines a requirement                           | No child DPIA; privacy information unreadable for the age range; persuasive features on by default; no signal for parental monitoring                                            |
| Low               | Weak practice, or a gap against non-binding guidance only                                | Settings explanations missing at the point of use; gaps against the Dutch code or Irish Fundamentals where no binding rule is breached                                            |
| Needs information | Cannot be graded without evidence outside the artifact                                   | Audience age data unknown; age-assurance vendor accuracy unknown; production defaults unavailable                                                                                |

Requirements under injunction are recorded as context with no severity. Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# Age-appropriate design review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, design file and version, or document and version>
- Child audience: <age ranges likely to access, with the evidence>
- Codes applied: <each code, with its in-force or enjoined status and the date checked>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm "likely to
> be accessed" conclusions, age-assurance choices and the status of litigated laws
> with qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Feature inventory

| Feature | Data | Child default | Profiling | Geolocation | Sharing | Engagement mechanics | Parental monitoring |
| ------- | ---- | ------------- | --------- | ----------- | ------- | -------------------- | ------------------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <ICO standard, statutory section or DSA article and guidelines section, with a one-line paraphrase; one line per applicable code>
- **Evidence:** <file:line, screen or design frame, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: default, code, design, disclosure or organizational step>

## Enjoined or pending requirements

<Requirements not graded because of an injunction or a future effective date, and what the product would need if they take effect.>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Codes, statutes, guidelines and court orders cited, with links and the date checked.>
```

## Completion checklist

- [ ] Child audience, the codes applied and their live status are stated
- [ ] The inventory covers every child-reachable feature found, with unknowns marked
- [ ] Every finding cites a standard or section and concrete evidence, and has a fix
- [ ] Enjoined and not-yet-effective requirements are separated from findings
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
