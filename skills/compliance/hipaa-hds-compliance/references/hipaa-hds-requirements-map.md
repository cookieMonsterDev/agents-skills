# HIPAA and HDS requirements map

A compact map from review topics to the HIPAA Rules and the French health data hosting regime. It summarizes; it does not replace the text. Quote or paraphrase the section itself in a finding, and open the source when the exact wording matters.

## Official sources

`hhs.gov` and `legifrance.gouv.fr` refuse scripted requests; open them in a browser.

- [45 CFR Part 164, eCFR](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164): Subpart C Security Rule, Subpart D Breach Notification Rule, Subpart E Privacy Rule. Definitions and enforcement are in [45 CFR Part 160](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160).
- [HHS: HIPAA for professionals](https://www.hhs.gov/hipaa/for-professionals/index.html): OCR guidance, FAQs and enforcement.
- [HHS: guidance on de-identification](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html): Safe Harbor and Expert Determination.
- [HHS: guidance on unsecured PHI](https://www.hhs.gov/hipaa/for-professionals/breach-notification/guidance/index.html): encryption and destruction that make PHI "secured".
- [HHS: sample business associate agreement provisions](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html)
- [HHS: cloud computing guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html): a cloud provider storing ePHI is a business associate even when it holds only encrypted data.
- [HHS: online tracking technologies bulletin](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html): partly vacated in *American Hospital Association v. Becerra* (N.D. Tex., 20 June 2024) for IP address plus a visit to an unauthenticated page; the rest stands.
- [HIPAA Security Rule NPRM, Federal Register, 6 January 2025](https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information): proposes removing the addressable category, mandatory encryption and MFA, an asset inventory and network map, and annual compliance audits. Not final as of October 2026; the regulatory agenda moved final action to July 2027. Check the live status.
- [Code de la santé publique, Art. L.1111-8, Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049577902): hosting contract, certification, ban on selling health data; version in force since 1 July 2025 after the SREN law (Loi n° 2024-449). Implementing provisions are Art. R.1111-8-8 to R.1111-11, amended by Décret n° 2026-209 of 24 March 2026 (EEA localisation and hosting contract content); check the consolidated text.
- [ANS: HDS certification](https://esante.gouv.fr/produits-et-services/hds-certification-hebergeur-de-donnees-de-sante): referential, FAQ and list of certified hosts.
- [ANS: transition to referential v2](https://esante.gouv.fr/faq/comment-sorganise-la-transition-avec-la-nouvelle-version-du-referentiel) and [ANS: referential v2.1 changes](https://esante.gouv.fr/actualites/referentiel-hds-v21-les-evolutions-anticiper-des-maintenant)

## HIPAA requirements by topic

| Topic | Sections | What to verify |
| ----- | -------- | -------------- |
| Scope and roles | 160.103 | PHI is individually identifiable health information held by a covered entity or business associate; employment records and FERPA records are excluded |
| Permitted uses | 164.502(a), 164.506, 164.508, 164.510, 164.512 | Treatment, payment and health care operations without authorization; authorization for marketing, sale of PHI and most psychotherapy notes uses; listed public-interest disclosures |
| Minimum necessary | 164.502(b), 164.514(d) | Uses, disclosures and requests limited to the minimum necessary; role-based access policies; treatment disclosures exempt |
| Business associates | 164.502(e), 164.504(e), 164.308(b), 164.314(a) | Written BAA before PHI flows, with subcontractor BAAs downstream; business associates are directly liable for the Security Rule |
| De-identification | 164.514(a)-(c) | Safe Harbor (remove the 18 listed identifiers and no actual knowledge of re-identification) or Expert Determination; re-identification codes not derived from PHI |
| Limited data set | 164.514(e) | Direct identifiers removed, for research, public health or operations, under a data use agreement |
| Individual rights | 164.520-164.528 | Notice of privacy practices; restrictions and confidential communications; access within 30 days (one 30-day extension) at a reasonable cost-based fee; amendment; accounting of disclosures for 6 years |
| Administrative requirements | 164.530 | Privacy official, training, sanctions, safeguards, complaints, mitigation, documentation kept 6 years |
| Security: general | 164.306 | Confidentiality, integrity and availability of ePHI; flexible approach; addressable specifications implemented, or the reason and an equivalent alternative documented |
| Security: administrative | 164.308 | Risk analysis and risk management, sanction policy, information system activity review, security official, workforce and access management, training, incident procedures, contingency plan (backup, disaster recovery, emergency mode), periodic evaluation |
| Security: physical | 164.310 | Facility access, workstation use and security, device and media controls including disposal and reuse |
| Security: technical | 164.312 | Access control with unique user IDs and emergency access (required), automatic logoff and encryption at rest (addressable); audit controls (required, (b)); integrity; person or entity authentication; transmission security with encryption (addressable) |
| Policies and documentation | 164.316 | Written policies, kept 6 years from creation or last effective date, reviewed and updated |
| Breach notification | 164.402-164.414 | Impermissible use or disclosure presumed a breach unless a four-factor assessment shows low probability of compromise; secured (encrypted per HHS guidance) PHI is exempt; individuals without unreasonable delay and within 60 days of discovery; HHS within 60 days for 500 or more, or yearly for fewer; media for more than 500 residents of a state; business associates notify the covered entity within 60 days |
| Preemption | 160.203 | More stringent state privacy law survives |
| Penalties | 160 Subpart D; 42 U.S.C. 1320d-5, 1320d-6 | Four culpability tiers with annual caps, inflation-adjusted yearly (check 45 CFR Part 102); criminal penalties for knowing misuse; OCR weighs recognized security practices in place for the prior 12 months |

## HDS requirements by topic

| Topic | Source | What to verify |
| ----- | ------ | -------------- |
| Who needs HDS | L.1111-8 | Hosting personal health data for a third party (controller or patient) on digital media needs an HDS certificate; a controller hosting its own data internally does not; electronic archiving needs the certificate and the culture ministry's approval (L.1111-8 II-III) |
| Use and return | L.1111-8 V | Host uses the data only to perform the hosting, returns it at the end without keeping copies, and is bound by professional secrecy |
| Activities | R.1111-9 | Six activities: physical sites; hardware infrastructure; virtual infrastructure; application hosting platform; administration and operation of the information system; backup. The certificate names the activities covered |
| Patient information | L.1111-8 | Patient informed of the hosting and able to object for a legitimate reason |
| Hosting contract | L.1111-8; R.1111-11 | Contract with the required clauses, including localisation, transfer safeguards, sub-hosts and reversibility; Décret n° 2026-209 expanded the content |
| Referential v2 | ANS | Builds on ISO/IEC 27001 with HDS-specific requirements; health data stored in the EEA, sub-hosts included; disclosure to clients of exposure to non-EEA law; a published map of transfers outside the EEA. Certificates last 3 years with surveillance audits |
| Transition | ANS FAQ | Referential v2 (arrêté of 26 April 2024): certified hosts had until 16 May 2026 to comply; v1.1 certificates are no longer valid. v2.1 was due in October 2026, effective three months after publication, treating remote access from outside the EEA as a transfer and bringing third-party archivers into scope; check its status |
| Sale ban | L.1111-8 | Any sale of identifying health data is prohibited, even with consent |
| Penalties | L.1115-1 | Hosting without certification: up to 3 years' imprisonment and a EUR 45,000 fine; check the live text |
