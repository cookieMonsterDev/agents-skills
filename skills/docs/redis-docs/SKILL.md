---
name: redis-docs
description: Official Redis documentation, answered with links to the exact pages. Use for any Redis question, including data types and commands, client libraries, search, JSON and vector features, or running Redis Open Source, Redis Cloud, Redis Software or Redis for Kubernetes.
---

# Redis Docs

Redis command behavior drifts with every release, so ground each answer in the live docs at <https://redis.io/docs/latest/>, not memory, and link the exact page behind every claim.

Route AWS CLI commands against ElastiCache or MemoryDB to `aws-cli-docs`, and Kafka topics, producers, consumers or brokers to `kafka-docs`. Framework caching abstractions belong to the framework's own docs unless the question turns on Redis server or client behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `redis.io/docs/latest` with the user's exact terms plus Redis vocabulary such as `XADD`, `FT.SEARCH`, `MULTI`, `ACL SETUSER`, `CLUSTER`, or `appendonly`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and commands or client code only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Beginner questions: start at Develop with Redis and the data-type guides, before the full command reference.
- Command syntax and behavior: the command reference plus the matching data-type page.
- Performance: pipelining, keyspace patterns, and scaling docs.
- Search or vector questions: search-and-query docs, keeping indexing and querying apart.
- Security: ACL, TLS, and the security pages for the user's deployment type.
- Persistence: tell RDB snapshots from AOF, and confirm the product (Open Source, Cloud, or Software) first.
- Client questions: the language-specific client guide, before generic command examples.

## Gotchas

- Redis pub/sub is fire-and-forget; durable, replayable event streams are Redis Streams (or Kafka).
- Redis Cloud and Redis Software expose some settings only in their consoles; match configuration advice to the user's product.
- HyperLogLog and Bloom filters are probabilistic: present their results as estimates.
- Iterate production keyspaces with `SCAN`; `KEYS` blocks the server.
