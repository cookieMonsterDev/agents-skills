---
name: stripe-docs
description: Use when users ask how to build, configure, integrate, test, secure, or troubleshoot Stripe payments, billing, subscriptions, Connect marketplaces, Checkout, Elements, webhooks, or the Stripe API, especially when they need official Stripe documentation, exact links, docs-grounded guidance, or the correct API/SDK behavior for handling money.
---

Stripe questions carry real financial and compliance risk if answered from stale memory, since API versions, webhook event names, and integration patterns change frequently. Use this skill to ground answers in the official Stripe documentation and return the closest authoritative page instead of generic payments advice.

## When to Use

Use this skill when the request is about:

- Payments: Payment Intents, Checkout, Elements, payment methods, and Terminal (in-person)
- Billing and revenue: subscriptions, invoices, usage-based pricing, tax, and the customer portal
- Connect: marketplace and platform payments, onboarding, charges, and payouts to connected accounts
- Webhooks: event types, signature verification, and idempotent event handling
- API usage: authentication, idempotency keys, error codes, versioning, and rate limits
- SDKs and client libraries for server-side and client-side integration
- Testing: test mode, test card numbers, the Stripe CLI, and webhook simulation
- Security and compliance: API key management, PCI scope, Radar fraud detection, and Identity verification
- Stripe Tax, Stripe Issuing, Stripe Treasury, and other adjacent Stripe products

Do not use this skill for:

- Generic e-commerce or checkout UX design unless the question is specifically about Stripe's prebuilt components (Checkout, Elements, Payment Links).
- Other payment processors (PayPal, Adyen, Braintree) unless the user is explicitly comparing them to Stripe.
- Tax law or accounting questions beyond what Stripe Tax or Stripe's revenue recognition docs directly document.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, development environment, and quickstarts
- Core payments (Payment Intents, Checkout, Elements, payment methods)
- Billing and subscriptions
- Connect (marketplaces and platforms)
- Webhooks and event handling
- API reference, authentication, and idempotency
- Testing and the Stripe CLI
- Security, compliance, and fraud prevention (Radar, Identity)

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Stripe docs first

- Treat `docs.stripe.com` as the source of truth for Stripe.
- Prefer pages under <https://docs.stripe.com/>.
- Every docs page also has a Markdown version at the same path with `.md` appended (for example `https://docs.stripe.com/payments.md`), which is useful for reading large pages efficiently.
- Search with the user's exact terms plus focused Stripe phrases such as `PaymentIntent`, `webhook signature`, `idempotency key`, `Connect account`, or `subscription schedule`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For exact request/response shapes, prefer the API reference over guide pages.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Stripe docs links, not just the docs homepage.
- Only provide API request or SDK code examples when the user asks for them or when the docs page makes an example necessary.
- Never fabricate API parameter names, webhook event names, or error codes; verify them against the API reference first.
- Make any inference explicit. Good phrasing:
  - `According to Stripe docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example API request or SDK code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer the quickstart and integration guides before the raw API reference.
- For payment-flow questions, distinguish Payment Intents (custom UI) from Checkout (hosted page) from Payment Links (no-code) from Elements (embeddable components).
- For subscription questions, prefer the Billing docs and distinguish subscription schedules from simple recurring prices.
- For marketplace questions, prefer Connect docs and confirm whether the integration is Standard, Express, or Custom accounts before giving onboarding steps.
- For webhook questions, always check the signature verification docs before writing handler code.
- For error-handling questions, prefer the API errors reference and the card decline codes page over generic HTTP status code assumptions.
- For security questions, distinguish publishable keys (client-side) from secret keys (server-side) and check current key-management guidance.

## Common Mistakes

- Answering from memory without verifying the current Stripe API version and docs
- Linking the Stripe docs homepage when a narrower product or API reference page exists
- Recommending secret API keys be used in client-side code
- Treating webhook events as guaranteed-ordered or guaranteed-once without checking idempotency and event-ordering docs
- Confusing test mode and live mode keys or data
- Mixing Connect (multi-account marketplace) concepts with single-account Billing or Payments concepts

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Stripe docs as the final authority.
