# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, which requirement it fails, and how to fix it.

## Severity

| Severity          | Meaning                                                                    | Examples                                                                                                                                                         |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | Account data exposed, SAD retained, or scope breaks the validation claimed | CVC stored after authorization; full PAN in logs; merchant server receives PANs under an SAQ A claim; payment-page scripts with no integrity control or inventory |
| Medium            | Missing control or documentation that undermines a requirement             | No retention purge; PAN shown unmasked to support staff; no MFA on remote CDE access; no TPSP responsibility matrix; stale data-flow diagram                      |
| Low               | Weak practice that raises risk without a clear failure of a requirement    | Over-broad service-account permissions outside the CDE; idle timeout near the limit; vague policy wording                                                        |
| Needs information | Cannot be graded without evidence outside the artifact                     | TPSP AOC not provided; segmentation test results missing; production WAF configuration unknown                                                                   |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed; it is not a Report on Compliance or a validated SAQ.

## Structure

```markdown
# PCI DSS review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Standard: PCI DSS v<version>, checked <date>
- Role: <merchant | service provider | both>
- Integration and candidate SAQ: <per payment channel>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not a PCI DSS assessment or legal
> advice. Confirm scope, SAQ eligibility and compensating controls with a QSA and
> the acquirer.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Cardholder-data flow inventory

| Flow | Elements | Entry point | Systems (CDE / connected / out of scope) | Service providers | Storage and protection | Retention |
| ---- | -------- | ----------- | ---------------------------------------- | ----------------- | ---------------------- | --------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <Req. X.Y.Z, with a one-line paraphrase; FAQ number if relevant>
- **Evidence:** <file:line, document section, or configuration value>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, scope reduction or document>

## Not assessed

<Requirements out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, QSA or acquirer, each tied to the finding it affects.>

## Sources

<PCI DSS version, SAQ, FAQs and information supplements cited, with links and the
date checked.>
```

## Completion checklist

- [ ] Role, integrations, candidate SAQ and standard version are stated
- [ ] The inventory covers every account-data flow found, with each system scoped
- [ ] Every finding cites a requirement number and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] No real PAN or SAD appears; test card numbers are masked to BIN and last four
- [ ] Requirement text is paraphrased, not quoted at length
- [ ] The not-legal-advice note is present and the status follows the severity rule
