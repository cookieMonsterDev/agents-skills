# LGPD requirements map

A compact map from review topics to the LGPD articles and ANPD regulations behind them. It summarizes; it does not replace the text. Quote or paraphrase the article itself in a finding, and open the source when the exact wording matters.

## Official sources

- [Lei nº 13.709/2018 (LGPD), Planalto](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm): the authoritative consolidated text, in Portuguese. Planalto may block scripted or foreign requests; open it in a browser.
- [ANPD regulations (Regulamentações da ANPD)](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd): every resolution and enunciado in force, with its status and links to the Diário Oficial text.
- [ANPD guidance and publications](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes): guides on agents and the encarregado, legitimate interest, cookies, security for small agents, and the RIPD.
- [ANPD incident communication](https://www.gov.br/anpd/pt-br/assuntos/incidente-de-seguranca): the form and instructions for communicating a security incident.
- [ANPD international affairs](https://www.gov.br/anpd/pt-br/assuntos/assuntos-internacionais): adequacy decisions and transfer mechanisms.

## Key definitions (Art. 5)

| Term                    | Article       | Review note                                                                                                                       |
| ----------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Personal data           | 5(I)          | Information related to an identified or identifiable natural person, including online identifiers                                 |
| Sensitive personal data | 5(II)         | Racial or ethnic origin, religious belief, political opinion, union or religious, philosophical or political membership, health, sex life, genetic or biometric data |
| Anonymised data         | 5(III), 12    | Out of scope only while re-identification is not possible with reasonable means; data used to build behavioural profiles may count as personal (Art. 12 §2) |
| Controller, operator    | 5(VI), 5(VII) | Controller decides; operator processes on the controller's behalf and instructions (Art. 39)                                       |
| Encarregado             | 5(VIII), 41   | Channel between controller, data subjects and the ANPD; regulated by Res. CD/ANPD 18/2024                                          |
| Consent                 | 5(XII), 8     | Free, informed and unambiguous expression for a specific purpose                                                                   |
| RIPD                    | 5(XVII), 38   | Data protection impact report: processes that may create risks, with measures and safeguards                                       |

## Requirements by topic

| Topic                     | Source                              | What to verify                                                                                                                                                                                                                                               |
| ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scope                     | Art. 3, 4                           | Territorial triggers; exclusions for private non-economic use, journalism, art, academia, public security and data from abroad not shared with Brazilian agents                                                                                              |
| Principles                | Art. 6(I)-(X)                       | Good faith plus purpose, adequacy, necessity, free access, data quality, transparency, security, prevention, non-discrimination, accountability                                                                                                              |
| Legal bases               | Art. 7(I)-(X), 10                   | One basis per purpose: consent, legal or regulatory obligation, public administration, research, contract, exercise of rights in proceedings, protection of life, health protection, legitimate interest (Art. 10 balancing, RIPD on request), credit protection |
| Consent                   | Art. 8, 9                           | Written or otherwise demonstrable, burden on the controller (8 §2); generic authorizations are void (8 §4); revocable free of charge (8 §5); Art. 9 information given clearly                                                                                 |
| Sensitive data            | Art. 11                             | Specific and highlighted consent, or one of the Art. 11(II) bases (no legitimate interest or credit protection; contract only as the regular exercise of rights, 11(II)(d)); fraud prevention and authentication security allowed (11(II)(g)); health data sharing for economic advantage restricted (11 §4)        |
| Children and adolescents  | Art. 14; Enunciado CD/ANPD 1/2023   | Best interest of the child; Art. 7 and 11 bases are available (Enunciado 1/2023), with specific parental consent for children where consent is the basis (14 §1); games and apps collect only what is strictly necessary (14 §4); age-appropriate information (14 §6) |
| Termination and retention | Art. 15, 16                         | Delete at end of purpose, period, revocation or ANPD order; retention only for the Art. 16 grounds (legal obligation, research, transfer to third party, controller's exclusive anonymised use)                                                              |
| Data subject rights       | Art. 17-22                          | Art. 18(I)-(IX); confirmation and access simplified immediately or complete within 15 days (Art. 19); review of automated decisions and their criteria (Art. 20); free of charge (18 §5); inform recipients of corrections and deletions (18 §6)              |
| Records and RIPD          | Art. 37, 38, 10 §3                  | Controller and operator keep records of processing; RIPD when the ANPD requests it, and as the practical evidence for legitimate interest and high-risk processing. No RIPD regulation was in force at the last check; check the live source        |
| Agents and encarregado    | Art. 37-42; Res. 18/2024            | Operator follows instructions; joint liability (Art. 42); encarregado appointed and identity and contact published on the website (Art. 41 §1); small agents exempt but must offer a channel (Res. 2/2022, Art. 11)                                           |
| Security                  | Art. 46-49, 50                      | Technical and administrative measures from design onward (46 §2); confidentiality duty on everyone in processing (Art. 47); governance programme as good practice (Art. 50)                                                                                 |
| Security incidents        | Art. 48; Res. 15/2024               | Communicate the ANPD and affected data subjects within 3 business days of knowing an incident with relevant risk or harm affected personal data (Art. 6, 9); supplement within 20 business days; record every incident for 5 years (Art. 10); small agents get double |
| International transfers   | Art. 33-36; Res. 19/2024            | Adequacy, ANPD standard contractual clauses adopted in full and unaltered (Res. 19, Art. 16), global corporate rules, specific clauses approved by the ANPD, or the other Art. 33 grounds; plus an Art. 7 or 11 basis; transparency page in Portuguese (Res. 19, Art. 17) |
| Small agents              | Res. 2/2022                         | Simplified records (Art. 9) and security policy (Art. 13); doubled deadlines (Art. 14); excluded when processing is high-risk (Art. 3-4: one general and one specific criterion)                                                                             |
| Sanctions                 | Art. 52-54; Res. 4/2023             | Warning; fine up to 2% of revenue in Brazil, capped at BRL 50 million per infraction; daily fine; publicization; blocking or deletion of data; suspension and prohibition of processing. Res. 4/2023 sets the dosimetry                                        |

## Transfer instruments

- [Resolução CD/ANPD nº 19/2024](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024): the international transfer regulation with the standard contractual clauses in Annex II. The 12-month grace period for incorporating them ended on 23 August 2025; contractual transfers now need the ANPD clauses or ANPD-approved specific clauses. The ANPD may recognise foreign clauses as equivalent (Art. 18-20).
- Resolução CD/ANPD nº 32/2026 recognises the European Union as adequate for transfers from Brazil. Check the [ANPD regulations page](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd) for further adequacy decisions before relying on memory.

## Small agents

[Resolução CD/ANPD nº 2/2022](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022) defines small agents by the revenue limits of Lei Complementar 123/2006 and 182/2021, and excludes any agent whose economic group exceeds them or whose processing is high-risk: large-scale or significantly affecting rights, combined with emerging technology, monitoring of public areas, solely automated decisions, or sensitive, children's or elderly people's data.
