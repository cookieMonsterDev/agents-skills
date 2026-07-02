---
name: aws-dynamodb-docs
description: Use when users ask how to create, model, query, index, secure, scale, stream, replicate, back up, cache, or troubleshoot Amazon DynamoDB tables and items, including partition keys, sort keys, GSIs, LSIs, on-demand or provisioned capacity, DynamoDB Streams, global tables, transactions, TTL, PartiQL, DAX, IAM access, or DynamoDB API behavior, especially when they need official Amazon DynamoDB documentation, exact links, or docs-grounded guidance.
---

Amazon DynamoDB questions are easy to answer from stale memory or relational-database assumptions. Use this skill to ground answers in the official Amazon DynamoDB documentation and return the closest authoritative page instead of generic NoSQL advice.

## When to Use

Use this skill when the request is about:

- DynamoDB concepts: tables, items, attributes, partition keys, and sort keys
- Creating tables, reading and writing items, and item sizes or limits
- Data modeling, access patterns, single-table design, and denormalization
- Global secondary indexes (GSI) and local secondary indexes (LSI)
- On-demand capacity, provisioned throughput, RCUs, WCUs, and autoscaling
- Strongly consistent vs eventually consistent reads
- DynamoDB Streams, Lambda triggers, and change data capture
- Global tables, multi-Region replication, and disaster recovery
- Transactions, conditional writes, and optimistic locking patterns
- TTL, backups, point-in-time recovery, and exports to Amazon S3
- Security: IAM policies, fine-grained access control, and encryption
- DynamoDB Accelerator (DAX), PartiQL, and NoSQL Workbench
- Integrations with Lambda, AppSync, API Gateway, Kinesis, and zero-ETL
- Troubleshooting throttling, hot partitions, access denied, and capacity errors

Do not use this skill for:

- AWS CLI install, profiles, or global CLI options. Use `aws-cli-docs` instead.
- IAM policy language fundamentals unrelated to DynamoDB resources. Use `aws-iam-docs` for general IAM concepts.
- Amazon DocumentDB or other document databases when the question is not about DynamoDB.
- ScyllaDB Alternator or self-managed Cassandra/CQL behavior. Use `scylladb-docs` or `cassandra-docs` instead.
- Third-party DynamoDB-compatible tools unless the question maps to documented DynamoDB API behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Data modeling and access patterns
- Reads, writes, queries, and indexes
- Capacity modes, throttling, and performance
- Streams, events, and Lambda integrations
- Global tables and resilience
- Transactions, TTL, and conditional updates
- Backup, restore, export, and migration
- Security, encryption, and access control
- DAX, PartiQL, and developer tooling
- Troubleshooting and service quotas

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Amazon DynamoDB docs first

- Treat `docs.aws.amazon.com/amazondynamodb/latest/developerguide` as the source of truth for Amazon DynamoDB.
- Prefer the developer guide at <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>.
- Prefer the API reference at <https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html> for operation-level details.
- Search with the user's exact terms plus focused DynamoDB phrases such as `partition key`, `GSI`, `on-demand capacity`, `DynamoDB Streams`, `global tables`, or `conditional write`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For access denied errors, check IAM, resource-based policies, and fine-grained access control docs before guessing permission fixes.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API operations, open the specific API reference page when request/response fields matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Amazon DynamoDB docs links, not just the docs homepage.
- Only provide table definitions, IAM policies, or SDK examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Amazon DynamoDB docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example table design, policy, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is Amazon DynamoDB? and core components before API reference pages.
- For modeling questions, prefer best practices and table design docs before inventing schemas.
- For index questions, distinguish GSI and LSI behavior, projections, and sparse indexes.
- For capacity questions, distinguish on-demand and provisioned modes before recommending autoscaling.
- For stream questions, distinguish DynamoDB Streams from Kinesis Data Streams for DynamoDB.
- For resilience questions, check global tables, PITR, and on-demand backup docs together.
- For CLI syntax-only questions, cross-check `aws-cli-docs` command reference for `aws dynamodb`.
- Note item size limits, hot partition risks, and eventually consistent read defaults.

## Common Mistakes

- Answering from memory without verifying the current Amazon DynamoDB docs
- Linking the DynamoDB landing page when a narrower developer guide or API page exists
- Designing relational schemas with JOIN assumptions instead of access-pattern-first modeling
- Confusing GSI and LSI capacity, key schema, and size limits
- Treating throttling as an IAM problem without checking capacity mode and hot partition docs
- Mixing DynamoDB Streams behavior with Kinesis Data Streams for DynamoDB
- Recommending scans for production query patterns without checking best practices

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Amazon DynamoDB docs as the final authority.
