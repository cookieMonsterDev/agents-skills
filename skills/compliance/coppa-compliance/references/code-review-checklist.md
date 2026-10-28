# Code review checklist

Use this checklist for repositories, diffs, mobile and web apps, SDK and tag configurations, ad-tech settings, schemas and data-flow descriptions. Code shows what is collected and where it flows; it rarely shows audience status, consent records or vendor contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed collection and its direct interactions: a new field, SDK, tag, upload feature or chat surface. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover children's personal information

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context.

```bash
# Contact and identity fields (§312.2 items 1-6)
rg -n -i '\b(first_?name|last_?name|full_?name|e-?mail|phone|mobile|address|street|city|zip|username|screen_?name|handle|ssn|birth|dob|age|grade|school)\b'

# Persistent identifiers and tracking (item 7)
rg -n -i '(idfa|gaid|advertising_?id|adid|device_?id|android_?id|identifierForVendor|ip_?addr|remote_?addr|x-forwarded-for|fingerprint|cookie|localStorage|session_?id)'

# Media, voice, location and biometrics (items 8-10)
rg -n -i '(camera|microphone|getUserMedia|AVCapture|MediaRecorder|upload|avatar|photo|video|audio|voice|speech|geoloc|CLLocation|LocationManager|lat(itude)?|lng|face|landmark|voiceprint|biometric)'

# Ad, analytics and engagement SDKs
rg -n -i '(admob|google-mobile-ads|gtag|googletagmanager|firebase.analytics|facebook|meta|appsflyer|adjust|branch\.io|unity.?ads|ironsource|applovin|mixpanel|amplitude|segment|braze|onesignal|hotjar|tiktok|snap)'

# Child-directed and age signals
rg -n -i '(tagForChildDirectedTreatment|tag_for_child_directed|child_?directed|under_?13|is_?child|coppa|age_?gate|age_?screen|birth_?year|parental|guardian|vpc)'
```

Also inspect: registration and profile forms, chat, comments and user-generated content, avatar and photo uploads, voice features, push notification registration, crash and error reporting, server access logs, and every SDK's initialization options.

Done when the inventory in SKILL.md step 2 lists each item, its source, where it is stored and where it flows.

## 2. Checks

Each check names its main sections. Severity guidance is in [report-template.md](report-template.md#severity).

### Age screen and audience handling (§312.2 mixed audience, §312.3)

- A mixed-audience service collects nothing beyond §312.5(c) before the age screen.
- The age screen is neutral: free entry of birth date or year, no pre-selected age, no hint that under-13 users are blocked, and no immediate retry with a different age.
- Users identified as under 13 route into a consent flow or a no-collection experience; the age result persists so the child cannot re-enter immediately.
- Age-verification data is used only to determine age, deleted promptly, and kept from other uses (FTC policy statement, February 2026).

### Consent before collection (§312.5(a)-(b))

- No personal information, including persistent identifiers beyond internal operations, is collected before verifiable parental consent completes.
- The consent method matches one in §312.5(b)(2) or a safe-harbor-approved method; email plus and text plus appear only where the operator does not disclose children's data.
- ID images, face images and ID numbers used for consent are deleted promptly after verification.
- Consent records store which parent, when, the notice version and the choices made, including the separate third-party disclosure choice.
- A material change in collection or disclosure triggers new notice and consent.

### Third-party SDKs and advertising (§312.2 third party, §312.5(a)(2), (c)(7))

- On child-directed screens and for under-13 users, ad SDKs run in child-directed mode (contextual ads, frequency capping) with behavioral advertising, cross-app tracking and audience building off.
- Analytics and attribution SDKs use persistent identifiers only for internal operations; their data is not shared onward for profiling, and the online notice names the internal operations.
- Third-party disclosure for targeted ads or sale happens only with the separate parental consent.
- No SDK collects precise location, contacts, or media without consent.

### Exceptions used narrowly (§312.5(c))

- Contact information collected to seek consent is deleted when consent does not arrive within a reasonable time.
- One-time responses delete the contact information after replying.
- Voice requests keep the audio only until the request is answered, then delete it.

### Public posting and communication (§312.2 collects, disclose)

- Chat, comments and profiles that let a child make information public require consent, or filter personal information out before posting and delete it from records.

### Data minimisation (§312.7)

- Games, contests and rewards ask for no more data than participation needs; optional fields stay optional.

### Retention and deletion (§312.10, §312.6(a)(2))

- Each store of children's data has a retention rule enforced in code or configuration, matching the written policy.
- Parent-requested deletion reaches the primary database, replicas, caches, analytics, SDK vendors through their deletion APIs, and backups on a documented cycle.
- Deletion meets the definition: data is no longer retrievable in the normal course of business.

### Security (§312.8)

- Encryption in transit and at rest, least-privilege access, audit logs for access to children's data, and secrets kept out of code.
- Children's data in test environments is synthetic or masked.

### Parental review (§312.6)

- A parent can view the categories and the actual data collected, revoke consent and request deletion, after verification that they are the parent.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the SDK's child-directed flag, the existing consent service, the job scheduler for purges. Note when a fix needs an organizational decision first (audience status, retention period, choice of consent method).
