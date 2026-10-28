# Code review checklist

Use this checklist for iOS and Android source repositories, diffs, cross-platform projects and built binaries. Code shows what the app collects and which SDKs it ships; it rarely shows server-side processing or what was answered in the store consoles. Pair each technical finding with the console answer or listing text it must match.

For a diff or pull request, review the changed permission, SDK, data flow or account path and its direct interactions. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover SDKs, permissions and data

Search before reading. Adapt paths to the project layout (`ios/`, `android/`, Flutter, React Native, Unity), and read every hit in context.

```bash
# iOS permission usage strings and tracking
rg -n --glob '*.plist' 'NS[A-Za-z]+UsageDescription|NSUserTrackingUsageDescription|NSLocationAlways|UIBackgroundModes'
rg -n 'ATTrackingManager|requestTrackingAuthorization|ASIdentifierManager|advertisingIdentifier|SKAdNetwork|AdAttributionKit'

# iOS privacy manifests and required-reason APIs
fd -H 'PrivacyInfo.xcprivacy'
rg -n 'NSPrivacy(Tracking|TrackingDomains|CollectedDataTypes|AccessedAPITypes)'
rg -n 'UserDefaults|NSUserDefaults|systemUptime|mach_absolute_time|volumeAvailableCapacity|statfs|creationDate|modificationDate|fileModificationDate|activeInputModes'

# Android permissions and restricted APIs
rg -n --glob '**/AndroidManifest.xml' '<uses-permission|foregroundServiceType|android:exported'
rg -n 'ACCESS_(FINE|COARSE|BACKGROUND)_LOCATION|READ_(SMS|CALL_LOG|CONTACTS|MEDIA_IMAGES|MEDIA_VIDEO|EXTERNAL_STORAGE)|SEND_SMS|RECEIVE_SMS|MANAGE_EXTERNAL_STORAGE|QUERY_ALL_PACKAGES|REQUEST_INSTALL_PACKAGES|SCHEDULE_EXACT_ALARM|USE_EXACT_ALARM|USE_FULL_SCREEN_INTENT|BIND_ACCESSIBILITY_SERVICE|BODY_SENSORS|gms.permission.AD_ID'
rg -n 'AdvertisingIdClient|getAdvertisingIdInfo|AppSetIdClient|Settings.Secure.ANDROID_ID|getImei|getLine1Number|getInstalledPackages'

# SDK lists: read each dependency file, then search for data-collecting SDKs
fd -H -E node_modules -E Pods -g '{Podfile.lock,Package.resolved,Cartfile.resolved,*.gradle,*.gradle.kts,libs.versions.toml,package.json,pubspec.lock,manifest.json}'
rg -n -i '(firebase|crashlytics|google-?analytics|admob|play-services-ads|applovin|ironsource|unity.?ads|facebook|meta|appsflyer|adjust|branch|kochava|singular|mixpanel|amplitude|segment|braze|onesignal|sentry|datadog|bugsnag|revenuecat|intercom)'
```

Also inspect: entitlements files, build-time merged manifests (`build/intermediates/merged_manifests`), `Info.plist` per target and extension, WebViews and the URLs they load, deep links, account and settings screens, and consent or CMP SDK configuration.

Done when the inventory in SKILL.md step 2 has every SDK, permission and data type found, with the feature that needs each.

## 2. Checks

Each check names its main guideline or policy. Severity guidance is in [report-template.md](report-template.md#severity).

### Permissions and usage strings (Apple 5.1.1(ii)-(iv), 5.1.5; Google sensitive permissions policy)

- Every iOS permission has a usage string that names the feature and the data, in the app's languages; generic text ("needs camera access") is a finding.
- Permissions are requested in context when the feature is used, not at launch; denial leaves the rest of the app working.
- Each Android permission maps to a shipped feature; merged manifests carry no unneeded permissions from libraries (remove with `tools:node="remove"`).
- Restricted Android permissions (background location, SMS, call log, broad media, all files, package visibility, exact alarm, full-screen intent, accessibility) have a qualifying core use and a matching Play Console declaration; the photo picker, coarse location, inexact alarms or system intents are used when they suffice.

### Tracking and advertising identifiers (Apple 5.1.2(i), ATT; Google Ads and User Data policies)

- On iOS, `requestTrackingAuthorization` runs before any tracking: IDFA access, tracking SDK initialisation, or sharing identifiers or events with data brokers or ad networks. Tracking SDKs start only after `.authorized`.
- `NSUserTrackingUsageDescription` is present whenever ATT is requested, and no feature, reward or content is gated on allowing tracking.
- `NSPrivacyTracking` and `NSPrivacyTrackingDomains` match the tracking the app and its SDKs do.
- On Android, `AD_ID` is declared when the advertising ID is read, and absent (removed) when it is not; the ID is not tied to persistent hardware identifiers or personal data for advertising without consent.

### Privacy manifests and SDKs (Apple privacy manifest and third-party SDK requirements)

- The app has a `PrivacyInfo.xcprivacy` declaring each required-reason API category it uses with an approved reason code.
- Each SDK on Apple's commonly used SDK list ships its own privacy manifest and a valid signature at a version that includes them.
- Collected data types in the manifests, aggregated by Xcode's privacy report, match the App Privacy label.

### Prominent disclosure and consent (Apple 5.1.1(ii), 5.1.2(i); Google User Data policy)

- Data collection users would not reasonably expect (contacts, installed apps, location in background, screen content) is preceded by an in-app disclosure in normal use and an affirmative consent action, before collection starts.
- Personal data sent to third-party AI services is disclosed and has explicit permission (Apple 5.1.2(i)).
- Consent state is enforced in code: SDK initialisation, event logging and network calls check it.

### Account deletion (Apple 5.1.1(v); Google account deletion requirement)

- An in-app path deletes the account and its data, reachable from account settings without contacting support; deletion is not only deactivation.
- A web deletion URL exists for Google Play and works without the app installed.
- Server-side deletion reaches processors and SDK backends; Sign in with Apple tokens are revoked through the REST API on deletion.

### Login services (Apple 4.8)

- Where Google, Facebook or another third-party login is the primary account, an equivalent privacy-focused option (such as Sign in with Apple) is offered on the same screen.

### Kids and families (Apple 1.3, 5.1.4; Google Families policies)

- Child-directed builds ship no third-party analytics or ad SDKs on Apple, beyond the guideline's exceptions; on Google Play only Families Self-Certified Ads SDKs at listed versions, configured for child-directed treatment.
- No advertising ID, precise location, or device identifiers are sent from children; external links and purchases sit behind a parental gate.
- Age-gating or age-signal APIs (Declared Age Range, Play Age Signals) are used where required, and their results limit features.

### Build requirements (Google target API level; Apple SDK minimums)

- `targetSdk` meets the current Google Play requirement for the form factor.
- The iOS build uses the Xcode and SDK version App Store Connect currently requires; check the live upcoming-requirements page.

## 3. Map findings to fixes

Give fixes in the project's own idiom: the existing permission helper, consent manager, SDK initialiser, account settings screen, or Gradle and Xcode build settings. Note when a fix also needs a console answer or listing change, and name it.
