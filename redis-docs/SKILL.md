---
name: redis-docs
description: Use when users ask how to build, explain, configure, tune, secure, scale, monitor, or troubleshoot Redis applications and deployments, including data types, commands, clients, pipelining, transactions, pub/sub, streams, JSON, search, vector search, AI/RAG patterns, clustering, replication, persistence, Redis Open Source, Redis Cloud, Redis Software, or Redis for Kubernetes, especially when they need official Redis documentation, exact links, or docs-grounded guidance.
---

Redis questions are easy to answer from stale memory or outdated command behavior. Use this skill to ground answers in the official Redis documentation and return the closest authoritative page instead of generic caching advice.

## When to Use

Use this skill when the request is about:

- Redis concepts, terminology, data structures, and command behavior
- Strings, hashes, lists, sets, sorted sets, streams, JSON, bitmaps, geospatial, probabilistic types, and vector sets
- Command syntax, pipelining, transactions, pub/sub, and keyspace patterns
- Client libraries (Node.js, Python, Java, Go, .NET, Ruby, PHP, Rust, C, and others)
- Search, query, indexing, and vector database features
- AI development patterns, RAG, and real-time context with Redis
- Redis Open Source installation, configuration, scaling, security, and persistence
- Redis Cloud, Redis Software, Redis for Kubernetes, and production operations
- Redis CLI, Redis Insight, and other client tools
- Monitoring, logging, backups, replication, clustering, and high availability

Do not use this skill for:

- Managed AWS ElastiCache or MemoryDB console operations when the question is provider-specific UI rather than Redis behavior. Use `aws-cli-docs` for AWS CLI commands against those services.
- Apache Kafka topics, producers, consumers, or brokers. Use `kafka-docs` instead.
- Application framework caching abstractions unless the question is specifically about Redis server or client behavior documented by Redis.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and installation
- Data types and commands
- Application development patterns (pipelining, transactions, pub/sub)
- Search, JSON, streams, and vector features
- AI and agent development
- Client libraries and tools
- Operations, scaling, security, and persistence
- Redis Cloud, Software, or Kubernetes products
- Monitoring, troubleshooting, and performance

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Redis docs first

- Treat `redis.io/docs/latest` as the source of truth for Redis.
- Prefer pages under <https://redis.io/docs/latest/>.
- Search with the user's exact terms plus focused Redis phrases such as `XADD`, `FT.SEARCH`, `MULTI`, `ACL SETUSER`, `CLUSTER`, or `appendonly`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For command behavior, prefer the command reference and data-type guides before answering from memory.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Redis docs links, not just the docs homepage.
- Only provide command or client code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Redis docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example commands or client code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Develop with Redis and data-type guides before the full command reference.
- For command syntax questions, prefer the command reference and the relevant data-type page.
- For performance questions, prefer pipelining, keyspace patterns, and scaling docs before guessing tuning advice.
- For search or vector questions, prefer search-and-query docs and distinguish indexing from querying.
- For security questions, prefer ACL, TLS, and product-specific security pages for the deployment type.
- For persistence questions, distinguish RDB snapshots from AOF and check the product (Open Source vs Cloud vs Software).
- For client questions, prefer the language-specific client guide before generic command examples.

## Common Mistakes

- Answering from memory without verifying the current Redis docs
- Linking the Redis docs homepage when a narrower page exists
- Confusing Redis pub/sub with Kafka-style durable event streaming
- Mixing Redis Open Source configuration with Redis Cloud or Software console-only settings
- Treating probabilistic data structures (HyperLogLog, Bloom filter) as exact counters
- Recommending `KEYS` for production key scans instead of `SCAN` as documented

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Redis docs as the final authority.
