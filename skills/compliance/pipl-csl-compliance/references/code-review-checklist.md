# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does and where data goes; it rarely shows lawful bases, CIIO status, filings or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, SDK, offshore call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal information

Search before reading. Adapt the patterns to the codebase's language and naming, including pinyin and Chinese identifiers, and read every hit in context.

```bash
# Identity, contact and account fields, including PRC identifiers
rg -n -i '\b(name|e-?mail|phone|mobile|shouji|address|dizhi|birth|gender|id_?card|shenfenzheng|sfz|resident_?id|passport|hukou|bank_?card|alipay|wechat_?(id|openid|unionid)|openid|unionid|real_?name)\b'

# Sensitive PI (PIPL Art. 28): biometrics, health, finance, whereabouts, minors
rg -n -i '(face|facial|renlian|biometric|fingerprint|voiceprint|iris|health|medical|diagnos|religio|ethnic|minzu|bank_?account|credit|transaction|location|lat(itude)?|lng|lon(gitude)?|gps|trajectory|track|guardian|minor|under_?14|age)'

# Online identifiers and tracking
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|imei|oaid|idfa|android_?id|mac_?addr|cookie|session_?id|fingerprint)'

# SDKs, offshore services and cloud regions
rg -n -i '(umeng|jpush|getui|bugly|tencent|aliyun|huaweicloud|firebase|google-analytics|sentry|datadog|segment|amplitude|openai|anthropic|s3\.amazonaws|blob\.core\.windows|region\s*[:=])'
```

Also inspect: database migrations and ORM models, API schemas, mobile SDK lists and permission manifests, analytics events, logs and error reports, caches, search indexes, data warehouse exports, backups, and infrastructure regions (cloud region, bucket and cluster definitions, CDN origins).

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows, with every offshore destination named.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Minimum necessary and purpose (PIPL Art. 5-6, 19)

- Each collected field and app permission has a use tied to a stated purpose; collection beyond the minimum scope is a finding.
- Features work with optional data refused, unless the PI is necessary for that feature (PIPL Art. 16).
- Retention is the shortest period the purpose needs, enforced in code or configuration.

### Consent capture (PIPL Art. 14-16, 29, 31, 39)

- Consent is recorded per purpose with who, when, policy version and choices.
- Each separate consent (sharing with another processor, public disclosure, sensitive PI, cross-border transfer) has its own explicit control, apart from accepting the privacy policy; a single "agree" covering them all is a finding.
- No PI is collected or SDKs initialized before consent; pre-ticked boxes are a finding.
- Withdrawal is as convenient as giving consent and stops processing, including SDKs and queued jobs.
- Age is established where minors may use the service, with guardian consent under 14.

### Sensitive PI and facial data (PIPL Art. 28-31; facial recognition measures)

- Sensitive fields are encrypted or held separately, with tighter access and audit logging.
- Facial recognition has a non-facial alternative for verification and stores face data only as long as needed; 100,000 or more individuals triggers a provincial filing.
- Precise location and trajectories are collected only while the feature needs them.

### Automated decisions and recommendations (PIPL Art. 24; NDSMR 42)

- Personalized feeds, ads or pushes offer a non-personalized option or an easy opt-out, and users can delete their profile tags.
- Pricing or terms do not discriminate unreasonably on profile data.

### Rights handling (PIPL Art. 44-50; NDSMR 23-25)

- The system exports one person's PI, corrects it, and deletes it everywhere: primary store, replicas, caches, indexes, analytics, entrusted parties.
- Account cancellation is available and leads to deletion or anonymization; data kept by law is limited to storage and protection.
- Portability to a designated processor is supported where the NDSMR conditions are met.

### Security and MLPS (PIPL Art. 51; CSL 23, 24, 27)

- Encryption in transit and at rest; secrets outside the code; least-privilege access to admin and support tools.
- Network and access logs are kept at least 6 months; flag when retention is shorter.
- Hashing is pseudonymization, not anonymization; masked or synthetic data in test environments.
- The system's MLPS level and filing are known; level 3 or above raises testing and audit obligations.

### Entrusted parties and SDKs (PIPL Art. 21, 23)

- List every third-party SDK and service receiving PI, what it receives and its role (entrusted party or independent processor). Independent processors need recipient notice and separate consent.

### Localization and cross-border flows (PIPL Art. 38-40; CSL 39; CBDF Provisions)

- Map every flow leaving mainland China: offshore APIs, monitoring and error tools, global CRMs, AI APIs, offshore support or engineers with remote access, and backups. Remote access from abroad counts as export.
- Count individuals exported since 1 January, split sensitive and other PI, and match the mechanism in [pipl-requirements-map.md](pipl-requirements-map.md#cross-border-thresholds-cbdf-provisions).
- CIIO systems, and data flagged as important, keep storage in China; flag any offshore copy.
- Only the fields the offshore recipient needs are exported.

### Important data (DSL 21; NDSMR 29-33)

- Datasets that may match a sector catalogue (mapping, large-scale population, industrial, health statistics) are flagged for identification and reporting.

### Incident readiness (PIPL Art. 57; CSL 27; NDSMR 11)

- Security events on PI stores raise alerts and leave enough record to tell which data and whose was affected, within the reporting windows.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the consent SDK's gating hook, the logger's redaction filter, a region-pinned bucket, a field-level encryption helper. Note when a fix needs an organizational decision first (transfer mechanism, CIIO status, retention period).
