---
name: mysql-docs
description: Use when users ask how to write, explain, configure, tune, secure, replicate, back up, monitor, or troubleshoot MySQL SQL, schemas, indexes, transactions, users, privileges, InnoDB, replication, Group Replication, InnoDB Cluster, connectors, or server settings, especially when they need official MySQL documentation, exact links, or docs-grounded guidance.
---

MySQL questions are easy to answer from stale memory, PostgreSQL assumptions, or the wrong major version. Use this skill to ground answers in the official MySQL documentation and return the closest authoritative page instead of generic relational-database advice.

## When to Use

Use this skill when the request is about:

- MySQL concepts, terminology, or product boundaries
- SQL syntax, DDL, DML, queries, data types, functions, operators, or views
- Indexes, full-text search, transactions, isolation levels, or locking
- Query performance, optimizer behavior, EXPLAIN output, or statistics
- Installation, server setup, configuration options, or runtime operation
- Users, privileges, roles, authentication, encryption, or auditing
- Routine maintenance, backups, restore, or binary logs
- Replication, Group Replication, InnoDB Cluster, InnoDB ReplicaSet, or failover
- InnoDB storage engine behavior, tablespaces, and buffer pool tuning
- Client libraries and connectors: Connector/J, Connector/Python, Connector/NET, ODBC
- MySQL Shell, Workbench, Router, Operator for Kubernetes, or NDB Cluster
- MySQL HeatWave, Enterprise features, or cloud deployment guides
- Release notes, version-specific behavior, or error codes

Do not use this skill for:

- PostgreSQL SQL, schemas, or server behavior. Use the appropriate `postgresql-*-docs` skill instead.
- MongoDB document modeling or aggregation. Use `mongodb-docs` instead.
- Amazon RDS or Aurora console operations when the question is provider-specific rather than MySQL behavior.
- MariaDB-only features unless the user explicitly asks about MySQL-compatible behavior documented by Oracle.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and tutorials
- SQL language and data modeling
- Query writing and performance
- Server administration and configuration
- Security, users, and authentication
- Backup, restore, and reliability
- Replication and high availability
- Storage engines and InnoDB internals
- Connectors, APIs, and client tools
- Cloud, HeatWave, or Enterprise features
- NDB Cluster, Router, or Kubernetes operator
- Reference, error codes, or release notes

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official MySQL docs first

- Treat `dev.mysql.com/doc` as the source of truth for MySQL.
- Prefer the MySQL Reference Manual at <https://dev.mysql.com/doc/refman/8.4/en/> unless the user names a different major version.
- For version-specific behavior, switch the manual path segment (`8.4`, `8.0`, `5.7`, `9.7`, etc.) before answering.
- Search with the user's exact terms plus focused MySQL phrases such as `InnoDB`, `binary log`, `Group Replication`, `EXPLAIN`, `privileges`, or `replication`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For connector or API questions, prefer the Connectors & APIs docs rather than the server reference manual.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish Community Server docs from HeatWave, Enterprise, NDB Cluster, or Router guides before answering.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact MySQL docs links, not just the docs homepage.
- Only provide SQL, `my.cnf`, or privilege examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to MySQL docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example SQL or configuration, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer the tutorial or introduction before deep reference pages.
- For syntax questions, prefer SQL Statements, DDL, DML, or Queries chapters.
- For performance questions, prefer optimization and EXPLAIN docs before guessing tuning advice.
- For locking or transaction questions, prefer InnoDB and transaction docs.
- For security questions, prefer account management, privileges, and enterprise security docs.
- For replication questions, distinguish asynchronous replication, Group Replication, and InnoDB Cluster before answering.
- For connector questions, route by language under Connectors & APIs.
- If the user asks for a beginner walkthrough, start with the tutorial instead of a raw reference page.

## Common Mistakes

- Answering from memory without verifying the current MySQL docs
- Linking the MySQL docs landing page when a narrower manual or connector page exists
- Mixing MySQL 5.7, 8.0, and 8.4 behavior without checking release notes
- Applying PostgreSQL syntax or semantics to MySQL without checking the manual
- Confusing Group Replication, InnoDB Cluster, and traditional replication
- Recommending deprecated storage engines or authentication plugins without checking current guidance
- Treating MariaDB-specific behavior as MySQL docs behavior

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live MySQL docs as the final authority.
