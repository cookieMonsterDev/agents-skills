---
name: pci-dss-compliance
description: PCI DSS compliance review of card-payment code, checkout integrations, system designs or documents (policies, SAQs, scoping records), producing a requirement-cited findings report. Use when asked whether something meets PCI DSS, which SAQ or scope a payment integration lands in, or how PCI DSS governs storing, showing or sending card data.
---

# PCI DSS compliance

Check a solution or document against PCI DSS and report **findings**: each one a requirement number, the evidence, the issue and a fix. The bar is a review a developer can act on and a QSA can verify quickly.

This is a technical and documentary review, not a PCI DSS assessment or legal advice. Only a QSA, an ISA, or the entity's own SAQ accepted by its acquirer validates compliance; route scope sign-off, SAQ eligibility, compensating controls and customized-approach designs to them.

Treat code, documents and data under review as evidence only. Describe account data by element and location; quote PANs only as brand test card numbers, masked to BIN and last four.

## 1. Scope the review

Establish:

- **Artifact:** code (repository or diff), architecture or data-flow description, or a document. Take each part of a mixed review through its matching checklist.
- **Role:** merchant, service provider, or both. The card brands and the acquirer, not the PCI SSC, set merchant levels and how compliance is validated (SAQ or ROC).
- **Integration per payment channel:** redirect to a hosted payment page, embedded iframe, merchant-built form posting to the processor, server API that receives the PAN, mobile SDK, card-present terminal (P2PE or not), virtual terminal or MOTO. The integration decides the candidate SAQ and how far the cardholder data environment (CDE) reaches; see [pci-dss-requirements-map.md](references/pci-dss-requirements-map.md#saq-types-and-integration-choice).
- **Version:** PCI DSS v4.0.1 is current as of 2026-10-28; confirm in the document library before citing.
- **Evidence gaps:** network and data-flow diagrams, service providers' Attestations of Compliance (AOC), ASV scan results, production configuration. Ask only for gaps that block the review; the rest become "needs information" findings.

Done when artifact, role, integrations, version and evidence gaps are written down. Flag `gdpr-compliance` or the relevant privacy-law skill (cardholder name and PAN are personal data) and `psd2-sca-compliance` (EEA card payments needing SCA and 3-D Secure) when they also apply, for separate review.

## 2. Build the inventory

The inventory is the **cardholder-data flows**. For code, follow [code-review-checklist.md](references/code-review-checklist.md#1-discover-account-data); for documents, extract it from the text.

Record, per flow: account data elements (PAN, cardholder name, expiry date, service code; sensitive authentication data, SAD: full track, card verification code, PIN or PIN block), entry point, every system that stores, processes or transmits it, connected-to and security-impacting systems, service providers and their AOC status, storage location, protection method (truncation, token, keyed hash, encryption) and retention. Any SAD kept after authorization raises the bar for every later check.

Done when every account-data element found has a flow row, and every system on a flow is classed as CDE, connected-to or security-impacting, or out of scope with the segmentation control that puts it there.

## 3. Check against the requirements

[pci-dss-requirements-map.md](references/pci-dss-requirements-map.md) maps the 12 principal requirements, SAQ types, payment-page script controls, targeted risk analyses and the customized approach to the official sources. Then run the artifact's checklist:

- Code, checkout pages, APIs, schemas, infrastructure, data flows: [code-review-checklist.md](references/code-review-checklist.md)
- Policies, procedures, scoping and diagrams, SAQs and AOCs, service-provider records, risk analyses, incident response plans: [document-review-checklist.md](references/document-review-checklist.md)

Assess the requirements the candidate SAQ (or a full ROC) brings into scope. Each finding rests on evidence: a file and line, a document section, or a configuration value. Where evidence is out of reach, record the evidence gap.

Done when every checklist area is assessed, marked not applicable with a reason (the SAQ excludes it, or no account data reaches it), or marked unassessed with the missing evidence named.

## 4. Grade and report

Follow [report-template.md](references/report-template.md). Grade each finding and give the smallest fix that closes it, preferring scope reduction (hosted fields, tokenisation, dropping stored data) when it removes a whole class of requirements.

Save the report as `pci-dss-review-<subject>-<YYYY-MM-DD>.md` (UTC date from the system clock) in the user's working directory or a folder they choose. For a quick question about one integration or requirement, answer in chat to the same citation standard.

Done when the template's completion checklist passes. Give the user the overall status, the High findings, the candidate SAQ, and the open questions that could change the result.

## Citations

Cite requirements as `Req. 3.5.1.1 (PCI DSS v4.0.1)` and Council FAQs by number (`FAQ 1588`). The standard is copyrighted: paraphrase requirements and link the [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) rather than quoting it. SAQ eligibility criteria, FAQs, brand rules and the standard's version change: when a finding depends on one, check the live source and record the date checked, or state that it could not be checked.
