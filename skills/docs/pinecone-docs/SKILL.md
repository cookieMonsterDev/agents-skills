---
name: pinecone-docs
description: Official Pinecone documentation, answered with links to the exact pages. Use for any Pinecone question, including serverless indexes, namespaces, upsert and query operations, metadata filtering, hybrid search and reranking, Pinecone Assistant, or SDKs.
---

# Pinecone Docs

Pinecone answers drift toward pod-based patterns now that serverless is the default index architecture, so ground each one in the live docs at <https://docs.pinecone.io/>, not memory, and link the exact page behind every claim.

Route Qdrant concepts to `qdrant-docs`, Weaviate concepts to `weaviate-docs`, MongoDB Atlas Vector Search to `mongodb-docs`, and Redis vector sets to `redis-docs`. Embedding model selection and RAG architecture fall outside these docs unless the question turns on Pinecone configuration or behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.pinecone.io` with the user's exact terms plus Pinecone vocabulary such as `namespace`, `upsert`, `metadata filter`, `sparse vector`, `integrated embedding`, or `serverless index`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and SDK code or `curl` examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Task how-tos: the guides under <https://docs.pinecone.io/guides/>.
- API and SDK details: the reference under <https://docs.pinecone.io/reference/>.
- Data operations: tell upsert (create or replace), update (partial field change), and fetch (read by ID) apart.
- Multitenancy: the namespace docs.
- Search quality: the hybrid-search and rerank-results docs, before changing the similarity metric.
- Cost or performance: the optimize guides (decrease latency, increase throughput, save on costs).
- SDK questions: the API version compatibility on the SDK's overview page.

## Gotchas

- Default new projects to serverless indexes; pod-based indexes are legacy, so confirm which architecture the user runs.
- Namespaces partition data within an index; projects and organizations scope the account.
- Isolate tenants with namespaces; metadata filtering alone is no substitute for namespace-based multitenancy.
- Answer Pinecone Assistant questions from the Assistant docs, apart from core vector database query behavior.
