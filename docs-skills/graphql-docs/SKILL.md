---
name: graphql-docs
description: Use when users ask how to design, query, mutate, subscribe to, validate, secure, deploy, or troubleshoot GraphQL APIs, including schemas and types, queries and mutations, subscriptions, resolvers, validation, execution, responses, introspection, HTTP transport, authorization, pagination, federation, performance, security, or schema evolution, especially when they need official GraphQL documentation, exact links, or docs-grounded guidance from graphql.org.
---

GraphQL questions are easy to answer from stale memory or REST-centric assumptions. Use this skill to ground answers in the official GraphQL documentation at graphql.org and return the closest authoritative page instead of generic API advice.

## When to Use

Use this skill when the request is about:

- GraphQL concepts, terminology, and how GraphQL compares to REST
- Schema definition language (SDL), types, fields, arguments, and nullability
- Queries, mutations, subscriptions, variables, fragments, aliases, and directives
- Validation rules, execution, resolvers, and response formats (`data`, `errors`, `extensions`)
- Introspection, `__typename`, and schema exploration
- Serving GraphQL over HTTP, request/response formats, and status codes
- Authorization, pagination, schema design, and global object identification
- Caching, performance (N+1, batching, DataLoader), and security
- Federation, subgraphs, gateways, and composite schemas
- Building robust clients that handle schema evolution
- GraphQL.js, the specification, and FAQ topics on graphql.org

Do not use this skill for:

- NestJS GraphQL module setup and decorators. Use `nestjs-docs` instead.
- Apollo Server, Yoga, Hasura, or other vendor-specific server docs unless graphql.org links to them.
- Raw Express or Fastify HTTP setup without GraphQL context. Use `expressjs-docs` or `fastify-docs` instead.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Schemas, types, and SDL
- Operations (queries, mutations, subscriptions)
- Request lifecycle (validation, execution, response)
- Introspection and tooling
- Best practices (HTTP, auth, pagination, schema design)
- Performance, caching, and security
- Federation and distributed schemas
- Client robustness and schema evolution
- Specification and FAQ

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official GraphQL docs first

- Treat `graphql.org/learn` as the source of truth for GraphQL concepts and best practices.
- Prefer pages under <https://graphql.org/learn/>.
- For specification details, use <https://spec.graphql.org/>.
- For GraphQL.js reference material, use <https://graphql.org/graphql-js/>.
- Search with the user's exact terms plus focused GraphQL phrases such as `resolver`, `selection set`, `Non-Null`, `@include`, or `node(id:)`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For HTTP transport questions, check Serving over HTTP and debug-errors before answering from memory.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact GraphQL docs links, not just the docs homepage.
- Only provide schema or query examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to GraphQL docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example schema or query, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Introduction and Schemas and Types before deep best-practice pages.
- For query syntax questions, prefer Queries before guessing operation structure.
- For write operations, distinguish mutations (serial top-level fields) from queries (parallel field resolution).
- For real-time data, prefer Subscriptions and note transport is implementation-specific (often WebSockets).
- For HTTP questions, prefer Serving over HTTP and debug-errors over generic REST guidance.
- For auth questions, distinguish authentication (middleware, before validation) from authorization (business logic during execution).
- For pagination, check the Pagination lesson before recommending Relay-style connections blindly.
- For performance, check Performance and Caching; mention N+1 and batching when resolver patterns are involved.
- For distributed APIs, check Federation before suggesting monolithic schema splits.

## Common Mistakes

- Answering from memory without verifying the current graphql.org docs
- Linking the graphql.org homepage when a narrower learn page exists
- Treating GraphQL as a database query language instead of an API query language
- Confusing validation errors (no `data` key) with field errors (partial `data` with `errors`)
- Placing authorization only in resolvers instead of delegating to the business logic layer
- Assuming subscriptions use HTTP like queries and mutations
- Recommending introspection in production without noting security trade-offs
- Using REST versioning patterns when GraphQL favors continuous schema evolution

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live GraphQL docs as the final authority.
