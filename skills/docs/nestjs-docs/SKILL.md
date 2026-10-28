---
name: nestjs-docs
description: Official NestJS documentation, answered with links to the exact pages. Use for any NestJS question, including modules and dependency injection, guards, pipes and interceptors, GraphQL, microservices, OpenAPI, Express or Fastify adapters, or NestJS 12 migration.
---

# NestJS Docs

NestJS 12 breaks many NestJS 11 assumptions, so ground each answer in the live docs at <https://docs.nestjs.com/>, not memory, and link the exact page behind every claim.

Route raw Express usage without Nest abstractions to `expressjs-docs`, and raw Fastify usage to `fastify-docs`. Angular frontend questions and third-party packages belong to their own docs unless the NestJS docs cover them.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.nestjs.com` with the user's exact terms plus NestJS vocabulary such as `CanActivate`, `ValidationPipe`, `NestFactory`, `SwaggerModule`, or `Transport`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and TypeScript examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: the NestJS 12 docs at <https://docs.nestjs.com/> by default; <https://docs.nestjs.com/v11> only when the user needs NestJS 11.
- Upgrades and version differences: the migration guide.
- Lifecycle or ordering: the request lifecycle FAQ.
- First steps: First Steps and the fundamentals, before technique pages.
- Dependency injection: providers, custom providers and injection scopes.
- Validation: pipes and the validation technique page; on NestJS 12, check whether the page uses Standard Schema (`StandardSchemaValidationPipe`, route `schema` options) or `class-validator`.
- Auth: keep authentication (who you are) apart from authorization (what you can do).
- OpenAPI: the OpenAPI introduction, then its decorators or operations pages.
- Microservices: tell message patterns, event patterns and HTTP gateways apart.
- Platform behavior: confirm Express or Fastify, then the platform section of First Steps.
- Module system or test runner: confirm whether the project is ESM or CommonJS first.
- Third-party ORM or queue libraries: the relevant application, data or recipe page.

## Gotchas

- NestJS 12 packages ship as ESM; ESM projects default to Vitest, and CommonJS projects keep Jest.
- Answer with NestJS 12 behavior; CommonJS-only packages, Jest as the default runner, `subscriptions-transport-ws`, the legacy Terminus health indicator API and inherited `@Optional()` constructor parameters are NestJS 11 assumptions.
- Middleware runs as its own stage, separate from the guard, interceptor and pipe order; take the full order from the request lifecycle FAQ.
- Match platform code to the user's adapter, Express or Fastify.
- `@nestjs/swagger` decorators are Nest-specific, separate from framework-agnostic OpenAPI concepts.
- Third-party ORM and queue APIs belong to those libraries, not NestJS core.
