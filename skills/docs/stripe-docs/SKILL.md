---
name: stripe-docs
description: Official Stripe documentation, answered with links to the exact pages. Use for any Stripe question, including Payment Intents, Checkout and Elements, Billing and subscriptions, Connect, webhooks, testing, or the Stripe API.
---

# Stripe Docs

Stripe API versions, webhook event names and integration patterns change frequently, and mistakes cost real money, so ground each answer in the live docs at <https://docs.stripe.com/>, not memory, and link the exact page behind every claim.

Generic e-commerce or checkout UX belongs outside these docs unless it turns on Stripe's prebuilt components (Checkout, Elements, Payment Links). Other processors (PayPal, Adyen, Braintree) belong to their own docs unless the user is comparing them to Stripe, and tax law or accounting goes beyond these docs except where Stripe Tax or Stripe's revenue recognition docs cover it.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.stripe.com` with the user's exact terms plus Stripe vocabulary such as `PaymentIntent`, `webhook signature`, `idempotency key`, `Connect account`, or `subscription schedule`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and API requests or SDK code only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Large pages: append `.md` to any docs path (for example <https://docs.stripe.com/payments.md>) to read its Markdown version.
- Request and response shapes: the API reference, before guide pages.
- Payment flows: tell Payment Intents (custom UI) from Checkout (hosted page), Payment Links (no-code) and Elements (embeddable components).
- Subscriptions: the Billing docs, telling subscription schedules from simple recurring prices.
- Marketplaces: the Connect docs, after confirming Standard, Express or Custom accounts.
- Webhooks: the signature verification docs, before writing handler code.
- Errors: the API errors reference and the card decline codes page, over generic HTTP status codes.
- API keys: tell publishable keys (client-side) from secret keys (server-side), then check the current key-management guidance.

## Gotchas

- Verify API parameter names, webhook event names and error codes against the API reference before citing them.
- Confirm the user's Stripe API version before answering version-sensitive behavior.
- Keep secret API keys on the server; client-side code uses publishable keys.
- Check the idempotency and event-ordering docs before treating webhook events as ordered or delivered once.
- Keep test mode and live mode keys and data apart.
- Keep Connect (multi-account marketplace) concepts apart from single-account Billing or Payments.
