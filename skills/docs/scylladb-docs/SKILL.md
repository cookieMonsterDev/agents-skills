---
name: scylladb-docs
description: Official ScyllaDB documentation, answered with links to the exact pages. Use for any ScyllaDB question, including CQL and data modeling, Alternator (DynamoDB-compatible API), shard-aware drivers, cluster operations, ScyllaDB Cloud, Manager and Operator, or migration from Cassandra or DynamoDB.
---

# ScyllaDB Docs

ScyllaDB departs from Apache Cassandra and DynamoDB behavior in places, and its manual has moved to new paths, so ground each answer in the live docs at <https://docs.scylladb.com/manual/stable/>, not memory, and link the exact page behind every claim.

Route Amazon DynamoDB managed-service behavior to `aws-dynamodb-docs`, and Apache Cassandra questions that are not about ScyllaDB compatibility to `cassandra-docs`. Route MongoDB to `mongodb-docs` and Redis to `redis-docs` unless the question is about ScyllaDB integration. Third-party managed Cassandra offerings belong to their own docs unless the question turns on ScyllaDB behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.scylladb.com` with the user's exact terms plus ScyllaDB vocabulary such as `shard-aware driver`, `Alternator`, `LWT`, `CDC`, `large partitions`, or `nodetool`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and CQL, YAML or nodetool examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Paths: the server manual lives under `/manual/stable/` (pin a version when the user names one) and the get-started tutorials under <https://docs.scylladb.com/stable/get-started/>; replace older `/stable/operating-scylla/...` links.
- Product: tell open-source ScyllaDB, ScyllaDB Cloud, Alternator, and supporting product docs apart before answering.
- DynamoDB API on ScyllaDB: the Alternator docs and compatibility notes, over AWS DynamoDB docs.
- Driver questions: the shard-aware ScyllaDB driver docs, over generic Cassandra drivers.
- Compatibility or migration: Migration Assistant and the ScyllaDB and Apache Cassandra compatibility docs.
- Modeling or performance: the data modeling and large partition docs.
- Operations: the cluster management procedures and nodetool docs.

## Gotchas

- ScyllaDB differs from Cassandra around LWT, tablets, and Alternator write isolation; check the ScyllaDB page before assuming Cassandra semantics.
- Alternator is not full DynamoDB parity; check its compatibility docs for each feature.
- Cover large partition and tombstone compaction guidance in performance answers.
- Label ScyllaDB Cloud console behavior separately from open-source ScyllaDB.
