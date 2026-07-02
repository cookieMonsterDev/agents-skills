---
name: rabbitmq-docs
description: Use when users ask how to install, configure, publish to, consume from, cluster, secure, monitor, or troubleshoot RabbitMQ brokers and messaging applications, including AMQP 0-9-1, AMQP 1.0, queues, exchanges, bindings, routing, streams, publishers, consumers, management UI, plugins, or production operations, especially when they need official RabbitMQ documentation, exact links, or docs-grounded guidance.
---

RabbitMQ questions are easy to answer from stale memory or AMQP tutorial patterns that do not match the user's protocol version. Use this skill to ground answers in the official RabbitMQ documentation and return the closest authoritative page instead of generic message-broker advice.

## When to Use

Use this skill when the request is about:

- RabbitMQ concepts, architecture, and messaging patterns
- Installing and upgrading RabbitMQ on Linux, Windows, macOS, or containers
- AMQP 0-9-1 and AMQP 1.0 client usage
- Queues, exchanges, bindings, routing keys, and virtual hosts
- Publishers, consumers, acknowledgements, prefetch, and durability
- RabbitMQ streams and stream offset tracking
- Clustering, quorum queues, mirrored queues, and high availability
- Security, access control, TLS, and authentication
- Management UI, CLI tools, and monitoring
- Performance, memory, disk alarms, and troubleshooting

Do not use this skill for:

- Apache Kafka topics, partitions, or consumer groups. Use `kafka-docs` instead.
- Redis pub/sub or BullMQ job queues. Use `redis-docs` or `bullmq-docs` instead.
- Managed AWS MQ console operations when the question is provider UI rather than RabbitMQ behavior. Use `aws-cli-docs` for AWS CLI commands.
- Generic MQTT or STOMP protocol questions unless RabbitMQ docs cover the relevant plugin or feature.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and tutorials
- Install and upgrade
- Developer usage: publish, consume, route, and RPC
- Streams and modern messaging features
- Broker management and configuration
- Clustering, replication, and reliability
- Security and access control
- Monitoring, logging, and troubleshooting

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official RabbitMQ docs first

- Treat `rabbitmq.com/docs` as the source of truth for RabbitMQ.
- Prefer pages under <https://www.rabbitmq.com/docs>.
- Default to the current documentation version (4.3) unless the user specifies another supported version.
- Search with the user's exact terms plus focused RabbitMQ phrases such as `quorum queue`, `prefetch`, `dead letter`, `stream`, `management plugin`, or `virtual host`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For protocol-specific behavior, distinguish AMQP 0-9-1 from AMQP 1.0 before answering.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For tutorials, prefer the official RabbitMQ tutorials when the user is learning patterns.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact RabbitMQ docs links, not just the docs homepage.
- Only provide client code or `rabbitmqctl` examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to RabbitMQ docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example commands or client snippets, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Getting Started and Tutorials before advanced management docs.
- For routing questions, distinguish direct, fanout, topic, and headers exchanges.
- For reliability questions, check publisher confirms, consumer acknowledgements, and quorum queue docs.
- For operations questions, prefer How to Manage RabbitMQ before guessing config file locations.
- For monitoring questions, open monitoring and management plugin docs before generic metrics advice.
- For stream questions, use stream-specific docs rather than classic queue tutorials.

## Common Mistakes

- Answering from memory without verifying the current RabbitMQ docs
- Linking the RabbitMQ docs homepage when a narrower guide page exists
- Mixing AMQP 0-9-1 tutorial APIs with AMQP 1.0 behavior
- Treating classic mirrored queues as the default HA choice without checking quorum queue guidance
- Recommending unbounded queues without checking memory and disk alarm docs
- Confusing RabbitMQ streams with Kafka-style partitioned logs without reading stream docs

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live RabbitMQ docs as the final authority.
