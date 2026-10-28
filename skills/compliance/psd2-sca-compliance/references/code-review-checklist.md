# Code review checklist

Use this checklist for repositories, diffs, API specs, 3-D Secure integrations, risk-engine rules, authentication services and open-banking interfaces. Code shows how authentication and exemptions run; it rarely shows fraud rates, authority notifications or the processor's configuration. Pair each technical finding with the evidence question it raises.

For a diff or pull request, review the changed flows and their direct interactions: a new payment path, exemption flag, session setting or TPP endpoint. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover payment and authentication flows

Search before reading, and read every hit in context.

```bash
# SCA, 3-D Secure and exemption handling
rg -n -i '(\bsca\b|3ds|three_?d_?secure|challenge|frictionless|exemption|low_?value|\btra\b|trusted_?beneficiar|whitelist|recurring|merchant_?initiated|\bmit\b|\bmoto\b|secure_?corporate)'

# Authentication events, factors and sessions
rg -n -i '(otp|totp|one_?time|biometric|face_?id|touch_?id|webauthn|passkey|device_?bind|push_?approv|pin\b|password|lockout|failed_?attempt|session_?(timeout|ttl)|idle)'

# Payments and amounts
rg -n -i '(payment_?initiat|credit_?transfer|sepa|instant|iban|payee|beneficiar|amount|currency|mandate|direct_?debit)'

# Open banking and TPP access
rg -n -i '(berlin_?group|nextgenpsd2|stet|open_?banking|\baisp?\b|\bpisp?\b|\bcbpii?\b|consent_?id|qwac|qseal|eidas|psd2_?role|x-request-id|psu-ip-address|tpp)'
```

Also inspect: authentication and step-up middleware, risk-scoring rules and thresholds, counters for cumulative amounts and transaction counts, processor or acquirer SDK calls and the exemption indicators they send, mTLS and certificate validation, consent stores, rate limits on account-information endpoints, and audit logs of authentication events.

Done when the three inventory tables in SKILL.md step 2 list every flow, authentication event and TPP access path found.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### SCA coverage (PSD2 97(1))

- Login, every electronic payment initiation, and every risky remote action (new payee, limit or address change, credential reset, device enrolment) requires SCA or a documented exemption.
- No path skips SCA through a fallback, retry, alternative API version, or a "remember me" token that outlives the RTS limits.

### Elements and independence (RTS 6-9)

- Two elements from different categories; an email address, user ID or static card details count as neither knowledge nor possession.
- Possession is bound to a device or key (device binding, signed challenge, hardware token), not to a value any party can copy.
- On a phone used for both factors, the app uses a secure execution environment (Secure Enclave, StrongBox or TEE keys), detects tampering or rooting, and protects the factors from each other.
- SMS OTP and recovery flows: the reset path itself requires SCA or an equivalent check.

### Authentication code and sessions (RTS 4)

- Codes are single-use, unpredictable, expire quickly, and failure messages do not reveal which element failed.
- At most five consecutive failed attempts before a block; the user is alerted before a block becomes permanent and has a secure recovery path.
- Online account sessions end after at most five minutes of inactivity.

### Dynamic linking (PSD2 97(2); RTS 5)

- The amount and payee the user approves are shown in the authentication step itself (the app screen, the 3-D Secure challenge), not only on the merchant page.
- The authentication code is cryptographically bound to amount and payee (a signature over both, or an equivalent transaction-binding mechanism), and the server rejects execution when either differs.
- Batch payments bind to the total and the payee list; card holds bind to the consented amount.

### Exemptions (RTS 10-18)

- Each exemption check enforces its exact thresholds and counters, resetting only on a completed SCA; cumulative counters persist across sessions and channels.
- TRA (Art. 18) runs in real time on the Art. 18(2)(c) risk signals, and the code reads the applicable exemption threshold value from configuration tied to the current fraud rate.
- Recurring and trusted-beneficiary exemptions require SCA when the series or list is created or changed, and compare amount and payee exactly.
- Merchant or acquirer code flags MIT, MOTO and exemption requests correctly in the 3-D Secure or authorization message, and handles a soft decline by stepping up to SCA.
- Every exempted transaction still passes through transaction monitoring (Art. 2).

### Credentials (PSD2 97(3); RTS 22-27)

- Credentials are masked on entry, never logged or stored in plaintext, and created, delivered, renewed and revoked through secure, logged procedures.
- Activation of a new device or credential is tied to the identified user.

### Open-banking interface, ASPSP side (RTS 30-36; PSD2 66, 67, 68)

- TPPs are identified by a validated eIDAS qualified certificate; the code checks issuer, validity, revocation and the PSD2 roles and registration number in it.
- AISPs and PISPs can rely on the ASPSP's SCA (redirect, decoupled or embedded) without extra registration, consent re-checks or mandatory redirection (RTS 32(3)).
- Art. 10a: account-information calls through an AISP skip SCA within the 180-day window; refreshes without the user present are capped at four per 24 hours unless agreed (36(5)).
- PISPs receive initiation and execution information and a yes or no funds confirmation; error responses explain the reason.
- Availability and performance are monitored against the customer interface, and fallback works unless an exemption was granted.

### TPP side (PSD2 66, 67; RTS 34-36)

- The TPP identifies itself on every call, keeps the user's credentials out of its own storage, and requests and stores only data its service needs.
- Consents are scoped, time-limited and revocable by the user.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing step-up middleware, the processor SDK's exemption and challenge parameters, the API gateway's mTLS policy. Note when a fix needs a policy or authority decision first (a TRA threshold, a fallback exemption).
