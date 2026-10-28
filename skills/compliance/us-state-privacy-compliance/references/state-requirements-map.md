# US state requirements map

A compact map of the comprehensive state privacy laws other than California, the requirements most of them share, and where each state departs. It summarizes; it does not replace the statutes. Quote or paraphrase the statute itself in a finding, and open the source when the exact wording matters. The roster was compiled on 2026-10-28; states keep enacting and amending these laws, so confirm each applicable state against the live sources first.

## Official sources

- [IAPP US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/): the live roster of enacted and pending laws. A secondary source: confirm each fact in the statute or the attorney general's guidance.
- Virginia Consumer Data Protection Act, Va. Code §59.1-575 et seq.: the model most states follow.
- [Colorado Attorney General: Colorado Privacy Act](https://coag.gov/resources/colorado-privacy-act/): the statute, the CPA Rules (4 CCR 904-3), and the list of recognized universal opt-out mechanisms.
- Connecticut Attorney General: Connecticut Data Privacy Act: guidance, FAQs and enforcement reports.
- Texas Data Privacy and Security Act, Bus. & Com. Code ch. 541
- Oregon DOJ: Oregon Consumer Privacy Act
- [New Jersey Division of Consumer Affairs: New Jersey Data Privacy Act](https://www.njconsumeraffairs.gov/ocp/Pages/NJ-Data-Privacy-Law.aspx): the act and its rulemaking.
- [Global Privacy Control specification](https://w3c.github.io/gpc/): the signal most universal opt-out mandates meet in practice.

For a state not linked here, open the statute on the state legislature's site and the attorney general's privacy page.

## Shared model

Most laws follow the Virginia model; the review baseline is that model plus each applicable state's deltas.

| Topic                    | Common requirement                                                                                                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Roles                    | Controller decides purposes and means; processor acts on instructions under a contract; consumers are residents acting in a personal or household context (employees and B2B contacts excluded) |
| Exemptions               | Usually HIPAA PHI, FCRA data, and GLBA entities or data, varying by state; most exempt nonprofits and public bodies, but several states cover nonprofits                                    |
| Rights                   | Confirm and access, correct, delete, portability; opt out of targeted advertising, sale, and profiling in furtherance of decisions with legal or similarly significant effects                |
| Requests                 | Respond within 45 days, one 45-day extension; free at least once a year; an appeal process with notice of how to contact the attorney general                                            |
| Privacy notice           | Categories processed, purposes, how to exercise rights and appeal, categories shared with third parties and the third parties' categories, contact method; sale and targeted advertising disclosed clearly with how to opt out |
| Sensitive data           | Opt-in consent, with COPPA-compliant parental consent for known children under 13                                                                                                       |
| Minimization             | Collection adequate, relevant and limited to what is reasonably necessary for disclosed purposes; secondary use needs consent                                                            |
| Security                 | Reasonable administrative, technical and physical safeguards                                                                                                                             |
| Dark patterns            | Consent obtained through a dark pattern is not consent (most post-2022 laws)                                                                                                             |
| Data protection assessment | Before targeted advertising, sale, sensitive data processing, or risky profiling; produced to the attorney general on request                                                          |
| Processor contract       | Instructions, nature and purpose, data types, duration, confidentiality, deletion or return, cooperation and audits, flow-down to subcontractors with an opportunity to object            |
| Enforcement              | Attorney general only, no private right of action; many states give a cure period, some expired                                                                                         |

## State roster

Thresholds count state residents per calendar year; "payment-only" means data processed solely to complete a payment is excluded. UOOM: a universal opt-out mechanism or opt-out preference signal must be honored.

| State          | Law and citation                                   | In effect  | Applies when (check amendments)                                                            | UOOM            | Sensitive data | DPA          |
| -------------- | -------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------ | --------------- | -------------- | ------------ |
| Virginia       | VCDPA, Va. Code §59.1-575 et seq.                   | 2023-01-01 | 100,000 consumers; or 25,000 and over 50% of revenue from sales                             | No              | Consent        | Yes          |
| Colorado       | CPA, C.R.S. §6-1-1301 et seq.; 4 CCR 904-3          | 2023-07-01 | 100,000; or 25,000 and revenue or discounts from sales; covers nonprofits                  | Yes, AG-recognized list | Consent | Yes          |
| Connecticut    | CTDPA, Conn. Gen. Stat. §42-515 et seq.             | 2023-07-01 | From 2026-07-01: 35,000 consumers, or any sensitive data processing, or any sale           | Yes             | Consent        | Yes          |
| Utah           | UCPA, Utah Code §13-61-101 et seq.                  | 2023-12-31 | Revenue $25M+ and either 100,000 consumers or 25,000 and over 50% of revenue from sales    | No              | Notice and opt-out | No       |
| Texas          | TDPSA, Bus. & Com. Code ch. 541                     | 2024-07-01 | Not an SBA-defined small business; small businesses still need consent to sell sensitive data | Yes          | Consent        | Yes          |
| Oregon         | OCPA, ORS 646A.570 et seq.                          | 2024-07-01 | 100,000 (payment-only excluded); or 25,000 and 25%+ of revenue from sales; nonprofits from 2025-07-01 | Yes  | Consent        | Yes          |
| Montana        | MCDPA, Mont. Code Ann. §30-14-2801 et seq.          | 2024-10-01 | From 2025-10-01: 25,000 (payment-only excluded); or 15,000 and over 25% of revenue from sales | Yes          | Consent        | Yes          |
| Iowa           | ICDPA, Iowa Code ch. 715D                           | 2025-01-01 | 100,000; or 25,000 and over 50% of revenue from sales                                      | No              | Notice and opt-out | No       |
| Delaware       | DPDPA, Del. Code tit. 6, ch. 12D                    | 2025-01-01 | 35,000 (payment-only excluded); or 10,000 and over 20% of revenue from sales; HB 380 (signed 2026-09-02) lowers these from 2027-01-01 | Yes | Consent | Yes |
| Nebraska       | NDPA, Neb. Rev. Stat. §87-1101 et seq.              | 2025-01-01 | Texas model: not an SBA-defined small business                                             | Yes             | Consent        | Yes          |
| New Hampshire  | RSA ch. 507-H                                       | 2025-01-01 | 35,000 (payment-only excluded); or 10,000 and over 25% of revenue from sales               | Yes             | Consent        | Yes          |
| New Jersey     | NJDPA, N.J.S.A. 56:8-166.4 et seq.                  | 2025-01-15 | 100,000 (payment-only excluded); or 25,000 and revenue or discounts from sales             | Yes             | Consent        | Yes          |
| Tennessee      | TIPA, Tenn. Code Ann. §47-18-3201 et seq.           | 2025-07-01 | Revenue over $25M and either 175,000 consumers or 25,000 and over 50% of revenue from sales | No             | Consent        | Yes          |
| Minnesota      | MCDPA, Minn. Stat. ch. 325M                         | 2025-07-31 | 100,000 (payment-only excluded); or 25,000 and over 25% of revenue from sales              | Yes             | Consent        | Yes          |
| Maryland       | MODPA, Md. Code, Com. Law §14-4601 et seq.          | 2025-10-01 | 35,000 (payment-only excluded); or 10,000 and over 20% of revenue from sales               | Yes             | Strictly necessary only; no sale | Yes |
| Indiana        | ICDPA, Ind. Code 24-15                              | 2026-01-01 | 100,000; or 25,000 and over 50% of revenue from sales                                      | No              | Consent        | Yes          |
| Kentucky       | KCDPA, KRS 367.3611 et seq.                         | 2026-01-01 | 100,000; or 25,000 and over 50% of revenue from sales                                      | No              | Consent        | Yes          |
| Rhode Island   | RIDTPPA, R.I. Gen. Laws §6-48.1-1 et seq.           | 2026-01-01 | 35,000 (payment-only excluded); or 10,000 and over 20% of revenue from sales               | No              | Consent        | Yes          |
| Oklahoma       | SB 546 (2026)                                       | 2027-01-01 | 100,000; or 25,000 and over 50% of revenue from sales                                      | No              | Consent        | Yes          |
| Louisiana      | SB 386 (2026), La. R.S. 51:1780 et seq.             | 2027-01-01 | Revenue over $25M; or 75,000 consumers, households or devices; or 50%+ of revenue from sales | Not explicit  | Consent        | Yes          |
| Alabama        | HB 351 (2026), Personal Data Protection Act         | 2027-05-01 | Over 25,000 (payment-only excluded); or over 25% of revenue from sales; small-business exemption for non-sellers | Unclear | Consent | No   |
| Vermont        | SB 71 (2026), Data Privacy and Online Surveillance Act | 2028-01-01 | Over 35,000 consumers; or sensitive data or sales of 3,000+                               | Yes             | Consent        | Yes          |

Florida's Digital Bill of Rights reaches only very large companies (about $1 billion in revenue plus specific business lines); assess it separately when the thresholds might be met.

## Departures that change findings

- **Maryland:** collection limited to what is reasonably necessary and proportionate to the requested service; sensitive data only when strictly necessary; sale of sensitive data banned; no sale or targeted advertising when the controller knew or should have known the consumer is under 18. Applies to processing from 2026-04-01.
- **Minnesota:** a data inventory, documented privacy policies and procedures, and the right to question a profiling decision and learn its reasons.
- **Colorado:** the CPA Rules add detail on notices, consent refresh, UOOM recognition and assessments; only mechanisms on the AG's list must be honored.
- **Minors:** several states (Colorado, Connecticut, Maryland, Montana, Oregon, Virginia among them) add duties for known or likely minors, such as consent or bans for targeted advertising, sale and profiling. Check each applicable state's current minors provisions.
- **Opt-out signals and timing:** UOOM duties in some states started after the law's effective date; check the start date for each state in scope.
