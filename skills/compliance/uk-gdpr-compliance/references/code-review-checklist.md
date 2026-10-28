# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code, tag and SDK configuration, and data-flow descriptions. Code shows what the system does; it rarely shows purposes, lawful bases or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, cookie, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identity, contact and account fields, including UK identifiers
rg -n -i '\b(first_?name|last_?name|full_?name|e-?mail|phone|mobile|address|postcode|birth|dob|gender|nationality|passport|ni_?number|national_?insurance|nhs_?number|driving_?licen[cs]e|sort_?code|account_?number|card_?number|username)\b'

# Online identifiers, tracking and location
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|advertising_?id|idfa|gaid|fingerprint|cookie|localStorage|sessionStorage|session_?id|pixel|lat(itude)?|lng|lon(gitude)?|geo)'

# Special category (Art. 9) and criminal offence data (Art. 10)
rg -n -i '\b(health|medical|diagnos|disabilit|biometric|face_?id|genetic|religio|ethnic|race|political|union|sexual|orientation|criminal|conviction|dbs_?check)'

# Marketing channels, processors, analytics and SDKs
rg -n -i '(newsletter|marketing|opt_?in|unsubscribe|sms|tps|google-analytics|gtag|googletagmanager|segment|mixpanel|amplitude|hotjar|sentry|datadog|intercom|hubspot|facebook|meta pixel|stripe|twilio|sendgrid|mailchimp|openai|anthropic)'
```

Also inspect: migrations and ORM models, API schemas, event payloads, analytics events, log and error-reporting calls, caches, search indexes, warehouse exports, backups, file uploads, tag manager containers, mobile SDK initialisation, and infrastructure regions.

Done when the inventory in SKILL.md step 2 lists each field, device identifier and marketing channel, where it is stored and where it flows.

## 2. Checks

Each check names its main provisions. Severity guidance is in [report-template.md](report-template.md#severity).

### Minimisation and purpose (Art. 5(1)(b)-(c), 8A, 25)

- Each collected field has a use; unused or "might be useful" fields are a finding.
- Reuse for another purpose is compatible under Art. 8A and Annex 2, or has its own basis, and is disclosed.
- Services likely to be accessed by children default to high privacy, reflecting children's higher protection matters (Art. 25; review in depth with `aadc-compliance`).

### Cookies and similar technologies (PECR reg. 6, Schedule A1)

- Each cookie, local storage key, pixel and SDK identifier maps to consent or a Schedule A1 exception.
- Analytics set without consent meet the statistical-purposes exception: sole purpose is improving the service, data shared only for that, clear information, and a free, simple way to object that the code honours. Advertising, cross-site tracking and fingerprinting need consent.
- Functionality and appearance storage without consent meets the same information and objection conditions.
- Non-exempt tags load only after consent; rejecting is as easy as accepting; withdrawal stops tags and server-side processing.
- Consent records store who, when, text version and choices (Art. 7(1)).

### Electronic marketing (PECR reg. 21-22; Art. 21(3))

- Email and SMS marketing to individuals sends only to consented recipients or soft opt-in customers (charities: supporters under the reg. 22 charity route).
- Every message carries a working opt-out, and opt-outs suppress across systems, queued jobs and processors.
- Marketing calls are screened against the TPS and the internal do-not-call list.

### Logging, monitoring and errors (Art. 5(1)(c), 5(1)(f), 32)

- Logs, traces, metric labels and error reports carry only necessary personal data; passwords, tokens, full request bodies, health and payment data are findings.
- Error tools scrub request data or capture only a pseudonymous user ID; log retention is bounded.

### Storage limitation and deletion (Art. 5(1)(e), 17)

- Every store has an enforced retention rule matching the stated retention.
- Erasure reaches replicas, caches, search indexes, object storage, analytics, processors and, on a documented cycle, backups; soft deletes are followed by hard delete or anonymisation.

### Data subject rights (Art. 12, 12A, 15-22)

- Access: the system can find one person's data across stores, supporting a reasonable and proportionate search (Art. 15(1A)) and the one-month limit.
- Portability, rectification, restriction and objection paths exist and propagate.
- Requests are authenticated proportionately.

### Automated decision-making (Art. 22A-22D)

- Solely automated significant decisions offer the Art. 22C safeguards in the product: information about the decision, a way to make representations, human intervention and contest.
- Such decisions avoid special category data unless an Art. 22B condition is met, and avoid processing based on Art. 6(1)(ea).
- "Human review" is meaningful: a reviewer with authority and the information to change the outcome.

### Security (Art. 5(1)(f), 32)

- Encryption in transit and at rest; secrets in a secret store; least-privilege access including admin and support tools.
- Passwords use a dedicated password hashing function (Argon2, scrypt, bcrypt).
- Non-production environments use synthetic or masked data.

### Processors and restricted transfers (Art. 28, Chapter 5)

- List every third-party service receiving personal data, what it receives and its hosting region.
- Data stored or accessed outside the UK has a transfer basis: UK adequacy regulations, the UK-US data bridge for certified recipients, or the IDTA or Addendum with a transfer risk assessment. Flag when the contract is not in evidence.

### Breach readiness (Art. 33, 34)

- Security events on personal data stores are detectable, and enough is logged to determine what data and whose was affected within the 72-hour window.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the consent management platform's tag categories, the logger's redaction hook, the existing scheduler for purges, the ESP's suppression list. Note when a fix needs an organizational decision first (retention period, lawful basis, transfer mechanism).
