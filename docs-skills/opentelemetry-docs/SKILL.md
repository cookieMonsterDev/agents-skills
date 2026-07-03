---
name: opentelemetry-docs
description: Use when users ask how to instrument, collect, process, export, or troubleshoot OpenTelemetry traces, metrics, and logs, including language SDKs, the OpenTelemetry Collector, zero-code instrumentation, semantic conventions, OTLP, platforms, security, compatibility, or reference architectures, especially when they need official OpenTelemetry documentation, exact links, or docs-grounded guidance.
---

OpenTelemetry questions are easy to answer from stale memory or vendor-specific SDK assumptions. Use this skill to ground answers in the official OpenTelemetry documentation and return the closest authoritative page instead of generic observability advice.

## When to Use

Use this skill when the request is about:

- OpenTelemetry concepts, signals, and architecture
- Getting started by role: developer, operator, or architect
- Language APIs and SDKs for traces, metrics, and logs
- Zero-code or auto-instrumentation agents
- The OpenTelemetry Collector: receivers, processors, exporters, and pipelines
- Semantic conventions and instrumentation libraries
- OTLP export, compatibility, and integration with other observability tools
- Blueprints, reference implementations, and deployment guidance
- Security, specifications, and contributing to OpenTelemetry

Do not use this skill for:

- Grafana dashboard design or Loki query syntax when the question is Grafana-specific. Use `grafana-docs` instead.
- Raw Prometheus scrape config without OpenTelemetry context unless the user is bridging OTel to Prometheus per OTel docs.
- Vendor product docs (Datadog, New Relic, Honeycomb) unless the question is specifically about OpenTelemetry integration patterns documented on opentelemetry.io.
- Application logging frameworks without telemetry export context unless tied to OpenTelemetry logs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Concepts and getting started
- Language SDK instrumentation
- Zero-code instrumentation
- Collector configuration and deployment
- Signals: traces, metrics, and logs
- Platforms and environments
- Blueprints and reference architectures
- Compatibility and specifications
- Security and operations

If you need a quick starting point, load `references/topic-map.md` and jump to the closest starting page. For broader discovery, the live docs index is at <https://opentelemetry.io/llms.txt>.

### 2. Search official OpenTelemetry docs first

- Treat `opentelemetry.io/docs` as the source of truth for OpenTelemetry.
- Prefer pages under <https://opentelemetry.io/docs/>.
- Search with the user's exact terms plus focused OpenTelemetry phrases such as `OTLP`, `semantic conventions`, `Collector`, `auto-instrumentation`, `span processor`, or `resource attributes`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For language-specific setup, prefer the language docs under Language APIs & SDKs before generic concept pages.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For Collector YAML, open the specific receiver, processor, or exporter page.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact OpenTelemetry docs links, not just the docs homepage.
- Only provide SDK or Collector config examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to OpenTelemetry docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example SDK or Collector config, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer Concepts and What is OpenTelemetry before language SDK pages.
- For instrumentation questions, route by language and signal type (traces vs metrics vs logs).
- For Collector questions, distinguish agent, gateway, and standalone deployment patterns.
- For export questions, check OTLP and compatibility docs before guessing endpoint formats.
- For Kubernetes questions, check platforms docs and blueprints before inventing sidecar patterns.
- For semantic attribute questions, prefer semantic conventions docs over ad hoc attribute names.

## Common Mistakes

- Answering from memory without verifying the current OpenTelemetry docs
- Linking the OpenTelemetry docs homepage when a narrower language or Collector page exists
- Mixing OpenTracing or OpenCensus APIs with current OpenTelemetry SDK guidance
- Recommending deprecated exporters without checking compatibility docs
- Treating vendor agents as OpenTelemetry standards without checking zero-code instrumentation docs
- Confusing Collector receivers with SDK instrumentation responsibilities

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live OpenTelemetry docs as the final authority.
