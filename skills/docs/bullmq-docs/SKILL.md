---
name: bullmq-docs
description: Official BullMQ documentation, answered with links to the exact pages. Use for any BullMQ question, including queues, workers and jobs, job schedulers, flows, retries and stalled jobs, NestJS integration, or Redis compatibility.
---

# BullMQ Docs

BullMQ answers drift toward legacy Bull (v3) patterns that do not apply, so ground each answer in the live docs at <https://docs.bullmq.io/>, not memory, and link the exact page behind every claim.

Route raw Redis server configuration to `redis-docs`, and RabbitMQ or Kafka messaging to `rabbitmq-docs` or `kafka-docs`. Legacy Bull (v3) belongs to the Bull docs linked from BullMQ, and Python, Rust, Elixir or PHP queue libraries to their own docs unless the question is about a BullMQ port documented on docs.bullmq.io.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.bullmq.io` with the user's exact terms plus BullMQ vocabulary such as `Queue`, `Worker`, `FlowProducer`, `repeat`, `limiter`, or `stalled`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and Node.js code only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Beginner questions: Quick Start and Guide > Introduction, before the API Reference.
- API details: the Guide and the API Reference.
- Job lifecycle: keep the Queue, Worker and Job docs apart.
- Scheduling: Job Schedulers and the repeatable-jobs docs, before any hand-rolled cron wrapper.
- Reliability: the retrying-failing-jobs and stalled-job-recovery docs.
- Redis issues: Redis Compatibility and Troubleshooting, before changing queue code.
- NestJS: the NestJS guide, before generic Worker examples.

## Gotchas

- BullMQ delivers jobs at least once, not exactly once; pair processors with the idempotency and deduplication patterns.
- Set up workers per the documented Redis connection and prefix requirements before running them.
- BullMQ is event-driven: react to jobs through workers and events; polling loops work against its design.
- Check the Redis Cluster limitations in the compatibility guides before running BullMQ on a cluster.
