# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under UK law, and how to fix it.

## Severity

| Severity          | Meaning                                                                    | Examples                                                                                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely infringement, or personal data exposed or processed without a basis | Advertising cookies before consent; marketing email without consent or soft opt-in; solely automated significant decision with no Art. 22C safeguards; restricted transfer with no mechanism |
| Medium            | Missing control or documentation that undermines a requirement             | Analytics exception relied on with no way to object; no complaints process; notice missing required items; no retention rule for a store; personal data in logs                           |
| Low               | Weak practice that raises risk without a clear breach of a requirement     | Overly precise identifiers; long default log retention; unclear wording in a notice                                                                                                         |
| Needs information | Cannot be graded without evidence outside the artifact                     | Lawful basis undocumented; IDTA or vendor contract not provided; hosting region unknown; fee status unknown                                                                                 |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# UK GDPR review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <controller, processor or joint controller, per activity>
- Law as at: <date; DUAA commencement status checked on YYYY-MM-DD>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm lawful basis,
> transfer and breach decisions with the DPO or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal data inventory

| Activity | Data categories | Data subjects | Purpose | Lawful basis | Storage and recipients | Restricted transfers | Retention |
| -------- | --------------- | ------------- | ------- | ------------ | ---------------------- | -------------------- | --------- |

## Cookies and marketing

| Identifier or channel | Purpose | Consent or exception | Evidence |
| --------------------- | ------- | -------------------- | -------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <UK GDPR Art., DPA 2018 s. or PECR reg., with a one-line paraphrase; ICO guidance if relevant>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, DPO or counsel, each tied to the finding it affects.>

## Sources

<Provisions and ICO guidance cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, roles, territorial applicability and the point in time are stated
- [ ] The inventory covers every personal-data category, device identifier and marketing channel found, with unknowns marked
- [ ] Every finding cites a provision and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
