# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, which states it fails, why, and how to fix it.

## Severity

| Severity          | Meaning                                                                       | Examples                                                                                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely violation in at least one in-scope state, or data used against a right | Ad pixels firing despite GPC where a UOOM is required; sensitive data processed without consent; no opt-out of sale or targeted advertising; deletion leaving live copies |
| Medium            | Missing control or documentation that undermines a requirement                | Processor contract missing required terms; notice missing required items; no appeal process; no data protection assessment for targeted advertising                      |
| Low               | Weak practice that raises risk without a clear breach of a requirement        | Overly precise geolocation; vague purpose wording; long log retention                                                                                                     |
| Needs information | Cannot be graded without evidence outside the artifact                        | Resident counts per state unknown; vendor contract not provided; production tag configuration not visible                                                                 |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the states and evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# US state privacy review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <controller, processor or third party, per activity>
- States in scope: <state: threshold met; upcoming laws listed separately>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm applicability,
> exemptions and assessment conclusions with privacy counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal data inventory

| Activity | Data categories (sensitive marked) | Purpose | Recipients and role | Targeted ads, sale or profiling | Retention |
| -------- | ---------------------------------- | ------- | ------------------- | ------------------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <state and section for each state affected, with a one-line paraphrase>
- **Evidence:** <file:line, document section, quoted clause, or observed request>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change, preferably one that meets the strictest in-scope state>

## Not assessed

<States or areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Statutes, rules and roster cited, with links and the date checked.>
```

## Completion checklist

- [ ] Each in-scope state is listed with the threshold it meets, and upcoming laws are noted
- [ ] The inventory covers every personal-data category found, with unknowns marked
- [ ] Every finding names the states it applies to, cites a section and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
