---
name: cassandra-docs
description: Official Apache Cassandra documentation, answered with links to the exact pages. Use for any Cassandra question, including CQL and data modeling, SAI and secondary indexes, vector search, replication and consistency levels, or compaction, repair, nodetool and cqlsh.
---

# Apache Cassandra Docs

The Cassandra docs site publishes the 5.0 GA line, the maintained 4.1 and 4.0 lines, and a 6.0 alpha, so ground each answer in the live docs at <https://cassandra.apache.org/doc/latest/>, not memory, and link the exact page behind every claim.

Route ScyllaDB-specific features, Alternator, or shard-aware drivers to `scylladb-docs`, Amazon DynamoDB to `aws-dynamodb-docs`, and MongoDB to `mongodb-docs`. DataStax Enterprise and Astra belong to DataStax's own docs unless the question maps to open-source Cassandra behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `cassandra.apache.org/doc` with the user's exact terms plus Cassandra vocabulary such as `partition key`, `clustering column`, `SAI`, `compaction`, `consistency level`, or `nodetool`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and CQL, `cassandra.yaml` or nodetool examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: `latest` serves the 5.0 docs but shows a prerelease banner (as does `stable`) because the 6.0 alpha branch is published; pin <https://cassandra.apache.org/doc/5.0/> for GA-only behavior, and switch the version path when the user names a version.
- CQL syntax: the CQL reference, before SQL or DynamoDB patterns.
- Indexes: the SAI docs for modern indexing, and the 2i docs for legacy secondary indexes.
- Performance: the compaction, large partition, and production recommendation docs.
- Operations: the operating and nodetool docs, before ad hoc repair advice.
- Vector search: the vector search docs, not generic CQL pages.

## Gotchas

- Model schemas query-first, around the queries the application runs, instead of JOINs or ad hoc filters.
- SAI and legacy secondary indexes are distinct; say which one advice applies to.
- Check performance guidance before recommending `ALLOW FILTERING` or unbounded scans.
- Base read and write advice on consistency level and replication factor together.
