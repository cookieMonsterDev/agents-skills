---
name: postgresql-17-docs
description: Use when users ask how to write, explain, configure, tune, secure, replicate, extend, or troubleshoot PostgreSQL 17 SQL, schemas, indexes, transactions, roles, authentication, backups, replication, monitoring, procedural languages, extensions, or server settings, especially when they need official PostgreSQL documentation, exact links, or docs-grounded SQL and configuration guidance.
---

PostgreSQL questions are easy to answer from stale memory or the wrong major version. Use this skill to ground answers in the official PostgreSQL 17 documentation and return the closest authoritative page instead of generic database advice.

## When to Use

Use this skill when the request is about:

- PostgreSQL concepts, terminology, or product boundaries
- SQL syntax, DDL, DML, queries, data types, functions, operators, or type conversion
- Indexes, full text search, concurrency, MVCC, locking, or isolation levels
- Query performance, planner behavior, parallel query, or statistics
- Installation, server setup, configuration parameters, or runtime operation
- Client authentication, roles, privileges, databases, schemas, or localization
- Routine maintenance, vacuuming, backups, restore, or WAL
- High availability, physical replication, logical replication, or failover
- Monitoring, activity views, logs, or troubleshooting server behavior
- Client interfaces such as libpq, large objects, ECPG, or the information schema
- Server programming: triggers, event triggers, rules, PL/pgSQL, SPI, or extensions
- SQL command reference, client utilities, or server applications
- PostgreSQL 17 release notes, new features, or version-specific behavior

Do not use this skill for:

- A different PostgreSQL major version when the user explicitly needs that version. Say which version you are using and offer to switch docs if needed.
- Application framework ORM configuration unless the question is specifically about PostgreSQL behavior or SQL.
- Managed cloud database console operations when the question is about provider-specific UI rather than PostgreSQL docs.
- Non-PostgreSQL databases such as MySQL, SQLite, or MongoDB.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started or tutorials
- SQL language and data modeling
- Query writing and performance
- Server administration and configuration
- Security, roles, and authentication
- Backup, restore, and reliability
- Replication and high availability
- Monitoring and troubleshooting
- Client interfaces and drivers
- Server programming and extensions
- SQL or utility reference
- Internals, limits, or appendix material

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official PostgreSQL docs first

- Treat `postgresql.org/docs/17` as the source of truth for PostgreSQL 17.
- Prefer pages under <https://www.postgresql.org/docs/17/>.
- Search with the user's exact terms plus a focused PostgreSQL phrase such as `MVCC`, `logical replication`, `runtime-config`, `EXPLAIN`, or `pg_hba.conf`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For version-specific behavior, check the PostgreSQL 17 release notes before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact PostgreSQL docs links, not just the docs homepage.
- Only provide SQL, `postgresql.conf`, or `pg_hba.conf` examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to PostgreSQL 17 docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example SQL or configuration, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer tutorial or overview pages before deep reference pages.
- For syntax questions, prefer SQL syntax, DDL, DML, queries, or the SQL command reference.
- For performance questions, prefer performance tips, parallel query, indexes, and planner statistics docs before guessing tuning advice.
- For locking or transaction questions, prefer concurrency control and transaction processing docs.
- For security questions, prefer client authentication, database roles, and privilege docs.
- For replication questions, distinguish physical replication, logical replication, and logical decoding before answering.
- For extension or procedural language questions, prefer server programming docs and the contrib appendix.
- If the user asks for a beginner walkthrough, start with the tutorial instead of a raw reference page.

## Common Mistakes

- Answering from memory without verifying the current PostgreSQL 17 docs
- Linking the PostgreSQL docs landing page when a narrower page exists
- Mixing up physical replication, logical replication, and logical decoding
- Suggesting settings or syntax from a different PostgreSQL major version without checking release notes
- Treating ORM or driver bugs as PostgreSQL server behavior without checking the relevant client interface docs
- Recommending `SERIAL` or other legacy patterns when the docs recommend `GENERATED ... AS IDENTITY` for new designs

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live PostgreSQL docs as the final authority.
