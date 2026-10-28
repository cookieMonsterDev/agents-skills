# PSD2 requirements map

A compact map from review topics to PSD2 and RTS articles and the EBA guidance behind them. It summarizes; it does not replace the text. Quote or paraphrase the article itself in a finding, and open the source when the exact wording matters.

## Official sources

- [Directive (EU) 2015/2366 (PSD2), EUR-Lex](https://eur-lex.europa.eu/eli/dir/2015/2366/oj): the directive; obligations reach firms through national transposition. EUR-Lex may show a bot check to scripted requests; open it in a browser.
- [Delegated Regulation (EU) 2018/389 (RTS on SCA and CSC), EUR-Lex](https://eur-lex.europa.eu/eli/reg_del/2018/389/oj): directly applicable since 14 September 2019. Use the consolidated version for the 2022 amendment.
- [Delegated Regulation (EU) 2022/2360, EUR-Lex](https://eur-lex.europa.eu/eli/reg_del/2022/2360/oj): amends RTS Art. 10 and adds Art. 10a, applying from 25 July 2023.
- [Regulation (EU) No 910/2014 (eIDAS), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/oj): qualified certificates for TPP identification under RTS Art. 34.
- [EBA: payment services and electronic money](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money): opinions, guidelines and reports under PSD2.
- [EBA Single Rulebook Q&A](https://www.eba.europa.eu/single-rule-book-qa): search by legal act (PSD2, RTS 2018/389) and cite by Q&A ID.
- [EDPB Guidelines 06/2020 on the interplay of PSD2 and the GDPR](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-062020-interplay-second-payment-services_en): PSD2 "explicit consent" is contractual, not a GDPR lawful basis; silent-party data.
- [Regulation (EU) 2022/2554 (DORA), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj): ICT risk management and major ICT incident reporting for PSPs since 17 January 2025, alongside PSD2 Art. 95.

## Definitions (PSD2 Art. 4)

| Term                           | Article | Review note                                                                                                          |
| ------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- |
| Authentication                 | 4(29)   | Verifying the identity of the user or the validity of a payment instrument, including its credentials                |
| Strong customer authentication | 4(30)   | Two or more independent elements from knowledge, possession and inherence, protecting the confidentiality of the data |
| Personalised security credentials | 4(31) | Features the PSP provides for authentication: PIN, password, OTP seed, device keys                                   |
| Sensitive payment data         | 4(32)   | Data, including credentials, usable for fraud; for PISPs and AISPs the account holder's name and account number are not |

## Requirements by topic

| Topic                     | Articles                     | What to verify                                                                                                                                                                                                 |
| ------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SCA triggers              | PSD2 97(1)                   | Online account access, initiating an electronic payment, and any remote action that may imply fraud risk (adding a payee, changing limits or credentials)                                                     |
| Dynamic linking           | PSD2 97(2); RTS 5            | Payer sees amount and payee; the code is specific to both and any change invalidates it; integrity across all phases; card holds and batches link to the consented or total amount and the payees            |
| Authentication code       | RTS 4                        | Single use, unforgeable, reveals no element; no hint which element failed; at most five consecutive failures before a block (4(3)(b)); online session idle for at most five minutes (4(3)(d)); alert before a block becomes permanent (4(4)) |
| Elements                  | RTS 6, 7, 8                  | Knowledge resists disclosure, possession resists replication, inherence has a low false-acceptance rate; EBA-Op-2019-06 lists which approaches qualify (static card details are not possession)            |
| Independence              | RTS 9                        | Breach of one element leaves the others intact; on a multi-purpose device, separate secure execution environments and tamper detection                                                                        |
| Transaction monitoring    | RTS 2, 3                     | Monitoring for compromised credentials, amount, known fraud scenarios, malware signs, device logs; security measures documented, tested and audited, the Art. 18 methodology first audited after a year of use, then at least every three years |
| Credentials               | PSD2 97(3); RTS 22-27        | Masking on input, no plaintext storage, secure creation, association with the user, delivery, renewal, destruction and revocation                                                                            |
| Liability                 | PSD2 73, 74                  | Unauthorised payments refunded by the end of the next business day; payer not liable where the PSP did not require SCA; a payee or acquirer that does not accept SCA refunds the issuer's loss (74(2))     |
| TPP access                | PSD2 66, 67, 68              | PISPs and AISPs identify themselves, keep credentials confidential, request and use only data needed for the service; ASPSPs treat TPP requests without discrimination and deny access only for documented fraud reasons, notifying the authority (68(5)) |
| Access interface          | RTS 30, 31                   | At least one interface letting TPPs identify themselves and rely on the ASPSP's SCA; technical documentation and a testing facility (30(3), 30(5))                                                            |
| Dedicated interface       | RTS 32, 33                   | Availability and performance at least equal to the customer interface, published quarterly statistics, no obstacles such as mandatory redirection or extra consent checks (32(3)); fallback to the customer interface unless the authority granted an exemption (33(6)) |
| Certificates and sessions | RTS 34, 35                   | Qualified certificates for electronic seals or website authentication naming the TPP's registration number and roles; encrypted sessions with short-lived tokens                                             |
| Data exchange             | RTS 36                       | Same information as the customer sees; yes or no funds confirmation for PISPs; AISP access without the user present at most four times in 24 hours unless agreed otherwise (36(5))                          |
| Data protection           | PSD2 94                      | Personal data processed only as necessary for the service; flag `gdpr-compliance`                                                                                                                             |

## Exemptions (RTS 10-18)

Exemptions are optional for the payer's PSP (issuer or ASPSP), except Art. 10a. A payee or acquirer can request one; the issuer decides. Art. 2 monitoring applies to every exempted transaction.

| Article | Exemption                       | Conditions                                                                                                                                         |
| ------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10      | Account information, direct     | Balance and last 90 days of transactions only, no sensitive payment data; SCA at first access and at least every 180 days                          |
| 10a     | Account information via an AISP | Mandatory for the ASPSP; SCA at first AISP access, renewed at least every 180 days; SCA otherwise only for documented fraud reasons notified to the authority |
| 11      | Contactless at point of sale    | At most EUR 50 per transaction, and either EUR 150 cumulative or five consecutive transactions since the last SCA                                 |
| 12      | Unattended transport and parking terminals | Fares and parking fees                                                                                                                     |
| 13      | Trusted beneficiaries           | SCA when the payer creates or amends the list                                                                                                       |
| 14      | Recurring transactions          | Same amount and same payee; SCA at creation, amendment and first payment                                                                            |
| 15      | Own accounts                    | Credit transfers between accounts of the same person at the same ASPSP                                                                              |
| 16      | Low-value remote                | At most EUR 30 per transaction, and either EUR 100 cumulative or five consecutive transactions since the last SCA                                  |
| 17      | Secure corporate processes      | Dedicated processes for non-consumers that the competent authority accepts as equally secure                                                       |
| 18      | Transaction risk analysis       | Real-time analysis finds no risk signal, and the PSP's fraud rate stays within the Annex reference rate for the amount band                          |

Art. 18 Annex reference fraud rates by exemption threshold value:

| Up to   | Remote card payments | Remote credit transfers |
| ------- | -------------------- | ----------------------- |
| EUR 100 | 0.13%                | 0.015%                  |
| EUR 250 | 0.06%                | 0.01%                   |
| EUR 500 | 0.01%                | 0.005%                  |

Fraud rates are calculated per Art. 19 at least quarterly; exceeding the rate for two consecutive quarters ends the exemption and the authority is notified (Art. 20). Fraud data goes to the authority per Art. 21 and EBA/GL/2018/05.

## EBA guidance worth opening

All on the EBA payment services page above, by reference number:

- EBA-Op-2018-04, opinion on implementing the RTS: scope of SCA, MOTO, merchant-initiated and one-leg-out transactions, TPP certificates.
- EBA-Op-2019-06, opinion on the elements of SCA: which methods count as knowledge, possession or inherence.
- EBA/Op/2020/10, opinion on obstacles under RTS Art. 32(3).
- EBA/GL/2018/05, guidelines on fraud reporting (amended by EBA/GL/2020/01).
- EBA/GL/2018/07, guidelines on the exemption from the contingency mechanism under RTS Art. 33(6).

## PSD3 and PSR

The Commission proposed a third Payment Services Directive (procedure 2023/0209(COD)) and a Payment Services Regulation (2023/0210(COD)) in June 2023. Parliament and Council reached political agreement on 27 November 2025, the Council published final compromise texts on 23 April 2026, and Parliament's ECON committee approved them on 5 May 2026. As of 2026-10-28 neither act was formally adopted or published in the Official Journal; the Legislative Observatory forecast a plenary in December 2026. Per the compromise texts, most PSR provisions apply 21 months after entry into force, with SCA and open-banking rules moving from the RTS into the PSR. Until then, PSD2 and the RTS govern. Check the [Legislative Observatory file for the PSR](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210%28COD%29) and EUR-Lex for the adopted text and dates.
