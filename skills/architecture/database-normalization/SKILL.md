---
name: database-normalization
description: Database normal forms (1NF to 5NF, BCNF) and deliberate denormalization, with a reference per form and worked examples per database. Use when a question names a normal form or a functional, multivalued, or join dependency, describes an insertion, update, or deletion anomaly, asks to normalize, denormalize, or review a schema, or asks how normalization applies in MongoDB, Cassandra, ScyllaDB, or DynamoDB.
---

# Database Normalization

Ground every normalization answer in this skill's reference files, not in improvised definitions. Each form exists to remove a real **anomaly**: normalize exactly as far as the user's data has anomalies to remove. Most schemas stop at 3NF/BCNF; 4NF and 5NF are narrow tools for specific dependency shapes.

## Workflow

1. **Identify the normal form(s)** in the catalog below. When the user describes symptoms instead of naming a form, trace each anomaly to the dependency causing it (functional, partial, transitive, multivalued, join) and the form that eliminates it. Done when every anomaly is traced to a named dependency and form, or the schema is shown anomaly-free at the form in question; then say so.
2. **Read each identified reference** at `references/<form>.md` in full, including its Database Notes. When comparing forms, read every one compared and contrast the dependency each one targets.
3. **Read the database example** at `examples/<form>/<file>` for the user's database (file names in the table below).
4. **Answer** with the dependency, the anomaly it causes stated in terms of the user's own schema, and a schema or model adapted to it. For MongoDB, Cassandra, ScyllaDB, and DynamoDB, lead with access patterns and consistency requirements, and say whether that database's idiom calls for staying normalized or denormalizing on purpose. Done when every identified form has all three parts.

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

| Database   | File            | Contents                                                   |
| ---------- | --------------- | ---------------------------------------------------------- |
| PostgreSQL | `postgres.sql`  | Runnable DDL/DML                                           |
| MySQL      | `mysql.sql`     | Runnable DDL/DML, noting MySQL-specific syntax             |
| SQLite     | `sqlite.sql`    | Runnable DDL/DML                                           |
| MongoDB    | `mongodb.js`    | `mongosh` script: embedding vs. referencing                |
| Cassandra  | `cassandra.cql` | CQL script: query-driven tables                            |
| ScyllaDB   | `scylladb.cql`  | CQL script: query-driven tables                            |
| DynamoDB   | `dynamodb.md`   | Walkthrough with item JSON and access patterns             |

The relational examples apply each form directly. The MongoDB, Cassandra, ScyllaDB, and DynamoDB examples show the analogous anomaly-causing shape and that database's idiomatic answer, which is often duplicating data on purpose: a rational trade-off there, explained in each reference's Database Notes.
