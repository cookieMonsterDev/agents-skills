# PIPL and CSL requirements map

A compact map from review topics to the PIPL, CSL, DSL and their implementing rules. It summarizes; it does not replace the text. The Chinese text is authoritative: quote or paraphrase the article itself in a finding, and open the source when the exact wording matters.

## Official sources

CAC (`cac.gov.cn`) and NPC (`npc.gov.cn`) pages may refuse scripted requests; open them in a browser and mark them inconclusive when they cannot be reached.

- [Personal Information Protection Law (PIPL), CAC](https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm), also on the [NPC site](http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html): in force since 1 November 2021.
- [Cybersecurity Law (CSL), amended text, CAC](https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm): amendment adopted 28 October 2025, in force 1 January 2026; renumbered articles, higher fines, AI provisions, and an explicit duty to follow the PIPL and Civil Code for PI.
- [Data Security Law (DSL), CAC](https://www.cac.gov.cn/2021-06/11/c_1624994566919140.htm): data classification, important data, and the approval rule for foreign judicial or law-enforcement requests (Art. 36).
- [Network Data Security Management Regulations (NDSMR), CAC](https://www.cac.gov.cn/2024-09/30/c_1729384452307680.htm): State Council regulation in force 1 January 2025.
- [Provisions on Promoting and Regulating Cross-Border Data Flows (CBDF Provisions), CAC](https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm), with the [CAC Q&A](https://www.cac.gov.cn/2024-03/22/c_1712776611649184.htm): in force 22 March 2024 and prevail over the earlier measures where they conflict (Art. 13).
- [Measures for Security Assessment of Data Exports, CAC](https://www.cac.gov.cn/2022-07/07/c_1658811536396503.htm)
- [Measures on the Standard Contract for Personal Information Export, CAC](https://www.cac.gov.cn/2023-02/24/c_1678884830036813.htm): the contract template and filing; the volume conditions in its Art. 4 are superseded by CBDF Provisions Art. 8.
- [Measures for Certification of Personal Information Export, CAC](https://www.cac.gov.cn/2025-10/17/c_1762449728720008.htm): CAC and SAMR, in force 1 January 2026; certificates valid 3 years.
- [Measures for Personal Information Protection Compliance Audits, CAC](https://www.cac.gov.cn/2025-02/14/c_1741233507681519.htm): in force 1 May 2025, with the audit guideline annexed.
- [CAC announcement on filing PI protection officer details](https://www.cac.gov.cn/2025-07/18/c_1754553420421538.htm): processors of PI of 1 million or more individuals file with the city-level CAC, within 30 working days of reaching the threshold.
- [Measures for Security Management of Facial Recognition Technology, CAC](https://www.cac.gov.cn/2025-03/21/c_1744174262156096.htm): in force 1 June 2025; PIPIA, an alternative to face-only verification, and a provincial CAC filing at 100,000 individuals.
- [CAC Q&A on the National Cybersecurity Incident Reporting Measures](https://www.cac.gov.cn/2025-09/15/c_1759583021718167.htm): in force 1 November 2025; CIIOs report within 1 hour. Check the Measures and their grading annex for other operators' deadlines.

## Requirements by topic

| Topic | Articles | What to verify |
| ----- | -------- | -------------- |
| Scope | PIPL 3, 4, 53, 73 | Offshore processors targeting or analyzing individuals in China name a PRC representative and report it; de-identified data stays PI, anonymized data does not |
| Principles | PIPL 5-9, 19 | Lawful, legitimate, necessary and good faith; clear and reasonable purpose; minimum scope; transparency; accuracy; security; retention no longer than necessary |
| Lawful basis | PIPL 13 | Consent; necessary for a contract with the individual or for HR management under lawful labor rules or collective contracts; legal duty; public health emergency; news reporting; reasonable use of disclosed PI; other laws. No legitimate-interests basis |
| Consent | PIPL 14-16 | Voluntary, explicit and fully informed; renewed when purpose, method or categories change; withdrawable as easily; refusal does not block a product unless the PI is necessary for it |
| Separate consent | PIPL 23, 25, 26, 29, 39; NDSMR 62 | A distinct, specific consent, apart from the general policy acceptance, for: providing PI to another processor, public disclosure, non-security use of public-camera images, sensitive PI, and cross-border transfer. Written consent where a law requires it |
| Notice | PIPL 17, 18, 30; NDSMR 21 | Processor identity and contact; purposes, methods, categories, retention; how to exercise rights; for sensitive PI, the necessity and impact; recipients listed; a separate policy for minors under 14 |
| Entrustment and sharing | PIPL 21, 22, 23, 59 | Entrustment contract fixing purpose, term, method, categories, protection measures and return or deletion; sub-entrustment only with consent; providing PI to another processor needs notice of recipient identity and separate consent |
| Automated decisions | PIPL 24; NDSMR 42 | Transparent and fair results; an easy opt-out of personalized push or a non-personalized option; explanation and refusal of decisions with major impact; delete user tags on request |
| Sensitive PI | PIPL 28-32 | Biometrics, religious beliefs, specific identities, medical health, financial accounts, whereabouts, and PI of minors under 14: specific purpose, sufficient necessity, strict protection, separate consent; parental consent under 14 |
| Rights | PIPL 44-50; NDSMR 23-25 | Know and decide, restrict or refuse, access and copy, portability to a designated processor, correction, deletion, explanation; an accessible request mechanism; reasons for refusals |
| Security measures | PIPL 51; CSL 23 | Internal rules, classification, encryption and de-identification, access permissions, training, incident plans; MLPS grading and filing; network logs kept at least 6 months |
| PI protection officer | PIPL 52; CAC 2025 announcement | Officer named and filed once PI of 1 million or more individuals is processed |
| Compliance audit | PIPL 54; NDSMR 27; audit measures | Regular audits; processors of PI of more than 10 million individuals audit at least every 2 years; CAC may order an audit by a professional body |
| PIPIA | PIPL 55, 56 | Required before: sensitive PI, automated decision-making, entrusting, providing to others or disclosing PI, cross-border transfer, and other processing with major impact. Covers legality and necessity, impact and risk, and the measures; kept at least 3 years |
| Incidents | PIPL 57; CSL 27, 44; NDSMR 11 | Remedy at once; notify the regulator and individuals of categories, causes, harm, remedies and contacts; notice to individuals may be skipped when measures avoid harm, unless the regulator requires it |
| Large platforms | PIPL 58; NDSMR 44-46 | Independent external oversight body, platform rules, annual PI social responsibility report |
| Localization | PIPL 40; CSL 39 | CIIOs, and processors reaching the volume CAC sets, store PI collected in China in China; export only after a CAC security assessment |
| Cross-border transfer | PIPL 38, 39; CBDF Provisions 3-8 | A valid mechanism (security assessment, standard contract filing or certification) unless an exemption applies; separate consent and notice of the recipient; PIPIA before export; recipient protection equivalent to the PIPL |
| Foreign authority requests | PIPL 41; DSL 36 | No provision of PI or data stored in China to foreign judicial or law-enforcement bodies without PRC approval |
| Important data | DSL 21, 27, 30, 31; NDSMR 29-33, 37 | Identify and report important data per sector catalogues; security officer and body; annual risk assessment report; export only after a security assessment. Processors of PI of 10 million or more individuals take on these duties too (NDSMR 28) |
| Penalties | PIPL 66; CSL 61, 69; DSL 45 | PIPL serious violations: up to RMB 50 million or 5% of the prior year's turnover, and personal fines and bans for responsible persons; amended CSL: up to RMB 10 million for the gravest cases |

## Cross-border thresholds (CBDF Provisions)

Volumes count individuals whose PI is exported cumulatively since 1 January of the current year. Exemptions (Art. 3-6) are checked first.

| Situation | Mechanism | Article |
| --------- | --------- | ------- |
| Data from international trade, transport, academic cooperation, manufacturing or marketing with no PI or important data | Exempt | 3 |
| PI collected abroad, processed in China and re-exported with no domestic PI or important data added | Exempt | 4 |
| Necessary for a contract with the individual (cross-border shopping, delivery, payment, account opening, bookings, visas, exams); cross-border HR management; emergencies protecting life, health or property | Exempt (not for important data) | 5 |
| Non-CIIO exporting non-sensitive PI of fewer than 100,000 individuals | Exempt | 5(4) |
| Data outside a pilot free-trade-zone negative list | Exempt | 6 |
| Non-CIIO: 100,000 to under 1 million individuals' non-sensitive PI, or under 10,000 individuals' sensitive PI | Standard contract (filed with the provincial CAC within 10 working days of taking effect) or certification | 8 |
| CIIO exporting any PI or important data; any processor exporting important data; non-CIIO at 1 million or more non-sensitive, or 10,000 or more sensitive, individuals | CAC security assessment, valid 3 years and extendable | 7, 9 |

Splitting volumes to stay under a threshold is itself a finding. An exemption lifts only the mechanism: notice, separate consent where consent is the basis, and the PIPIA still apply (CBDF Provisions Art. 10; PIPL Art. 39, 55).

## Related standards

MLPS 2.0 is graded under GB/T 22239-2019; important data is identified under GB/T 43697-2024 and sector catalogues. Check the current standard on the SAMR or TC260 site before citing a clause.
