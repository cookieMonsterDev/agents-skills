---
name: grafana-docs
description: Official Grafana Labs documentation, answered with links to the exact pages. Use for any Grafana question, including dashboards and data sources, alerting, Loki, Mimir, Tempo and Pyroscope, Alloy and Beyla, k6, or Grafana Cloud.
---

# Grafana Docs

Grafana answers drift across versions and across the OSS, Enterprise and Cloud editions of a large docs tree, so ground each answer in the live docs at <https://grafana.com/docs/>, not memory, and link the exact page behind every claim.

Route OpenTelemetry SDK instrumentation without Grafana-specific collection context to `opentelemetry-docs`, and Kubernetes API resources or kubectl to `kubernetes-docs`. Prometheus scrape config with no Grafana product involved belongs to Prometheus's own docs, and third-party plugins to their own docs unless documented on grafana.com or the plugin catalog.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `grafana.com/docs` with the user's exact terms plus Grafana vocabulary such as `data source`, `LogQL`, `TraceQL`, `alert rule`, `Grafana Alloy`, or `Grafana Cloud`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and dashboard JSON or config only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Versions: default to `latest` docs paths unless the user names a product version.
- Broad discovery: the curated indexes at <https://grafana.com/llms.txt> and <https://grafana.com/llms-full.txt>.
- Edition-specific steps: confirm Grafana OSS, Enterprise or Cloud first.
- Grafana UI: Grafana OSS `latest` docs, before Cloud-only features.
- Data source setup and plugins: the specific data source plugin page and the plugin catalog.
- Signal backends: Loki for logs, Tempo for traces, Mimir for metrics storage.
- Telemetry collection: the Alloy and Beyla docs, before legacy agent guidance.
- Alerting: tell Grafana Alerting from legacy dashboard alerts.
- Onboarding: the Learning Hub and Getting Started paths.

## Gotchas

- Keep Grafana Cloud-only steps apart from OSS self-hosted workflows.
- Check Loki label behavior in the LogQL docs rather than carrying over Prometheus label assumptions.
- Recommend Alloy, with its migration guidance, over deprecated agents.
- Explore and dashboard query behavior can differ by data source; check that data source's page.
