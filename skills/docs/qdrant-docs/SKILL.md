---
name: qdrant-docs
description: Official Qdrant documentation, answered with links to the exact pages. Use for any Qdrant question, including collections, points and payloads, filtering and hybrid search, HNSW and quantization, snapshots and distributed deployment, Qdrant Cloud, or client libraries.
---

# Qdrant Docs

Qdrant answers drift toward stale memory and patterns borrowed from other vector databases, so ground each one in the live docs at <https://qdrant.tech/documentation/>, not memory, and link the exact page behind every claim.

Route Pinecone concepts to `pinecone-docs`, Weaviate concepts to `weaviate-docs`, and Redis vector sets or RediSearch vector fields to `redis-docs`. Embedding model selection and RAG architecture fall outside these docs unless the question turns on Qdrant configuration or behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `qdrant.tech/documentation` with the user's exact terms plus Qdrant vocabulary such as `HNSW`, `payload index`, `quantization`, `named vectors`, `sparse vectors`, or `shard key`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and client code or `curl` examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- REST endpoints and parameters: the API reference at <https://api.qdrant.tech/api-reference>.
- Client code: the language-specific client repository or the Interfaces page, with the client library version matched to the server version the docs note.
- Data model: tell collections (schema-level), points (row-level), and payload (metadata) apart.
- Search quality: the filtering and hybrid-queries docs, before changing the distance metric.
- Performance: tell quantization (memory/speed trade-off), indexing (HNSW parameters), and sharding (horizontal scale) apart.
- Production: the distributed deployment and snapshots docs, before designing a backup strategy.

## Gotchas

- Payload indexes serve filtering; the vector index (HNSW) serves similarity search.
- State the recall trade-off documented for each quantization type when recommending quantization.
- Match configuration advice to the deployment: Qdrant Cloud console steps differ from self-hosted configuration file settings.
- Build multitenancy from the multitenancy docs; collection aliases solve a different problem.
