# Report template

Use this structure for a written review. Keep each finding self-contained: someone reading only that finding should see what is wrong, where, which article it fails, and how to fix it.

## Severity

| Severity          | Meaning                                                                    | Examples                                                                                                                                                   |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High              | A required SCA is missing or bypassable, or an exemption runs outside its conditions | Payment path with one factor; approval screen without amount and payee; low-value counters reset without SCA; TRA applied above the supported threshold value; TPP access blocked by obstacles |
| Medium            | Missing control or documentation that undermines a requirement             | No permanent-block alert; idle timeout above five minutes; no quarterly interface statistics; exemption policy out of step with the code                    |
| Low               | Weak practice that raises risk without a clear breach of a requirement     | SMS OTP without SIM-swap signals; verbose authentication errors; consent screens with unclear wording                                                      |
| Needs information | Cannot be graded without evidence outside the artifact                     | Fraud rates not provided; processor exemption configuration unknown; authority notifications not in evidence                                               |

Overall status: **Non-compliant** with any High finding, **At risk** with Medium findings only, **No issues found in scope** otherwise. The status speaks only for the evidence reviewed, so "No issues found in scope" is the strongest claim a report makes.

## Structure

```markdown
# PSD2 SCA review: <subject>

- Date: <YYYY-MM-DD, UTC>
- Scope: <repository and commit, PR, or document and version>
- Role: <ASPSP, issuer, acquirer, PISP, AISP, payee or technical service provider>
- Law: PSD2 as transposed in <member state>; RTS 2018/389 as amended; PSD3 and PSR status checked <date>
- Overall status: <Non-compliant | At risk | No issues found in scope>

> This is a technical and documentary review, not legal advice. Confirm exemption,
> fraud-reporting and liability decisions with compliance or qualified counsel.

## Summary

<Three to five sentences: what was reviewed, the most important findings, and the
open questions that could change the result.>

## Inventory

### Payment flows

| Flow | Channel | Art. 97(1) trigger | Payment type | Amount range | PSP applying SCA | Exemption and who applies it |
| ---- | ------- | ------------------ | ------------ | ------------ | ---------------- | ---------------------------- |

### Authentication events

| Event | Elements and categories | Dynamic linking | Failed-attempt limit | Idle timeout |
| ----- | ----------------------- | --------------- | -------------------- | ------------ |

### TPP access

| Interface | TPP identification | SCA approach | Consent and frequency |
| --------- | ------------------ | ------------ | --------------------- |

## Findings

### <ID>. <Short title> (<Severity>)

- **Requirement:** <PSD2 Art. X or RTS Art. Y, with a one-line paraphrase; EBA Q&A or opinion if relevant>
- **Evidence:** <file:line, document section, or configuration value>
- **Issue:** <what the artifact does or omits, and why that fails the requirement>
- **Fix:** <concrete change: code, configuration, policy or notification>

## Not assessed

<Areas out of scope or blocked, with the evidence needed to assess them.>

## Open questions

<Questions for the owner, compliance or counsel, each tied to the finding it affects.>

## Sources

<PSD2 and RTS articles, EBA documents and Q&As cited, with links and the date checked.>
```

## Completion checklist

- [ ] Role, territorial and transaction scope, and the PSD3 and PSR status are stated
- [ ] The inventory covers every flow, authentication event and TPP access path found, with unknowns marked
- [ ] Every finding cites an article and concrete evidence, and has a fix
- [ ] Every unassessed area is listed with the evidence it needs
- [ ] Credentials, account numbers and card data appear only as types and locations
- [ ] The not-legal-advice note is present and the status follows the severity rule
