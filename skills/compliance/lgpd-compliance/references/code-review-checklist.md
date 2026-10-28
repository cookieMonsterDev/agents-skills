# Code review checklist

Use this checklist for repositories, diffs, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows what the system does; it rarely shows purposes, legal bases or contracts. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed processing and its direct interactions: a new field, log line, vendor call or export path. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover personal data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives and miss renamed fields. Brazilian codebases often name fields in Portuguese.

```bash
# Identity, contact and account fields, English and Portuguese
rg -n -i '\b(first_?name|last_?name|full_?name|nome|sobrenome|e-?mail|phone|telefone|celular|address|endereco|logradouro|cep|zip|birth|nascimento|dob|gender|genero|sexo|username)\b'

# Brazilian identifiers and financial data
rg -n -i '\b(cpf|cnpj|rg|cnh|pis|nis|titulo_?eleitor|passaporte|passport|pix|chave_?pix|agencia|conta_?bancaria|numero_?conta|iban|card_?number|cartao)\b'

# Online identifiers, tracking and location
rg -n -i '\b(ip_?addr(ess)?|remote_?addr|x-forwarded-for|user_?agent|device_?id|advertising_?id|idfa|gaid|fingerprint|cookie|session_?id|lat(itude)?|lng|lon(gitude)?|geo)'

# Sensitive data (Art. 5(II), 11) and minors (Art. 14)
rg -n -i '\b(health|saude|medical|medico|diagnos|cid_?10|allerg|deficien|disabilit|biometr|face_?id|impressao_?digital|genetic|religi|etni|raca|race|politic|sindic|union|sexual|orientac|crianca|child|menor|minor|adolescente)'

# Third-party operators, analytics and SDKs
rg -n -i '(google-analytics|gtag|googletagmanager|segment|mixpanel|amplitude|hotjar|clarity|sentry|datadog|newrelic|intercom|zendesk|hubspot|rd ?station|facebook|meta pixel|stripe|pagar\.?me|mercado ?pago|twilio|zenvia|sendgrid|mailchimp|openai|anthropic)'
```

Also inspect: database migrations and ORM models, API request and response schemas, event payloads, analytics events, log and error-reporting calls, caches, search indexes, warehouse exports, backups, file uploads, and infrastructure regions (`region`, `location`, bucket and cluster definitions) to find data leaving Brazil.

Done when the inventory in SKILL.md step 2 lists each field, where it is stored and where it flows.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Necessity and purpose (Art. 6(I)-(III), 46 §2)

- Each collected field has a use in the code; unused or "might be useful" fields fail necessity.
- Optional data stays optional; defaults collect and expose the least.
- Data stays with its purpose; reuse for another purpose (support data into marketing or model training) needs its own basis and disclosure.
- CPF and other national identifiers are collected only where a purpose requires them, and are masked in displays and exports.

### Logging, monitoring and errors (Art. 6(III), 46)

- Logs, traces, metric labels and error reports carry only necessary personal data; passwords, tokens, CPF, full request bodies, health and payment data are findings.
- Error tools scrub request data and user context, or capture only a pseudonymous user ID.
- Log retention is bounded. Marco Civil da Internet (Lei 12.965/2014, Art. 15) requires application providers to keep access logs for 6 months; retention far beyond what a law or purpose requires is a finding.

### Retention and deletion (Art. 15, 16, 18(IV), 18(VI))

- Every store with personal data has a retention rule enforced in code or configuration: TTLs, scheduled purges, lifecycle policies.
- Deletion and consent revocation reach every copy: primary database, replicas, caches, search indexes, object storage, analytics, operators' systems through their APIs, and backups on a documented expiry cycle.
- Retention after the purpose ends maps to an Art. 16 ground (legal obligation, research, controller's exclusive anonymised use).
- "Anonymised" data cannot be re-identified with reasonable means (Art. 12); hashing an email or CPF is pseudonymisation.

### Data subject rights (Art. 18-20)

- Confirmation and access: the system can export all of one person's data, in a simplified form immediately and a complete one within 15 days (Art. 19).
- Correction, anonymisation, blocking and deletion paths exist, and changes propagate to recipients (Art. 18 §6).
- Portability exports a structured, interoperable format.
- Consent revocation stops consent-based processing everywhere, including queued jobs and operators.
- Automated decisions affecting the person (credit scoring, fraud blocks, profiling) have a review path and can explain their criteria (Art. 20).
- Requests are authenticated proportionately, so each person reaches only their own data.

### Consent and tracking (Art. 7(I), 8, 9; ANPD cookie guide)

- Non-essential cookies, pixels and SDK identifiers load only after consent, or under a documented legitimate-interest assessment for the rest.
- Consent is per purpose, opt-in, and records who, when, which text version and which choices (burden on the controller, Art. 8 §2).
- Revocation is as simple as giving consent and takes effect in tags and server-side processing (Art. 8 §5).
- Sensitive-data consent is specific and highlighted, separate from general terms (Art. 11(I)).

### Children and adolescents (Art. 14)

- Services likely used by minors have age signals; processing of children's data under consent captures specific consent from a parent or guardian, with reasonable verification (14 §1, §5).
- Games and apps condition participation only on strictly necessary data (14 §4).
- Flag the ECA Digital for separate review when the service is likely accessed by minors.

### Security and incidents (Art. 46-49; Res. 15/2024)

- Encryption in transit and at rest for personal data stores and backups; secrets live in a secret store or environment.
- Least-privilege access, including admin and support tools; access to sensitive data is logged.
- Passwords use Argon2, scrypt or bcrypt.
- Test and staging environments use synthetic or masked data.
- Security events are detectable, and logs show what data and whose data an incident affected, fast enough to meet the 3-business-day communication deadline.

### Operators and international transfers (Art. 33-39; Res. 19/2024)

- List every third-party service that receives personal data, what it receives, and its hosting region.
- Calls to analytics, AI APIs and support tools send only the fields the operator needs.
- Data stored or sent outside Brazil has a mechanism (adequacy, ANPD standard clauses, global corporate rules, approved specific clauses or another Art. 33 ground); flag the need when the contract is not in evidence.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing logger's redaction hook, the ORM's soft-delete pattern, the existing job scheduler for purges. Note when a fix needs an organizational decision first (retention period, legal basis).
