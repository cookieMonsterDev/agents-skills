---
name: grafana-docs
description: Use when users ask how to install, configure, query, visualize, alert on, administer, or troubleshoot Grafana and the Grafana Labs observability stack, including Grafana OSS, Grafana Enterprise, Grafana Cloud, dashboards, panels, data sources, Loki, Mimir, Tempo, Pyroscope, Alloy, Beyla, k6, alerting, IRM, SLOs, or OpenTelemetry integrations, especially when they need official Grafana Labs documentation, exact links, or docs-grounded guidance.
---

Grafana questions are easy to answer from stale memory or product-specific assumptions across the large Grafana Labs docs tree. Use this skill to ground answers in the official Grafana Labs documentation and return the closest authoritative page instead of generic observability UI advice.

## When to Use

Use this skill when the request is about:

- Grafana OSS, Grafana Enterprise, and Grafana Cloud
- Dashboards, panels, visualizations, and Explore
- Data sources, queries, transformations, and variables
- Alerting, contact points, notification policies, and IRM
- Metrics with Mimir and Prometheus-compatible workflows
- Logs with Loki and log query languages
- Traces with Tempo and distributed tracing visualization
- Profiles with Pyroscope and continuous profiling
- Grafana Alloy, Beyla, and telemetry collection agents
- k6 performance testing and synthetic monitoring
- Account management, upgrades, and administration

Do not use this skill for:

- OpenTelemetry SDK instrumentation details without Grafana-specific collection context. Use `opentelemetry-docs` instead.
- Core Kubernetes API resources or kubectl usage. Use `kubernetes-docs` instead.
- Raw Prometheus server docs when the question is only about Prometheus scrape config with no Grafana product involvement.
- Third-party plugin behavior unless documented on grafana.com or the plugin catalog.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Grafana core: setup, dashboards, panels, and Explore
- Data sources and query patterns
- Alerting, IRM, and SLOs
- Metrics stack: Mimir and Prometheus integrations
- Logs stack: Loki
- Traces stack: Tempo
- Profiles stack: Pyroscope
- Collection agents: Alloy and Beyla
- Grafana Cloud onboarding and account management
- Performance testing: k6

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section. For broader discovery, curated indexes are at <https://grafana.com/llms.txt> and <https://grafana.com/llms-full.txt>.

### 2. Search official Grafana docs first

- Treat `grafana.com/docs` as the source of truth for Grafana Labs products.
- Prefer pages under <https://grafana.com/docs/>.
- Default to `latest` docs paths unless the user specifies a product version.
- Search with the user's exact terms plus focused Grafana phrases such as `dashboard`, `data source`, `LogQL`, `TraceQL`, `alert rule`, `Grafana Alloy`, or `Grafana Cloud`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- Distinguish Grafana OSS, Enterprise, and Cloud docs before answering with product-specific steps.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For data source setup, open the specific data source plugin docs.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Grafana docs links, not just the docs homepage.
- Only provide dashboard JSON or config examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Grafana docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example config or query snippets, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For Grafana UI questions, prefer Grafana OSS `latest` docs before Cloud-only features.
- For log queries, open Loki docs; for traces, Tempo; for metrics storage, Mimir.
- For telemetry collection, check Alloy and Beyla docs before legacy agent guidance.
- For alerting questions, distinguish Grafana Alerting from legacy dashboard alerts.
- For onboarding questions, use Learning Hub and Getting Started paths when appropriate.
- For plugin questions, check the plugin catalog and the specific data source page.

## Common Mistakes

- Answering from memory without verifying the current Grafana docs
- Linking the Grafana docs homepage when a narrower product or feature page exists
- Mixing Grafana Cloud-only steps with OSS self-hosted workflows
- Confusing Loki labels with Prometheus labels without checking LogQL docs
- Recommending deprecated agents without checking Alloy migration guidance
- Treating Explore and Dashboard query behavior as identical across all data sources

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Grafana docs as the final authority.
