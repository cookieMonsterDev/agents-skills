---
name: pinecone-docs
description: Use when users ask how to build, configure, index, query, filter, scale, or troubleshoot Pinecone vector database applications, including serverless indexes, namespaces, upsert/query/update/delete operations, metadata filtering, hybrid search, reranking, Pinecone Assistant, or SDKs, especially when they need official Pinecone documentation, exact links, or docs-grounded guidance.
---

Pinecone questions are easy to answer from stale memory, especially since pod-based indexes were replaced by the serverless architecture. Use this skill to ground answers in the official Pinecone documentation and return the closest authoritative page instead of generic vector-search advice.

## When to Use

Use this skill when the request is about:

- Pinecone concepts: organizations, projects, serverless indexes, namespaces, and records
- Creating and configuring serverless indexes (dense, sparse/BM25, or integrated-embedding indexes)
- Upserting, querying, updating, deleting, or fetching records
- Namespaces for multitenancy and data isolation
- Metadata filtering, hybrid search, and reranking search results
- Bulk import from object storage, backups, and restoring indexes
- Pinecone Assistant for retrieval-augmented generation
- SDKs (Python, Node.js, Java, Go) and the REST API reference
- Authentication, API keys, limits, quotas, and billing plans
- Performance: reducing latency, increasing throughput, and managing cost

Do not use this skill for:

- Qdrant-specific concepts (payload indexes, HNSW parameter tuning, on-premise clustering). Use `qdrant-docs` instead.
- Weaviate-specific concepts (GraphQL API, modules, classes as collections). Use `weaviate-docs` instead.
- MongoDB Atlas Vector Search or Redis vector sets. Use `mongodb-docs` or `redis-docs` instead.
- General embedding model selection or RAG architecture unless the question is specifically about Pinecone configuration or behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Creating and managing indexes
- Upserting, querying, updating, and deleting records
- Namespaces, metadata filtering, and multitenancy
- Search quality: hybrid search and reranking
- Backups, restores, and bulk import
- Pinecone Assistant
- SDKs and API reference
- Limits, cost, and performance optimization

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Pinecone docs first

- Treat `docs.pinecone.io` as the source of truth for Pinecone.
- Prefer pages under <https://docs.pinecone.io/guides/> for task-focused how-to content and <https://docs.pinecone.io/reference/> for API and SDK details.
- Pinecone indexes are serverless by default; pod-based indexes are a legacy architecture. Confirm which the user means before answering.
- Search with the user's exact terms plus focused Pinecone phrases such as `namespace`, `upsert`, `metadata filter`, `sparse vector`, `integrated embedding`, or `serverless index`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Pinecone docs links, not just the docs homepage.
- Only provide SDK code or `curl` examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Pinecone docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example SDK code or request, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer the quickstart before deep guide pages.
- For data operations, distinguish upsert (create/replace) from update (partial field change) from fetch (read by ID).
- For multitenancy questions, prefer namespace docs over trying to simulate tenants with metadata alone.
- For search-quality questions, prefer hybrid-search and rerank-results docs before recommending a different similarity metric from memory.
- For cost or performance questions, check the optimize guides (decrease latency, increase throughput, save on costs) before improvising tuning advice.
- For SDK questions, confirm the SDK's API version compatibility noted on its overview page.

## Common Mistakes

- Answering from memory without verifying the current Pinecone docs, especially pre-serverless (pod-based) patterns
- Linking the Pinecone docs homepage when a narrower guide page exists
- Confusing namespaces (data partitioning within an index) with projects or organizations (account-level scoping)
- Recommending pod-based index configuration for a new project when serverless is the current default
- Treating metadata filtering as a replacement for proper namespace-based multitenancy
- Mixing Pinecone Assistant behavior with core vector database query behavior

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Pinecone docs as the final authority.
