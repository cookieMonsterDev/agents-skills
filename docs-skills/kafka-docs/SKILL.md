---
name: kafka-docs
description: Use when users ask how to build, explain, configure, tune, secure, operate, replicate, or troubleshoot Apache Kafka clusters and applications, including topics, partitions, producers, consumers, consumer groups, KRaft, brokers, replication, exactly-once semantics, Kafka Connect, Kafka Streams, ACLs, SASL, SSL, tiered storage, monitoring, or upgrading, especially when they need official Apache Kafka 4.3 documentation, exact links, or docs-grounded guidance.
---

Kafka questions are easy to answer from stale memory or ZooKeeper-era patterns. Use this skill to ground answers in the official Apache Kafka 4.3 documentation and return the closest authoritative page instead of generic messaging advice.

## When to Use

Use this skill when the request is about:

- Kafka concepts, terminology, events, topics, partitions, and replication
- Producers, consumers, consumer groups, offsets, and delivery semantics
- Broker configuration, topic configuration, and cluster operations
- KRaft mode, controller quorum, and migration from ZooKeeper
- Security: listeners, SSL/TLS, SASL, and ACLs
- Kafka Connect connectors, source/sink integration, and connector development
- Kafka Streams applications, state stores, windowing, and processing guarantees
- Monitoring, hardware sizing, datacenter deployment, and geo-replication
- Tiered storage, transactions, and consumer rebalance protocol
- Upgrading Kafka, compatibility, and Docker deployment

Do not use this skill for:

- A different Kafka major/minor version when the user explicitly needs that version. Say which version you are using and offer to switch docs if needed.
- Managed AWS MSK console operations when the question is provider-specific rather than Kafka behavior. Use `aws-cli-docs` for AWS CLI commands against MSK.
- Redis streams or pub/sub. Use `redis-docs` instead.
- Third-party client library APIs not covered by Kafka docs unless the question is about core Kafka protocol or configuration behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and quickstart
- Core design and protocol concepts
- Producer, consumer, and admin client configuration
- Broker, topic, and group configuration
- Cluster operations and scaling
- KRaft and metadata management
- Security and ACLs
- Kafka Connect
- Kafka Streams
- Monitoring, hardware, and production operations
- Upgrading, compatibility, and migration

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Kafka docs first

- Treat `kafka.apache.org/43` as the source of truth for Apache Kafka 4.3.
- Prefer pages under <https://kafka.apache.org/43/>.
- Search with the user's exact terms plus focused Kafka phrases such as `min.insync.replicas`, `acks`, `isolation.level`, `KRaft`, `rebalance`, or `cleanup.policy`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For KRaft or ZooKeeper questions, check the KRaft vs ZooKeeper guide before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Kafka docs links, not just the docs homepage.
- Only provide configuration or client code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Kafka docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example configuration or client code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer Introduction and Design before configuration reference pages.
- For topic management questions, prefer Basic Kafka Operations and topic configuration docs.
- For producer reliability questions, prefer producer configs (`acks`, `retries`, `enable.idempotence`) before guessing.
- For consumer lag or rebalance questions, distinguish consumer configs from broker and group configs.
- For security questions, start with Security Overview, then listener, SSL, SASL, or ACL pages as needed.
- For KRaft questions, prefer KRaft operations and KRaft vs ZooKeeper docs over legacy ZooKeeper-only guidance.
- For stream processing questions, distinguish Kafka Streams from plain consumer/producer usage.

## Common Mistakes

- Answering from memory without verifying the current Kafka 4.3 docs
- Linking the Kafka homepage when a narrower page exists
- Assuming ZooKeeper is still required for new deployments without checking KRaft docs
- Confusing Kafka topic retention with message deletion after consumption
- Mixing Kafka Connect connector settings with core broker or client configs
- Recommending `auto.offset.reset=latest` without noting the data-loss implications documented for consumers

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Kafka docs as the final authority.
