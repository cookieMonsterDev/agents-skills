# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under the Directive or national law, and how to fix it.

## Severity

| Severity          | Meaning                                                                        | Examples                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely infringement: storage, access or marketing without consent or exemption | Analytics or ad cookies before consent; tags firing after "reject all"; fingerprinting without consent; email campaigns to purchased lists; no unsubscribe |
| Medium            | Missing control or documentation that undermines a requirement                 | Reject only on the second layer; withdrawal hard to find; cookie list out of date; consent not recorded; Consent Mode advanced mode without assessment    |
| Low               | Weak practice that raises risk without a clear breach of a requirement         | Exempt cookies with long lifetimes; vague purpose labels; re-consent cycle undefined                                                                       |
| Needs information | Cannot be graded without evidence outside the artifact                         | Production CMP settings not provided; marketing list source unknown; national exemption relied on but not stated                                           |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# ePrivacy review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <site or app and build, repository and commit, or document and version>
- Branches: <Art. 5(3) | Art. 13 | Art. 6, 9>
- Member states and national law: <list>
- Scan: <date, locale, tool, passes run>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm exemption,
> national-law and marketing decisions with the DPO or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Storage and access inventory

| Name or key | Technique | Party | Purpose | Exempt or consent purpose | Lifetime | First seen (no interaction, reject, accept) |
| ----------- | --------- | ----- | ------- | ------------------------- | -------- | ------------------------------------------- |

## Marketing channels

| Channel | List source | Consent or soft opt-in | Opt-out mechanism |
| ------- | ----------- | ---------------------- | ----------------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <ePrivacy Art. X(Y) or national section, one-line paraphrase; EDPB guidance or case if relevant>
- **Evidence:** <file:line, scan record, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, tag or CMP setting, text, or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, DPO or counsel, each tied to the finding it affects.>

## Sources

<Directive articles, national law, EDPB documents and cases cited, with links and the date checked.>
```

## Completion checklist

- [ ] Branches, member states and national laws are stated
- [ ] The inventory covers every operation found, with the pass in which it first appeared and unknowns marked
- [ ] Every finding cites an article or national section and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Identifiers and personal data appear only as names, categories and locations, never values
- [ ] The not-legal-advice note is present and the status follows the severity rule
