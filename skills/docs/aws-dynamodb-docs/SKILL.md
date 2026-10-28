---
name: aws-dynamodb-docs
description: Official Amazon DynamoDB documentation, answered with links to the exact pages. Use for any DynamoDB question, including data modeling, keys and secondary indexes, capacity and throttling, Streams and global tables, transactions and TTL, backups, security, or DAX and PartiQL.
---

# Amazon DynamoDB Docs

DynamoDB answers drift with every release and relational habits mislead them, so ground each answer in the live docs at <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>, not memory, and link the exact page behind every claim.

Route AWS CLI install, profiles and global options to `aws-cli-docs`, IAM policy language unrelated to DynamoDB resources to `aws-iam-docs`, and ScyllaDB Alternator or Cassandra/CQL behavior to `scylladb-docs` or `cassandra-docs`. Amazon DocumentDB and third-party DynamoDB-compatible tools belong to their own docs unless the question turns on documented DynamoDB API behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/amazondynamodb/latest` with the user's exact terms plus DynamoDB vocabulary such as `partition key`, `GSI`, `on-demand capacity`, `DynamoDB Streams`, `global tables`, or `conditional write`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and table designs, policies or SDK code only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Operation request and response fields: the API reference at <https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html>.
- Data modeling: the best practices and table design pages, before inventing a schema.
- Indexes: the GSI and LSI pages, covering projections and sparse indexes.
- Capacity: tell on-demand from provisioned mode before recommending auto scaling.
- Streams: tell DynamoDB Streams from Kinesis Data Streams for DynamoDB.
- Resilience: the global tables, point-in-time recovery, and on-demand backup pages together.
- Access denied: the IAM, resource-based policy, and fine-grained access control pages, before guessing permission fixes.
- `aws dynamodb` syntax: cross-check `aws-cli-docs`.

## Gotchas

- Model from access patterns first; relational schemas with JOIN assumptions do not fit DynamoDB.
- GSIs and LSIs differ in capacity, key schema, and size limits.
- Investigate throttling through capacity mode and hot partitions before IAM.
- DynamoDB Streams and Kinesis Data Streams for DynamoDB behave differently; name which one applies.
- Reads are eventually consistent by default.
- Serve production access patterns as the best practices pages describe, with queries rather than scans.
- Check the documented item size limits and hot partition risks in any design.
