# Code review checklist

Use this checklist for repositories, diffs, checkout pages, API specs, database schemas, infrastructure code and data-flow descriptions. Code shows where account data goes; it rarely shows the AOCs, scan results or risk analyses an assessor also needs. Pair each technical finding with the evidence question it raises.

For a diff or pull request, review the changed flows and their direct interactions: a new field, log line, script tag or vendor call. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover account data

Search before reading, and read every hit in context. Brand test card numbers in tests and fixtures are expected; a PAN-shaped value elsewhere is a finding to confirm with a Luhn check, without copying the value into the report.

```bash
# Field names for card data and SAD
rg -n -i '\b(pan|card_?(number|num|no)|cc_?(num|number)|primary_?account|cvv2?|cvc2?|cid|card_?(code|verification)|security_?code|track_?[12]?|magstripe|pin_?block|expir(y|ation)|exp_?(month|year|date))\b'

# PAN-shaped literals (13-19 digits, optional separators)
rg -n -P '\b(?:\d[ -]?){12,18}\d\b'

# Payment SDKs, hosted fields and processors
rg -n -i '(stripe|braintree|adyen|checkout\.com|worldpay|cybersource|authorize\.net|paypal|square|mollie|klarna|hosted.?fields|iframe|tokeni[sz])'
```

Also inspect: database migrations and models, request and response schemas, message payloads, logs and error reporting, analytics events, caches, search indexes, exports and backups, payment-page HTML and its script tags, and the network boundary (security groups, firewall rules, VPC peering).

Done when the inventory in SKILL.md step 2 lists each element, every system it touches, and how each system is scoped.

## 2. Checks

Each check names its main requirements. Severity guidance is in [report-template.md](report-template.md#severity).

### Integration and scope (1.2.3, 1.2.4, 12.5.2)

- The code matches the claimed integration: a "hosted page" merchant whose server or frontend sees the PAN is no longer SAQ A.
- Card fields come from the processor (redirect, iframe, hosted fields); merchant-rendered inputs posting to the processor point to SAQ A-EP; server endpoints accepting the PAN point to SAQ D.
- Systems outside the CDE are separated from it by enforced controls, not by naming; flat networks pull everything into scope.

### Storage and retention (3.2.1, 3.3.1-3.3.2, 3.5.1)

- No CVC, track data or PIN block is persisted after authorization anywhere: database, logs, queues, caches, crash dumps.
- Stored PANs have a business need, a retention limit enforced by a purge, and are rendered unreadable: truncation, a token, a keyed hash of the full PAN (3.5.1.1), or strong encryption. Disk-level encryption alone suffices only on removable media (3.5.1.2).
- Keys are stored apart from the data, in the fewest places, under split knowledge or a KMS or HSM, with rotation at the end of the cryptoperiod (3.6.1, 3.7).

### Display and transmission (3.4.1, 4.2.1, 4.2.2)

- Screens, receipts, emails, admin tools and API responses mask the PAN to at most BIN and last four, unless a role has a documented need for the full PAN.
- PANs cross open, public networks only over strong cryptography with valid certificates; no PAN in URLs, query strings or end-user messaging without protection.

### Logging and errors (3.3.1, 10.2)

- Request logging, APM traces and error tools redact card fields before capture; full request bodies on payment endpoints are a finding.
- Audit logs record the 10.2.1 events with user, event type, time, outcome, origin and affected resource (10.2.2), shipped to protected storage.

### Payment-page scripts (6.4.3, 11.6.1)

- Each script on the payment page (or the page embedding the payment iframe) is in an inventory with a justification and is authorized.
- Integrity is enforced: Subresource Integrity, a strict Content-Security-Policy with reporting, or a script-monitoring service.
- A mechanism detects and alerts on changes to the page's scripts and security-impacting headers, at the frequency 11.6.1 or the risk analysis sets.

### Secure development (6.2.4, 6.3.2, 6.3.3, 6.4.2, 6.5.5, 6.5.6)

- Injection, broken access control, insecure deserialization and similar flaws addressed on payment and admin paths.
- Third-party components are inventoried and patched; critical security patches within one month.
- Public-facing web applications sit behind an automated attack-detecting solution such as a WAF.
- Test and staging use test card numbers; test data and accounts are removed before release.

### Authentication and access (7.2, 8.2.8, 8.3, 8.4, 8.6)

- Least privilege for users and service accounts reaching the CDE, including support and admin tools.
- MFA on all non-console access into the CDE and all remote access from outside the network (8.4.2, 8.4.3), not bypassable and resistant to replay (8.5.1).
- Password rules, lockout and idle timeout meet 8.3.4, 8.3.6 and 8.2.8; system-account secrets live in a secret store, not in code or config files (8.6.2).

### Testing hooks (11.3, 11.4.5)

- Vulnerability scanning and segmentation tests cover the CDE boundary the code and infrastructure define; flag when scope changed since the last scan or test.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing logger's redaction hook, the processor's hosted fields or tokens, the infrastructure tool's security-group module. Prefer the fix that shrinks scope over one that adds controls to keep it.
