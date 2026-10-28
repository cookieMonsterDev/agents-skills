# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, why it matters under Chinese law, and how to fix it.

## Severity

| Severity          | Meaning                                                                | Examples                                                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| High              | Likely violation, or PI exposed, exported or processed without a basis | Sensitive PI without separate consent; export above a threshold with no mechanism; CIIO or important data stored offshore; SDKs collecting before consent; PI leaked in logs |
| Medium            | Missing control or documentation that undermines a requirement         | No PIPIA for an Art. 55 scenario; privacy policy missing recipients or retention; standard contract not filed; no account cancellation path; logs kept under 6 months         |
| Low               | Weak practice that raises risk without a clear breach of a requirement | Overly precise location; vague purpose wording; long default retention                                                                                                       |
| Needs information | Cannot be graded without evidence outside the artifact                 | CIIO status unknown; export volumes uncounted; MLPS level unknown; offshore contract not provided                                                                            |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# PIPL and CSL review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Roles: <PI processor, joint processor or entrusted party, per activity; CIIO status>
- Volumes: <individuals processed; exported since 1 January, sensitive and other>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm CIIO status,
> important data, transfer mechanism, filings and incident reports with qualified PRC counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Personal information inventory

| Activity | PI categories | Sensitive | Purpose | Lawful basis and consent | Storage and recipients | Export and mechanism | Retention |
| -------- | ------------- | --------- | ------- | ------------------------ | ---------------------- | -------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <PIPL Art. X(Y), CSL Art. Z or rule, with a one-line paraphrase>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, clause, filing or organizational step>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Articles and CAC rules cited, with links and the date checked; mark sources that could
not be reached as inconclusive.>
```

## Completion checklist

- [ ] Scope, roles, CIIO status and export volumes are stated, or marked unknown
- [ ] The inventory covers every PI category found, with unknowns marked
- [ ] Every finding cites an article and concrete evidence, and has a fix
- [ ] Every offshore flow has a mechanism, an exemption with its facts, or a finding
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] PI appears only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
