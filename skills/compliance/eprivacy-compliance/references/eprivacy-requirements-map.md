# ePrivacy requirements map

A compact map from review topics to the ePrivacy Directive articles and official guidance behind them. It summarizes; it does not replace the text or the national implementing law. Quote or paraphrase the article itself in a finding, and open the source when the exact wording matters.

## Official sources

- [Directive 2002/58/EC (ePrivacy Directive), EUR-Lex](https://eur-lex.europa.eu/eli/dir/2002/58/oj): the base text. Open the consolidated version from this page for the 2009 amendments. EUR-Lex may show a bot check to scripted requests; open it in a browser.
- [Directive 2009/136/EC, EUR-Lex](https://eur-lex.europa.eu/eli/dir/2009/136/oj): replaced the Art. 5(3) opt-out with consent; Recital 66 covers browser settings and the exemptions.
- [Regulation (EU) 2016/679 (GDPR), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj): Art. 4(11) and 7 set the consent standard that ePrivacy consent must meet (GDPR Art. 94(2), 95).
- [EDPB guidelines, recommendations and best practices](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en): the index of current interpretive guidance.
- [EDPB members (national supervisory authorities)](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en): national guidance. In some member states Art. 5(3) is enforced by a telecom or consumer authority, not the data protection authority; confirm per state.

## Requirements by topic

| Topic                        | Articles              | What to verify                                                                                                                                                                                                                                                                                  |
| ---------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scope of Art. 5(3)           | 5(3)                  | Any storing of information, or gaining access to information already stored, in a user's terminal equipment, whether or not it is personal data (CJEU C-673/17 Planet49). Covers cookies, web storage, SDK and advertising IDs, pixels, URL tracking and fingerprinting (EDPB Guidelines 2/2023) |
| Consent                      | 5(3); GDPR 4(11), 7   | Prior, freely given, specific, informed, unambiguous affirmative act; pre-ticked boxes and continued browsing fail (Planet49); provable; withdrawable as easily as given                                                                                                                        |
| Exemptions                   | 5(3)                  | Only (a) sole purpose of carrying out the transmission of a communication, or (b) strictly necessary for a service the user explicitly requested. Read narrowly, per purpose; analytics and advertising fall outside unless national law adds an exemption                                       |
| Information                  | 5(3)                  | Clear and comprehensive information, under the GDPR's transparency standard, before storage or access: purposes, parties, duration                                                                                                                                                              |
| Confidentiality              | 5(1)                  | Interception or surveillance of communications content and related traffic data without consent is prohibited, outside legal authorisation                                                                                                                                                      |
| Traffic data                 | 6                     | ECS providers erase or anonymise traffic data when no longer needed for transmission; billing use only until the bill can be challenged; marketing and value-added services only with consent, after informing the user                                                                         |
| Location data                | 9                     | Location data other than traffic data only anonymised or with consent for a value-added service; the user can refuse temporarily, free and simply, per connection                                                                                                                                |
| Security and breaches        | 4                     | ECS providers secure the service and notify personal data breaches to the national authority; Commission Regulation (EU) No 611/2013 sets timing (24 hours) and content                                                                                                                         |
| Unsolicited marketing        | 13(1)                 | Automated calling systems, fax and electronic mail (email, SMS, MMS: Art. 2(h)) for direct marketing need prior consent; in-inbox ads count as electronic mail (CJEU C-102/20 StWL)                                                                                                            |
| Soft opt-in                  | 13(2)                 | Existing customer's details obtained in a sale of a product or service, used by the same person for its own similar products or services, with a free, easy opt-out offered at collection and in every message                                                                                 |
| Other channels, legal persons | 13(3), 13(5)         | Member states choose opt-in or opt-out for other channels (live phone calls) and set protection for legal persons; check national law                                                                                                                                                           |
| Sender identity              | 13(4)                 | No disguised or concealed sender, a valid address for opt-out requests, and no messages that breach Directive 2000/31/EC Art. 6                                                                                                                                                                |
| Directories                  | 12                    | Subscribers informed and able to decide whether to be listed                                                                                                                                                                                                                                    |
| Penalties                    | 15a                   | Set nationally; GDPR-level fines apply where national law routes Art. 5(3) through the GDPR authority                                                                                                                                                                                            |

Arts. 4, 6 and 9 bind providers of publicly available electronic communications services, which since Directive (EU) 2018/1972 include number-independent interpersonal communications services such as messaging apps.

## EDPB guidance and case law worth opening

- [Guidelines 2/2023 on the technical scope of Art. 5(3)](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en): pixels, URL and link decoration, local processing, IP-only tracking, IoT reporting.
- [Guidelines 05/2020 on consent](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en): cookie walls, scrolling as consent, granularity, withdrawal.
- [Guidelines 03/2022 on deceptive design patterns](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media_en): banner and settings interfaces.
- [Cookie Banner Taskforce report (January 2023)](https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-cookie-banner-taskforce_en): reject button on the first layer, pre-ticked boxes, deceptive colours, legitimate interest for cookies.
- [CJEU C-673/17 Planet49](https://curia.europa.eu/juris/liste.jsf?num=C-673/17): consent by active behaviour; information on duration and third-party access.
- [CJEU C-604/22 IAB Europe](https://curia.europa.eu/juris/liste.jsf?num=C-604/22): the TCF consent string is personal data; the framework operator can be a joint controller.

## National implementation

- France: [CNIL cookies and other trackers](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/lignes-directrices-modificatives-et-recommandation): guidelines and recommendation of 2020, with a conditional exemption for audience measurement.
- Germany: [TDDDG § 25](https://www.gesetze-im-internet.de/ttdsg/__25.html) (formerly TTDSG): consent rule and the two exemptions.
- United Kingdom: PECR, outside this skill; use `uk-gdpr-compliance`.
- Others: start from the EDPB members list, then the national telecom or e-commerce law that transposes Art. 5(3) and 13.

## Reform status

- The ePrivacy Regulation proposal (COM(2017) 10) was withdrawn by the Commission in 2025; the Directive and national laws remain in force.
- Digital Omnibus proposal (19 November 2025; [Commission Q&A on the Digital Package](https://digital-strategy.ec.europa.eu/en/faqs/digital-package), including the cookie reform): would move storage and access of personal data on devices into the GDPR (proposed Art. 88a and 88b), add consent-free purposes such as aggregated audience measurement and security, and require honouring automated browser signals. It is a proposal under negotiation; Council texts have reportedly cut or reshaped the cookie provisions. Check the legislative status before citing any of it, and review against the Directive until it applies.
