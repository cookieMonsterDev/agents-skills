---
name: opensearch-docs
description: Official OpenSearch documentation, answered with links to the exact pages. Use for any OpenSearch question, including Query DSL, mappings and ISM, k-NN vector search and ML Commons, the security plugin, OpenSearch Dashboards, Data Prepper, or migration from Elasticsearch.
---

# OpenSearch Docs

OpenSearch answers drift toward stale Elasticsearch memory and wrong plugin names, so ground each one in the live docs at <https://docs.opensearch.org/latest/>, not memory, and link the exact page behind every claim.

Route Elastic-licensed Elasticsearch or Kibana features documented only on `elastic.co` to `elasticsearch-docs`, MySQL questions to `mysql-docs`, and PostgreSQL questions to the version's skill (`postgresql-16-docs`, `postgresql-17-docs`, or `postgresql-18-docs`). Amazon OpenSearch Service console operations, Solr, Meilisearch and other search engines belong to their own docs unless the question turns on OpenSearch behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.opensearch.org/latest` with the user's exact terms plus OpenSearch vocabulary such as `Query DSL`, `k-NN`, `ISM`, `security plugin`, `index template`, or `ML Commons`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and API requests, mappings or security configuration only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Versions: the `latest` docs, unless the user names a specific version.
- REST API questions: the API reference, before forum posts or Elasticsearch docs.
- Plugin behavior: the plugin's own docs, before core cluster defaults.
- Data modeling: the mappings and index management docs.
- Query behavior: the Query DSL docs, before syntax recalled from Elasticsearch.
- Vector search: the vector-search docs and k-NN plugin pages.
- Security: the security plugin docs, before generic TLS guidance.
- Dashboards: the OpenSearch Dashboards docs, not Kibana pages.
- Migration: Migration Assistant and the version-specific upgrade guides.

## Gotchas

- Verify plugin and API behavior in the OpenSearch docs; it differs from Elasticsearch in places.
- Name features in OpenSearch Dashboards terms; Kibana feature names do not carry over.
- Recommend current index settings; deprecated index types and settings from older Elasticsearch versions are not current guidance.
- ML Commons, k-NN, and neural search are distinct features; check the docs for which one applies.
- Answer authentication and TLS questions through the security plugin.
- Amazon OpenSearch Service may lag or restrict plugins; confirm support there before recommending a plugin for the managed service.
