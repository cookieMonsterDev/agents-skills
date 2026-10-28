---
name: elasticsearch-docs
description: Official Elasticsearch documentation, answered with links to the exact pages. Use for any Elasticsearch or Elastic Stack question, including mappings and data streams, Query DSL and ES|QL, ingest pipelines, vector search, Kibana, or Elastic Cloud and self-managed deployments.
---

# Elasticsearch Docs

Elasticsearch answers drift toward pre-data-stream patterns, OpenSearch assumptions and the older `elastic.co/guide` pages, so ground each one in the live docs at <https://www.elastic.co/docs/>, not memory, and link the exact page behind every claim.

Route OpenSearch plugins, APIs or Dashboards to `opensearch-docs`, and Grafana or OpenTelemetry to `grafana-docs` or `opentelemetry-docs` unless the question is about an Elastic Observability integration. Amazon OpenSearch Service console operations, Solr, Meilisearch and other search engines belong to their own docs unless the question turns on Elasticsearch behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `elastic.co/docs` with the user's exact terms plus Elastic vocabulary such as `data stream`, `ingest pipeline`, `Query DSL`, `index template`, `snapshot`, or `vector search`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and API requests, mappings or pipeline examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- REST API questions: the Elasticsearch API reference, before blog posts or older `elastic.co/guide` pages.
- Version-specific behavior: the release notes and versioning docs.
- Deployment differences: the page's applicability badges for serverless, Elastic Cloud hosted, and self-managed clusters.
- Data modeling: the data store and mapping docs.
- Query behavior: the Query DSL or ES|QL docs.
- Ingestion: tell ingest pipelines, Fleet, connectors, and Logstash apart, then open the matching docs.
- Production: the deploy-and-manage and production guidance docs.
- Security: the deploy-manage security docs and the Elastic Security docs.
- Observability: the Elastic Observability solution docs, before generic Elasticsearch search pages.

## Gotchas

- Keep Elasticsearch and OpenSearch apart; their APIs and features differ.
- Treat index types and types mappings as legacy, not current guidance.
- Check the performance docs before recommending unbounded wildcard or regex queries.
- Confirm whether the user has a data stream or a regular index when lifecycle or rollover behavior matters.
- Link current `elastic.co/docs` pages; `elastic.co/guide` Asciidoc URLs are the older docs.
