# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, tag manager and SDK configuration, infrastructure code and data-flow descriptions. Code shows what the system collects and where it flows; it rarely shows resident counts, contracts or assessments. Pair each technical finding with the organizational question it raises, and name the states each finding applies to.

For a diff or pull request, review the changed processing and its direct interactions: a new field, tag, SDK, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identity, contact and account fields
rg -n -i '\b(first_?name|last_?name|e-?mail|phone|address|zip|postal|birth|dob|ssn|driver_?license|passport|account_?number|card_?number|username)\b'

# Online identifiers, tracking and precise geolocation
rg -n -i '\b(ip_?addr(ess)?|user_?agent|device_?id|idfa|gaid|advertising_?id|cookie|fingerprint|lat(itude)?|lng|lon(gitude)?|geo)'

# Sensitive data (definitions vary by state; search broadly)
rg -n -i '\b(health|medical|diagnos|pregnan|reproductive|biometric|face_?id|genetic|neural|ethnic|race|religio|sexual|orientation|transgender|immigration|citizenship|crime_?victim|union)'

# Targeted advertising and sale paths
rg -n -i '(googletagmanager|gtag|doubleclick|facebook|fbq|meta pixel|tiktok|linkedin insight|criteo|trade ?desk|liveramp|segment|mixpanel|amplitude|hotjar|fullstory)'

# Opt-out signals, consent and age signals
rg -n -i '(sec-gpc|globalPrivacyControl|opt.?out|privacy.?choices|gpp|consent|age_?gate|is_?minor|under_?1[368])'
```

Also inspect: database migrations and ORM models, analytics events, server-side tag forwarding, data exports to partners, customer list uploads (custom audiences), scoring or eligibility models, logs, and the field or service that records a user's state of residence.

Done when the inventory in SKILL.md step 2 lists each field, where it is stored, and every recipient it flows to.

## 2. Checks

Severity guidance is in [report-template.md](report-template.md#severity). Check each item against the strictest in-scope state unless the system applies rules per state.

### Minimization and purpose

- Each collected field has a use the notice discloses; unused fields are a finding, graded higher where Maryland's necessity standard applies.
- Reuse for a new purpose not disclosed at collection (support data into ad targeting or model training) lacks the consent most states require.
- Each store has a retention rule enforced in code or configuration.

### Targeted advertising, sale and profiling opt-outs

- Each third-party tag, pixel, SDK and data export is classified: processor under contract, or third party (sale or targeted advertising).
- The opt-out stops every path for that user: client tags, server-side forwarding, audience uploads and partner feeds, including queued jobs.
- Profiling that feeds decisions with legal or similarly significant effects (credit, housing, insurance, education, employment, healthcare) can be opted out of; note Minnesota's right to question the result.
- Known or likely minors are excluded from targeted advertising and sale where an in-scope state requires it.

### Universal opt-out mechanisms

- Where any in-scope state requires a UOOM, the server reads `Sec-GPC: 1` or the client reads `navigator.globalPrivacyControl` before any sale or targeted-advertising tag fires, on every page.
- The signal opts out the browser or device and any profile linked to it; for Colorado, mechanisms on the attorney general's list are honored.
- Applying the signal nationwide is the usual fix; geofencing by state needs a reliable residency signal and is a finding when it fails open.

### Sensitive data

- No sensitive-data processing without recorded opt-in consent before collection (notice and opt-out in Utah and Iowa only); consent records store who, when, which text and which choices.
- Maryland in scope: sensitive data only where strictly necessary, and no sale of it.
- Children's data under 13 is handled under COPPA parental consent.

### Consumer requests and appeals

- Access and portability export one consumer's data in a portable, machine-readable format.
- Correction and deletion reach every copy: primary stores, caches, search indexes, analytics, backups on a documented cycle, and processors through their APIs.
- Requests are authenticated proportionately; opt-out requests need no verification; an appeal path exists and is logged.
- Response clocks (45 days plus one 45-day extension) are tracked.

### Interfaces and consent

- Opt-out and decline paths take no more steps than opt-in; consent is a clear affirmative act, never a pre-ticked box or a dark pattern.

### Security

- Encryption in transit and at rest; least-privilege access including admin and support tools; secrets in a secret store; production data kept out of test environments.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the tag manager's consent trigger, a middleware that reads `Sec-GPC`, the existing job scheduler for purges. Note when a fix needs an organizational decision first (is this disclosure a sale, which states are in scope).
