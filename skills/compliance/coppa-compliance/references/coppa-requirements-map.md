# COPPA requirements map

A compact map from review topics to the COPPA statute, the FTC COPPA Rule (16 CFR Part 312, as amended 90 FR 16977, April 22, 2025) and FTC guidance. It summarizes; it does not replace the text. Quote or paraphrase the section itself in a finding, and open the source when the exact wording matters.

## Official sources

- [16 CFR Part 312, eCFR](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312): the current Rule text. eCFR may show a bot check to scripted requests; open it in a browser.
- [2025 amendments, Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule): effective June 23, 2025; compliance date April 22, 2026, with earlier dates for safe harbor programs in §312.11. The preamble explains each change.
- [15 U.S.C. chapter 91 (§§6501-6506), LII](https://www.law.cornell.edu/uscode/text/15/chapter-91): the statute.
- FTC: Complying with COPPA, Frequently Asked Questions: staff interpretation; check its revision date against the 2025 amendments.
- FTC Enforcement Policy Statement on age verification (February 25, 2026): enforcement discretion for general- and mixed-audience operators collecting data solely to verify age; in force until Rule amendments on age verification are final or it is withdrawn.
- FTC COPPA safe harbor programs: the approved programs.

## Key definitions (§312.2)

| Term                     | Review note                                                                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Child                    | Under 13                                                                                                                                                                                                 |
| Collects                 | Requesting or prompting submission, enabling a child to make information public, or passive tracking                                                                                                   |
| Personal information     | Name, address, online contact information, screen name used as contact, phone, government ID, persistent identifier, photo, video or audio with the child's image or voice, geolocation to street and city, biometric identifiers (fingerprints, voiceprints, facial templates, gait, genetic data), and information combined with any of these |
| Persistent identifier    | Recognizes a user over time and across sites or services: cookie IDs, IP address, device serial or advertising ID                                                                                        |
| Support for internal operations | Maintaining or analyzing functioning, network communications, authentication and personalization, contextual ads and frequency capping, security, legal compliance, fulfilling a child's request; never to contact a specific person, behavioral advertising or profiling |
| Third party              | Anyone other than the operator or an internal-operations service provider that uses the data for nothing else                                                                                           |
| Mixed audience           | Child-directed by the factors but not primarily for children, and collects nothing beyond §312.5(c) before a neutral age screen; age screens must not default to an age or encourage falsifying it    |
| Delete                   | Not maintained in retrievable form and not retrievable in the normal course of business                                                                                                                |

## Directed to children

The FTC weighs: subject matter, visual content, animated characters, child-oriented activities and incentives, music and audio, age of models, child celebrities, language, child-directed advertising, and empirical audience evidence, including marketing plans, representations to consumers or third parties, user and third-party reviews, and the age of users on similar services. A service with actual knowledge that it collects directly from users of a child-directed service (an SDK or ad network embedded in a kids' app) is itself treated as directed to children. Linking to a child-directed service alone does not make a service child-directed.

## Requirements by topic

| Topic                           | Section                       | What to verify                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coverage                        | §312.3; 15 U.S.C. 6502(a)     | Child-directed operators and operators with actual knowledge of collecting from a child                                                                                                                                             |
| Online notice                   | §312.4(d)                     | Prominent link on the home page and at each collection point; all operators' contact details; what is collected, how used, disclosure practices with third-party identities or categories and purposes; retention policy; internal-operations identifier uses and safeguards; parental rights |
| Direct notice                   | §312.4(b)-(c)                 | Sent to the parent before collection, and on material change; content per purpose: consent (c)(1), voluntary notice (c)(2), multiple contacts (c)(3), safety (c)(4)                                                                |
| Verifiable parental consent     | §312.5(a)-(b)                 | Before any collection, use or disclosure; a method reasonably calculated to reach the parent; listed methods in (b)(2)(i)-(ix); safe-harbor-approved methods (b)(3)                                                                    |
| Separate third-party consent    | §312.5(a)(2)                  | Parent can consent to collection and use without consenting to third-party disclosure (targeted advertising, data sales) unless integral to the service; separate VPC for that disclosure                                            |
| Consent exceptions              | §312.5(c)(1)-(9)              | Obtaining consent, voluntary notice, one-time response, multiple responses, child safety, security and legal process, persistent identifier for internal operations only, previously registered adult user, audio file deleted after a request |
| Parental rights                 | §312.6                        | Describe categories collected, review the data, refuse further use and collection, delete; verify the requester is the parent without undue burden                                                                                |
| No conditioning                 | §312.7                        | Participation in a game, prize or activity needs no more personal information than reasonably necessary                                                                                                                            |
| Security                        | §312.8                        | Reasonable procedures plus a written information security program: named coordinator, at least annual risk assessments, safeguards, testing and monitoring, annual evaluation; vendor diligence and written assurances before release |
| Retention and deletion          | §312.10                       | Only as long as reasonably necessary; no indefinite retention; written retention policy with purposes, business need and deletion timeframe, published in the online notice; secure deletion                                     |
| Safe harbor                     | §312.11; 15 U.S.C. 6503       | Compliance with approved guidelines is deemed compliance with §§312.2-312.8 and 312.10; programs report annually and publish member lists                                                                                          |
| Enforcement and penalties       | §312.9; 15 U.S.C. 6502(c), 6504, 6505 | A violation is a violation of an FTC trade regulation rule; civil penalties under FTC Act §5(m)(1)(A), $53,088 per violation (16 CFR 1.98(d); the 2026 inflation adjustment was cancelled, so 2025 amounts apply); state attorneys general may sue; no private right of action |
| Preemption                      | 15 U.S.C. 6502(d)             | Inconsistent state law on child-directed collection is preempted; consistent state laws, including those covering teens, still apply                                                                                               |

## Verifiable parental consent methods (§312.5(b)(2))

(i) signed form by mail, fax or scan; (ii) credit, debit or other payment system with transaction notice to the account holder; (iii) toll-free call to trained staff; (iv) video conference with trained staff; (v) government ID checked against databases, deleted promptly; (vi) knowledge-based authentication with dynamic multiple-choice questions a child could not answer (new in 2025); (vii) government photo ID matched to a live face image by facial recognition and confirmed by trained staff, both deleted promptly (new in 2025); (viii) email plus, and (ix) text plus (new in 2025): only for operators that do not disclose children's data, with a confirming step and notice that consent can be revoked.

Check live whether the FTC's announced age-verification rule review has produced amendments, and whether federal bills extending protection to teens have been enacted.
