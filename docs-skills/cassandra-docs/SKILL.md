---
name: cassandra-docs
description: Use when users ask how to install, configure, model, query, index, secure, scale, repair, compact, back up, monitor, or troubleshoot Apache Cassandra clusters and CQL applications, including keyspaces, tables, partition keys, clustering columns, SAI, secondary indexes, replication, compaction, nodetool, cqlsh, vector search, CDC, or the native protocol, especially when they need official Apache Cassandra documentation, exact links, or docs-grounded guidance.
---

Apache Cassandra questions are easy to answer from stale memory or relational-database assumptions. Use this skill to ground answers in the official Apache Cassandra documentation and return the closest authoritative page instead of generic wide-column or NoSQL advice.

## When to Use

Use this skill when the request is about:

- Cassandra concepts: keyspaces, tables, partitions, clustering keys, and replicas
- Getting started, installation, configuration, and production recommendations
- CQL syntax, DDL, DML, data types, functions, operators, and security
- Data modeling: query-first design, denormalization, and physical modeling
- Storage Attached Indexing (SAI) and secondary indexes (2i)
- Vector search, materialized views, and JSON support
- Replication, consistency levels, snitches, and topology changes
- Compaction, repair, hints, backups, and CDC
- Security, authentication, authorization, and audit logging
- Tools: cqlsh, nodetool, SSTable tools, and cassandra-stress
- Architecture, storage engine, and native protocol behavior
- Troubleshooting cluster health, performance, and misbehaving nodes

Do not use this skill for:

- ScyllaDB-specific features, Alternator, or shard-aware drivers. Use `scylladb-docs` instead.
- Amazon DynamoDB tables, items, or GSIs. Use `aws-dynamodb-docs` instead.
- MongoDB documents or aggregation pipelines. Use `mongodb-docs` instead.
- DataStax Enterprise or Astra features unless the question maps to open-source Cassandra docs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and installation
- Architecture and core concepts
- Data modeling and schema design
- CQL language and reference
- Indexing: SAI and secondary indexes
- Vector search
- Configuration and operating procedures
- Replication, repair, and compaction
- Security and auditing
- Tools and administration
- Troubleshooting and FAQ
- Reference and native protocol

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Apache Cassandra docs first

- Treat `cassandra.apache.org/doc` as the source of truth for Apache Cassandra.
- Prefer pages under <https://cassandra.apache.org/doc/latest/>.
- If the user names a specific Cassandra version, switch the docs version selector path when needed.
- Search with the user's exact terms plus focused Cassandra phrases such as `partition key`, `clustering column`, `SAI`, `compaction`, `repair`, `consistency level`, or `nodetool`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For CQL syntax questions, prefer the CQL reference before guessing from SQL or DynamoDB patterns.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish SAI from legacy secondary indexes before recommending index types.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Apache Cassandra docs links, not just the docs homepage.
- Only provide CQL, `cassandra.yaml`, or nodetool examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Apache Cassandra docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example CQL or configuration, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started and the quickstart before deep reference pages.
- For modeling questions, prefer data modeling docs before inventing relational schemas.
- For query behavior, prefer CQL DDL/DML and indexing docs before guessing syntax.
- For performance questions, check compaction, large partition, and production recommendation docs.
- For index questions, route to SAI docs for modern indexing and 2i docs for legacy secondary indexes.
- For operations questions, prefer operating and nodetool docs before ad hoc repair advice.
- For vector search questions, open vector search docs rather than generic CQL pages.

## Common Mistakes

- Answering from memory without verifying the current Apache Cassandra docs
- Linking the Cassandra docs homepage when a narrower CQL or operations page exists
- Designing schemas around JOINs or ad hoc filters instead of query-driven modeling
- Confusing SAI with legacy secondary indexes or treating them as interchangeable
- Recommending `ALLOW FILTERING` or unbounded scans without checking performance guidance
- Mixing ScyllaDB-only behavior with Apache Cassandra docs
- Ignoring consistency level and replication factor interactions in read/write advice

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Apache Cassandra docs as the final authority.
