---
name: fastify-docs
description: Use when users ask how to build, explain, configure, extend, validate, test, deploy, or troubleshoot Fastify HTTP servers, including routes, plugins, hooks, decorators, lifecycle, JSON Schema validation, serialization, logging, middleware, TypeScript, serverless, or the @fastify ecosystem, especially when they need official Fastify documentation, exact links, or docs-grounded JavaScript/TypeScript guidance.
---

Fastify questions are easy to answer from stale memory or Express-centric assumptions. Use this skill to ground answers in the official Fastify documentation and return the closest authoritative page instead of generic Node.js HTTP advice.

## When to Use

Use this skill when the request is about:

- Fastify concepts, architecture, plugins, and encapsulation
- Server creation, configuration, routing, and the request lifecycle
- Request and reply objects, hooks, decorators, and error handling
- JSON Schema validation, serialization, and content-type parsing
- Plugins, `fastify-plugin`, encapsulation scopes, and the `@fastify/*` ecosystem
- Logging, middleware (Express-style), HTTP/2, and TypeScript support
- Testing with `inject()`, serverless deployment, and production recommendations
- Migration between Fastify major versions

Do not use this skill for:

- NestJS with the Fastify adapter unless the question is about underlying Fastify APIs. Use `nestjs-docs` for Nest abstractions.
- Raw Express middleware patterns without Fastify context. Use `expressjs-docs` instead.
- Third-party plugins not documented in the Fastify ecosystem guide unless the user needs general Fastify plugin patterns.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started or introductory guides
- Core reference (server, routes, request, reply)
- Lifecycle, hooks, and plugins
- Validation, serialization, and parsers
- Logging, errors, and middleware
- TypeScript and production operations
- Ecosystem plugins and serverless

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Fastify docs first

- Treat `fastify.dev/docs/latest` as the source of truth for the current Fastify release.
- Prefer pages under <https://fastify.dev/docs/latest/>.
- Search with the user's exact terms plus focused Fastify phrases such as `fastify.register`, `fastify-plugin`, `schema`, `preHandler`, or `reply.send`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For version-specific breaking changes, check the migration guides before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Fastify docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Fastify docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started and the Plugins Guide before deep reference pages.
- For routing questions, prefer the Routes reference and note Fastify's routing trie behavior.
- For validation questions, prefer Validation and Serialization before guessing AJV options.
- For plugin questions, distinguish encapsulation, decorators, and `fastify-plugin` scope breaking.
- For hook questions, map the hook to the correct lifecycle phase (onRequest, preHandler, etc.).
- For ecosystem package questions, check the Ecosystem guide for the official `@fastify/*` package.
- For serverless questions, prefer the Serverless guide over generic FaaS advice.

## Common Mistakes

- Answering from memory without verifying the current Fastify docs
- Linking the Fastify docs landing page when a narrower page exists
- Treating Fastify like Express (synchronous middleware stacking, `app.use` semantics)
- Forgetting encapsulation: decorators and routes registered in a plugin may not be visible outside its scope
- Suggesting validation patterns without JSON Schema when the docs recommend schema-based validation
- Mixing up Fastify v3/v4/v5 APIs without checking migration guides

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Fastify docs as the final authority.
