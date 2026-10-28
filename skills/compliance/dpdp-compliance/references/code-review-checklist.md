# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does; it rarely shows purposes, notices or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields.

```bash
# Identity, contact and account fields
rg -n -i '\b(first_?name|last_?name|full_?name|e-?mail|phone|mobile|msisdn|address|pin_?code|pincode|birth|dob|gender|username)\b'

# Indian identifiers and financial data
rg -n -i '\b(aadhaar|aadhar|uidai|pan(_?(no|number|card))?|voter_?id|epic|passport|driving_?licen[cs]e|gstin|upi|vpa|ifsc|account_?(no|number)|card_?number|cvv)\b'

# Online identifiers, tracking and location
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|imei|advertising_?id|idfa|gaid|fingerprint|cookie|session_?id|lat(itude)?|lng|lon(gitude)?|geo)'

# Children, guardians and higher-risk data
rg -n -i '\b(child|minor|age_?(gate|check|verif)|parent|guardian|kyc|digilocker|health|medical|diagnos|biometric|face_?id|caste|religio)'

# Third-party processors, analytics and SDKs
rg -n -i '(google-analytics|gtag|googletagmanager|firebase|segment|mixpanel|amplitude|clevertap|moengage|webengage|hotjar|clarity|sentry|datadog|newrelic|freshdesk|zendesk|razorpay|payu|cashfree|paytm|stripe|msg91|gupshup|twilio|sendgrid|openai|anthropic)'
```

Also inspect: database migrations and ORM models, API request and response schemas, event payloads, analytics events, log and error-reporting calls, caches, search indexes, warehouse exports, backups, file uploads, and infrastructure regions (`region`, `location`, bucket and cluster definitions) to find data leaving India.

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows.

## 2. Checks

Each check names its main sections and rules. Severity guidance is in [report-template.md](report-template.md#severity).

### Notice and consent (s.5, 6; Rule 3)

- Every consent-based collection point shows a notice before or with the request: itemised data, specified purposes, and links to withdraw, exercise rights and complain to the Board.
- Consent is an affirmative act per purpose (unticked box, explicit button); bundling unnecessary data into a service's consent is a finding (s.6(1)).
- Consent records store who, when, which notice version and which purposes, so the fiduciary can prove notice and consent (s.6(10)).
- Withdrawal is as easy as giving consent, and stops processing in the fiduciary and its processors, including queued jobs (s.6(4), 6(6)).
- Processing without consent maps to a specific s.7 legitimate use; "legitimate interest" in the GDPR sense is not available.
- Notices and consent screens can be shown in English or an Eighth Schedule language (s.5(3), 6(3)).

### Children and guardianship (s.9; Rules 10-12)

- Services reachable by under-18s have an age signal, and processing waits for verifiable parental consent: an identifiable adult, checked against identity and age data held, or a DigiLocker or authorised virtual token (Rule 10).
- No tracking, behavioural monitoring or targeted advertising directed at children; analytics, ad SDKs and recommendation features are switched off or exempt under the Fourth Schedule with its conditions.
- Guardian consent for persons with disability checks the court or authority appointment (Rule 11).

### Security safeguards (s.8(5); Rule 6)

- Encryption, masking, obfuscation or tokenisation of personal data at rest and in transit; secrets in a secret store or environment.
- Access control on the systems that hold personal data, including admin and support tools.
- Access to personal data is logged and monitored, and those logs and the data needed to investigate are kept for 1 year (Rule 6(1)(e)).
- Backups and continuity measures exist for loss of availability.
- Test and staging environments use synthetic or masked data.

### Breach readiness (s.8(6); Rule 7)

- Security events on personal data stores are detectable and alerting reaches an owner.
- Logs show what data and whose data a breach affected, fast enough for the Board's 72-hour detailed report.
- Each affected Data Principal can be contacted through the user account or registered contact.

### Retention and erasure (s.8(7)-(8); Rule 8, Third Schedule)

- Every store has a retention rule enforced in code or configuration, tied to the purpose or a legal retention duty.
- Withdrawal or end of purpose triggers erasure everywhere: primary store, replicas, caches, search indexes, object storage, analytics, processors through their APIs, and backups on a documented cycle.
- Third Schedule platforms (e-commerce with at least 2 crore registered users in India, online gaming with at least 50 lakh, social media with at least 2 crore) purge after 3 years of inactivity and warn the user 48 hours before.
- Processing logs and associated personal and traffic data are kept at least 1 year before erasure (Rule 8(3)); retention past that needs a legal reason.

### Data Principal rights and grievances (s.11-14; Rules 9, 14)

- Access: the system can export a summary of one person's data and processing, and the list of fiduciaries and processors it was shared with (s.11).
- Correction, completion, updating and erasure paths exist and propagate (s.12).
- A grievance channel tracks each complaint to a response within 90 days (Rule 14(3)).
- Nomination of another individual is supported (s.14).
- Requests are authenticated using the identifiers the fiduciary publishes, so each person reaches only their own data.

### Processors and transfers (s.8(1)-(2), 16; Rules 13(4), 15)

- List every third-party service that receives personal data, what it receives, and its hosting region.
- Calls to analytics, AI APIs and support tools send only the fields the processor needs.
- Transfers abroad are checked against any destination notified under s.16 and any sectoral localisation rule; payment data under the RBI circular stays in India.
- Significant Data Fiduciaries keep any Government-specified data and its traffic data in India (Rule 13(4)).

### Accuracy and automated decisions (s.8(3); Rule 13(3))

- Data used to make decisions about a person, or disclosed to another fiduciary, is checked for completeness, accuracy and consistency.
- Significant Data Fiduciaries document due diligence that algorithmic software processing personal data poses no risk to Data Principals' rights.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing logger's redaction hook, the ORM's soft-delete pattern, the existing job scheduler for purges. Note when a fix needs an organizational decision first (retention period, legitimate use, SDF status).
