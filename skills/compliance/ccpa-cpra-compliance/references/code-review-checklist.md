# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, tag manager and SDK configuration, infrastructure code and data-flow descriptions. Code shows what the system collects and where it flows; it rarely shows contracts, revenue or whether a recipient is a service provider. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, tag, SDK, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal information

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identifiers and account fields
rg -n -i '\b(first_?name|last_?name|e-?mail|phone|address|zip|postal|birth|dob|ssn|driver_?license|passport|state_?id|account_?number|card_?number|username|password)\b'

# Online identifiers, tracking and precise geolocation
rg -n -i '\b(ip_?addr(ess)?|user_?agent|device_?id|idfa|gaid|advertising_?id|cookie|fingerprint|lat(itude)?|lng|lon(gitude)?|geo)'

# Sensitive personal information (§1798.140(ae))
rg -n -i '\b(health|medical|diagnos|biometric|face_?id|genetic|neural|ethnic|race|religio|union|sexual|orientation|immigration|citizenship)'

# Sale and sharing paths: ad tech, pixels, data partners
rg -n -i '(googletagmanager|gtag|doubleclick|facebook|fbq|meta pixel|tiktok|linkedin insight|criteo|trade ?desk|liveramp|segment|mixpanel|amplitude|hotjar|fullstory|clarity)'

# Opt-out signal and consent handling
rg -n -i '(sec-gpc|globalPrivacyControl|do.?not.?sell|opt.?out|privacy.?choices|usp(api)?|gpp|consent)'
```

Also inspect: database migrations and ORM models, API schemas, analytics events, server-side tag forwarding, data warehouse exports to partners, customer list uploads (custom audiences), logs, and mobile SDK manifests.

Done when the inventory in SKILL.md step 2 lists each field, where it is stored, and every recipient it flows to.

## 2. Checks

Each check names its main sections. Severity guidance is in [report-template.md](report-template.md#severity).

### Minimization and purpose (§1798.100(c); Regs. §7002)

- Each collected field has a use the notice discloses; unused or "might be useful" fields are a finding.
- Reuse for an undisclosed, incompatible purpose (support data into ad targeting or model training) is a finding.
- Each store has a retention rule enforced in code or configuration that matches the disclosed period.

### Sale and sharing (§1798.120, .135; Regs. §7026)

- Each third-party tag, pixel, SDK and data export is classified: service provider or contractor (contract needed), or third party (likely sale or sharing).
- The opt-out stops every sale and sharing path for that user: client tags, server-side forwarding, audience uploads and partner feeds, including jobs already queued.
- The opt-out page works without an account, login or verification, and records the choice against the browser, device and any known profile.
- Consumers under 16 get no sale or sharing until opt-in is recorded (§1798.120(c)).

### Opt-out preference signals (§1798.135; Regs. §7025)

- The server reads `Sec-GPC: 1` or the client reads `navigator.globalPrivacyControl` before any sale or sharing tag fires, on every page.
- The signal opts out the browser or device and any profile linked to it, including pseudonymous ones; a known user's opt-out persists when a later visit lacks the signal.
- The site displays that the signal was honored (Regs. §7025(c)(6)), and a conflicting earlier opt-in yields to the signal unless the user re-consents.

### Sensitive personal information (§1798.121; Regs. §7027)

- Uses beyond the Regs. §7027(m) purposes (inferring characteristics, ad targeting) trigger the limit right; the limit choice stops them everywhere.
- Precise geolocation is coarsened where precision is unneeded; sensitive fields get field-level protection.

### Consumer requests (§1798.105, .106, .110, .115, .130; Regs. §7020-7024, 7060-7063)

- Access can export every category and specific piece held about one consumer, including inferences.
- Deletion and correction reach every copy: primary stores, caches, search indexes, analytics, backups on a documented cycle, and service providers through their APIs.
- Verification matches the data's sensitivity and does not demand more data than needed; authorized agents are supported.
- Request handling logs what is needed for the 24-month record (Regs. §7101) without copying the requested data.

### Interfaces and dark patterns (§1798.140(h), (l); Regs. §7004)

- Opt-out and limit paths take no more steps than the opt-in path; choices are symmetric in size, color and wording.
- Cookie banners labeled "Accept all" with only "More options" on the other side are a finding.

### Security (§1798.100(e), §1798.150)

- Encryption in transit and at rest; field-level encryption or redaction for the data §1798.150 covers (with §1798.81.5), since encryption or redaction defeats the private action.
- Least-privilege access for admin and support tools; secrets in a secret store; production data kept out of test environments.

### ADMT and profiling (Regs. §7150, §7200-7222)

- Models or rules that make or substantially make a significant decision (credit, housing, education, hiring, healthcare) are listed, with whether a human reviewer can change the outcome.
- Pre-use notice, opt-out or appeal, and access to the logic are wired in; training on personal data for such models, or for identification, points to a risk assessment.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the tag manager's consent trigger, a middleware that reads `Sec-GPC`, the existing job scheduler for purges. Note when a fix needs an organizational decision first (is this vendor a service provider, is this disclosure a sale).
