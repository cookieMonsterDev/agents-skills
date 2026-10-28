# Code review checklist

Use this checklist for websites, web apps, mobile apps and SDKs, tag manager containers, server-side tagging, CMP configuration and marketing systems. Code shows what can fire; only a scan of the running build shows what does fire and when. Run both when you can, and record which one each finding rests on.

For a diff or pull request, review the changed tags, SDKs, storage keys and marketing sends, and their consent gating. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover storage and access

Search the code first. Read every hit in context, since names alone produce false positives.

```bash
# Direct device storage and access
rg -n '(document\.cookie|localStorage|sessionStorage|indexedDB|caches\.open|navigator\.(userAgentData|hardwareConcurrency|deviceMemory)|getContext\(.webgl|toDataURL|AudioContext|SharedPreferences|UserDefaults|Keychain|ASIdentifierManager|AdvertisingIdClient|identifierForVendor)'

# Tags, pixels and SDKs
rg -n -i '(gtag|googletagmanager|google-analytics|doubleclick|fbq|connect\.facebook|tiktok|linkedin|snap\.licdn|hotjar|clarity\.ms|segment|mixpanel|amplitude|appsflyer|adjust|branch\.io|firebase|braze|onesignal|sentry)'

# Consent plumbing
rg -n -i '(__tcfapi|__gpp|tcString|gdprApplies|consent\(.(default|update)|ad_storage|analytics_storage|ad_user_data|ad_personalization|onetrust|cookiebot|didomi|usercentrics|consentmanager|iubenda)'
```

Then scan the running build in a fresh browser profile with an EEA locale and IP, in three passes: no interaction, after "reject all", after "accept all". In each pass record cookies, web storage, IndexedDB and every network request to a third-party host. A Playwright sketch:

```js
const ctx = await browser.newContext({ locale: "de-DE" });
const page = await ctx.newPage();
const requests = [];
page.on("request", (r) => requests.push(r.url()));
await page.goto(SITE_URL, { waitUntil: "networkidle" });
const cookies = await ctx.cookies();
const storage = await page.evaluate(() => ({ ...localStorage }));
// Store names, domains and lifetimes only; drop values before writing the report.
```

For mobile apps, route traffic through an intercepting proxy on a clean install and record requests and SDK initialisation before the consent prompt is answered. Repeat for withdrawal: change the choice and confirm the next page load stops the tags.

Done when the inventory in SKILL.md step 2 has a row for every cookie, storage key, SDK identifier and third-party request observed, with the pass in which it first appeared.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Consent before load (Art. 5(3))

- Nothing beyond strictly necessary operations appears in the no-interaction pass: no analytics or advertising cookies, no pixel requests, no SDK identifiers read, no fingerprinting calls.
- Third-party scripts are blocked until consent (script `type="text/plain"` with a CMP data attribute, a tag-manager consent trigger, or deferred SDK initialisation), not merely hidden after loading.
- The reject pass matches the no-interaction pass; any extra operation after "reject all" is a High finding.
- Mobile SDKs start with collection disabled (for example Firebase Analytics collection flags, ad ID collection off) and enable per purpose after consent.

### Strictly necessary exemption (Art. 5(3))

- Each exempt operation serves a function the user requested: session, load balancing, security, cart, the consent record itself, user-chosen preferences.
- Each exempt cookie has a lifetime matched to its function and carries no cross-site or advertising use.
- Analytics claimed as exempt meets the specific national conditions (CNIL audience measurement: first party, aggregated statistics only, limited lifetime, no cross-site tracking); otherwise it needs consent.

### CMP and consent signals (Art. 5(3); GDPR 7)

- Consent is stored per purpose with timestamp, banner version and choices, so it can be proven; the record holds a pseudonymous ID, not an email.
- TCF: the CMP is registered, the TC string reflects the user's choices, vendors read it through `__tcfapi` before acting, and purposes relying on legitimate interest are checked against national guidance. Check the current TCF policy version.
- Choices persist only as long as national guidance allows (CNIL suggests re-asking after about six months), and refusal is remembered as long as acceptance.
- Withdrawal is reachable from every page and takes effect without reload loops; consent-based cookies are removed on withdrawal.

### Google Consent Mode (Art. 5(3))

- `gtag('consent', 'default', {...})` sets `ad_storage`, `analytics_storage`, `ad_user_data` and `ad_personalization` to `denied` before any Google tag fires, and `update` runs only from the CMP callback.
- Basic mode (tags blocked until consent) is the reference setup. Advanced mode sends cookieless pings before consent; those requests still trigger access to device information (EDPB Guidelines 2/2023), so record them as a finding or a needs-information item for counsel.
- Region-specific defaults cover every EEA country the service targets.

### Server-side tagging (Art. 5(3); GDPR)

- Moving tags to a server container does not remove consent needs: the client script that sets first-party identifiers or sends events is still storage or access, so it waits for consent.
- The server container forwards to vendors only the events and fields consent covers, and drops identifiers on refusal.

### Fingerprinting and other techniques (Art. 5(3))

- Canvas, WebGL, audio, font or device-attribute collection for identification needs consent like a cookie.
- Link decoration and URL parameters (`gclid`, `fbclid`, custom IDs) read for tracking, tracking pixels in emails, and IP-plus-user-agent identification count as access (EDPB Guidelines 2/2023).

### Electronic marketing (Art. 13)

- Each email, SMS or push campaign audience is filtered by a consent flag or a soft opt-in flag tied to the purchase it relied on.
- Every message carries the sender identity and a working one-step unsubscribe, honoured promptly across all sending systems.
- Purchased or scraped lists without consent records are a High finding.

### Traffic and location data (Art. 6, 9)

- For communications services: traffic data is deleted or anonymised on a schedule tied to transmission and billing; location data for value-added services needs consent with a per-session off switch.

## 3. Map findings to fixes

Give fixes in the stack's own idiom: the CMP's blocking attribute, a tag-manager consent check, an SDK's collection flag, a list filter in the email platform. Note when a fix needs a decision first (a national exemption claim, a soft opt-in policy).
