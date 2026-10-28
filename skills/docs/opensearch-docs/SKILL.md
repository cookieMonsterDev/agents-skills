---
name: opensearch-docs
description: Use when users ask how to deploy, index, search, map, secure, scale, monitor, ingest, aggregate, or troubleshoot OpenSearch clusters and OpenSearch Dashboards, including Query DSL, vector search, k-NN, ML Commons, Data Prepper, security plugin, index management, ISM, snapshots, clients, or migration from Elasticsearch, especially when they need official OpenSearch documentation, exact links, or docs-grounded guidance.
---

OpenSearch questions are easy to answer from stale Elasticsearch memory or wrong plugin names. Use this skill to ground answers in the official OpenSearch documentation and return the closest authoritative page instead of generic search-engine advice.

## When to Use

Use this skill when the request is about:

- OpenSearch concepts, indices, documents, mappings, and aliases
- Getting started with OpenSearch and OpenSearch Dashboards
- Installation, configuration, upgrades, and plugins
- Indexing, updating, searching, aggregating, and deleting data
- Query DSL, SQL plugin, PPL, and search patterns
- Mappings, analyzers, index templates, and index management
- Vector search, k-NN, semantic search, and hybrid search
- ML Commons: model deployment, connectors, and AI agents
- Security plugin: authentication, authorization, and encryption
- Index State Management (ISM), snapshots, and cluster administration
- OpenSearch Dashboards: visualizations, Discover, and alerting
- Data Prepper, clients, Benchmark, and Migration Assistant
- Observability, anomaly detection, and trace analytics
- Troubleshooting cluster health, shard allocation, and query performance

Do not use this skill for:

- Elastic-licensed Elasticsearch or Kibana features documented only on `elastic.co`. Use `elasticsearch-docs` instead.
- Amazon OpenSearch Service console operations when the question is provider-specific rather than OpenSearch behavior.
- Solr, Meilisearch, or other search engines unless the question maps to documented OpenSearch API behavior.
- MySQL or PostgreSQL relational database questions.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and tutorials
- Install, configure, and upgrade
- Data modeling: mappings, templates, and index management
- Search, Query DSL, SQL, and PPL
- Vector search and machine learning
- Security and access control
- Cluster operations, ISM, and snapshots
- OpenSearch Dashboards and visualization
- Clients, Data Prepper, and supporting tools
- API reference and plugin docs
- Troubleshooting and migration

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official OpenSearch docs first

- Treat `docs.opensearch.org` as the source of truth for OpenSearch.
- Prefer pages under <https://docs.opensearch.org/latest/> unless the user names a specific version.
- Distinguish core OpenSearch docs, plugin docs, Dashboards docs, and supporting tool docs before answering.
- Search with the user's exact terms plus focused OpenSearch phrases such as `Query DSL`, `k-NN`, `ISM`, `security plugin`, `index template`, or `ML Commons`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For REST API questions, prefer the API reference over forum posts or Elasticsearch docs.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For plugin-specific behavior, open the plugin documentation rather than assuming core cluster defaults.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact OpenSearch docs links, not just the docs homepage.
- Only provide API requests, mappings, or security configuration examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to OpenSearch docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example API request, mapping, or configuration, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started before deep reference pages.
- For data modeling questions, prefer mappings and index management docs before guessing index design.
- For query behavior, prefer Query DSL docs before inventing syntax from Elasticsearch memory.
- For vector search questions, route to vector-search docs and k-NN plugin pages.
- For security questions, prefer the security plugin docs rather than generic TLS guidance.
- For Dashboards questions, open OpenSearch Dashboards docs rather than Kibana pages.
- For migration questions, check Migration Assistant and version-specific upgrade guides.
- Note managed-service differences: Amazon OpenSearch Service may lag or restrict certain plugins.

## Common Mistakes

- Answering from Elasticsearch docs when OpenSearch plugin or API behavior differs
- Linking the OpenSearch docs homepage when a narrower plugin or API page exists
- Mixing Kibana feature names with OpenSearch Dashboards terminology
- Recommending deprecated index types or settings from older Elasticsearch versions
- Treating ML Commons, k-NN, and neural search as interchangeable without checking docs
- Ignoring the security plugin when answering authentication or TLS questions
- Assuming Amazon OpenSearch Service supports every plugin documented for self-managed OpenSearch

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live OpenSearch docs as the final authority.
