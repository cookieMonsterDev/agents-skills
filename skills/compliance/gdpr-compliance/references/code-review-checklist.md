# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does; it rarely shows purposes, lawful bases or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identity, contact and account fields
rg -n -i '\b(first_?name|last_?name|full_?name|e-?mail|phone|mobile|address|street|zip|postal|birth|dob|gender|nationality|passport|ssn|national_?id|tax_?id|iban|card_?number|username)\b'

# Online identifiers, tracking and location
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|advertising_?id|idfa|gaid|fingerprint|cookie|session_?id|lat(itude)?|lng|lon(gitude)?|geo)'

# Special categories (Art. 9) and criminal data (Art. 10)
rg -n -i '\b(health|medical|diagnos|allerg|disabilit|biometric|face_?id|fingerprint|genetic|religio|ethnic|race|political|union|sexual|orientation|criminal|conviction)'

# Third-party processors, analytics and SDKs
rg -n -i '(google-analytics|gtag|googletagmanager|segment|mixpanel|amplitude|hotjar|fullstory|sentry|datadog|newrelic|intercom|hubspot|facebook|meta pixel|stripe|twilio|sendgrid|mailchimp|openai|anthropic)'
```

Also inspect: database migrations and ORM models, API request and response schemas, event and message payloads, analytics events, log and error-reporting calls, caches, search indexes, data warehouse exports, backups, file uploads, and infrastructure regions (`region`, `location`, bucket and cluster definitions).

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Minimisation and purpose (Art. 5(1)(b)-(c), 25)

- Each collected field has a use in the code; unused or "might be useful" fields are a finding.
- Forms and APIs keep optional data optional; defaults collect and expose the least (privacy by default).
- Data stays with the purpose it was collected for; reuse for another purpose (support data into marketing or model training) is a finding unless compatible under Art. 6(4) and disclosed.
- Identifiers are coarsened where precision is unnecessary: truncated IPs, city-level location, age band instead of birth date.

### Logging, monitoring and errors (Art. 5(1)(c), 5(1)(f), 32)

- Logs, traces, metric labels and error reports carry only necessary personal data; passwords, tokens, full request bodies, health and payment data are findings.
- Error tools (Sentry, Datadog and similar) scrub request data and user context, or capture only a pseudonymous user ID.
- Log retention is bounded and matches the stated retention.

### Storage limitation and deletion (Art. 5(1)(e), 17)

- Every store with personal data has a retention rule enforced in code or configuration: TTLs, scheduled purges, lifecycle policies.
- Account or record deletion reaches every copy: primary database, replicas, caches, search indexes, object storage, analytics, processors' systems through their APIs, and backups (expiring backups on a documented cycle is the usual accepted approach).
- Soft deletes are followed by a hard delete or anonymisation within a defined period.
- "Anonymised" data is truly anonymous; hashing an email or ID is pseudonymisation, not anonymisation.

### Data subject rights (Art. 12, 15-22)

- Access and portability: the system can export all of one person's data, portability in a structured, machine-readable format (JSON, CSV).
- Rectification: users or support can correct data, and corrections propagate.
- Erasure and restriction: a supported path exists, with documented exceptions (legal retention).
- Objection and marketing: opt-out stops direct marketing processing everywhere, including queued jobs and processors.
- Automated decisions (Art. 22): solely automated decisions with legal or similarly significant effects offer human review, a way to contest, and an explanation of the logic.
- Requests are authenticated proportionately, so each person reaches only their own data.

### Consent and tracking (Art. 6(1)(a), 7, 8; ePrivacy Art. 5(3))

- Non-essential cookies, local storage, pixels and SDK identifiers are set or read only after consent.
- Consent is granular per purpose and opt-in through an unticked box or explicit button, and refusing is as easy as accepting.
- Consent records store who, when, which version of the text, and which choices, so consent can be proven (Art. 7(1)).
- Withdrawal takes effect: tags stop loading and server-side processing based on consent stops.
- Age gating or parental consent exists where the service targets children.

### Security (Art. 5(1)(f), 25, 32)

- Encryption in transit (TLS) and at rest for personal data stores and backups; secrets live in a secret store or environment.
- Access control follows least privilege, including admin and support tools and internal APIs; access to sensitive data is logged.
- Passwords use a dedicated password hashing function (Argon2, scrypt, bcrypt).
- Special-category or high-risk fields get extra protection: field-level encryption, pseudonymisation, separate stores.
- Test, staging and developer environments use synthetic or masked data, or production-equivalent protection.

### Processors and transfers (Art. 28, 44-49)

- List every third-party service that receives personal data, what it receives, and its hosting region.
- Calls to analytics, AI APIs and support tools send only the fields the processor needs.
- Data stored or sent outside the EEA has a transfer mechanism; flag the need for a DPA and transfer basis when the contract is not in evidence.
- Client-side scripts loaded from third-party CDNs are processors or controllers too: they receive IP addresses.

### Breach readiness (Art. 33, 34)

- Security events on personal data stores are detectable: audit logs, alerting, anomaly detection.
- Enough is logged to determine what data and whose data a breach affected, within the 72-hour window.

### Profiling and AI (Art. 5, 6, 9, 22, 35)

- Personal data used for training, fine-tuning or prompts has a lawful basis and is covered by the notice.
- Inferences that reveal special categories are treated as special-category data.
- Large-scale profiling or novel technology points to a DPIA; flag whether one exists.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing logger's redaction hook, the ORM's soft-delete pattern, the existing job scheduler for purges. Note when a fix needs an organizational decision first (retention period, lawful basis).
