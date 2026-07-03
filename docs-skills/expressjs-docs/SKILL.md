---
name: expressjs-docs
description: Use when users ask how to build, explain, configure, route, secure, debug, migrate, or troubleshoot Express.js web applications and APIs, including middleware, routing, error handling, request/response objects, the Router, static files, templates, proxies, performance, security, graceful shutdown, or Express 5 migration, especially when they need official Express documentation, exact links, or docs-grounded JavaScript guidance.
---

Express questions are easy to answer from stale memory or outdated Express 4 patterns. Use this skill to ground answers in the official Express.js documentation and return the closest authoritative page instead of generic Node.js HTTP advice.

## When to Use

Use this skill when the request is about:

- Express concepts, middleware model, routing, and application structure
- `express()`, the application object, request/response objects, and `Router`
- Route paths, parameters, handlers, and HTTP method routing
- Writing and using middleware, including error-handling middleware
- Static files, template engines, and serving assets
- Error handling, debugging, and working behind proxies
- Database integration patterns documented by Express
- Express 5 migration, performance best practices, security, and graceful shutdown
- Official Express middleware packages (body-parser, cors, session, etc.)

Do not use this skill for:

- NestJS abstractions built on Express. Use `nestjs-docs` instead.
- Fastify-specific APIs or plugin architecture. Use `fastify-docs` instead.
- Third-party middleware behavior not covered by Express docs unless the question is about general Express middleware integration.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and installation
- Routing and route handlers
- Middleware (application-level and router-level)
- Request and response APIs
- Error handling and debugging
- Templates, static files, and proxies
- Migration (Express 4 to 5)
- Performance, security, and production operations
- Official middleware reference

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Express docs first

- Treat `expressjs.com/en` as the source of truth for Express.js.
- Prefer pages under <https://expressjs.com/en/>.
- Default to Express 5.x docs unless the user explicitly needs Express 4.
- Search with the user's exact terms plus focused Express phrases such as `app.use`, `next(err)`, `Router`, `res.send`, or `path-to-regexp`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Express 5 breaking changes, check the migration guide before answering from Express 4 knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Express docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Express docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started and basic routing before API reference pages.
- For routing questions, note Express 5 uses path-to-regexp v8; check the routing guide for wildcard and optional segment syntax.
- For middleware questions, distinguish application-level `app.use` from router-level middleware.
- For error questions, prefer the error handling guide and remember Express 5 auto-forwards rejected promises to `next`.
- For API method questions, use the 5.x API reference for Application, Request, Response, and Router.
- For production questions, prefer health checks, graceful shutdown, performance, and security advanced guides.
- For middleware package questions, check the official Middleware section before recommending alternatives.

## Common Mistakes

- Answering from memory without verifying the current Express docs
- Linking the Express homepage when a narrower page exists
- Using Express 4 route syntax (e.g. `:param?`, `*`) without checking Express 5 path-to-regexp changes
- Forgetting that error-handling middleware requires four arguments: `(err, req, res, next)`
- Placing error-handling middleware before routes instead of after them
- Treating Express as opinionated about project structure when it is intentionally minimal

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Express docs as the final authority.
