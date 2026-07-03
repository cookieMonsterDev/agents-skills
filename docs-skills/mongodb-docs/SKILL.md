---
name: mongodb-docs
description: Use when users ask how to deploy, connect to, query, model, index, aggregate, secure, scale, back up, monitor, or troubleshoot MongoDB databases and applications, including Atlas, Community Edition, Enterprise Advanced, CRUD, the aggregation framework, search, vector search, transactions, change streams, replication, sharding, drivers, Compass, or data modeling, especially when they need official MongoDB documentation, exact links, or docs-grounded guidance.
---

MongoDB questions are easy to answer from stale memory or SQL-centric assumptions. Use this skill to ground answers in the official MongoDB documentation and return the closest authoritative page instead of generic NoSQL advice.

## When to Use

Use this skill when the request is about:

- MongoDB concepts, documents, collections, and databases
- Getting started with Atlas, Community Edition, or local development
- CRUD operations, queries, updates, and deletes
- Indexes, query optimization, and explain plans
- Data modeling, schema design, and embedding vs referencing
- Aggregation pipelines and analytics patterns
- MongoDB Search, Atlas Search, and Vector Search
- Transactions, change streams, and time series collections
- Replication, sharding, and deployment architecture
- Security, authentication, authorization, and encryption
- Client libraries and language drivers
- Atlas administration, backups, monitoring, and scaling
- Tools: Compass, Atlas CLI, Charts, and Migrator

Do not use this skill for:

- Raw AWS DocumentDB console operations when the question is provider-specific rather than MongoDB behavior. Use `aws-cli-docs` for AWS CLI commands.
- PostgreSQL SQL, schemas, or relational modeling. Use the appropriate `postgresql-*-docs` skill instead.
- Redis caching or BullMQ job queues. Use `redis-docs` or `bullmq-docs` instead.
- Kafka change data capture unless the question is specifically about MongoDB stream processing documented by MongoDB.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and deployment choice
- Development: CRUD, queries, indexes, and modeling
- Aggregation, search, and vector features
- Transactions, change streams, and streaming data
- Management: security, backup, scaling, and monitoring
- Client libraries and application integration
- Atlas cloud operations and architecture guidance
- Server administration for self-managed deployments

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section. For broader discovery, the live docs index is at <https://www.mongodb.com/docs/llms.txt>. Markdown versions of pages are available by appending `.md` to URL paths.

### 2. Search official MongoDB docs first

- Treat `mongodb.com/docs` as the source of truth for MongoDB.
- Prefer pages under <https://www.mongodb.com/docs/>.
- Distinguish Atlas docs, Development docs, and self-managed server docs before answering.
- Search with the user's exact terms plus focused MongoDB phrases such as `aggregation pipeline`, `$lookup`, `compound index`, `replica set`, `change stream`, or `vector search`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For driver API questions, prefer the language-specific driver docs under Client Libraries.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For shell examples, check whether the user is on Atlas, local deployment, or self-managed server.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact MongoDB docs links, not just the docs homepage.
- Only provide query or driver code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to MongoDB docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example queries or driver code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Get Started before the full manual.
- For query behavior, prefer CRUD and manual reference pages before guessing syntax.
- For performance questions, check indexes and explain output docs before recommending schema changes.
- For Atlas questions, open Atlas docs rather than self-managed install guides.
- For AI and RAG questions, check Vector Search and AI Integrations docs.
- For driver questions, route by language under Client Libraries.

## Common Mistakes

- Answering from memory without verifying the current MongoDB docs
- Linking the MongoDB docs homepage when a narrower Atlas, manual, or driver page exists
- Treating MongoDB as schema-less without checking data modeling guidance
- Mixing Atlas-only features with Community Edition capabilities
- Recommending unindexed regex or `$where` queries without checking performance docs
- Confusing MongoDB Search with Atlas Vector Search feature boundaries

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live MongoDB docs as the final authority.
