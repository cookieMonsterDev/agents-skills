# Report template

Use this structure for the world-wide report. It sits next to the regime reports and links them; keep regime-level detail there and cross-regime decisions here.

## Status

Each regime keeps the status its own report gives: **Non-compliant**, **At risk** or **No issues found in scope**. The overall status is the worst of them. A regime marked Needs information, and every Not covered market, is listed beside the status: the status speaks only for the regimes assessed.

## Structure

```markdown
# World-wide compliance review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Footprint: <establishments, user markets, data locations, distribution channels>
- Overall status: <Non-compliant | At risk | No issues found in scope>, for the regimes assessed

> This is a technical and documentary review, not legal advice. Confirm applicability,
> conflicts between laws and risk decisions with the DPO, compliance officer or
> qualified counsel in each jurisdiction.

## Summary

<Three to five sentences: what was reviewed, which regimes apply, the most important
cross-regime findings and conflicts, and the open questions that could change the result.>

## Applicability

| Regime | Decision | Deciding fact | Report | Status |
| ------ | -------- | ------------- | ------ | ------ |

<One row per matrix row: Applies, Does not apply or Needs information. Report links
the regime report file; Status copies its overall status.>

## Not covered

| Market or sector | Trigger | Regime to assess | Route to |
| ---------------- | ------- | ---------------- | -------- |

## Shared personal data inventory

| Activity | Data categories | Data subjects and ages | Purpose | Legal basis per regime | Storage and countries | Recipients and processors | Transfers | Retention |
| -------- | --------------- | ---------------------- | ------- | ---------------------- | --------------------- | ------------------------- | --------- | --------- |

## Cross-regime findings

### <ID>. <Short title> (<Severity>)

- **Requirements:** <each citation in its regime's style, with the regime finding IDs>
- **Evidence:** <file:line, document section, or quoted clause>
- **Issue:** <what the artifact does or omits, and why that fails each requirement>
- **Fix:** <one change that closes every listed requirement; note any market that needs more>

## Control baseline

| Control | Baseline | Strictest source | Regimes needing more |
| ------- | -------- | ---------------- | -------------------- |

## Conflicts

### <ID>. <Short title>

- **Requirements:** <the two citations that cannot both be met by one design>
- **Options:** <regional stores, per-market flows or builds, feature limits>
- **Decision owner:** <role, per jurisdiction>

## Open questions

<Questions for the owner or counsel, each tied to the regime, finding or conflict it affects.>

## Sources

<The regime reports, each with its sources and date checked.>
```

## Completion checklist

- [ ] Footprint, signals and business facts are stated
- [ ] Every applicability matrix row has a decision and a deciding fact
- [ ] Every applicable regime links a report that passed its own completion checklist, or is listed as unassessed with the evidence it needs
- [ ] Every uncovered market or sector in the footprint is in Not covered
- [ ] Every cross-regime finding cites each requirement it closes, with evidence and one fix
- [ ] Every conflict names both requirements, the options and the decision owner
- [ ] Personal data appears only as categories and locations
- [ ] The not-legal-advice note is present and the overall status is the worst regime status
