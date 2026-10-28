---
name: opentelemetry-docs
description: Official OpenTelemetry documentation, answered with links to the exact pages. Use for any OpenTelemetry question, including language SDKs, zero-code instrumentation, the Collector, semantic conventions, or OTLP export of traces, metrics and logs.
---

# OpenTelemetry Docs

OpenTelemetry answers drift toward vendor-specific SDKs and the older OpenTracing and OpenCensus APIs, so ground each answer in the live docs at <https://opentelemetry.io/docs/>, not memory, and link the exact page behind every claim.

Route Grafana dashboards and Loki queries to `grafana-docs`. Raw Prometheus scrape config belongs to Prometheus's own docs unless the user is bridging OpenTelemetry to Prometheus; vendor products (Datadog, New Relic, Honeycomb) and application logging frameworks belong to their own docs unless the question turns on OpenTelemetry integration or OpenTelemetry logs.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `opentelemetry.io/docs` with the user's exact terms plus OpenTelemetry vocabulary such as `OTLP`, `semantic conventions`, `Collector`, `auto-instrumentation`, `span processor`, or `resource attributes`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and SDK or Collector config only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Broad discovery: the live docs index at <https://opentelemetry.io/llms.txt>.
- Concepts: Concepts and What is OpenTelemetry, before language SDK pages.
- Instrumentation: the language page under Language APIs & SDKs for the user's signal (traces, metrics or logs), before generic concept pages.
- Collector YAML: the specific receiver, processor or exporter page.
- Collector deployment: tell agent, gateway and standalone patterns apart.
- Export: the OTLP and compatibility docs, before guessing endpoint formats.
- Kubernetes: the platforms docs and blueprints, before inventing sidecar patterns.
- Attribute names: the semantic conventions docs.

## Gotchas

- Answer with current OpenTelemetry SDK APIs, kept apart from OpenTracing and OpenCensus APIs.
- Check the compatibility docs before recommending an exporter; some are deprecated.
- Vendor agents are not OpenTelemetry standards; check the zero-code instrumentation docs.
- Collector receivers ingest telemetry; producing it is the SDK instrumentation's job.
