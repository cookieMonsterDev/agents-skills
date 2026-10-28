# Applicability matrix

Screen every row against the scope from step 1. A matching trigger marks the regime as a candidate; step 1 of the regime's skill confirms it with that law's thresholds and exemptions.

## Contents

- [Privacy and data protection](#privacy-and-data-protection)
- [Sector and audience](#sector-and-audience)
- [Platforms, AI and distribution](#platforms-ai-and-distribution)
- [Coverage gaps](#coverage-gaps)

## Privacy and data protection

| Regime                                    | Trigger to look for                                                                                                                                             | Skill                                                                       | Report file                 |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------- |
| EU GDPR                                   | EU/EEA establishment, or offering goods or services to, or monitoring, people in the EU (Art. 3)                                                                | [`gdpr-compliance`](../../gdpr-compliance/SKILL.md)                         | `gdpr-review-…`             |
| UK GDPR, DPA 2018, PECR                   | UK establishment, or offering goods or services to, or monitoring, people in the UK; PECR for cookies and electronic marketing aimed at UK users                | [`uk-gdpr-compliance`](../../uk-gdpr-compliance/SKILL.md)                   | `uk-gdpr-review-…`          |
| EU ePrivacy Directive                     | Cookies, device storage, pixels, fingerprinting or SDKs on devices of EU users, or email and SMS marketing to them, whether or not the data is personal         | [`eprivacy-compliance`](../../eprivacy-compliance/SKILL.md)                 | `eprivacy-review-…`         |
| California CCPA/CPRA                      | For-profit doing business in California that meets a revenue, volume or sale-or-sharing threshold; employees and B2B contacts count as consumers                | [`ccpa-cpra-compliance`](../../ccpa-cpra-compliance/SKILL.md)               | `ccpa-review-…`             |
| Other US state comprehensive privacy laws | Residents of a state with a comprehensive privacy law outside California; most apply above a resident-count threshold, some to any non-small business           | [`us-state-privacy-compliance`](../../us-state-privacy-compliance/SKILL.md) | `us-state-privacy-review-…` |
| Brazil LGPD                               | Processing in Brazil, offering goods or services to individuals in Brazil, or data collected in Brazil (Art. 3)                                                 | [`lgpd-compliance`](../../lgpd-compliance/SKILL.md)                         | `lgpd-review-…`             |
| Canada PIPEDA and Québec Law 25           | Personal information collected, used or disclosed in commercial activity in Canada; Law 25 when the enterprise holds personal information of people in Québec   | [`pipeda-law25-compliance`](../../pipeda-law25-compliance/SKILL.md)         | `pipeda-law25-review-…`     |
| India DPDP Act and Rules                  | Digital personal data processed in India, or outside India in connection with offering goods or services to people in India (s. 3)                              | [`dpdp-compliance`](../../dpdp-compliance/SKILL.md)                         | `dpdp-review-…`             |
| China PIPL and CSL                        | Processing in mainland China, or offshore processing of people in China to serve them or analyze their behavior (PIPL Art. 3); networks operated in China (CSL) | [`pipl-csl-compliance`](../../pipl-csl-compliance/SKILL.md)                 | `pipl-review-…`             |

## Sector and audience

| Regime                                 | Trigger to look for                                                                                                                                           | Skill                                                         | Report file          |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------- |
| US COPPA                               | Service directed to children under 13 in the US, mixed audience, actual knowledge of a user under 13, or an SDK or ad network on a child-directed service     | [`coppa-compliance`](../../coppa-compliance/SKILL.md)         | `coppa-review-…`     |
| Age-appropriate design codes           | Service likely to be accessed by under-18s in the UK, a US state with a design code, or on an EU online platform (DSA Art. 28)                                | [`aadc-compliance`](../../aadc-compliance/SKILL.md)           | `aadc-review-…`      |
| US HIPAA and French HDS                | Protected health information handled by or for a US covered entity; health data hosted for a third party in France                                            | [`hipaa-hds-compliance`](../../hipaa-hds-compliance/SKILL.md) | `hipaa-hds-review-…` |
| PCI DSS                                | The system stores, processes or transmits cardholder data, or can affect the security of a page or system that does, including hosted and iframe checkouts    | [`pci-dss-compliance`](../../pci-dss-compliance/SKILL.md)     | `pci-dss-review-…`   |
| EU PSD2 strong customer authentication | Payment or account access through a PSP in the EEA: card checkouts with 3-D Secure, bank logins, open-banking APIs, payment initiation or account information | [`psd2-sca-compliance`](../../psd2-sca-compliance/SKILL.md)   | `psd2-sca-review-…`  |

## Platforms, AI and distribution

| Regime                    | Trigger to look for                                                                                                                              | Skill                                                         | Report file          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | -------------------- |
| EU Digital Services Act   | Intermediary service offered to recipients in the EU: conduit, caching, hosting, online platform, marketplace or search engine                   | [`eu-dsa-compliance`](../../eu-dsa-compliance/SKILL.md)       | `dsa-review-…`       |
| EU AI Act                 | AI system or general-purpose AI model placed on the EU market, put into service or used in the EU, or whose output is used in the EU (Art. 2(1)) | [`eu-ai-act-compliance`](../../eu-ai-act-compliance/SKILL.md) | `ai-act-review-…`    |
| App Store and Google Play | An app distributed, or about to be submitted, through the Apple App Store or Google Play                                                         | [`app-store-compliance`](../../app-store-compliance/SKILL.md) | `app-store-review-…` |

## Coverage gaps

No sibling skill covers the regimes below. When the footprint reaches one, list it in the report as **Not covered** with the trigger that reached it, and route it to local counsel. The list is a prompt, not a complete register; check for others in every country of the footprint.

- **Other national privacy laws:** Switzerland (FADP), Japan (APPI), South Korea (PIPA), Singapore (PDPA), Australia (Privacy Act 1988), New Zealand (Privacy Act 2020), South Africa (POPIA), Türkiye (KVKK), Israel (Privacy Protection Law), Saudi Arabia and the UAE (PDPL), Nigeria (NDPA), Indonesia (PDP Law), Vietnam, Thailand (PDPA), Argentina and other Latin American laws.
- **EU and UK law outside the sibling skills:** NIS2 and DORA (cybersecurity and financial resilience), the Data Act, the Digital Markets Act, the European Accessibility Act, the UK Online Safety Act, and member-state employment, health and age-of-consent rules.
- **US law outside the sibling skills:** GLBA and FCRA, FERPA, BIPA and other biometric laws, state health-data laws such as Washington's My Health My Data Act, state breach-notification statutes, CAN-SPAM and TCPA, and the FTC Act Section 5.
- **Sector regimes:** financial services licensing and outsourcing rules, telecoms, education, employment monitoring, and export controls and sanctions.
