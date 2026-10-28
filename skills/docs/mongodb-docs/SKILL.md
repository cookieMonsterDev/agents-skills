---
name: mongodb-docs
description: Official MongoDB documentation, answered with links to the exact pages. Use for any MongoDB question, including CRUD and data modeling, indexes, aggregation, Search and Vector Search, transactions and change streams, replication and sharding, drivers, or Atlas.
---

# MongoDB Docs

MongoDB features differ between Atlas, Community Edition and Enterprise Advanced and shift across releases, so ground each answer in the live docs at <https://www.mongodb.com/docs/>, not memory, and link the exact page behind every claim.

Route AWS CLI commands to `aws-cli-docs`, PostgreSQL to `postgresql-16-docs`, `postgresql-17-docs` or `postgresql-18-docs` by version, Redis caching to `redis-docs`, BullMQ job queues to `bullmq-docs`, and Kafka change data capture to `kafka-docs` unless it is MongoDB stream processing. Amazon DocumentDB console operations belong to AWS's own docs unless the question turns on MongoDB behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `mongodb.com/docs` with the user's exact terms plus MongoDB vocabulary such as `aggregation pipeline`, `$lookup`, `compound index`, `replica set`, `change stream`, or `vector search`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and query or driver code only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Deployment: tell Atlas docs, Development docs, and self-managed server docs apart; Atlas questions go to Atlas docs, not self-managed install guides.
- Shell examples: confirm whether the user runs Atlas, a local deployment, or a self-managed server.
- Driver questions: the language-specific driver docs under Client Libraries.
- Performance: the indexes and explain-output docs, before recommending schema changes.
- AI and RAG: the Vector Search and AI Integrations docs.
- Discovery beyond the map: the live index at <https://www.mongodb.com/docs/llms.txt>; append `.md` to a page path for its Markdown version.

## Gotchas

- Ground schema advice in the data modeling docs; MongoDB collections are flexible, not schema-less.
- Confirm a feature is available outside Atlas before offering it to Community Edition users.
- Check the performance docs before recommending unindexed regex or `$where` queries.
- Keep MongoDB Search and Atlas Vector Search feature boundaries apart.
