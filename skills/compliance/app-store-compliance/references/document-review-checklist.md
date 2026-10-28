# Document review checklist

Use this checklist for the App Store Connect App Privacy answers, the Google Play Data safety form and other App content declarations, store listing metadata, the privacy policy, App Review notes and app access instructions, permission declaration forms, and rejection or policy notices.

Check two things for each document: that it contains what the store requires, and that it matches what the app and its SDKs actually do. A label or form that omits data an SDK collects is the most common finding; both stores hold the developer responsible for third-party SDK data. When code is also in scope, reconcile every answer against the step 2 inventory.

## Apple App Privacy details

- [ ] Every data type collected by the app or any SDK is declared, using Apple's categories (contact info, health and fitness, financial info, location, sensitive info, contacts, user content, browsing and search history, identifiers, purchases, usage data, diagnostics, surroundings, body, other)
- [ ] For each type: purposes, whether it is linked to the user's identity, and whether it is used to track
- [ ] "Data not collected" is claimed only when no data leaves the device beyond Apple's optional-disclosure criteria
- [ ] "Used to track you" matches ATT use and `NSPrivacyTracking`
- [ ] Answers updated with the build that changed collection

## Google Play Data safety form

- [ ] Completed, including for apps that collect no data
- [ ] Each data type marked collected, shared, or both, with Google's definitions (transfers to service providers, legal disclosures and user-initiated transfers are not "sharing")
- [ ] Purposes per type, and whether each is optional or required
- [ ] Ephemeral processing claimed only where data is held in memory for the request alone
- [ ] Encryption in transit answered truthfully
- [ ] Data deletion answers and the account deletion web link entered when accounts exist
- [ ] Optional independent security review claims backed by a current validation

## Other Play Console declarations

- [ ] Target audience and content matches the app's actual audience; child ages selected only if the Families policy is met
- [ ] Ads declaration matches the shipped ad SDKs
- [ ] Advertising ID declaration matches the `AD_ID` permission
- [ ] Permission declaration forms (background location, SMS and call log, photo and video, all files access, package visibility, exact alarm, full-screen intent, foreground service types) name a core feature visible in the listing, with a video where requested
- [ ] Health apps declaration and Health Connect access where applicable

## Privacy policy (Apple 5.1.1(i); Google User Data policy)

- [ ] Linked in App Store Connect, in Play Console, and inside the app
- [ ] A public, active, non-geofenced URL, not a PDF or editable document
- [ ] Names the developer as in the listing, with a privacy contact
- [ ] States the data collected, how, all uses, and the third parties it is shared with, including SDK and AI providers
- [ ] States retention and deletion, and how to request deletion and revoke consent
- [ ] Consistent with the privacy label and the Data safety form

## Store listing metadata (Apple 2.3; Google Metadata and Families policies)

- [ ] Description and screenshots show only features the build contains; features that justify restricted permissions appear in the listing
- [ ] Kids-targeted wording, imagery or category only when the app meets Apple 1.3 and Google Families rules
- [ ] Age rating answers match the content, including user-generated content, chat, ads and web access

## App Review notes and app access (Apple 2.1; Google app access)

- [ ] Demo account credentials, or a full-featured demo mode, for every login-gated area; credentials are test-only and synthetic
- [ ] Credentials work from any region and in English; second factors, QR codes or hardware needs are explained
- [ ] Notes explain non-obvious features, background modes, restricted-permission use, and where account deletion lives
- [ ] Contact details for the reviewer are current

## Rejections and policy notices

- [ ] The cited guideline or policy section is quoted, and the finding maps to it
- [ ] The fix addresses the cause in the build or form, not only the reply
- [ ] The response or appeal states what changed, where, and in which build
