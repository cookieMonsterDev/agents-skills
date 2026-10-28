# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does; it rarely shows purposes, consents obtained or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal information

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identity, contact and account fields, including Canadian identifiers
rg -n -i '\b(first_?name|last_?name|full_?name|e-?mail|phone|mobile|address|postal_?code|province|birth|dob|gender|sin|social_?insurance|health_?card|ohip|ramq|driver_?licen[cs]e|passport|bank|transit|iban|card_?number|username)\b'

# Online identifiers, tracking and location
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|advertising_?id|idfa|gaid|fingerprint|cookie|session_?id|lat(itude)?|lng|lon(gitude)?|geo)'

# Sensitive information (express consent; Québec s. 12)
rg -n -i '\b(health|medical|diagnos|disabilit|biometric|face_?id|fingerprint|genetic|religio|ethnic|race|political|union|sexual|orientation|income|credit_?score|criminal|minor|child)'

# Service providers, analytics, SDKs and hosting regions
rg -n -i '(google-analytics|gtag|googletagmanager|segment|mixpanel|amplitude|hotjar|fullstory|sentry|datadog|intercom|hubspot|facebook|meta pixel|stripe|twilio|sendgrid|mailchimp|openai|anthropic|region|location)'
```

Also inspect: database migrations and ORM models, API schemas, event payloads, analytics events, log and error-reporting calls, caches, search indexes, warehouse exports, backups, file uploads, and where each store is hosted (in Québec, elsewhere in Canada, or abroad).

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows.

## 2. Checks

Each check names its main sections. Severity guidance is in [report-template.md](report-template.md#severity).

### Limiting collection and purposes (Principles 4.2, 4.4; PIPEDA s. 5(3); Québec s. 4, 5)

- Each collected field has a use tied to a stated purpose; "might be useful" fields are a finding.
- Optional data stays optional in forms and APIs.
- Reuse for a new purpose (support data into marketing or model training) has fresh consent or a listed exception (Principle 4.2.4; Québec s. 12).

### Privacy by default and tracking (Québec s. 8.1, 9.1; Principle 4.3)

- Settings of a technological product or service default to the highest confidentiality level, with no user action needed (Québec s. 9.1).
- Features that identify, locate or profile a person (geolocation, fingerprinting, behavioural profiling) are off until the person activates them, with notice (Québec s. 8.1).
- Analytics and advertising cookies or SDKs load only after consent where they are outside the person's reasonable expectations; strictly necessary ones are documented. Check the CAI's current position on cookies, since s. 9.1 excludes them from the default-settings rule but not from consent.
- Consent records store who, when, which text version and which purposes, so consent can be shown; withdrawal stops the processing (Principle 4.3.8).

### Sensitive information and minors (Principle 4.3.4, 4.3.6; Québec s. 4.1, 12, 14)

- Sensitive fields are collected with express, purpose-specific consent and get extra protection (field-level encryption, separate stores, narrower access).
- Data of minors under 14 is collected only with parent or tutor consent (Québec s. 4.1).

### Logging, monitoring and errors (Principles 4.4, 4.7)

- Logs, traces, metric labels and error reports carry only necessary personal information; passwords, tokens, full request bodies, health and payment data are findings.
- Error tools scrub request data or capture only a pseudonymous user ID; log retention is bounded.

### Retention, destruction and anonymization (Principle 4.5.3; Québec s. 23)

- Every store has a retention rule enforced in code or configuration, matching the retention policy.
- Deletion reaches replicas, caches, search indexes, object storage, analytics and service providers; backups expire on a documented cycle.
- "Anonymized" data is irreversibly non-identifying under the anonymization regulation; hashed IDs are de-identified, so still personal information.

### Individual rights (Principle 4.9; Québec s. 12.1, 27, 28, 28.1)

- Access: the system can export one person's information across stores, within 30 days.
- Portability: computerized information collected from the person exports in a structured, commonly used format, to the person or a designated body (Québec s. 27).
- Rectification propagates; requests are authenticated proportionately.
- Automated decisions: a decision based exclusively on automated processing triggers a notice, can be explained (information used, reasons, principal factors) and routed to a staff member for review (Québec s. 12.1).
- Published content about a person can be de-indexed or taken down on a valid request (Québec s. 28.1).

### Security safeguards (Principle 4.7; Québec s. 10)

- Encryption in transit and at rest; secrets in a secret store; least-privilege access including admin and support tools; access to sensitive data logged.
- Passwords use a dedicated password hashing function (Argon2, scrypt, bcrypt).
- Non-production environments use synthetic or masked data.

### Service providers and cross-border flows (Principle 4.1.3; Québec s. 17, 18.3)

- List every third party receiving personal information, what it receives and its hosting region.
- Calls to analytics, AI APIs and support tools send only the fields the provider needs.
- Information leaving Québec has a documented PIA and written agreement (Québec s. 17); information leaving Canada is disclosed in the privacy policy and protected by contract (OPC cross-border guidelines). Flag when the contract or PIA is not in evidence.

### Incident readiness (PIPEDA s. 10.1-10.3; Québec s. 3.5-3.8)

- Security events on personal information stores are detectable: audit logs, alerting, anomaly detection.
- Enough is logged to determine what information and whose was affected, feeding both the federal breach record and the Québec incident register.

### New systems (Québec s. 3.3)

- A new or overhauled information system or electronic service handling personal information points to a PIA; flag whether one exists, and whether the system can export portable data.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing logger's redaction hook, the ORM's soft-delete pattern, the existing scheduler for purges, the feature-flag system for off-by-default functions. Note when a fix needs an organizational decision first (retention period, consent form, hosting region).
