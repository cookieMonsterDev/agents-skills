# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the LGPD, and how to fix it.

## Severity

| Severity          | Meaning                                                                    | Examples                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| High              | Likely infringement, or personal data exposed or processed without a basis | Sensitive data under legitimate interest; tracking before consent with no other basis; deletion that leaves live copies; transfer abroad with no Art. 33 mechanism; no incident procedure able to meet 3 business days |
| Medium            | Missing control or documentation that undermines a requirement             | No retention rule for a store; notice missing required items; encarregado contact unpublished; operator contract without security or incident terms; CPF or health data in logs                                          |
| Low               | Weak practice that raises risk without a clear breach of a requirement     | Overly precise identifiers; long default log retention; unclear wording in a notice; notice available only in English                                                                                                    |
| Needs information | Cannot be graded without evidence outside the artifact                     | Legal basis undocumented; operator contract not provided; hosting region unknown; small-agent status unclear                                                                                                             |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# LGPD review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <controlador or operador, per activity; small agent: yes, no or unknown>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm legal basis,
> transfer and incident decisions with the encarregado or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal data inventory

| Activity | Data categories | Data subjects | Purpose | Legal basis | Storage and recipients | International transfers | Retention |
| -------- | --------------- | ------------- | ------- | ----------- | ---------------------- | ----------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <Art. X(Y) or Res. CD/ANPD N/YYYY, Art. Z, with a one-line paraphrase>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, encarregado or counsel, each tied to the finding it affects.>

## Sources

<LGPD articles, ANPD resolutions and guidance cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, roles, small-agent status and territorial applicability are stated
- [ ] The inventory covers every personal-data category found, with unknowns marked
- [ ] Every finding cites an article or resolution and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
