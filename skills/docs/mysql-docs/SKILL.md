---
name: mysql-docs
description: Official MySQL documentation, answered with links to the exact pages. Use for any MySQL question, including SQL and the optimizer, InnoDB, users and privileges, replication, Group Replication and InnoDB Cluster, connectors, or MySQL Shell, Router, NDB Cluster and HeatWave.
---

# MySQL Docs

MySQL behavior drifts between the 8.0, 8.4 and 9.7 LTS series and the calendar-versioned Innovation releases, so ground each answer in the live Reference Manual at <https://dev.mysql.com/doc/refman/9.7/en/>, not memory, and link the exact page behind every claim.

Route PostgreSQL to `postgresql-16-docs`, `postgresql-17-docs` or `postgresql-18-docs` by version, and MongoDB modeling or aggregation to `mongodb-docs`. Amazon RDS or Aurora console operations belong to AWS's own docs, and MariaDB-only features to MariaDB's, unless the question turns on MySQL behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `dev.mysql.com/doc` with the user's exact terms plus MySQL vocabulary such as `InnoDB`, `binary log`, `Group Replication`, `EXPLAIN`, or `privileges`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and SQL, `my.cnf` or privilege examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: start in the 9.7 Reference Manual; when the user names another version, switch the path segment (`9.7`, `8.4`, `8.0`, `26.10`) before answering.
- Product: tell Community Server docs apart from the HeatWave, Enterprise, NDB Cluster, and Router guides.
- Connector or API questions: the Connectors & APIs docs for the user's language, not the server Reference Manual.
- Performance: the optimization and `EXPLAIN` docs.
- Locking or transactions: the InnoDB and transaction docs.
- Access control: the account management and privileges docs, plus the enterprise security docs for Enterprise features.
- Replication: tell asynchronous replication, Group Replication, and InnoDB Cluster apart before answering.

## Gotchas

- 9.7 is the current LTS series, 8.4 and 8.0 are older LTS series, and 5.7 is end-of-life; check the release notes before carrying behavior across them.
- Since 9.7, Innovation and LTS releases use `YY.M` calendar versions, so `26.10` (October 2026) is newer than `9.7`.
- Check syntax and semantics in the MySQL manual; PostgreSQL's differ.
- Check current guidance before recommending a storage engine or authentication plugin; some are deprecated.
