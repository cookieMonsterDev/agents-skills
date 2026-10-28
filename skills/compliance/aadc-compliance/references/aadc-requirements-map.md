# Age-appropriate design requirements map

A compact map from design topics to the age-appropriate design codes, their sections and the official sources. It summarizes; it does not replace the texts. Quote or paraphrase the standard or section itself in a finding, and open the source when the exact wording matters.

## Jurisdictions

| Code                                                                 | Covers                                                                                           | Legal force and status (checked 2026-10-28; check live)                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UK ICO Age appropriate design code (Children's Code)                 | Information society services likely to be accessed by under-18s in the UK                        | Statutory code under DPA 2018 s.123; the ICO and courts take it into account (s.127). In force since 2 September 2021. Since 5 February 2026, UK GDPR Art. 25 also requires weighing the "children's higher protection matters" (inserted by Data (Use and Access) Act 2025 s.81); the ICO treats code conformance as the likely way to meet it |
| California Age-Appropriate Design Code Act (AB 2273)                 | CCPA "businesses" with online services likely to be accessed by under-18s                       | Cal. Civ. Code §§1798.99.28-1798.99.40. NetChoice v. Bonta, No. 25-2366 (9th Cir. March 12, 2026): DPIA duties, the "materially detrimental" and best-interests data use limits (§1798.99.31(b)(1)-(4)), the dark patterns ban (b)(7) and the notice-and-cure clause stay enjoined; age estimation, high-privacy defaults, child-appropriate privacy information, monitoring and geolocation signals, geolocation limits and rights tools are no longer enjoined. Remanded; check the docket |
| Maryland Age-Appropriate Design Code Act (Kids Code, 2024 HB 603 / SB 571) | Covered entities with online products reasonably likely to be accessed by under-18s       | Effective October 1, 2024; DPIAs due from April 1, 2026; best-interests duty, high-privacy defaults, profiling and geolocation limits. NetChoice v. Brown (D. Md. No. 1:25-cv-00322) pending without an injunction as last checked; check the docket |
| Vermont Age-Appropriate Design Code Act (Act 63 of 2025, S.69)       | Covered businesses with services reasonably likely to be accessed by minors                      | Takes effect January 1, 2027, with Attorney General rules                                                                                                                                                                                                                                                                     |
| Nebraska Age-Appropriate Online Design Code Act (LB 504, 2025)       | Covered online services reasonably likely to be accessed by minors                               | Reported operative January 1, 2026; confirm the operative and enforcement dates and any 2026 amendments on the Legislature site                                                                                                                                                                                              |
| EU Digital Services Act Art. 28                                      | Online platforms accessible to minors (not micro or small enterprises, Art. 19)                  | Binding regulation. Art. 28(1): appropriate and proportionate measures for a high level of privacy, safety and security of minors; 28(2): no ads based on profiling when the provider is aware with reasonable certainty the user is a minor; 28(3): no duty to process extra data to assess age; 28(4): Commission guidelines, adopted 14 July 2025, the Commission's benchmark for 28(1) |
| Ireland DPC "Children Front and Centre: Fundamentals for a Child-Oriented Approach to Data Processing" | Organisations processing children's data under the GDPR, Ireland as lead authority for many platforms | Regulator guidance (December 2021), 14 Fundamentals; the DPC's basis for supervision and enforcement                                                                                                                                                                                                                       |
| Netherlands Code voor Kinderrechten (Code for Children's Rights)     | Designers and developers of digital services used by children                                     | Non-binding, 10 principles (2021), commissioned by the Ministry of the Interior, grounded in the UN CRC and the GDPR                                                                                                                                                                                                        |

Other US states have passed or are debating design codes and minors' social media laws, and several are enjoined. Search for new enactments and court orders before concluding a state has none.

## ICO Children's Code: the 15 standards

1. Best interests of the child: a primary consideration in design and development.
2. Data protection impact assessments: assess and mitigate risks to children, by age range.
3. Age appropriate application: establish age with certainty proportionate to the risk, or apply the code to all users.
4. Transparency: concise, prominent, child-friendly privacy information, with bite-sized explanations at the point of use.
5. Detrimental use of data: no use shown to be detrimental to children's wellbeing or against industry codes, regulatory provisions or government advice.
6. Policies and community standards: uphold published terms, policies and community standards.
7. Default settings: high privacy by default, unless a compelling reason in the child's best interests.
8. Data minimisation: the minimum data for each element of the service the child actively and knowingly engages with, with separate choices per element.
9. Data sharing: no disclosure unless a compelling reason in the child's best interests.
10. Geolocation: off by default, an obvious sign while tracking is active, and options making location visible to others reset to off after each session.
11. Parental controls: age-appropriate information about them, and an obvious sign to the child when monitored.
12. Profiling: off by default, allowed only with measures to protect the child from harmful effects, such as harmful content.
13. Nudge techniques: no nudging toward weaker privacy settings or more data; pro-privacy nudges are fine.
14. Connected toys and devices: effective tools to conform, including transparency at purchase and set-up.
15. Online tools: prominent, accessible tools to exercise data protection rights and report concerns.

## Requirements by topic

| Topic                      | UK Children's Code | California (§1798.99.31)               | DSA Art. 28 guidelines                                              |
| -------------------------- | ------------------ | -------------------------------------- | ------------------------------------------------------------------- |
| Best interests             | Std 1              | Best-interests tests in (b) (enjoined) | Child rights and best interests as the frame for proportionality    |
| Risk assessment            | Std 2              | DPIA (a)(1)-(4) (enjoined)             | Risk review of likelihood and impact on minors                       |
| Age assurance              | Std 3              | Age estimation (a)(5); data use limit (b)(8) | Age verification for high-risk services; estimation where proportionate; self-declaration alone is insufficient |
| Transparency               | Std 4              | Child-appropriate information (a)(7)   | Child-friendly terms and explanations (with DSA Art. 14)             |
| Defaults                   | Std 7              | High-privacy defaults (a)(6)           | Private accounts and restricted contact and visibility by default    |
| Geolocation                | Std 10             | Off by default (b)(5); signal (b)(6)   | Location and contact features off by default                         |
| Profiling and recommenders | Std 12             | Profiling off by default (b)(2) (enjoined) | Recommender option not based on profiling; no profiling-based ads (28(2)) |
| Nudges and dark patterns   | Std 13             | Dark patterns ban (b)(7) (enjoined)    | Persuasive design limits: streaks, autoplay, infinite scroll, night-time notifications |
| Parental controls          | Std 11             | Monitoring signal (a)(8)               | Parental tools complement, never replace, service-level protection   |
| Data sharing, minimisation | Std 8, 9           | (b)(3)-(4) (enjoined)                  | Commercial practices: no exploiting minors' commercial inexperience  |
| Rights and reporting tools | Std 15             | Prominent tools (a)(10)                | Accessible reporting, feedback and complaint tools                   |
| Connected toys             | Std 14             | Covered as online products             | Not specific                                                        |

Enjoined provisions are context, not findings; record them so the report holds up if an injunction lifts.

## Official sources

- [ICO: Age appropriate design, a code of practice for online services](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/)
- [Data Protection Act 2018 s.123](https://www.legislation.gov.uk/ukpga/2018/12/section/123) and [Data (Use and Access) Act 2025 s.81](https://www.legislation.gov.uk/ukpga/2025/18/section/81)
- [California AB 2273, leginfo](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202120220AB2273): may refuse scripted requests; open it in a browser.
- Maryland 2024 SB 571 as enacted, on the Maryland General Assembly site
- Vermont S.69 (Act 63) and the [Vermont Attorney General rulemaking](https://ago.vermont.gov/vermont-age-appropriate-design-code-rulemaking): the Attorney General site may refuse scripted requests; open it in a browser.
- [Regulation (EU) 2022/2065 (DSA), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2065/oj): may show a bot check to scripted requests.
- [Commission guidelines on the protection of minors under the DSA](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors)
- [Irish DPC: the Fundamentals](https://www.dataprotection.ie/en/dpc-guidance/fundamentals-child-oriented-approach-data-processing)
- [Code voor Kinderrechten, English version (PDF)](https://codevoorkinderrechten.waag.org/wp-content/uploads/2022/02/Code-voor-Kinderrechten-EN.pdf)
