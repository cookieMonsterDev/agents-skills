---
name: fastify-docs
description: Official Fastify documentation, answered with links to the exact pages. Use for any Fastify question, including routes, plugins and encapsulation, hooks and the lifecycle, JSON Schema validation and serialization, TypeScript, serverless, or the @fastify ecosystem.
---

# Fastify Docs

Fastify APIs change across major versions, so ground each answer in the live docs at <https://fastify.dev/docs/latest/>, not memory, and link the exact page behind every claim.

Route Nest abstractions on the Fastify adapter to `nestjs-docs`, and raw Express middleware patterns to `expressjs-docs`. Third-party plugins outside the Ecosystem guide belong to their own docs unless the question turns on general Fastify plugin patterns.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `fastify.dev/docs/latest` with the user's exact terms plus Fastify vocabulary such as `fastify.register`, `fastify-plugin`, `schema`, `preHandler`, or `reply.send`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Breaking changes between majors: the migration guides.
- First steps: Getting Started and the Plugins Guide, before deep reference pages.
- Routing: the Routes reference, noting Fastify's routing trie behavior.
- Validation: Validation and Serialization, before AJV options.
- Plugins: tell encapsulation, decorators and `fastify-plugin` scope breaking apart.
- Hooks: map the hook to its lifecycle phase (`onRequest`, `preHandler`, and so on) with the Lifecycle and Hooks references.
- Ecosystem packages: the Ecosystem guide, for the official `@fastify/*` package.
- Serverless: the Serverless guide.

## Gotchas

- Structure Fastify apps as plugins and hooks; Express `app.use` middleware stacking semantics do not carry over.
- Decorators and routes registered inside a plugin stay in its encapsulated scope; `fastify-plugin` breaks that scope when they must be visible outside.
- Validate with JSON Schema, as the docs recommend.
- Match APIs to the user's Fastify major version (v3, v4 or v5) using the migration guides.
