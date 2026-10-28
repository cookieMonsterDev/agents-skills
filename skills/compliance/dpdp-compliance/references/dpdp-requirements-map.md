# DPDP requirements map

A compact map from review topics to the sections of the Digital Personal Data Protection Act, 2023 (DPDP Act) and the rules of the Digital Personal Data Protection Rules, 2025 (G.S.R. 846(E)). It summarizes; it does not replace the text. Quote or paraphrase the provision itself in a finding, and open the source when the exact wording matters.

## Official sources

- [Digital Personal Data Protection Act, 2023 (Act 22 of 2023), MeitY](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf): the Gazette text as enacted on 11 August 2023.
- [Digital Personal Data Protection Rules, 2025, MeitY](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf): G.S.R. 846(E) of 13 November 2025. A corrigendum (G.S.R. 892(E), 10 December 2025) corrected parts of the text; check the Gazette for the corrected wording when a finding turns on it.
- [MeitY data protection framework](https://www.meity.gov.in/data-protection-framework): the index of the Act, Rules, commencement notifications, orders and FAQs.

The Digital Personal Data Protection (Removal of Difficulties) Order, 2026 (S.O. 5458(E), October 2026) made drafting corrections to s.9(1) and s.10(2)(c)(ii) ("data audit"); it moved no deadline.

## Commencement

| From             | Provisions                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 13 November 2025 | Act s.1(2), 2, 18-26, 35, 38-43, 44(1) and 44(3); Rules 1, 2 and 17-21 (the Data Protection Board and its procedure)      |
| 13 November 2026 | Act s.6(9) and 27(1)(d); Rule 4 and First Schedule (Consent Manager registration and obligations)                          |
| 13 May 2027      | Everything else: notice, consent, legitimate uses, fiduciary obligations, children, SDFs, rights, transfers, penalties; Rules 3, 5-16, 22, 23 |

Some commentators count the later dates as 14 November 2026 and 14 May 2027, and MeitY consulted in early 2026 on shortening the 18-month period. Check the live MeitY page and the Gazette for any amending notification before stating a date. Until s.44(2) commences, IT Act s.43A and the SPDI Rules, 2011 continue to apply.

## Key definitions (s.2)

| Term                         | Section    | Review note                                                                                                          |
| ---------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| Personal data                | 2(t), 2(n) | Any data about an identifiable individual; the Act covers only digital personal data, including digitised paper data |
| Data Fiduciary               | 2(i)       | Determines purpose and means, alone or with others                                                                   |
| Data Processor               | 2(k)       | Processes on behalf of a Data Fiduciary, only under a valid contract (s.8(2))                                         |
| Data Principal               | 2(j)       | Includes the parent of a child and the lawful guardian of a person with disability                                    |
| Child                        | 2(f)       | Under 18                                                                                                             |
| Consent Manager              | 2(g)       | A Board-registered person providing an interoperable platform to give, manage, review and withdraw consent            |
| Personal data breach         | 2(u)       | Any unauthorised processing, accidental disclosure, loss of access or destruction that compromises confidentiality, integrity or availability |
| Significant Data Fiduciary   | 2(z), 10   | Notified by the Central Government on volume and sensitivity of data, risk to rights, sovereignty, electoral democracy, security and public order |

## Requirements by topic

| Topic                        | Source                                   | What to verify                                                                                                                                                                                                                   |
| ---------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Grounds for processing       | s.4, 6, 7                                | Lawful purpose with either consent or a legitimate use. s.7 is a closed list: voluntarily provided data for its specified purpose without objection, State benefits and functions, legal disclosure, court orders, medical emergency, epidemic, disaster, employment |
| Notice                       | s.5; Rule 3                              | Standalone and understandable on its own; itemised personal data; specified purposes and the goods, services or uses enabled; links to withdraw consent, exercise rights and complain to the Board; available in English or an Eighth Schedule language (s.5(3)) |
| Consent                      | s.6                                      | Free, specific, informed, unconditional, unambiguous, by clear affirmative action, limited to necessary data; withdrawal as easy as giving (6(4)); processing and processors stop on withdrawal (6(6)); fiduciary proves notice and consent (6(10)) |
| Consent Managers             | s.6(7)-(9); Rule 4, First Schedule       | Board registration; Indian company with net worth of at least INR 2 crore; cannot read the data it routes; consent records kept at least 7 years; no sub-contracting of obligations; fiduciary capacity towards the Data Principal                                                              |
| Fiduciary obligations        | s.8                                      | Responsible for processors (8(1)); valid processor contract (8(2)); accuracy when data drives decisions or is disclosed (8(3)); technical and organisational measures (8(4)); security (8(5)); erasure on withdrawal or end of purpose and by processors (8(7)) |
| Security safeguards          | s.8(5); Rule 6                           | Encryption, obfuscation, masking or tokenisation; access control; access logs and monitoring; backups and continuity; logs and personal data kept 1 year for detection; security terms in processor contracts                     |
| Breach intimation            | s.8(6); Rule 7                           | Each affected Data Principal without delay, with the Rule 7(1) content; the Board without delay, then a detailed report within 72 hours (longer only if the Board allows on written request). No risk threshold: every breach |
| Retention                    | s.8(7)-(8); Rule 8, Third Schedule       | Erase when the purpose is served or consent withdrawn, unless law requires retention; Third Schedule platforms erase after 3 years of inactivity with 48 hours' prior notice; keep personal data, traffic data and logs at least 1 year (Rule 8(3)) |
| Contact and grievance        | s.8(9)-(10); Rules 9, 14(3)              | Publish DPO or contact person details prominently and in every rights response; grievance redressal answering within at most 90 days                                                                                             |
| Children and guardianship    | s.9; Rules 10-12, Fourth Schedule        | Verifiable parental consent before processing (Rule 10: parent is an identifiable adult, via data held or a DigiLocker or authorised virtual token); nothing detrimental to well-being; no tracking, behavioural monitoring or targeted advertising directed at children; Fourth Schedule exemptions with conditions |
| Significant Data Fiduciary   | s.10; Rule 13                            | India-based DPO answerable to the board; independent data auditor; DPIA and audit every 12 months with a report to the Board; due diligence that algorithmic software poses no risk to rights; localisation of data the Government specifies (Rule 13(4)) |
| Data Principal rights        | s.11-14; Rule 14                         | Access summary of data, processing and every fiduciary and processor it was shared with (s.11); correction, completion, updating, erasure (s.12); grievance redressal, exhausted before the Board (s.13); nomination (s.14); publish how to exercise them |
| Data Principal duties        | s.15                                     | No false particulars, impersonation or frivolous complaints; penalty up to INR 10,000                                                                                                                                             |
| Cross-border transfer        | s.16; Rule 15                            | Transfer is allowed except to countries the Government notifies (none listed at the last check); Rule 15 lets the Government set requirements for making data available to foreign States; stricter sectoral laws prevail (s.16(2)) |
| Exemptions                   | s.17; Rule 5, 16, Second Schedule        | s.17(1) grounds (legal claims, courts and regulators, crime prevention, foreign Data Principals under contracts with foreign persons, mergers, loan defaulters) still leave s.8(1) and 8(5) in force; research and statistics under Second Schedule standards; notified startups may be exempt from some duties (17(3)) |
| Penalties                    | s.33, Schedule                           | Up to INR 250 crore (security safeguards), 200 crore (breach intimation; children), 150 crore (SDF duties), 50 crore (any other breach), 10,000 (Data Principal duties)                                                            |

## Data localisation

The DPDP Act does not require data to stay in India. s.16 is a negative list: transfers are free unless the Government restricts a destination. Localisation comes from other sources, each needing separate review:

- **Significant Data Fiduciaries:** Rule 13(4) lets the Government specify personal data that SDFs may not transfer outside India, on a committee's recommendation. Check whether any data has been specified.
- **Payments:** [RBI circular on Storage of Payment System Data](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) (RBI/2017-18/153, 6 April 2018) requires payment system data to be stored only in India. The RBI site refuses scripted requests; open it in a browser.
- **Other sectors:** SEBI, IRDAI, telecom licence conditions and public-sector cloud rules impose their own storage limits, and CERT-In Directions (28 April 2022) require ICT logs kept within India for 180 days.
- **s.16(2):** any such law that gives a higher degree of protection or restriction prevails over the DPDP transfer regime.
