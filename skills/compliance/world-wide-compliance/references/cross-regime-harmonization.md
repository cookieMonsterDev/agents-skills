# Cross-regime harmonization

Merge the regime reports into one control set. Each regime's requirement, threshold and deadline comes from that regime's requirements map; this file gives the method and the places where regimes most often disagree.

## Contents

- [Group findings](#group-findings)
- [Set the baseline per control](#set-the-baseline-per-control)
- [Known divergences](#known-divergences)
- [Conflicts](#conflicts)

## Group findings

Group findings from different regime reports into one cross-regime finding when one fix closes all of them: the same code location, document section or missing process. Keep the regime finding IDs (`GDPR-3`, `LGPD-5`) so each counsel can trace their own law. A cross-regime finding takes the highest severity of the findings it groups.

Leave a finding standalone when only one regime requires the fix, and say so.

## Set the baseline per control

For each control, take the strictest value from the applicable regimes and record the regimes that need more than the baseline:

| Control                  | What to compare across regimes                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| Notice                   | Required items, languages, timing (at collection or before), and the channel                             |
| Legal basis and consent  | Opt-in or opt-out, separate consent for sensitive data, transfers or sharing, withdrawal mechanics       |
| Sale, sharing, targeting | Opt-out links and signals (Global Privacy Control), consent for targeted advertising, profiling opt-outs |
| Sensitive data           | Which categories each law treats as sensitive, and the extra basis or consent each requires              |
| Children and teens       | Age thresholds, parental consent methods, default settings, profiling and advertising limits             |
| Data subject requests    | Rights offered, verification, response deadlines and extensions, appeal routes                           |
| Retention and deletion   | Fixed periods, deletion triggers, legal holds, and deletion in backups and processors                    |
| Processors and vendors   | Mandatory contract terms, sub-processor approval, audits                                                 |
| Transfers and location   | Transfer mechanisms, assessments, regulator filings, and localization duties                             |
| Security                 | Named controls (encryption, MFA, logging, testing) and certification or assessment duties                |
| Breach and incidents     | Who is notified (regulator, individuals, partners), within what deadline, and what the record must hold  |
| Assessments              | DPIA, PIA, RIPD, FRIA, risk analysis or risk assessment: when each is required and what it contains      |
| Representation           | Local representatives, DPOs, grievance officers and registration duties                                  |

A baseline at the strictest value can still miss a regime-specific form, channel or filing; list those as additions to the baseline rather than raising the baseline for everyone.

## Known divergences

Confirm each value in the regime's skill before relying on it.

- **Consent model:** EU, UK, Brazil, India and China lean on consent or another basis decided before processing; California and the other US states mostly use opt-out for sale, sharing and targeted advertising, with opt-in for sensitive data in several states.
- **Children's ages:** COPPA protects under 13; the GDPR lets member states set the age of digital consent between 13 and 16; the UK sets 13; the DPDP Act treats everyone under 18 as a child; PIPL treats data of under-14s as sensitive; design codes reach under-18s.
- **Sensitive data:** the categories differ (precise geolocation, financial account data, neural data, minors' data, biometric and health data), so a field may be sensitive in one regime only.
- **Transfers:** EU and UK use adequacy or safeguards, China uses security assessment, standard contract or certification with exemptions, and India allows transfers except to countries the government restricts by notification.
- **Breach deadlines:** regulator deadlines range from hours to "without unreasonable delay"; take each from the regime's requirements map.

## Conflicts

A conflict exists when no single design satisfies two applicable regimes, for example localization of PI or important data in China against a single global database, or a regulator's retention duty against an erasure request. For each conflict, record:

- the two requirements with citations;
- the options (regional data stores, separate builds or flows per market, feature limits per market);
- the decision owner, usually counsel in both jurisdictions.

Leave the choice to the owner: the report presents the options and names who decides.
