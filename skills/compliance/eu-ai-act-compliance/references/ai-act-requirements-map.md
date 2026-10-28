# AI Act requirements map

A compact map from review topics to the AI Act articles, the application timeline and official guidance. It summarizes; it does not replace the text. Quote or paraphrase the article itself in a finding, and open the source when the exact wording matters. Article numbers follow the consolidated text, including the amendments of the Digital Omnibus on AI.

## Official sources

- [Regulation (EU) 2024/1689 (AI Act), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj): the authoritative text, recitals and annexes. EUR-Lex may show a bot check to scripted requests; open it in a browser.
- [Regulation (EU) 2026/1744 (Digital Omnibus on AI), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2026/1744/oj): amends the timeline, Art. 4, SME regimes and adds prohibitions; in force since 27 July 2026. Read it with the AI Act until a consolidated version is published.
- [European Commission: AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai): guidelines, codes of practice, templates and implementation news.
- [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en): the Commission's FAQs and the single information platform.

## Application timeline

Checked 2026-10-28 against the AI Act and the Digital Omnibus. Check the live sources before relying on a date; postponements and transitional rules change.

| Date            | What applies                                                                                                          | Article          |
| --------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------- |
| 2 February 2025 | Definitions, AI literacy (Art. 4) and prohibited practices (Art. 5)                                                   | 113(a)           |
| 2 August 2025   | GPAI model obligations, governance, notified bodies, penalties                                                        | 113(b)           |
| 2 August 2026   | General application, including transparency (Art. 50) and Commission enforcement of GPAI obligations (Art. 101)        | 113              |
| 2 December 2026 | New prohibitions on non-consensual intimate imagery and CSAM generation (Art. 5(1)(ba)-(bb)); end of the Art. 50(2) marking grace period for generative systems placed on the market before 2 August 2026 | 113, 111(4)      |
| 2 August 2027   | GPAI models placed on the market before 2 August 2025 must comply                                                     | 111(3)           |
| 2 December 2027 | High-risk obligations for Annex III systems (Art. 6(2))                                                                | 113 as amended   |
| 2 August 2028   | High-risk obligations for Annex I product systems (Art. 6(1))                                                          | 113 as amended   |

High-risk systems already on the market before their date fall in scope only on a significant design change, except those used by public authorities, which must comply by 2 August 2030 (Art. 111(2)).

## Key definitions (Art. 3)

| Term                  | Article     | Review note                                                                                                                      |
| --------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| AI system             | 3(1)        | Machine-based, with some autonomy, inferring outputs from inputs; see the Commission guidelines on the definition                |
| Provider, deployer    | 3(3), 3(4)  | Provider develops or has developed and places on the market under its name; deployer uses it under its authority professionally  |
| Importer, distributor | 3(6), 3(7)  | Supply-chain roles with verification duties (Art. 23, 24)                                                                        |
| Intended purpose      | 3(12)       | Set by the provider's documentation and marketing; drives classification                                                         |
| Substantial modification | 3(23)    | A change that affects compliance or the intended purpose; makes the modifier a provider (Art. 25)                                |
| Serious incident      | 3(49)       | Death or serious harm to health, critical infrastructure disruption, fundamental-rights infringement, serious property or environmental harm |
| GPAI model            | 3(63)       | Significant generality, competent at a wide range of tasks; systemic risk presumed above 10^25 training FLOPs (Art. 51(2))       |

## Requirements by topic

| Topic                         | Articles            | What to verify                                                                                                                                                                                                                         |
| ----------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI literacy                   | 4                   | Providers and deployers take measures to support their staff's AI literacy (as amended by the Digital Omnibus)                                                                                                                        |
| Prohibited practices          | 5                   | Manipulation, exploiting vulnerabilities, social scoring, crime prediction from profiling alone, untargeted facial scraping, emotion recognition at work or school, sensitive biometric categorisation, real-time remote biometric ID for law enforcement, intimate-imagery and CSAM generation |
| High-risk classification      | 6, Annex I, Annex III | Safety component of an Annex I product needing third-party assessment, or an Annex III use (biometrics, critical infrastructure, education, employment, essential services and credit, law enforcement, migration, justice and elections) |
| Art. 6(3) derogation          | 6(3), 6(4), 49(2)   | Annex III system not high-risk when it only performs a narrow procedural or preparatory task, improves a completed human activity, or detects decision patterns without replacing human assessment; never when it profiles people; document the assessment and register |
| Risk management               | 9                   | Continuous, documented process across the lifecycle; foreseeable misuse; residual risk; testing against defined metrics; impact on minors and vulnerable groups                                                                       |
| Data and data governance      | 10, 4a              | Training, validation and test data relevant, representative, as error-free and complete as possible; documented provenance, preparation and bias examination; special-category data for bias correction only under the Art. 4a conditions |
| Technical documentation       | 11, Annex IV        | Drawn up before placing on the market and kept current; simplified form for SMEs and small mid-caps                                                                                                                                    |
| Record-keeping                | 12, 19, 26(6)       | Automatic event logs over the lifetime enabling traceability and post-market monitoring; providers and deployers keep logs at least six months                                                                                        |
| Transparency to deployers     | 13                  | Instructions for use: provider identity, purpose, accuracy and its metrics, known risks, human oversight measures, input data specs, log handling                                                                                       |
| Human oversight               | 14                  | Designed so natural persons can understand, monitor, interpret, override and stop the system; automation-bias awareness; two-person verification for remote biometric ID                                                               |
| Accuracy, robustness, security | 15                 | Declared accuracy metrics; resilience to errors and feedback loops; protection against data poisoning, model poisoning, adversarial examples and confidentiality attacks                                                               |
| Provider obligations          | 16-21, 43, 47-49, 72 | QMS (17), documentation kept ten years (18), corrective action and information duties (20), conformity assessment (43), EU declaration (47), CE marking (48), registration (49, 71), post-market monitoring (72)                       |
| Value chain                   | 22-25               | Authorised representative for non-EU providers, importer and distributor checks, role changes on rebranding or modification, written agreements with component suppliers (25(4))                                                     |
| Deployer obligations          | 26                  | Use per instructions, competent human oversight, relevant input data, monitoring, informing the provider of risks and incidents, log retention, informing workers and affected persons, registration by public bodies                 |
| Fundamental rights impact assessment | 27           | Before first use, by public bodies, private entities providing public services, and deployers of Annex III point 5(b)-(c) systems (credit scoring, life and health insurance pricing); notify the market surveillance authority         |
| Transparency obligations      | 50                  | Chatbot disclosure (50(1)); machine-readable marking of synthetic audio, image, video and text (50(2)); informing people exposed to emotion recognition or biometric categorisation (50(3)); deepfake and public-interest text labelling (50(4)) |
| GPAI models                   | 53, 54, Annex XI, XII | Technical documentation for the AI Office and downstream providers, copyright policy honouring opt-outs, public training-content summary on the Commission template, authorised representative for non-EU providers; open-source models partly exempt |
| GPAI with systemic risk       | 51, 52, 55          | Notify the Commission within two weeks of meeting the threshold; model evaluation and adversarial testing, systemic-risk mitigation, serious-incident reporting, cybersecurity                                                         |
| Serious incident reporting    | 73                  | Provider reports immediately after establishing the causal link, and within 15 days of awareness; 2 days for widespread infringements or critical-infrastructure disruption; 10 days for a death                                     |
| Right to explanation          | 86                  | Affected persons get clear explanations of the role of an Annex III system in a decision with legal or similarly significant effects                                                                                                 |
| Penalties                     | 99, 101             | Up to EUR 35 million or 7% for prohibited practices; EUR 15 million or 3% for most other obligations and for GPAI providers; EUR 7.5 million or 1% for misleading information to authorities                                            |

## Guidance worth opening

- [Guidelines on the AI system definition](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application)
- [Guidelines on prohibited AI practices](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act)
- [Draft guidelines on high-risk classification](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems): published as a draft in May 2026; check whether a final version has replaced it.
- [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai): transparency, copyright, and safety and security chapters; signing gives a recognised route to show compliance with Art. 53 and 55.
- [Template for the public summary of training content](https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models)
- [Code of Practice on marking and labelling AI-generated content](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content): the voluntary route for Art. 50(2) and 50(4), published June 2026.

Harmonised standards under Art. 40 are still being developed by CEN-CENELEC JTC 21; check which, if any, are cited in the Official Journal before treating one as giving a presumption of conformity.
