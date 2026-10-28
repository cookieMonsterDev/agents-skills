# UK GDPR requirements map

A compact map from review topics to the UK GDPR, the DPA 2018, PECR and the DUAA amendments. It summarizes; it does not replace the text. Quote or paraphrase the provision itself in a finding, and open the source when the exact wording matters. The UK GDPR shares most article numbers with the EU GDPR; this map lists the topics where UK law now differs, and [`gdpr-compliance`](../../gdpr-compliance/references/gdpr-requirements-map.md) covers the shared baseline.

## Official sources

- [UK GDPR, legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/contents): the retained Regulation as amended; select the point-in-time view for a date before an amendment.
- [Data Protection Act 2018](https://www.legislation.gov.uk/ukpga/2018/12/contents): exemptions, Schedule 1 conditions for special category and criminal offence data, ICO powers, complaints (s. 164A), fines (s. 155-157).
- [Privacy and Electronic Communications Regulations 2003 (PECR)](https://www.legislation.gov.uk/uksi/2003/2426/contents): cookies and similar technologies (reg. 6, Schedule A1), electronic marketing (reg. 19-24).
- [Data (Use and Access) Act 2025 (DUAA)](https://www.legislation.gov.uk/ukpga/2025/18/contents): the amending Act; Part 5 changes the UK GDPR, DPA 2018 and PECR.
- [DUAA plans for commencement, GOV.UK](https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement): which provisions are in force, by commencement regulation.
- [ICO UK GDPR guidance and resources](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/) and [ICO DUAA hub](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/): guidance, with updates for each DUAA change.

## DUAA changes and when they apply

| Change                              | Provision                               | In force         | What to verify                                                                                                                                                                                   |
| ----------------------------------- | --------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reasonable and proportionate search | UK GDPR Art. 15(1A) (DUAA s. 78)        | Treated as from 1 Jan 2024 | Subject access covers what a reasonable and proportionate search finds; the search approach is documented                                                                                         |
| Response time limits               | Art. 12A (DUAA s. 76)                   | 5 Feb 2026       | One month runs from receipt, identity confirmation or fee; the clock pauses while awaiting reasonably needed clarification; extension by two months for complex or numerous requests             |
| Recognised legitimate interests     | Art. 6(1)(ea), Annex 1 (DUAA s. 70, Sch. 4) | 5 Feb 2026   | Only the five listed conditions (disclosure to a public body for its task, national security and defence, emergencies, crime, safeguarding vulnerable individuals); no balancing test; not for public authorities' own tasks |
| Legitimate interest examples        | Art. 6(11)                              | 5 Feb 2026       | Direct marketing, intra-group transmission for internal administration and network security may be legitimate interests; Art. 6(1)(f) balancing still applies                                    |
| Further processing                  | Art. 8A, Annex 2 (DUAA s. 71, Sch. 5)   | 5 Feb 2026       | Compatibility test and the listed compatible purposes                                                                                                                                             |
| Automated decision-making           | Art. 22A-22D (DUAA s. 80)               | 5 Feb 2026       | Solely automated significant decisions are allowed with safeguards (information, representations, human intervention, contest) (22C); restricted for special category data (22B(1)-(3)) and barred where processing relies on Art. 6(1)(ea) (22B(4)) |
| Children's higher protection        | Art. 25 (DUAA s. 81)                    | 5 Feb 2026       | Information society services likely to be accessed by children account for children's higher protection matters in design                                                                       |
| International transfers             | Chapter 5, from Art. 44A (DUAA s. 85, Sch. 7) | 5 Feb 2026   | The "data protection test": protection in the destination not materially lower than in the UK; existing adequacy regulations, IDTA and Addendum continue                                        |
| Malicious-allegation erasure ground | Art. 17(1)(g) (DUAA Sch. 11 para. 32)   | 31 Mar 2026      | Erasure where data was processed because of an unfounded allegation by a malicious person                                                                                                        |
| Complaints to controllers           | DPA 2018 s. 164A (DUAA s. 103)          | 19 Jun 2026      | A means to complain (an electronic form, for example); acknowledge within 30 days; investigate without undue delay; inform of the outcome                                                         |
| Cookie exemptions                   | PECR reg. 6, Schedule A1 (DUAA s. 112, Sch. 12) | 5 Feb 2026 | Consent, or an exception: transmission, strictly necessary, statistical analytics or website appearance and functionality (each with clear information and a free, simple means to object), emergency location |
| Charity soft opt-in                 | PECR reg. 22 (DUAA s. 114)              | 5 Feb 2026       | Charities may email supporters who showed interest, with an opt-out at collection and in each message                                                                                            |
| PECR enforcement                    | PECR reg. 31 onward (DUAA s. 115, Sch. 13) | 5 Feb 2026    | UK GDPR-level fines (up to £17.5 million or 4% of worldwide turnover) and investigation powers; conduct before 5 February 2026 stays under the old regime                                        |
| Regulator                           | DUAA s. 117-120                         | 30 Sep 2026      | The Information Commission replaces the Information Commissioner; powers unchanged                                                                                                               |

## Unchanged UK specifics

| Topic                    | Provision                                     | What to verify                                                                                                                                                      |
| ------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UK representative        | Art. 27                                       | Non-UK controllers or processors in Art. 3(2) scope designate a UK representative in writing, unless processing is occasional and low risk                         |
| Children's consent age   | Art. 8; DPA 2018 s. 9                         | 13 for information society services offered directly to a child                                                                                                    |
| Special category data    | Art. 9; DPA 2018 s. 10, Sch. 1                | A Schedule 1 condition, and an appropriate policy document where Schedule 1 requires one                                                                           |
| Breach notification      | Art. 33, 34                                   | Report to the ICO within 72 hours unless unlikely to result in risk; tell individuals when high risk; record all breaches                                          |
| Electronic marketing     | PECR reg. 21-22                               | Prior consent for marketing email and SMS to individuals, or the soft opt-in for similar products from a sale or negotiation; screen live calls against the TPS    |
| Data protection fee      | Data Protection (Charges and Information) Regulations 2018 | Controllers pay a tiered annual fee unless exempt; check the [ICO fee page](https://ico.org.uk/for-organisations/data-protection-fee/) for current tiers |
| Fines                    | Art. 83; DPA 2018 s. 157                      | Up to £17.5 million or 4% of worldwide turnover (higher maximum), £8.7 million or 2% (standard maximum)                                                            |

## Transfer instruments

- [ICO international transfers guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/) and [the IDTA and the Addendum](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/appropriate-safeguards/what-are-standard-data-protection-clauses-the-uk-idta-and-the-addendum/): the UK's standard data protection clauses; the Addendum attaches to the EU SCCs. The ICO plans to update both in 2026; check which version is current.
- [UK-US data bridge (SI 2023/1028)](https://www.legislation.gov.uk/uksi/2023/1028/contents/made): covers only US organizations certified to the UK Extension of the EU-US Data Privacy Framework; check the recipient's certification.
- The EU renewed its adequacy decisions for the UK on 19 December 2025, to 27 December 2031; this governs EU-to-UK flows, not UK exports.

## ICO guidance worth opening

- [Guidance on storage and access technologies](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/) and the [Guide to PECR](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/)
- [Recognised legitimate interest](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/recognised-legitimate-interest/)
- [Right of access](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/right-of-access/)
- [How to deal with data protection complaints](https://ico.org.uk/for-organisations/how-to-deal-with-data-protection-complaints/)
- [Report a breach](https://ico.org.uk/for-organisations/report-a-breach/)

Commencement, adequacy regulations, fee tiers and ICO guidance change: check the live source rather than relying on memory.
