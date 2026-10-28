# PCI DSS requirements map

A compact map from review topics to PCI DSS v4.0.1 requirement numbers. It paraphrases a copyrighted standard; open the document itself when the exact wording or testing procedure matters.

## Official sources

- [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/): PCI DSS v4.0.1, every SAQ and its instructions, the ROC and AOC templates, the summary of changes, and information supplements (scoping and segmentation, tokenisation, e-commerce, third-party security).
- [PCI SSC FAQs](https://www.pcisecuritystandards.org/faqs/): the Council's official interpretations, cited by number.
- [PCI SSC glossary](https://www.pcisecuritystandards.org/glossary/): account data, CDE, connected-to and security-impacting systems, TPSP, truncation, tokenisation.
- [PCI DSS v4.0.1 publication note](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1): v4.0 retired on 31 December 2024; v4.0.1 adds no new requirements. Requirements that v4.0 marked as best practice became mandatory on 31 March 2025.
- [FAQ 1588 on the SAQ A script eligibility criterion](https://blog.pcisecuritystandards.org/faq-clarifies-new-saq-a-eligibility-criteria-for-e-commerce-merchants)

## Account data

| Element                                         | Class | Storage rule                                                                                                    |
| ----------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------- |
| PAN                                             | CHD   | Only with a documented business need and retention (3.2.1); unreadable wherever stored (3.5.1); masked on display (3.4.1) |
| Cardholder name, expiry date, service code      | CHD   | Protected when stored with the PAN                                                                               |
| Full track data, card verification code, PIN or PIN block | SAD | Not retained after authorization, even encrypted (3.3.1-3.3.1.3); encrypted if held before authorization completes (3.3.2); issuers only under 3.3.3 |

PAN presence decides scope: the other elements bring a system into scope only alongside the PAN. Masking (display) differs from truncation (storage); show at most the BIN and last four digits, with truncation formats per brand rules and the FAQs. Keyed cryptographic hashes cover the entire PAN (3.5.1.1); hashed and truncated versions of the same PAN need controls that stop them being correlated. Tokens that cannot be reversed in the entity's environment take the token store out of scope; tokenisation itself stays in the service provider's scope.

## The 12 principal requirements

| Req. | Goal                                                       | Review hot spots                                                                                                     |
| ---- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1    | Network security controls                                  | Accurate network and data-flow diagrams (1.2.3, 1.2.4); inbound and outbound CDE traffic restricted (1.3, 1.4)       |
| 2    | Secure configurations                                      | Vendor defaults changed, one primary function per server, unnecessary services off (2.2)                             |
| 3    | Protect stored account data                                | Retention (3.2.1), no SAD after authorization (3.3.1), masking (3.4.1), PAN unreadable (3.5.1), key management (3.6, 3.7) |
| 4    | Strong cryptography in transmission over open, public networks | Trusted keys and valid certificates (4.2.1, 4.2.1.1); PAN over end-user messaging secured (4.2.2)            |
| 5    | Anti-malware                                               | Coverage, updates, scans; anti-phishing mechanisms (5.4.1)                                                          |
| 6    | Secure systems and software                                | Secure coding (6.2.4), software and component inventory (6.3.2), critical patches within one month (6.3.3), automated protection of public-facing web apps (6.4.2), payment-page scripts (6.4.3), no live PANs in pre-production (6.5.5) |
| 7    | Access by business need to know                            | Least privilege for users, application and system accounts (7.2.1-7.2.6)                                             |
| 8    | Identify users and authenticate access                     | Unique IDs (8.2.1), idle timeout 15 minutes (8.2.8), lockout after at most 10 attempts (8.3.4), passwords at least 12 characters (8.3.6), MFA (8.4.1-8.4.3, 8.5.1), no hard-coded system-account passwords (8.6.2) |
| 9    | Physical access                                            | Media, POI device inspection and tamper checks (9.5)                                                                 |
| 10   | Log and monitor all access                                 | Required events (10.2.1.1-10.2.1.7) and fields (10.2.2), log protection (10.3), automated review (10.4.1.1), 12 months retained with 3 immediately available (10.5.1), time sync (10.6), critical control failures detected (10.7.2) |
| 11   | Test security regularly                                    | Quarterly internal and ASV scans (11.3.1, 11.3.2), annual penetration test (11.4), segmentation tests (11.4.5, six-monthly for service providers 11.4.6), payment-page tamper detection (11.6.1) |
| 12   | Policies and programs                                      | Targeted risk analyses (12.3.1, 12.3.2), scope confirmed every 12 months (12.5.2), TPSP management (12.8), service providers' acknowledgements (12.9), incident response including unexpected stored PAN (12.10.7) |

Each requirement's x.1.1 and x.1.2 sub-requirements demand documented policies and assigned roles. Appendix A1 covers multi-tenant service providers, A2 early TLS on POS POI terminals, A3 designated entities.

## SAQ types and integration choice

The acquirer decides which validation form it accepts; the SAQ instructions hold the binding eligibility criteria.

| SAQ          | Fits                                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| A            | Card-not-present, all account-data functions outsourced to PCI DSS compliant TPSPs: redirect to a hosted page, or an iframe from the TPSP. Since the January 2025 revision, 6.4.3 and 11.6.1 are out of SAQ A, replaced by an eligibility criterion that the merchant's site is not susceptible to script attacks (FAQ 1588) |
| A-EP         | E-commerce where the merchant's page builds or affects the payment form but never receives the PAN: direct post, JavaScript-built fields |
| D (merchant) | The merchant's servers receive, store or transmit the PAN (server-side card API) or no other SAQ fits                       |
| D (service provider) | Every service provider eligible to self-assess                                                                     |
| B, B-IP, C, C-VT, P2PE, SPoC | Card-present terminals, payment application systems, virtual terminals, validated P2PE solutions, software-based PIN entry on COTS devices |

## Payment-page scripts (6.4.3, 11.6.1)

6.4.3: every script on the payment page that runs in the consumer's browser is authorized, its integrity assured, and inventoried with a written justification. 11.6.1: a change- and tamper-detection mechanism alerts on unauthorized changes to the security-impacting HTTP headers and script contents of the payment page as the browser receives it, at least weekly or at the frequency a targeted risk analysis sets. They apply to the merchant page that embeds a TPSP iframe too; scripts inside the TPSP's frame are the TPSP's to control.

## Targeted risk analysis and customized approach

- 12.3.1: a targeted risk analysis, reviewed at least every 12 months, for each requirement that lets the entity set the frequency (for example 5.2.3.1, 7.2.5.1, 10.4.2.1, 11.6.1).
- Customized approach (12.3.2, Appendices D and E): meet a requirement's stated objective with a different control, backed by a per-requirement targeted risk analysis and a controls matrix the assessor tests. Available only with a ROC, not in an SAQ, and only where the requirement offers it.
- Compensating controls (Appendix B, worksheet in Appendix C): for a documented legitimate constraint, under the defined approach.
