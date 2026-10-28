# Document review checklist

Use this checklist for cookie banners and preference centres, cookie policies, consent texts for apps and SDKs, marketing sign-up forms and unsubscribe flows, and vendor terms for tags and SDKs.

Check two things for each document: that it contains what the Directive and national law require, and that it matches what the system does. A cookie list that omits a cookie the scan found, or a banner promising "no tracking before consent" while pixels fire, is a finding. When both a document and a scan or code are in scope, cross-check them against the step 2 inventory.

## Cookie banner, first layer (Art. 5(3); GDPR 4(11), 7)

- [ ] Shown before any non-exempt storage or access
- [ ] Accept and reject are offered on the first layer with equal prominence, wording and effort (EDPB Cookie Banner Taskforce; CNIL)
- [ ] No pre-ticked purposes, and closing or scrolling is not taken as consent
- [ ] States the purposes in plain language and that third parties are involved, with a link to the full list
- [ ] Neutral design: no colour or contrast trick that steers to accept (EDPB Guidelines 03/2022)
- [ ] Cookie walls assessed against the target member states' guidance; record the national position relied on

## Preference centre and withdrawal

- [ ] Granular choice per purpose, with vendors listed per purpose
- [ ] Withdrawal is as easy as consent: a persistent link or icon on every page, reachable without contacting support
- [ ] "Legitimate interest" toggles are not used for storage or access under Art. 5(3), which allows only consent or an exemption
- [ ] Choices are re-asked on a defined cycle, and on a material change of purposes or vendors

## Cookie policy (Art. 5(3) information requirement)

- [ ] Every cookie, storage key, SDK identifier and pixel, matching the scan
- [ ] For each: name, provider, first or third party, purpose, lifetime, and whether exempt or consent-based
- [ ] Third-party access to the information, and links to the vendors' notices
- [ ] How to change or withdraw choices
- [ ] Date of the last update, and the processing after collection covered in the privacy notice (review that under `gdpr-compliance`)

## App and SDK consent

- [ ] The consent prompt runs before SDK initialisation that reads or writes device identifiers
- [ ] OS-level prompts (iOS App Tracking Transparency, Android advertising ID settings) are treated as separate from ePrivacy consent; one does not satisfy the other
- [ ] Vendor terms say whether the SDK collects by default and how to disable it

## Marketing consent and soft opt-in (Art. 13)

- [ ] Sign-up forms: consent per channel (email, SMS, phone), unticked, separate from terms acceptance
- [ ] Consent text names the sender and the kind of messages
- [ ] Soft opt-in claims rest on a purchase or negotiation for a sale, are limited to the sender's own similar products, and the opt-out was offered at collection
- [ ] Each message template carries the sender identity and a working unsubscribe
- [ ] Rules for business recipients and live calls follow the target member state's choice under Art. 13(3) and 13(5)
- [ ] Consent records keep source, date, text version and channel

## Vendor and joint-controller terms

- [ ] Who obtains consent for third-party tags, and how proof is shared (CJEU C-40/17 Fashion ID: the site embedding a plugin is a joint controller for collection and transmission)
- [ ] Vendors commit to honour the consent signal they receive (TCF, Consent Mode, or an API flag)

## Communications service documents (Art. 4, 6, 9)

For providers of electronic communications services: retention schedule for traffic data, consent texts for value-added services using traffic or location data, the per-session location opt-out, and the breach notification procedure under Regulation (EU) No 611/2013. Record each silence as an evidence gap.
