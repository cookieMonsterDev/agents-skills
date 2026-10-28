---
name: weaviate-docs
description: Official Weaviate documentation, answered with links to the exact pages. Use for any Weaviate question, including collections and schema, similarity, hybrid and generative search, multi-tenancy and replication, model provider integrations, client libraries, or self-hosted and Weaviate Cloud deployment.
---

# Weaviate Docs

Weaviate answers drift as client libraries move from the legacy GraphQL API to REST/gRPC-first APIs, so ground each one in the live docs at <https://docs.weaviate.io/weaviate/>, not memory, and link the exact page behind every claim.

Route Qdrant concepts to `qdrant-docs`, Pinecone concepts to `pinecone-docs`, MongoDB Atlas Vector Search to `mongodb-docs`, and Redis vector sets to `redis-docs`. Embedding model selection and RAG architecture fall outside these docs unless the question turns on Weaviate configuration or behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.weaviate.io` with the user's exact terms plus Weaviate vocabulary such as `collection`, `vectorizer`, `hybrid search`, `nearText`, `multi-tenancy`, or `HNSW`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and client code or GraphQL/REST examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Core database questions: the docs under <https://docs.weaviate.io/weaviate/>.
- Deployment questions: the docs under <https://docs.weaviate.io/deploy/>, after confirming self-hosting (Docker or Kubernetes) or Weaviate Cloud.
- Client code: the language-specific client library docs, before guessing method names.
- Data model: tell collections (schema-level, like a table) from objects (row-level, like a record).
- Search: tell similarity search (`nearVector`/`nearText`), hybrid search (vector plus BM25), and generative search (retrieval plus LLM generation) apart.
- Scaling: tell multi-tenancy (isolating tenant data within a collection), replication (redundancy), and sharding (horizontal scale) apart.
- Embeddings: the model provider integration docs for the specific vectorizer module.

## Gotchas

- Collections are the schema; tenants are data partitions within a multi-tenant collection.
- Read the vectorizer module from the collection configuration rather than assuming one is enabled by default.
- Match configuration steps to the deployment: Weaviate Cloud console steps differ from self-hosted Docker or Kubernetes configuration.
- Check which API the client library uses; the legacy GraphQL API and the current REST/gRPC-first client APIs differ.
