---
name: nestjs-docs
description: Use when users ask how to build, explain, configure, secure, test, deploy, or troubleshoot NestJS applications, including modules, controllers, providers, dependency injection, middleware, guards, pipes, interceptors, exception filters, configuration, databases, validation, caching, queues, GraphQL, microservices, WebSockets, OpenAPI/Swagger, CLI, or platform adapters (Express/Fastify), especially when they need official NestJS documentation, exact links, or docs-grounded TypeScript guidance.
---

NestJS questions are easy to answer from stale memory or generic Node.js advice. Use this skill to ground answers in the official NestJS documentation and return the closest authoritative page instead of improvising framework patterns.

## When to Use

Use this skill when the request is about:

- NestJS concepts, architecture, terminology, or project structure
- Modules, controllers, providers, services, and dependency injection
- Middleware, guards, pipes, interceptors, exception filters, and custom decorators
- Request lifecycle, execution context, or scoping (global, controller, route)
- Configuration, environment variables, and dynamic modules
- Databases, ORMs, validation, serialization, caching, queues, and task scheduling
- Authentication, authorization, CORS, Helmet, CSRF, rate limiting, and encryption
- GraphQL, microservices, WebSockets, and hybrid applications
- OpenAPI/Swagger documentation and API design with `@nestjs/swagger`
- Testing, CLI scaffolding, deployment, serverless, and performance tuning
- Express or Fastify as the underlying HTTP platform (`@nestjs/platform-express`, `@nestjs/platform-fastify`)

Do not use this skill for:

- Raw Express or Fastify usage without NestJS abstractions. Use `expressjs-docs` or `fastify-docs` instead.
- Angular frontend questions unless the user is asking about shared Nest/Angular patterns in the NestJS docs.
- Third-party package behavior not covered by NestJS docs unless the docs explicitly reference that package.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started or first steps
- Core fundamentals (modules, controllers, providers, DI)
- Request pipeline (middleware, guards, pipes, interceptors, filters)
- Techniques (configuration, database, validation, caching, queues, etc.)
- Security and authentication
- GraphQL, microservices, or WebSockets
- OpenAPI/Swagger
- CLI, testing, deployment, or FAQ
- Recipes and integration patterns

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official NestJS docs first

- Treat `docs.nestjs.com` as the source of truth for NestJS.
- Prefer pages under <https://docs.nestjs.com/>.
- Search with the user's exact terms plus focused NestJS phrases such as `CanActivate`, `ValidationPipe`, `NestFactory`, `SwaggerModule`, or `Transport`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For lifecycle or ordering questions, check the request lifecycle FAQ before answering from memory.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact NestJS docs links, not just the docs homepage.
- Only provide TypeScript examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to NestJS docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer First Steps and fundamentals before deep technique pages.
- For DI questions, prefer providers, custom providers, and injection scopes docs.
- For validation questions, prefer pipes and the validation technique page before guessing `class-validator` setup.
- For auth questions, distinguish authentication (who you are) from authorization (what you can do).
- For OpenAPI questions, start with the OpenAPI introduction, then decorators or operations as needed.
- For microservice questions, distinguish message patterns, event patterns, and HTTP gateways.
- For platform-specific behavior, check whether the user is on Express or Fastify and consult the platform section in First Steps.

## Common Mistakes

- Answering from memory without verifying the current NestJS docs
- Linking the NestJS docs landing page when a narrower page exists
- Confusing middleware order with guard/pipe/interceptor order in the request lifecycle
- Suggesting Express-only patterns when the user is on the Fastify adapter (or vice versa)
- Mixing up `@nestjs/swagger` decorators with framework-agnostic OpenAPI concepts
- Treating third-party ORM or queue library APIs as NestJS core behavior without checking the relevant technique or recipe page

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live NestJS docs as the final authority.
