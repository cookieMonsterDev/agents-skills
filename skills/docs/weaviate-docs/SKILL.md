---
name: weaviate-docs
description: Use when users ask how to build, configure, query, filter, index, scale, deploy, or troubleshoot Weaviate vector database applications, including collections, schema, CRUD operations, similarity/hybrid/generative search, multi-tenancy, replication, model provider integrations, client libraries, or self-hosted vs Weaviate Cloud deployment, especially when they need official Weaviate documentation, exact links, or docs-grounded guidance.
---

Weaviate questions are easy to answer from stale memory or from patterns borrowed from a different vector database. Use this skill to ground answers in the official Weaviate documentation and return the closest authoritative page instead of generic vector-search advice.

## When to Use

Use this skill when the request is about:

- Weaviate concepts: collections, objects, properties, and vector indexes
- Creating and managing collections, schema design, and CRUD operations on objects
- Similarity search, hybrid search (vector plus keyword), and generative search (RAG)
- Filtering, aggregations, and the REST, GraphQL, or gRPC APIs
- Model provider integrations (embedding and generative modules) and vectorizer configuration
- Multi-tenancy, replication, and sharding architecture
- Client libraries (Python, TypeScript/JavaScript, Java, Go)
- Deployment: Docker, Kubernetes, embedded Weaviate, and Weaviate Cloud
- Performance tuning, vector quantization, and best practices

Do not use this skill for:

- Qdrant-specific concepts (payload indexes, collection-level shard keys). Use `qdrant-docs` instead.
- Pinecone-specific concepts (serverless index architecture, namespaces-as-tenants). Use `pinecone-docs` instead.
- MongoDB Atlas Vector Search or Redis vector sets. Use `mongodb-docs` or `redis-docs` instead.
- General embedding model selection or RAG architecture unless the question is specifically about Weaviate configuration or behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, quickstart, and starter guides
- Concepts and architecture
- Managing collections and objects (schema, CRUD)
- Search: similarity, hybrid, generative, and filtering
- Model provider integrations
- Configuration: replication, multi-tenancy, quantization
- Client libraries and API reference
- Deployment: Docker, Kubernetes, embedded, or Weaviate Cloud

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Weaviate docs first

- Treat `docs.weaviate.io` as the source of truth for Weaviate.
- Prefer pages under <https://docs.weaviate.io/weaviate/> for core database docs and <https://docs.weaviate.io/deploy/> for deployment docs.
- Search with the user's exact terms plus focused Weaviate phrases such as `collection`, `vectorizer`, `hybrid search`, `nearText`, `multi-tenancy`, or `HNSW`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For client code questions, prefer the language-specific client library docs before guessing method names.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Weaviate docs links, not just the docs homepage.
- Only provide client code or GraphQL/REST examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Weaviate docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example query or client code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer the quickstart and starter guides before deep concept or configuration pages.
- For data-model questions, distinguish collections (schema-level, like a table) from objects (row-level, like a record).
- For search questions, distinguish similarity search (`nearVector`/`nearText`), hybrid search (vector plus BM25), and generative search (retrieval plus LLM generation).
- For scaling questions, distinguish multi-tenancy (isolating tenant data within a collection) from replication (redundancy) from sharding (horizontal scale).
- For deployment questions, confirm whether the user is self-hosting (Docker/Kubernetes) or using Weaviate Cloud before giving configuration steps.
- For embedding questions, check the model provider integration docs for the specific vectorizer module before assuming default behavior.

## Common Mistakes

- Answering from memory without verifying the current Weaviate docs
- Linking the Weaviate docs homepage when a narrower concept or guide page exists
- Confusing collections (schema) with tenants (data partitions within multi-tenant collections)
- Assuming a vectorizer module is enabled by default without checking the collection configuration
- Mixing Weaviate Cloud console steps with self-hosted Docker or Kubernetes configuration
- Treating the legacy GraphQL API and the current REST/gRPC-first client APIs as interchangeable without checking which the client library uses

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Weaviate docs as the final authority.
