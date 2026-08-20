---
name: qdrant-docs
description: Use when users ask how to build, configure, query, filter, index, scale, secure, or troubleshoot Qdrant vector database deployments, including collections, points, payloads, vectors, hybrid search, filtering, quantization, snapshots, distributed deployment, Qdrant Cloud, or client libraries, especially when they need official Qdrant documentation, exact links, or docs-grounded guidance.
---

Qdrant questions are easy to answer from stale memory or from patterns borrowed from a different vector database. Use this skill to ground answers in the official Qdrant documentation and return the closest authoritative page instead of generic vector-search advice.

## When to Use

Use this skill when the request is about:

- Qdrant concepts: collections, points, vectors, payloads, and named vectors
- Search, filtering, hybrid queries, recommendation, and discovery API behavior
- Indexing: HNSW parameters, payload indexes, sparse vectors, and quantization (scalar, product, binary)
- Storage, snapshots, backups, and the write-ahead log
- Distributed deployment, sharding, replication, and consistency guarantees
- Multitenancy and payload-based partitioning
- Client libraries (Python, JavaScript/TypeScript, Go, Rust, Java, .NET) and the REST/gRPC APIs
- FastEmbed, built-in inference, and hybrid text search (BM25 plus dense vectors)
- Qdrant Cloud provisioning, RBAC, and Qdrant Edge/on-device deployments
- Security: API keys, TLS, and role-based access control

Do not use this skill for:

- Pinecone-specific concepts (serverless index architecture, namespaces-as-tenants). Use `pinecone-docs` instead.
- Weaviate-specific concepts (GraphQL API, modules, classes as collections). Use `weaviate-docs` instead.
- Redis vector sets or RediSearch vector fields. Use `redis-docs` instead.
- General embedding model selection or RAG architecture unless the question is specifically about Qdrant configuration or behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, quickstart, and local/cloud setup
- Data model: collections, points, vectors, payload
- Search: similarity search, filtering, hybrid queries, recommendation
- Indexing and performance: HNSW, quantization, payload indexes
- Storage and operations: snapshots, backups, distributed deployment
- Client libraries and API reference
- Qdrant Cloud and Qdrant Edge
- Security and access control

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Qdrant docs first

- Treat `qdrant.tech/documentation` as the source of truth for Qdrant.
- Prefer pages under <https://qdrant.tech/documentation/>.
- Prefer <https://api.qdrant.tech/api-reference> for REST API endpoint and parameter details.
- Search with the user's exact terms plus focused Qdrant phrases such as `HNSW`, `payload index`, `quantization`, `named vectors`, `sparse vectors`, or `shard key`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For client code questions, prefer the language-specific client repository or the Interfaces page before guessing method names.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Qdrant docs links, not just the docs homepage.
- Only provide client code or `curl` examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Qdrant docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example query or client code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer the local or cloud quickstart before deep concept pages.
- For data-model questions, distinguish collections (schema-level) from points (row-level) from payload (metadata).
- For search-quality questions, prefer filtering and hybrid-queries docs before recommending a different distance metric from memory.
- For performance questions, distinguish quantization (memory/speed trade-off) from indexing (HNSW parameters) from sharding (horizontal scale).
- For production questions, check distributed deployment and snapshots docs before improvising a backup strategy.
- For client questions, confirm the client library version matches the server version noted in the docs.

## Common Mistakes

- Answering from memory without verifying the current Qdrant docs
- Linking the Qdrant docs homepage when a narrower concept or guide page exists
- Confusing payload indexes (for filtering) with the vector index (HNSW, for similarity search)
- Recommending quantization without noting the recall trade-off documented for each quantization type
- Mixing Qdrant Cloud console steps with self-hosted configuration file settings
- Treating collection aliases as a substitute for proper multitenancy or vice versa

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Qdrant docs as the final authority.
