# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, which guideline or policy it breaks, and how to fix it.

## Severity

| Severity          | Meaning                                                                          | Examples                                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Likely rejection or removal, or user data handled against the store's rules     | Tracking before ATT permission; no in-app account deletion; restricted Android permission without a qualifying use; ad SDK outside the Families list in a children's app |
| Medium            | Disclosure or configuration gap that undermines a requirement                    | Privacy label or Data safety form missing an SDK's data; vague usage strings; no prominent disclosure for unexpected collection; missing privacy manifest reason          |
| Low               | Weak practice that raises review or privacy risk without a clear violation       | Permissions requested at launch; review notes thin on a non-obvious feature; privacy policy wording out of step with the label                                           |
| Needs information | Cannot be graded without evidence outside the artifact                           | Console answers not provided; server-side data sharing unknown; SDK dashboard settings not visible                                                                        |

Overall status: **Not ready** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed and does not predict a review outcome, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# App store review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, build number, or listing and form version>
- Stores and audience: <App Store, Google Play; general, mixed or children>
- Overall status: <Not ready | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice and not a prediction
> of App Review or Play review outcomes. Confirm legal and children's-data decisions
> with the privacy owner or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Inventory

### SDKs

| SDK | Version | Platform | Purpose | Data collected | Tracks |
| --- | ------- | -------- | ------- | -------------- | ------ |

### Permissions

| Permission | Platform | Usage string or declaration | Feature | When requested |
| ---------- | -------- | --------------------------- | ------- | -------------- |

### Data types

| Data type | Collected | Linked (Apple) | Shared (Google) | Tracking (Apple) | Purposes | Optional |
| --------- | --------- | -------------- | --------------- | ---------------- | -------- | -------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <Guideline X.Y or policy and section, with a one-line paraphrase>
- **Evidence:** <file:line, console answer, or quoted listing or policy clause>
- **Issue:** <what the app or form does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, manifest, console answer, listing text or review note>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner or counsel, each tied to the finding it affects.>

## Sources

<Guidelines and policy pages cited, with links and the date checked.>
```

## Completion checklist

- [ ] Scope, stores, audience and trigger are stated
- [ ] The inventory covers every SDK, permission and data type found, with unknowns marked
- [ ] Every store form answer is reconciled with the inventory
- [ ] Every finding cites a guideline or policy and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Personal data and credentials appear only as categories and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
