---
name: bullmq-docs
description: Use when users ask how to create, configure, process, schedule, retry, rate-limit, monitor, or troubleshoot BullMQ job queues and workers in Node.js, including queues, workers, jobs, flows, job schedulers, events, telemetry, Redis compatibility, NestJS integration, patterns, or production deployment, especially when they need official BullMQ documentation, exact links, or docs-grounded guidance.
---

BullMQ questions are easy to answer from stale memory or Bull (v3) patterns that do not apply to BullMQ. Use this skill to ground answers in the official BullMQ documentation and return the closest authoritative page instead of generic Redis queue advice.

## When to Use

Use this skill when the request is about:

- BullMQ concepts: queues, workers, jobs, and Redis-backed execution
- Creating queues, adding jobs, and processing jobs with workers
- Priorities, delays, repeatable jobs, cron schedules, and job schedulers
- Retries, backoff, failure handling, and stalled job recovery
- Concurrency, rate limiting, parallelism, and sandboxed processors
- Flows and parent-child job dependencies
- Events, metrics, telemetry, and observability
- Redis compatibility, hosting, and cluster considerations
- NestJS integration and production deployment guidance
- BullMQ patterns: deduplication, idempotency, bulk jobs, and manual retry

Do not use this skill for:

- Raw Redis server configuration unrelated to BullMQ usage. Use `redis-docs` instead.
- RabbitMQ or Kafka messaging patterns. Use `rabbitmq-docs` or `kafka-docs` instead.
- Legacy Bull (v3) API questions unless the user explicitly asks about Bull docs linked from BullMQ.
- Python, Rust, Elixir, or PHP queue libraries unless the question is about those BullMQ ports documented on docs.bullmq.io.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Quick start and core concepts
- Connections and Redis setup
- Queues, workers, and jobs
- Scheduling, retries, and failure handling
- Flows and advanced job relationships
- Events, metrics, and telemetry
- Patterns and production guidance
- NestJS and framework integration

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section. For broader discovery, the live docs index is at <https://docs.bullmq.io/llms.txt>.

### 2. Search official BullMQ docs first

- Treat `docs.bullmq.io` as the source of truth for BullMQ.
- Prefer pages under <https://docs.bullmq.io/>.
- Search with the user's exact terms plus focused BullMQ phrases such as `Queue`, `Worker`, `FlowProducer`, `repeat`, `limiter`, `sandboxed`, or `stalled`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For API details, prefer the Guide and API Reference before answering from memory.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Markdown versions of pages are available by appending `.md` to page URLs when helpful for reading.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact BullMQ docs links, not just the docs homepage.
- Only provide Node.js code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to BullMQ docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example BullMQ code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Quick Start and Guide > Introduction before API Reference.
- For job lifecycle questions, distinguish Queue, Worker, and Job docs.
- For scheduling questions, check Job Schedulers and repeatable jobs docs before inventing cron wrappers.
- For reliability questions, prefer retrying failing jobs and stalled job recovery docs.
- For Redis issues, check Redis Compatibility and Troubleshooting before changing queue code.
- For NestJS questions, open the NestJS guide rather than generic Worker examples.

## Common Mistakes

- Answering from Bull (v3) memory without verifying BullMQ docs
- Linking the BullMQ docs homepage when a narrower Guide or Pattern page exists
- Confusing at-least-once delivery guarantees with exactly-once semantics
- Running workers without understanding Redis connection and prefix requirements
- Recommending polling loops when BullMQ is event-driven by design
- Ignoring Redis Cluster limitations documented in BullMQ compatibility guides

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live BullMQ docs as the final authority.
