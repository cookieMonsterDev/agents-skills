---
name: graphql-docs
description: Official GraphQL documentation, answered with links to the exact pages. Use for any GraphQL question, including schemas and types, queries, mutations and subscriptions, validation and execution, serving over HTTP, pagination, or federation.
---

# GraphQL Docs

GraphQL answers drift toward REST-centric assumptions, so ground each answer in the live docs at <https://graphql.org/learn/>, not memory, and link the exact page behind every claim.

Route NestJS GraphQL module setup to `nestjs-docs`, and raw Express or Fastify HTTP setup to `expressjs-docs` or `fastify-docs`. Apollo Server, Yoga, Hasura and other vendor servers belong to their own docs unless graphql.org links to them.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `graphql.org/learn` with the user's exact terms plus GraphQL vocabulary such as `resolver`, `selection set`, `Non-Null`, `@include`, or `node(id:)`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and schema or query examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Specification details: <https://spec.graphql.org/>.
- GraphQL.js reference: <https://graphql.org/graphql-js/>.
- Beginner questions: Introduction and Schemas and Types, before the best-practice pages.
- Query syntax: the Queries page.
- Write operations: Mutations; top-level mutation fields run serially, while query fields resolve in parallel.
- Real-time data: Subscriptions.
- HTTP transport: Serving over HTTP and debug-errors.
- Auth: tell authentication (middleware, before validation) from authorization (business logic, during execution).
- Pagination: the Pagination lesson, before recommending Relay-style connections.
- Performance: Performance and Caching, covering N+1 and batching when resolver patterns are involved.
- Distributed APIs: Federation, before suggesting monolithic schema splits.

## Gotchas

- GraphQL is an API query language, not a database query language.
- Validation errors return no `data` key; field errors return partial `data` alongside `errors`.
- Delegate authorization to the business logic layer rather than placing it only in resolvers.
- Subscription transport is implementation-specific (often WebSockets), unlike queries and mutations over HTTP.
- Note the security trade-offs before recommending introspection in production.
- Evolve the schema continuously; GraphQL favors that over REST-style versioning.
