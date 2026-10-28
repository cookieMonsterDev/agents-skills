---
name: expressjs-docs
description: Official Express.js documentation, answered with links to the exact pages. Use for any Express question, including routing and the Router, middleware, error handling, request and response APIs, Express 5 migration, or production security and performance.
---

# Express.js Docs

Express 5 changed route syntax and async error handling from Express 4, so ground each answer in the live docs at <https://expressjs.com/en/>, not memory, and link the exact page behind every claim.

Route NestJS abstractions built on Express to `nestjs-docs`, and Fastify APIs or plugin architecture to `fastify-docs`. Third-party middleware belongs to its own docs unless the question turns on Express middleware integration.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `expressjs.com/en` with the user's exact terms plus Express vocabulary such as `app.use`, `next(err)`, `Router`, `res.send`, or `path-to-regexp`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: the Express 5.x docs by default; Express 4 pages only when the user needs Express 4.
- Breaking changes: the Express 4 to 5 migration guide.
- First steps: Getting Started and basic routing, before API reference pages.
- Route syntax: the routing guide, for path-to-regexp v8 wildcard and optional segment syntax.
- Middleware: tell application-level `app.use` from router-level middleware.
- Errors: the error handling guide.
- API methods: the 5.x API reference for Application, Request, Response and Router.
- Production: the advanced guides on health checks, graceful shutdown, performance and security.
- Middleware packages: the official Middleware section, before alternatives.

## Gotchas

- Write routes in Express 5's path-to-regexp v8 syntax; Express 4 forms such as `:param?` and `*` changed.
- Express 5 forwards rejected promises from handlers to `next` automatically.
- Error-handling middleware takes four arguments, `(err, req, res, next)`, and goes after the routes.
- Express is intentionally minimal and leaves project structure to the user.
