# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does with health data; it rarely shows BAAs, certificates, risk analyses or the purpose behind a disclosure. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, vendor call, region or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover health data

Search before reading. Adapt the patterns to the codebase's language and naming, including French field names, and read every hit in context.

```bash
# Patient identity and the Safe Harbor identifiers
rg -n -i '\b(patient|mrn|medical_?record|member_?id|subscriber|beneficiary|health_?plan|ssn|nir|ins_?(nir)?|date_?of_?(birth|admission|discharge|death)|dob|zip|postal|phone|fax|e-?mail|address|device_?serial|license|vehicle|url|ip_?addr(ess)?|biometric|photo)\b'

# Clinical content
rg -n -i '(diagnos|icd-?1[01]|cpt|snomed|loinc|rxnorm|prescri|medication|allerg|lab_?result|vital|encounter|claim|procedure|imaging|dicom|hl7|fhir|psychotherap|substance|genetic|pregnan|reproductive|hiv|mental)'

# Vendors, tracking and AI services that may receive PHI
rg -n -i '(google-analytics|gtag|googletagmanager|meta pixel|facebook|segment|mixpanel|amplitude|hotjar|fullstory|sentry|datadog|newrelic|intercom|zendesk|twilio|sendgrid|openai|anthropic|bedrock|vertex)'

# Hosting regions and providers
rg -n -i '(region\s*[:=]|location\s*[:=]|us-east|us-west|eu-west|eu-central|francecentral|europe-west9|ovh|scaleway|outscale|azure|aws|gcp)'
```

Also inspect: database migrations and ORM models, FHIR or HL7 interfaces, API schemas, message payloads, analytics events, logs and error reports, caches, search indexes, data warehouse exports, backups, file uploads (scans, images), mobile app storage, and infrastructure regions.

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows, with each hosting provider and region named.

## 2. HIPAA checks

Severity guidance is in [report-template.md](report-template.md#severity).

### Uses, disclosures and minimum necessary (164.502, 164.514(d))

- Every outbound flow of PHI has a permitted purpose; marketing, analytics for third-party benefit and sale of PHI need authorization.
- APIs, exports and reports return only the fields the caller's role needs; whole-record responses to narrow use cases are a finding.
- Role-based access in admin, support and reporting tools maps to minimum necessary policies.

### Business associates and tracking (164.502(e), 164.504(e))

- List every vendor receiving PHI: what it receives, its role, and whether a BAA is in evidence.
- Tracking pixels, session replay and analytics on authenticated pages, appointment flows, symptom checkers and patient apps receive PHI; without a BAA and permission, that is an impermissible disclosure and a presumed breach.
- AI and LLM calls with PHI go only to vendors under a BAA, with retention and training use excluded.

### De-identification (164.514(a)-(c))

- Data labeled de-identified removes all 18 Safe Harbor identifiers, including dates more precise than the year, ZIP codes beyond the first three digits with the population rule, and ages over 89; otherwise an expert determination is in evidence.
- Hashing an MRN or email is not de-identification; re-identification keys are not derived from PHI and are kept apart.

### Access control and authentication (164.312(a), (d))

- Unique user IDs for every person and service; no shared accounts.
- Emergency (break-glass) access exists, is logged and reviewed.
- Sessions time out; MFA protects remote and privileged access (expected in the NPRM; current practice under the risk analysis).

### Audit controls and activity review (164.312(b), 164.308(a)(1)(ii)(D))

- Reads, writes, exports and deletes of ePHI are logged with user, time, record and action, and logs are protected from tampering.
- Logs themselves keep PHI out of free text; error tools scrub request bodies.
- Someone reviews the logs: alerts or scheduled reports exist.

### Encryption and integrity (164.312(a)(2)(iv), (c), (e))

- ePHI is encrypted at rest and in transit with current NIST-recommended algorithms; where not, a documented reason and equivalent alternative exist. Encryption per HHS guidance also makes a lost dataset "secured" and outside breach notification.
- Integrity controls detect improper alteration: checksums, signed messages, database constraints and audit trails.

### Contingency and disposal (164.308(a)(7), 164.310(d))

- Backups exist, are encrypted, tested for restore, and cover every ePHI store.
- Media and environment teardown wipes or destroys ePHI; test environments use synthetic or de-identified data.

### Breach readiness (164.400-164.414)

- Enough is logged to determine what PHI and whose was affected, to meet the 60-day notice clock.

## 3. HDS checks

### Hosting scope and certification (L.1111-8; R.1111-9)

- Identify each provider hosting French health data for a third party and the R.1111-9 activities it performs: cloud IaaS, PaaS, managed database, backup, monitoring with data access, outsourced operations.
- Each such provider holds a current HDS certificate covering those activities; a general ISO 27001 certificate does not suffice.

### Localisation and transfers (referential v2; Décret n° 2026-209)

- Storage regions, replicas and backups for health data sit in the EEA; flag any non-EEA region, CDN cache or support tooling holding the data.
- Remote administration or support from outside the EEA is a transfer (explicit in v2.1); confirm it appears in the host's published transfer map and has a GDPR transfer mechanism.
- Services under non-EEA parents are disclosed by the host as exposed to non-EEA law; flag them for the controller's risk decision.

### Reversibility and security

- Data can be exported in a usable format and deleted at the end of the contract.
- The checks in section 2 on access, logging, encryption and backups apply as security evidence for HDS and GDPR Art. 32.

## 4. Map findings to fixes

Give fixes in the codebase's own idiom: the logger's redaction hook, a server-side tag manager that strips PHI, a region-pinned bucket, the ORM's audit plugin. Note when a fix needs an organizational decision first (signing a BAA, changing host, a risk acceptance).
