# App store requirements map

A compact map from review topics to Apple guideline numbers and Google Play policies, with the official pages behind them. It summarizes; it does not replace the text. Quote or paraphrase the guideline or policy itself in a finding, and open the page when the exact wording matters. Checked 2026-10-28; both stores revise their rules often, so check the live page before relying on a date or threshold.

## Official sources

Apple:

- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): the authoritative guideline text; the page shows its last-updated date and links the change notes.
- [App privacy details](https://developer.apple.com/app-store/app-privacy-details/): data types, "linked to you", "used to track you" and optional-disclosure criteria for the App Store Connect privacy label.
- [User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/) and [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency): what counts as tracking and how to request permission.
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) and [required reason APIs](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)
- [Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/): the commonly used SDKs that need a privacy manifest and signature.
- [Offering account deletion in your app](https://developer.apple.com/support/offering-account-deletion-in-your-app/)
- [Declared Age Range](https://developer.apple.com/documentation/declaredagerange): age-range signals used for state app-store age laws.

Google Play:

- [Developer Program Policy center](https://play.google/developer-content-policy/): every policy, with announced upcoming changes.
- [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) and [Prominent Disclosure guidance](https://support.google.com/googleplay/android-developer/answer/11150561)
- [Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/9888170): SMS and call log, location, all files access, package visibility, photo and video, accessibility, exact alarm, health and other restricted permissions.
- [Account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111)
- [Families policies](https://support.google.com/googleplay/android-developer/answer/9893335) and [Families Self-Certified Ads SDK Policy](https://support.google.com/googleplay/android-developer/answer/12918983)
- [Target API level requirements](https://developer.android.com/google/play/requirements/target-sdk)
- [Login credentials for app access](https://support.google.com/googleplay/android-developer/answer/15748846)

## Apple App Store Review Guidelines

| Topic                       | Guideline          | What to verify                                                                                                                                                                   |
| --------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App completeness and review | 2.1, 2.3           | Final build, live backend; demo account or full-featured demo mode for login-gated apps; review notes explain non-obvious features; metadata matches the app                       |
| Kids Category               | 1.3, 5.1.4         | No external links or purchases outside a parental gate; no third-party analytics or advertising except under the narrow exceptions; no personal data or device info sent to third parties |
| Login services              | 4.8                | When a third-party or social login is the primary account, offer an equivalent login that limits data to name and email, lets users hide their email, and does no ad tracking without consent; exceptions listed in the guideline |
| Privacy policy              | 5.1.1(i)           | Linked in App Store Connect and in the app; states data collected, how, uses, third parties and their equal protection, retention and deletion, and how to revoke consent          |
| Permission and minimisation | 5.1.1(ii)-(iv)     | Consent for collection; purpose strings explain the use clearly; only data relevant to core functionality; no forcing or tricking into consent; features work without non-essential permissions where possible |
| Account sign-in             | 5.1.1(v)           | Account creation only when significant account-based features need it; apps that support account creation offer account deletion inside the app                                 |
| Data use and sharing        | 5.1.2(i)-(vi)      | Explicit permission before sharing personal data with third parties, including third-party AI; ATT permission before tracking; no gating features or rewards on tracking consent; no data repurposing or profiles from contacts or photos |
| Health                      | 5.1.3              | Health, fitness and research data never used for advertising or data mining; HealthKit data not stored in iCloud; research needs consent and ethics-board approval               |
| Location                    | 5.1.5              | Location used only when directly relevant to the app's features, with purpose explained                                                                                          |
| App Privacy details         | App Store Connect  | Label covers all data the app and its SDKs collect, linked and tracking status, and purposes; kept accurate on every update                                                      |
| Privacy manifests           | App Store Connect  | `PrivacyInfo.xcprivacy` in the app and in each listed SDK declares tracking, tracking domains, collected data types and required-reason API use; enforced on upload since 1 May 2024 |
| Age ratings and age signals | App Store Connect  | Age rating questionnaire answered on the current scale; where state app-store age laws apply, the Declared Age Range API and parental-consent flows are used as Apple requires     |

## Google Play Developer Program Policies

| Topic                          | Policy                                       | What to verify                                                                                                                                                                         |
| ------------------------------ | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Privacy policy and handling    | User Data                                    | Privacy policy in Play Console and inside the app; data use limited to disclosed purposes; secure transmission; no sale of personal and sensitive data                                 |
| Prominent disclosure           | User Data, Prominent Disclosure and Consent  | In-app disclosure, in normal use, describing the data and its use, shown before collection when users would not reasonably expect it, followed by an affirmative consent action        |
| Data safety                    | Data safety section                          | Every app completes it, including apps that collect nothing; collected and shared data types, purposes, optional or required, encryption in transit, deletion; covers SDK data           |
| Account deletion               | User Data, account deletion                  | In-app path and a web link usable without reinstalling; deletes account and associated data; retention reasons disclosed; web link entered in the Data safety form                      |
| Sensitive permissions          | Permissions and APIs that Access Sensitive Information | Requested only for current features promoted in the listing; in context; minimum-scope alternatives used first; Play Console declaration forms for restricted permissions          |
| Location                       | Location Permissions                         | Background location only for core user-facing features, with a declaration and video; a location-button minimum-scope rule is announced for 27 January 2027                             |
| SMS and call log               | SMS and Call Log Permissions                 | Only for the default SMS, phone or assistant handler, or a listed exception, with an approved declaration                                                                              |
| Photo and video                | Photo and Video Permissions                  | `READ_MEDIA_IMAGES` and `READ_MEDIA_VIDEO` only when broad access is core; otherwise the system photo picker                                                                            |
| Other restricted permissions   | Same policy                                  | All files access, `QUERY_ALL_PACKAGES`, accessibility API, `REQUEST_INSTALL_PACKAGES`, exact alarm, full-screen intent, Health Connect, VPN; contacts gets its own policy on 27 January 2027 |
| Advertising ID                 | Ads policy, Advertising ID; User Data        | `AD_ID` permission declared when the advertising ID is used; not linked to persistent identifiers without consent; reset and opt-out respected                                          |
| Families                       | Families policies                            | Target-audience answers match the app; child-directed apps send no advertising ID, location or device identifiers of children; ads only through Families Self-Certified Ads SDKs        |
| App access for review          | Login credentials for app access             | Working credentials or instructions for every gated area, usable from any region, in English                                                                                          |
| Target API level               | Target API level requirements                | New apps and updates target the current required level (Android 16, API 36, from 31 August 2026 for phones); existing apps below the floor lose visibility on newer devices             |
