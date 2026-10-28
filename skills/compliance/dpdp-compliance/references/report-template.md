# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the DPDP Act, from when it applies, and how to fix it.

## Severity

| Severity          | Meaning                                                                    | Examples                                                                                                                                                                                               |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| High              | Likely contravention, or personal data exposed or processed without a ground | Processing with neither consent nor a s.7 legitimate use; tracking or targeted ads on children; no parental consent; erasure that leaves live copies; no way to meet breach intimation; unencrypted stores |
| Medium            | Missing control or documentation that undermines a requirement             | Notice missing Rule 3 items; no grievance mechanism or 90-day bound; processor contract without security or breach terms; no retention rule; personal data in logs                                        |
| Low               | Weak practice that raises risk without a clear breach of a requirement     | Overly precise identifiers; notice only in English for a regional audience; unclear wording                                                                                                              |
| Needs information | Cannot be graded without evidence outside the artifact                     | Ground for processing undocumented; SDF status unknown; processor contract not provided; hosting region unknown                                                                                          |

Grade by the obligation's substance, whether or not it is in force yet, and label each finding with its commencement ("in force" or "from <date>"). Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# DPDP review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <Data Fiduciary, Data Processor or Consent Manager, per activity; SDF: yes, no or unknown>
- Commencement checked: <date checked and the commencement dates relied on>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm legitimate-use,
> transfer, SDF and breach decisions with the Data Protection Officer or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal data inventory

| Activity | Data categories | Data Principals | Purpose | Ground (consent or s.7 use) | Storage and recipients | Transfers outside India | Retention |
| -------- | --------------- | --------------- | ------- | --------------------------- | ---------------------- | ----------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>, <in force | from YYYY-MM-DD>)

- **Requirement:** <s.X(Y) or Rule Z, with a one-line paraphrase>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Flagged for separate review

<Sectoral localisation, CERT-In, IT Act s.43A and SPDI Rules, or other regimes found in scope.>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, DPO or counsel, each tied to the finding it affects.>

## Sources

<Sections, rules, notifications and orders cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, roles, SDF status and territorial applicability are stated
- [ ] Every finding carries its commencement label
- [ ] The inventory covers every personal-data category found, with unknowns marked
- [ ] Every finding cites a section or rule and concrete evidence, and has a fix
- [ ] Sectoral localisation and other regimes are flagged, not graded as DPDP findings
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
