---
name: rabbitmq-docs
description: Official RabbitMQ documentation, answered with links to the exact pages. Use for any RabbitMQ question, including AMQP 0-9-1 and AMQP 1.0, exchanges and queues, quorum queues and streams, clustering, the management UI and plugins, or production operations.
---

# RabbitMQ Docs

RabbitMQ answers drift with the 4.x removal of classic queue mirroring and with AMQP 0-9-1 tutorial patterns applied to AMQP 1.0, so ground each one in the live docs at <https://www.rabbitmq.com/docs>, not memory, and link the exact page behind every claim.

Route Apache Kafka topics, partitions or consumer groups to `kafka-docs`, Redis pub/sub to `redis-docs`, BullMQ job queues to `bullmq-docs`, and AWS CLI commands to `aws-cli-docs`. Amazon MQ console operations belong to AWS's own docs, and generic MQTT or STOMP questions to those protocols' docs, unless the question turns on RabbitMQ behavior or a plugin the RabbitMQ docs cover.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `rabbitmq.com/docs` with the user's exact terms plus RabbitMQ vocabulary such as `quorum queue`, `prefetch`, `dead letter`, `stream`, `management plugin`, or `virtual host`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and client code or `rabbitmqctl` examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Versions: the current documentation version (4.3), unless the user names another supported version.
- High availability: the quorum queue or stream docs; the classic mirroring `/docs/ha` page is gone in 4.x.
- Protocol behavior: settle AMQP 0-9-1 or AMQP 1.0 first.
- Learning messaging patterns: Getting Started and the official RabbitMQ tutorials.
- Routing: tell direct, fanout, topic, and headers exchanges apart.
- Reliability: the publisher confirms, consumer acknowledgements, and quorum queue docs.
- Operations: How to Manage RabbitMQ, before guessing config file locations.
- Monitoring: the monitoring and management plugin docs.
- Streams: the stream-specific docs, not classic queue tutorials.

## Gotchas

- Keep AMQP 0-9-1 tutorial APIs apart from AMQP 1.0 behavior.
- Recommend quorum queues for high availability; classic mirrored queues were removed in 4.x.
- Check the memory and disk alarm docs before recommending unbounded queues.
- RabbitMQ streams differ from Kafka-style partitioned logs; read the stream docs before comparing them.
