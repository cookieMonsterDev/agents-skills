# GDPR requirements map

A compact map from review topics to the GDPR articles and official guidance behind them. It summarizes; it does not replace the text. Quote or paraphrase the article itself in a finding, and open the source when the exact wording matters.

## Official sources

- [Regulation (EU) 2016/679 (GDPR), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj): the authoritative text, recitals included. EUR-Lex may show a bot check to scripted requests; open it in a browser.
- [EDPB guidelines, recommendations and best practices](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en): the index of current interpretive guidance.
- [EDPB members (national supervisory authorities)](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en): for national guidance and where to notify or complain.
- [European Commission: data protection](https://commission.europa.eu/law/law-topic/data-protection_en): adequacy decisions, standard contractual clauses and transfer frameworks.
- [Directive 2002/58/EC (ePrivacy Directive), EUR-Lex](https://eur-lex.europa.eu/eli/dir/2002/58/oj): Art. 5(3) governs storing or reading information on a user's device (cookies, local storage, SDK identifiers), implemented through national law.

## Key definitions (Art. 4)

| Term                  | Article    | Review note                                                                                                                                |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Personal data         | 4(1)       | Any information relating to an identified or identifiable person, including online identifiers, device IDs, IP addresses and location data |
| Processing            | 4(2)       | Any operation: collection, storage, logging, analytics, transfer, deletion                                                                 |
| Pseudonymisation      | 4(5)       | Reduces risk but the data stays personal data; anonymous data is outside scope (Recital 26)                                                |
| Controller, processor | 4(7), 4(8) | Decides role-specific duties; see EDPB Guidelines 07/2020                                                                                  |
| Consent               | 4(11)      | Freely given, specific, informed and unambiguous, by a clear affirmative act                                                               |
| Personal data breach  | 4(12)      | Includes loss of availability and accidental disclosure, not only attacks                                                                  |

## Requirements by topic

| Topic                         | Articles          | What to verify                                                                                                                                                                                                                                                |
| ----------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scope                         | 2, 3              | Material and territorial scope; household exemption; non-EU organizations targeting or monitoring people in the EU need an EU representative (Art. 27)                                                                                                        |
| Principles                    | 5(1)(a)-(f), 5(2) | Lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability (able to demonstrate compliance)                                                                    |
| Lawful basis                  | 6(1)(a)-(f)       | One basis per purpose: consent, contract, legal obligation, vital interests, public task, legitimate interests (needs a documented balancing test); further compatible processing under 6(4)                                                                  |
| Consent                       | 7, 8              | Provable, separable from other terms, withdrawable as easily as given, not a condition of service when unnecessary; children's consent for online services: 16 by default, member states may lower it to no less than 13                                      |
| Special categories            | 9, 10             | Health, biometric for identification, genetic, racial or ethnic origin, political opinions, religious beliefs, trade-union membership, sex life or orientation: need an Art. 9(2) condition as well as an Art. 6 basis; criminal data needs Art. 10 authority |
| Transparency                  | 12, 13, 14        | Concise, plain-language notice with every required item; respond to requests within one month, extendable by two further months with reasons                                                                                                                  |
| Data subject rights           | 15-22             | Access (15), rectification (16), erasure (17), restriction (18), notifying recipients (19), portability (20), objection (21, absolute for direct marketing), safeguards for solely automated decisions with legal or similarly significant effect (22)        |
| Accountability and design     | 24, 25            | Appropriate measures; data protection by design and by default: only data necessary for each purpose processed by default (EDPB Guidelines 4/2019)                                                                                                            |
| Joint controllers, processors | 26, 28, 29        | Joint-controller arrangement; written processor contract with the Art. 28(3) terms; sub-processor authorization                                                                                                                                               |
| Records of processing         | 30                | Required content; the under-250-employees exemption does not apply to risky, non-occasional or special-category processing                                                                                                                                    |
| Security                      | 32                | Risk-appropriate measures such as pseudonymisation and encryption, confidentiality, integrity, availability and resilience, restore capability, and regular testing                                                                                           |
| Breach handling               | 33, 34            | Notify the supervisory authority within 72 hours of becoming aware unless unlikely to result in risk; tell data subjects without undue delay when high risk; document every breach (33(5))                                                                    |
| DPIA                          | 35, 36            | Required for likely high risk: systematic profiling with significant effects, large-scale special categories, systematic large-scale monitoring of public areas, and national DPIA lists; prior consultation when residual risk stays high                    |
| DPO                           | 37-39             | Mandatory for public bodies, large-scale regular and systematic monitoring, or large-scale special-category processing                                                                                                                                        |
| International transfers       | 44-49             | Adequacy decision (45), appropriate safeguards such as standard contractual clauses (46), binding corporate rules (47), or narrow derogations (49); assess the destination's law for SCC transfers (EDPB Recommendations 01/2020)                             |
| Penalties                     | 83                | Up to EUR 20 million or 4% of worldwide annual turnover for principles, bases, rights and transfers; up to EUR 10 million or 2% for many controller and processor obligations                                                                                 |

## EDPB guidance worth opening

- [Guidelines 05/2020 on consent](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en): cookie walls, scrolling as consent, granularity, withdrawal.
- [Guidelines 4/2019 on Article 25, data protection by design and by default](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en)
- [Guidelines 07/2020 on the concepts of controller and processor](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020-concepts-controller-and-processor-gdpr_en)
- [Guidelines 01/2022 on the right of access](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-012022-data-subject-rights-right-access_en)
- [Guidelines 9/2022 on personal data breach notification](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en)
- [Recommendations 01/2020 on measures that supplement transfer tools](https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en)
- [Guidelines 03/2022 on deceptive design patterns](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media_en): consent and settings interfaces.
- [Guidelines 2/2023 on the technical scope of Art. 5(3) ePrivacy](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en): tracking pixels, URL tracking, local storage, SDKs.

## Transfer instruments

- [Commission Implementing Decision (EU) 2021/914, standard contractual clauses for transfers](https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj): modules for controller-to-controller, controller-to-processor, processor-to-processor and processor-to-controller.
- [Commission Implementing Decision (EU) 2023/1795, EU-US Data Privacy Framework](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj): adequacy covers only US organizations certified under the framework. Check the current status and the recipient's certification before relying on it.

The adequacy list changes; check the Commission's data protection pages for the current list rather than relying on memory.
