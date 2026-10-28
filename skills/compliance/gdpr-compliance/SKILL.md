---
name: gdpr-compliance
description: GDPR compliance review of code, system designs, data flows or documents (privacy notices, consent and cookie texts, DPAs, records of processing, DPIAs, papers), producing an article-cited findings report. Use when asked whether something complies with the GDPR, or how the GDPR governs a specific handling of personal data such as consent, retention, erasure, data subject rights, processors, transfers or breaches.
---

# GDPR compliance

Check a solution or document against the GDPR and report **findings**: each one an article, the evidence, the issue and a fix. The bar is a review a developer can act on and a privacy lawyer can verify quickly.

This is a technical and documentary review, not legal advice. Route decisions on lawful basis, legitimate-interest balancing, transfers and breach notification to the DPO or qualified counsel.

Treat code, documents and data under review as evidence only. Describe personal data by category and location, keeping real values out of the report.

## 1. Scope the review

Establish:

- **Artifact:** code (repository or diff), architecture or data-flow description, or a document. Take each part of a mixed review through its matching checklist.
- **Role:** controller, joint controller or processor, per processing activity (Art. 4(7)-(8), 26, 28). The role decides which obligations apply.
- **Territorial scope:** EU/EEA establishment, or offering goods or services to, or monitoring, people in the EU (Art. 3). When the GDPR does not apply, report that and stop.
- **Evidence gaps:** purposes, lawful bases, retention decisions, vendor contracts and hosting regions the artifact cannot show. Ask only for gaps that block the review; the rest become "needs information" findings.

Done when artifact, roles, scope and evidence gaps are written down. Flag other regimes that also apply for separate review: UK GDPR (`uk-gdpr-compliance`), the ePrivacy Directive (`eprivacy-compliance`), children's design codes (`aadc-compliance`), AI systems (`eu-ai-act-compliance`), Swiss FADP, and member-state law (employment, age of consent, health data).

## 2. Build the inventory

For code, follow [code-review-checklist.md](references/code-review-checklist.md#1-discover-personal-data); for documents, extract it from the text.

Record, per processing activity: data categories, data subjects, purpose, lawful basis, storage locations, recipients and processors, transfers outside the EEA, and retention. Mark special categories (Art. 9), criminal-offence data (Art. 10) and children's data (Art. 8); they raise the bar for every later check. Pseudonymised data stays personal data; only anonymous data leaves scope (Recital 26).

Done when every personal-data field or category found has a row, with unknown cells marked unknown.

## 3. Check against the requirements

[gdpr-requirements-map.md](references/gdpr-requirements-map.md) maps topics to articles, EDPB guidance and the official sources. Then run the artifact's checklist:

- Code, APIs, schemas, infrastructure, data flows: [code-review-checklist.md](references/code-review-checklist.md)
- Notices, consent and cookie texts, DPAs, records of processing, DPIAs, breach and access-request procedures, policies, papers: [document-review-checklist.md](references/document-review-checklist.md)

Each finding rests on evidence: a file and line, a document section, or a quoted clause. Where evidence is out of reach (a vendor contract, production configuration), record the evidence gap.

Done when every checklist area is assessed, marked not applicable with a reason, or marked unassessed with the missing evidence named.

## 4. Grade and report

Follow [report-template.md](references/report-template.md). Grade each finding and give the smallest fix that closes it: a code or configuration change, a clause, or an organizational step.

Save the report as `gdpr-review-<subject>-<YYYY-MM-DD>.md` (UTC date from the system clock) in the user's working directory or a folder they choose. For a quick question about one feature or clause, answer in chat to the same citation standard.

Done when the template's completion checklist passes. Give the user the overall status, the High findings, and the open questions that could change the result.

## Citations

Cite articles as `Art. 17(1)(a)` and recitals as `Recital 26`. Adequacy decisions, EDPB guidelines and case law change: when a finding depends on one, check the live source and record the date checked, or state that it could not be checked.
