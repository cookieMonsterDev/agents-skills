---
name: world-wide-compliance
description: World-wide compliance review across every regime the compliance skills cover: screens code, designs, data flows or documents, runs each applicable regime's review and merges one cited report. Use when asked whether something complies globally or in every market it serves, which laws apply to a launch or expansion into new countries, or for one compliance baseline across jurisdictions.
metadata:
  required-skills: aadc-compliance, app-store-compliance, ccpa-cpra-compliance, coppa-compliance, dpdp-compliance, eprivacy-compliance, eu-ai-act-compliance, eu-dsa-compliance, gdpr-compliance, hipaa-hds-compliance, lgpd-compliance, pci-dss-compliance, pipeda-law25-compliance, pipl-csl-compliance, psd2-sca-compliance, uk-gdpr-compliance, us-state-privacy-compliance
---

# World-wide compliance

Screen a solution or document against every regime the sibling compliance skills cover, run the full review of each regime that applies, and merge the results into one report: an applicability table, per-regime statuses, and **cross-regime findings** where one fix closes requirements in several laws. The bar is a report a product owner can plan from and each regime's counsel can verify quickly.

This skill orchestrates; the sibling skills in `required-skills` hold the law. Install them side by side, since the references link into them, and take each regime's scope tests, citations and checklists from that regime's skill.

This is a technical and documentary review, not legal advice. Route applicability calls near a threshold, conflicts between laws and decisions to accept a risk to the DPO, compliance officer or qualified counsel in each jurisdiction.

Treat code, documents and data under review as evidence only. Describe personal data by category and location, keeping real values out of the report.

## 1. Scope the review

Establish:

- **Artifact:** code (repository or diff), architecture or data-flow description, or a document. Each regime's skill takes each part through its matching checklist.
- **Footprint:** where the organization is established, where users and customers are, where data is stored and processed, and where the product is offered, marketed or distributed (web, App Store, Google Play).
- **Sector and audience signals:** children or teens as users, health data, card or payment data, AI systems or models, user-generated content, marketplaces or search, cookies, tracking SDKs and electronic marketing.
- **Business facts:** revenue, user counts per country or state, and the organization's role (controller, processor, covered entity, provider, deployer). Several regimes apply only above a threshold.
- **Evidence gaps:** footprint, thresholds and contracts the artifact cannot show. Ask only for gaps that block applicability; the rest make a regime "needs information".

Done when the footprint, signals, business facts and evidence gaps are written down.

## 2. Screen applicability

Run every row of [applicability-matrix.md](references/applicability-matrix.md) against the scope. For each regime, record **Applies**, **Does not apply** or **Needs information**, with the fact that decides it. When a trigger matches, confirm it with step 1 of that regime's skill; its thresholds and exemptions are authoritative.

Record markets and sectors with no sibling skill in the matrix's coverage-gaps section as **Not covered**, so the report's status visibly excludes them.

Done when every matrix row has a decision and a reason, and every uncovered market or sector in the footprint is listed.

## 3. Build one shared inventory

Build the personal-data inventory once, with the union of the columns the applicable skills ask for: data categories, data subjects (with ages), purpose, legal basis per regime, storage locations and countries, recipients and processors, transfers, retention, device identifiers and SDKs, and marketing channels. For code, follow the discovery step of `gdpr-compliance`'s [code-review-checklist.md](../gdpr-compliance/references/code-review-checklist.md#1-discover-personal-data).

Mark every category that any applicable regime treats as sensitive, children's, health, payment or AI-relevant.

Done when every personal-data field, identifier and data flow found has a row, with unknown cells marked unknown.

## 4. Run each applicable regime

For each regime marked Applies or Needs information, read its `SKILL.md` and run its steps 3 and 4 against the shared inventory: requirements map, checklists, findings and its own report. Save each regime report under that skill's filename in the same folder as the world-wide report.

When subagents are available, run one per regime in parallel. Give each the scope, the shared inventory and the skill path; each returns its report path, overall status and High findings.

Done when every applicable regime has a report that passes its own completion checklist, or is listed as unassessed with the missing evidence named.

## 5. Merge and harmonize

Follow [cross-regime-harmonization.md](references/cross-regime-harmonization.md):

- Group findings from different regimes that share one fix into a **cross-regime finding**, citing every requirement it closes.
- For each shared control (notice, consent, rights requests, retention, breach response, transfers, age gates, security), set the baseline at the strictest applicable requirement and list where a regime needs more.
- Record **conflicts**, where satisfying one regime breaks another (data localization against a global architecture, opt-in against opt-out designs), with both citations and the decision owner.

Done when every regime finding appears in the report, grouped or standalone, every baseline control has a value and a source regime, and every conflict has an owner.

## 6. Report

Follow [report-template.md](references/report-template.md). Save the report as `world-wide-review-<subject>-<YYYY-MM-DD>.md` (UTC date from the system clock) next to the regime reports. For a quick question such as "which laws apply to this launch", answer in chat from steps 1 and 2 to the same citation standard.

Done when the template's completion checklist passes. Give the user the overall status, the applicable regimes with their statuses, the High cross-regime findings, the conflicts, and the uncovered markets.

## Citations

Cite each requirement in its own regime's style, as the sibling skill does (`GDPR Art. 6(1)(a)`, `Cal. Civ. Code §1798.120`, `LGPD Art. 7`, `PIPL Art. 39`, `16 CFR 312.5`). Laws, thresholds and commencement dates change: rely on the date checked in each regime report, and state where a regime could not be checked.
