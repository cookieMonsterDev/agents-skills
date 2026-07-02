---
name: scylladb-docs
description: Use when users ask how to install, configure, model, query, secure, scale, repair, monitor, migrate to, or troubleshoot ScyllaDB clusters, ScyllaDB Cloud, Alternator, CQL applications, shard-aware drivers, CDC, nodetool, cqlsh, Manager, Monitoring Stack, Operator, or DynamoDB-compatible APIs, especially when they need official ScyllaDB documentation, exact links, or docs-grounded guidance.
---

ScyllaDB questions are easy to answer from stale Cassandra memory or DynamoDB assumptions. Use this skill to ground answers in the official ScyllaDB documentation and return the closest authoritative page instead of generic wide-column or NoSQL advice.

## When to Use

Use this skill when the request is about:

- ScyllaDB concepts, architecture, shards, and Cassandra compatibility
- Getting started, installation, configuration, and cluster creation
- CQL syntax, schema design, query patterns, and ScyllaDB extensions
- Data modeling, large partitions, and query-first design
- Alternator: DynamoDB-compatible API behavior in ScyllaDB
- Shard-aware drivers for CQL and DynamoDB APIs
- Security: authentication, authorization, RBAC, and encryption in transit
- Cluster operations: repair, compaction, topology changes, and nodetool
- Change Data Capture (CDC), consistency, and lightweight transactions (LWT)
- ScyllaDB Cloud, Manager, Monitoring Stack, Operator, and Migrator
- Migration from Cassandra or DynamoDB to ScyllaDB
- Troubleshooting startup, cluster, schema, and performance issues

Do not use this skill for:

- Amazon DynamoDB managed service behavior. Use `aws-dynamodb-docs` instead.
- Open-source Apache Cassandra docs when the question is not about ScyllaDB compatibility or differences. Use `cassandra-docs` instead.
- MongoDB, Redis, or relational database questions unless the question is specifically about ScyllaDB integration docs.
- Third-party managed Cassandra offerings unless the question maps to documented ScyllaDB behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and installation
- CQL, schema, and application development
- Data modeling and performance
- Alternator and DynamoDB API compatibility
- Drivers and client integration
- Security and access control
- Cluster management and operations
- CDC, consistency, and architecture
- ScyllaDB Cloud, Manager, Monitoring, and Operator
- Migration from Cassandra or DynamoDB
- Troubleshooting and knowledge base

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official ScyllaDB docs first

- Treat `docs.scylladb.com` as the source of truth for ScyllaDB.
- Prefer pages under <https://docs.scylladb.com/stable/> unless the user names a specific version.
- Distinguish open-source ScyllaDB, ScyllaDB Cloud, Alternator, and supporting product docs before answering.
- Search with the user's exact terms plus focused ScyllaDB phrases such as `shard-aware driver`, `Alternator`, `LWT`, `CDC`, `large partitions`, or `nodetool`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For DynamoDB API questions in ScyllaDB, prefer Alternator docs over AWS DynamoDB docs.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For compatibility questions, check ScyllaDB and Apache Cassandra compatibility docs before assuming identical behavior.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact ScyllaDB docs links, not just the docs homepage.
- Only provide CQL, YAML, or nodetool examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to ScyllaDB docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example CQL, configuration, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started before deep reference pages.
- For modeling questions, prefer data modeling and large partition docs before inventing relational schemas.
- For CQL syntax, prefer CQL reference pages before guessing from Cassandra or SQL memory.
- For DynamoDB API on ScyllaDB, route to Alternator docs and compatibility notes.
- For driver questions, prefer shard-aware ScyllaDB driver docs over generic Cassandra drivers.
- For operations questions, prefer cluster management procedures and nodetool docs.
- For migration questions, check Migration Assistant and Cassandra compatibility docs.
- Note ScyllaDB-specific differences from Cassandra, especially around LWT, tablets, and Alternator write isolation.

## Common Mistakes

- Answering from Apache Cassandra or DynamoDB docs when ScyllaDB behavior differs
- Linking the ScyllaDB docs homepage when a narrower Alternator, CQL, or operations page exists
- Recommending generic Cassandra drivers without checking shard-aware ScyllaDB driver guidance
- Treating Alternator as full DynamoDB parity without checking compatibility docs
- Ignoring large partition and tombstone compaction guidance in performance answers
- Mixing ScyllaDB Cloud console behavior with open-source ScyllaDB docs without clarification
- Assuming LWT semantics match Cassandra without checking ScyllaDB LWT docs

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live ScyllaDB docs as the final authority.
