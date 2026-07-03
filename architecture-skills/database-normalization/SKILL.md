---
name: database-normalization
description: Explains and applies the database normal forms (1NF, 2NF, 3NF, BCNF, 4NF, 5NF) and strategic denormalization, with worked examples in PostgreSQL, MySQL, SQLite, MongoDB, Cassandra, ScyllaDB, and DynamoDB. Use when users ask about normal forms, functional/multivalued/join dependencies, anomalies (insertion/update/deletion), schema design and refactoring, when they need help deciding how far to normalize a schema, or when they want a normalization concept translated into a specific database's modeling idioms (relational tables, MongoDB embedding/referencing, Cassandra/ScyllaDB query-driven tables, DynamoDB single-table design).
---

# Database Normalization

Ground normalization answers in the reference files bundled with this skill instead of improvising definitions. Each normal form has a reference file explaining it and a folder of worked examples across popular databases.

## When to Use

- The user names a normal form directly ("what is BCNF", "show me 3NF in PostgreSQL")
- The user describes an anomaly that maps to a missing normal form ("if I delete the last order for a customer I lose their address")
- The user asks whether a schema is normalized, or asks to normalize/denormalize a schema
- The user asks how a normalization concept applies (or doesn't) in a non-relational database ("does 1NF matter in MongoDB?", "how do I avoid joins in DynamoDB?")
- The user wants existing tables or documents refactored toward or away from a normal form

## Workflow

1. **Identify the normal form(s)** from the user's question using the catalog below. If the user describes symptoms (repeating groups, partial/transitive dependency, update anomalies) rather than naming a form, diagnose which form addresses it.
2. **Read the reference file** at `references/<form>.md` for the definition, the dependency it eliminates, the anomalies it prevents, and when going further stops paying off.
3. **Read the database example** at `examples/<form>/<database>.<ext>` when the user works in (or asks for) a specific database. Adapt it to their schema rather than pasting the generic example verbatim.
4. **Answer** with: what the form requires, what anomaly it prevents, and a schema/model adapted to the user's context — including whether that database's idioms call for staying normalized or deliberately denormalizing.

If the user's schema is already anomaly-free at a given form, say so — do not push further normalization for its own sake. Every step past 3NF/BCNF is a judgment call against real anomalies, not a checklist to exhaust.

## Normal Form Catalog

### Core Forms

The forms nearly every relational schema should reach; each eliminates a specific class of anomaly caused by a specific kind of dependency.

| Form | Eliminates                                                                | Reference                                                            |
| ---- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1NF  | Repeating groups and non-atomic (multi-valued) column values              | [references/first-normal-form.md](references/first-normal-form.md)   |
| 2NF  | Partial dependency of a non-key attribute on part of a composite key      | [references/second-normal-form.md](references/second-normal-form.md) |
| 3NF  | Transitive dependency of a non-key attribute on another non-key attribute | [references/third-normal-form.md](references/third-normal-form.md)   |

### Advanced Forms

Forms that close gaps 3NF leaves open — situations 3NF permits but that still cause anomalies. Most production schemas stop at 3NF/BCNF; 4NF and 5NF apply to specific dependency shapes.

| Form | Eliminates                                                                                             | Reference                                                                    |
| ---- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| BCNF | Every functional dependency not sourced from a candidate key (a 3NF gap when candidate keys overlap)   | [references/boyce-codd-normal-form.md](references/boyce-codd-normal-form.md) |
| 4NF  | Multivalued dependencies — independent multi-valued facts forced into one table                        | [references/fourth-normal-form.md](references/fourth-normal-form.md)         |
| 5NF  | Join dependencies not implied by candidate keys — lossy binary decompositions of an n-ary relationship | [references/fifth-normal-form.md](references/fifth-normal-form.md)           |

### Beyond Normalization

The deliberate, informed reversal of normalization for a specific performance or access-pattern reason — the default posture in most NoSQL databases.

| Topic           | Trades                                                                           | Reference                                                      |
| --------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Denormalization | Write-time consistency and storage for read-time speed (fewer joins/round trips) | [references/denormalization.md](references/denormalization.md) |

## Examples

Each form has a folder `examples/<form>/` with a worked example per database, named `<database>.<ext>`:

| Database   | File            | Notes                                                                                                                                               |
| ---------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| PostgreSQL | `postgres.sql`  | Runnable DDL/DML; uses `psql`-compatible SQL (identity columns, `CHECK`, `jsonb` where relevant)                                                    |
| MySQL      | `mysql.sql`     | Runnable DDL/DML; calls out `AUTO_INCREMENT`, engine (InnoDB), and syntax that diverges from PostgreSQL                                             |
| SQLite     | `sqlite.sql`    | Runnable DDL/DML; uses `INTEGER PRIMARY KEY AUTOINCREMENT`, `PRAGMA foreign_keys`, and a summary table instead of materialized views where relevant |
| MongoDB    | `mongodb.js`    | `mongosh` script; shows the document shape and when embedding vs. referencing plays the role a normal form plays in SQL                             |
| Cassandra  | `cassandra.cql` | CQL script; shows the query-driven, denormalized-by-default table design and where atomicity/dependency concerns still apply                        |
| ScyllaDB   | `scylladb.cql`  | CQL script (compatible with Cassandra); same query-driven modeling posture as Cassandra with ScyllaDB-specific operational notes in the reference files |
| DynamoDB   | `dynamodb.md`   | Walkthrough with item JSON and access patterns (no native query language); shows single-table design as the intentional counterpoint to normalizing |

Normalization is a relational concept built on functional/multivalued/join dependencies. The PostgreSQL, MySQL, and SQLite examples are direct applications of a form. The MongoDB, Cassandra, ScyllaDB, and DynamoDB examples show the _analogous_ problem (an anomaly-causing shape) and that database's idiomatic answer, which is frequently "duplicate the data on purpose" rather than "add another table." The reference files explain why that's a rational trade-off there, not a violation of best practice.

## Answering Guidelines

- Name the dependency (functional, partial, transitive, multivalued, join) causing the anomaly — "normalize this" without naming the dependency doesn't help the user recognize the next case themselves.
- State the anomaly a form prevents (insertion, update, or deletion anomaly) in terms of the user's own schema, not the abstract definition.
- Don't recommend normalizing past the point where it prevents a real anomaly in the user's data; 4NF and 5NF are narrow tools for narrow dependency shapes, not a ladder to climb by default.
- For MongoDB, Cassandra, ScyllaDB, and DynamoDB, lead with access patterns and consistency requirements, not with "how do I make this look like a normalized relational schema" — read the matching reference's database-specific notes before answering.
- When comparing forms, read both reference files and contrast the dependency each one targets, not just "which number is higher."
