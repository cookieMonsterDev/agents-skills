---
name: elasticsearch-docs
description: Use when users ask how to deploy, index, search, map, secure, scale, monitor, ingest, aggregate, alert on, or troubleshoot Elasticsearch clusters and the Elastic Stack, including Kibana, Query DSL, ES|QL, data streams, ingest pipelines, vector search, machine learning, Elastic Cloud, Fleet, Beats, Logstash, Elastic Security, or Elastic Observability, especially when they need official Elastic documentation, exact links, or docs-grounded guidance.
---

Elasticsearch questions are easy to answer from stale memory, OpenSearch assumptions, or pre–data-stream patterns. Use this skill to ground answers in the official Elastic documentation and return the closest authoritative page instead of generic search-engine advice.

## When to Use

Use this skill when the request is about:

- Elasticsearch concepts, indices, documents, mappings, and data streams
- Getting started with Elastic Cloud, self-managed, or serverless deployments
- Indexing, updating, searching, aggregating, and deleting data
- Query DSL, ES|QL, EQL, SQL, and search application patterns
- Mappings, analyzers, templates, aliases, and text analysis
- Ingest pipelines, connectors, Fleet, Elastic Agent, Beats, and Logstash
- Vector search, semantic search, RAG, and Elastic Inference
- Machine learning, anomaly detection, and alerting
- Kibana: Discover, Lens, Dashboards, reporting, and workflows
- Cluster deployment, scaling, autoscaling, backup, and snapshot/restore
- Security: users, roles, API keys, encryption, and Elastic Security
- Elastic Observability: logs, metrics, traces, APM, and Synthetics
- Cross-cluster search, remote clusters, and data lifecycle management
- Troubleshooting cluster health, shard allocation, and query performance

Do not use this skill for:

- OpenSearch-specific plugins, APIs, or Dashboards behavior. Use `opensearch-docs` instead.
- Raw AWS OpenSearch Service console operations when the question is provider-specific rather than Elasticsearch behavior.
- Solr, Meilisearch, or other search engines unless the question maps to documented Elasticsearch API behavior.
- Grafana or OpenTelemetry unless the question is specifically about Elastic Observability integration documented by Elastic.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and deployment choice
- Data store: indices, mappings, templates, and data streams
- Ingestion, pipelines, and connectors
- Search, query languages, and aggregations
- Vector search, AI features, and machine learning
- Kibana exploration, visualization, and alerting
- Deploy, scale, backup, and production guidance
- Security, users, roles, and API keys
- Elastic Observability or Elastic Security solutions
- Reference APIs, clients, and scripting
- Troubleshooting and release notes

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Elastic docs first

- Treat `elastic.co/docs` as the source of truth for Elasticsearch and the Elastic Stack.
- Prefer pages under <https://www.elastic.co/docs/>.
- Distinguish Elasticsearch reference, solution guides, deployment docs, and Kibana docs before answering.
- Check applicability badges for deployment type (Elastic Cloud, self-managed, serverless) when features may differ.
- Search with the user's exact terms plus focused Elastic phrases such as `data stream`, `ingest pipeline`, `Query DSL`, `index template`, `snapshot`, or `vector search`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For REST API questions, prefer the Elasticsearch API reference over blog posts or older `elastic.co/guide` pages.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For version-specific behavior, check release notes and versioning docs before answering from older knowledge.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Elastic docs links, not just the docs homepage.
- Only provide API requests, mappings, or pipeline examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Elastic docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example API request, mapping, or configuration, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Get Started and fundamentals before deep reference pages.
- For data modeling questions, prefer data store and mapping docs before guessing index design.
- For query behavior, prefer Query DSL or ES|QL docs before inventing syntax.
- For ingestion questions, distinguish ingest pipelines, Fleet, connectors, and Logstash.
- For production questions, prefer deploy-and-manage and production guidance docs.
- For security questions, prefer deploy-manage security and Elastic Security docs.
- For observability questions, route to Elastic Observability solution docs rather than generic Elasticsearch search pages.
- Note deployment type: serverless, Elastic Cloud hosted, and self-managed clusters differ in available features.

## Common Mistakes

- Answering from memory without verifying the current Elastic docs
- Linking the Elastic docs homepage when a narrower reference or solution page exists
- Mixing OpenSearch and Elasticsearch API or feature behavior
- Treating legacy index types or types mapping as current guidance
- Recommending unbounded wildcard or regex queries without checking performance docs
- Confusing data streams with regular indices when lifecycle or rollover behavior matters
- Using outdated `elastic.co/guide` Asciidoc URLs when newer `elastic.co/docs` pages exist

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Elastic docs as the final authority.
