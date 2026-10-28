---
name: postgresql-16-docs
description: Official PostgreSQL 16 documentation, answered with links to the exact pages. Use for PostgreSQL 16 questions, or version-unspecified ones when 16 is the target, including SQL and indexes, transactions and locking, configuration, roles and authentication, backup and replication, or PL/pgSQL and extensions.
---

# PostgreSQL 16 Docs

PostgreSQL settings and syntax change between major versions, so ground each answer in the live PostgreSQL 16 docs at <https://www.postgresql.org/docs/16/>, not memory, and link the exact page behind every claim.

Route PostgreSQL 17 and 18 questions to `postgresql-17-docs` and `postgresql-18-docs`, MySQL to `mysql-docs`, and MongoDB to `mongodb-docs`. When the user names no version, say you are answering from PostgreSQL 16 and offer to switch. ORM configuration belongs to the framework's own docs, and managed-cloud consoles to the provider's docs, unless the question turns on PostgreSQL behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `postgresql.org/docs/16` with the user's exact terms plus PostgreSQL vocabulary such as `MVCC`, `logical replication`, `runtime-config`, `EXPLAIN`, or `pg_hba.conf`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and SQL, `postgresql.conf` or `pg_hba.conf` examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version-specific behavior: the PostgreSQL 16 release notes.
- Performance: the performance tips, parallel query, indexes, and planner statistics docs.
- Locking or transactions: the concurrency control and transaction processing docs.
- Access control: the client authentication, database roles, and privileges docs.
- Replication: tell physical replication, logical replication, and logical decoding apart before answering.
- Extensions or procedural languages: the server programming docs and the contrib appendix.

## Gotchas

- Check settings and syntax against the PostgreSQL 16 release notes; newer major versions add settings and syntax that 16 lacks.
- Check ORM or driver bugs against the client interface docs before attributing them to the server.
- Use `GENERATED ... AS IDENTITY` for new designs; the docs treat `SERIAL` as a legacy pattern.
