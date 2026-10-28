# Document review checklist

Use this checklist for SCA and exemption policies, fraud-monitoring and fraud-rate reports, security-measure reviews and audits, open-banking interface documentation, TPP agreements and onboarding, customer terms and help pages, and papers or specifications that describe payment authentication.

Check two things for each document: that it contains what PSD2 and the RTS require, and that it matches what the system actually does. A policy that lists an exemption the code does not enforce, or omits one it applies, is a finding. When both a document and code are in scope, cross-check them against the step 2 inventory.

## SCA policy

- [ ] Lists every Art. 97(1) trigger the PSP supports and the SCA method for each channel
- [ ] Names each element and its category, with the reasoning for methods EBA-Op-2019-06 treats as borderline
- [ ] States the dynamic-linking mechanism and what the user sees at approval (RTS 5)
- [ ] Sets failed-attempt limits, block and recovery procedure, and the five-minute idle timeout (RTS 4)
- [ ] Covers multi-purpose devices and how independence is preserved (RTS 9)

## Exemption policy

- [ ] Lists each exemption applied, its article, thresholds and counters (RTS 10-18)
- [ ] TRA: the methodology, risk signals, model, exemption threshold values and the fraud rates that support them (RTS 18, 19)
- [ ] Procedure to stop an exemption and notify the authority when fraud rates exceed the reference rate for two consecutive quarters (RTS 20)
- [ ] Art. 10a: documented fraud reasons and authority notification for any SCA request on AISP access
- [ ] Art. 17: the authority's acceptance of the corporate process is in evidence

## Security review and audit (RTS 3)

- [ ] Security measures are documented, periodically tested, evaluated and audited by independent, qualified auditors
- [ ] The TRA methodology, model and reported fraud rates are audited after the first year of use, then at least every three years
- [ ] Audit reports are available to the competent authority on request

## Fraud reporting (PSD2 96(6); EBA/GL/2018/05)

- [ ] Statistical fraud data is collected per the guidelines' breakdown (SCA and exempted, by exemption) and reported to the authority on the required cycle

## Open-banking interface documentation (RTS 30-33)

- [ ] Technical specification available free of charge to authorised TPPs on request, and a summary published on the website (30(3))
- [ ] Testing facility with support available for TPPs (30(5))
- [ ] KPIs and quarterly availability and performance statistics published (32(2), 32(4))
- [ ] Contingency procedure: fallback to the customer interface, or the authority's exemption decision (33)
- [ ] Change notifications to TPPs ahead of interface changes

## TPP onboarding and agreements (PSD2 66-68; RTS 34)

- [ ] TPP authorisation checked against the national and EBA registers, and the certificate's roles matched
- [ ] Access denials record the objectively justified fraud reason and the notification to the authority (68(5))
- [ ] No contractual precondition for TPP access that PSD2 forbids (66(5), 67(4))

## Customer terms and communications

- [ ] Liability rules: EUR 50 cap, no payer liability where SCA was not required, refund by end of the next business day (PSD2 73, 74)
- [ ] How to report lost or stolen credentials and how blocks and recovery work
- [ ] Clear wording of what the user approves at each SCA step

## Papers and other documents

For proposals, specifications and research that describe payment authentication or account access: build the inventory from the text, then check SCA coverage, element categories and independence, dynamic linking, exemptions with their thresholds, TPP access, and the PSD3 and PSR status the document assumes. Record each silence in the document as an evidence gap.
