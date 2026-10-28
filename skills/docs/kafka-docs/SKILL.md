---
name: kafka-docs
description: Official Apache Kafka 4.3 documentation, answered with links to the exact pages. Use for any Kafka question, including topics and partitions, producers and consumer groups, KRaft and broker operations, Kafka Connect, Kafka Streams, or security with ACLs, SASL and SSL.
---

# Apache Kafka Docs

Kafka answers drift toward ZooKeeper-era patterns, so ground each one in the live Apache Kafka 4.3 docs at <https://kafka.apache.org/43/>, not memory, and link the exact page behind every claim.

Route AWS CLI commands against MSK to `aws-cli-docs`, and Redis streams or pub/sub to `redis-docs`. MSK console operations belong to AWS's own docs, and third-party client library APIs to their own docs, unless the question turns on core Kafka protocol, configuration or behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `kafka.apache.org/43` with the user's exact terms plus Kafka vocabulary such as `min.insync.replicas`, `acks`, `isolation.level`, `KRaft`, `rebalance`, or `cleanup.policy`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and configuration or client code only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Another Kafka version: say you are using the 4.3 docs and offer to switch.
- Concepts: Introduction and Design, before the configuration reference.
- Topic management: Basic Kafka Operations and the topic configuration docs.
- Producer reliability: the producer configs (`acks`, `retries`, `enable.idempotence`).
- Consumer lag or rebalance: tell consumer configs apart from broker and group configs.
- Security: Security Overview, then the listener, SSL, SASL, or ACL pages.
- KRaft or ZooKeeper: the KRaft operations docs and the KRaft vs ZooKeeper guide.
- Stream processing: tell Kafka Streams apart from plain consumer/producer usage.

## Gotchas

- Ground cluster-metadata advice in the KRaft docs; ZooKeeper-only guidance is legacy.
- Topic retention decides when messages are deleted; consuming a message leaves it in the log.
- Keep Kafka Connect connector settings apart from core broker and client configs.
- Pair any `auto.offset.reset=latest` recommendation with the data-loss implications documented for consumers.
