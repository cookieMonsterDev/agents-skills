# Denormalization

**Category:** Beyond Normalization

## Intent

Deliberately reintroduce redundancy that normalization removed, in order to trade write-time consistency and storage for read-time speed — fewer joins, fewer round trips, fewer partitions touched per query. Denormalization done well is a _named, scoped_ decision made after normalizing, not a schema that was never normalized in the first place.

## Problem

- A fully normalized schema answers "what are this order's items, with product names and the customer's name" only by joining `orders`, `order_items`, `products`, and `customers` — correct, but every read pays that join cost.
- At small scale the join is free. At scale, or on a system where reads vastly outnumber writes, or where a single logical read must not fan out across network hops (a distributed database where "join" means "cross-partition scatter-gather"), the join cost becomes the bottleneck, not the anomaly the join was avoiding.
- Some databases don't offer a join at all as an efficient primitive (Cassandra, DynamoDB), or offer one that only works within a single document (MongoDB) — for these, some amount of denormalization isn't an optimization, it's the only way to answer a multi-entity query at all.

## Structure

- **A source of truth stays normalized (or close to it)** — the tables/collections where writes land and where the anomaly-preventing properties of normalization still apply.
- **A denormalized copy serves reads** — a summary table, a materialized view, an embedded subset of another entity's fields, or a second table/collection built for one specific query, populated from the source of truth.
- **An explicit synchronization mechanism** — a scheduled refresh, a trigger, a change-data-capture stream, an application-level write to both places, or acceptance of eventual consistency — because the redundant copy does not automatically stay correct the way a normalized schema's single copy does.

## When to Use

- A specific, measured read path is too slow because of joins or cross-partition fan-out, and the alternative (better indexing, a smaller join, caching) doesn't close the gap.
- The database's native query model has no efficient multi-entity join (Cassandra, DynamoDB) — here, denormalizing per access pattern isn't optional, it's how the database is meant to be used.
- A value should be captured as a historical snapshot rather than a live reference (`price_at_purchase` on an order line) — this looks like denormalization but is really a distinct fact that happens to start out equal to another fact; see the note on this in [[second-normal-form]].

## When Not to Use

- As a default starting posture in a relational OLTP schema — denormalize a specific, identified hot path after normalizing, not the whole schema up front "for performance," which is premature optimization at the cost of every anomaly normalization would have prevented.
- When the write volume to the redundant copy, or the cost of the copies drifting out of sync, would cause more operational pain than the join it was meant to avoid — denormalization is a trade, and the write/consistency side of that trade is real, not free.
- To paper over a missing index or a bad query plan — check those first; a join that's slow because of a missing index is not evidence that the join itself is the problem.

## Trade-offs

- **Pros:** fewer joins/round trips per read, often the only way to get single-digit-millisecond reads at scale or in a distributed store; can shape data exactly for one access pattern instead of general-purpose.
- **Cons:** every redundant copy is a place the data can go stale or disagree with the source of truth; every write that should update all copies is a place a bug or a missed step can introduce an anomaly identical to the ones normalization existed to prevent; more storage; the schema now encodes _how the data is read_, which makes it more brittle to new, un-anticipated access patterns.

## Database Notes

- **PostgreSQL:** `CREATE MATERIALIZED VIEW` is the built-in, explicit form — a denormalized, queryable snapshot refreshed with `REFRESH MATERIALIZED VIEW` (optionally `CONCURRENTLY`), so the redundancy and its staleness window are both visible in the schema rather than hidden in application code. Regular (non-materialized) views give the _appearance_ of a denormalized read shape without actually duplicating storage, and are the right first choice when the join itself, not the storage, is what's expensive to write repeatedly.
- **MySQL:** no native materialized view; the idiomatic substitute is a real table kept in sync by triggers on the source tables, or a scheduled job (`EVENT`) that rebuilds a summary table. This makes the synchronization mechanism an explicit, auditable piece of schema rather than an implicit assumption.
- **SQLite:** no materialized view either; use a summary table populated by triggers on the source tables or rebuilt by application code on a schedule. Common in mobile and embedded apps where a single-file database serves a read-heavy local cache.
- **MongoDB:** the Extended Reference Pattern (embed a small, frequently-needed subset of a referenced document's fields alongside the reference itself) and the Subset Pattern (embed only the most relevant N items of an unboundedly large array, referencing the rest) are MongoDB's named vocabulary for exactly this trade — embed what's read together and changes rarely, reference what's large, shared, or changes independently. Most production MongoDB schemas are a deliberate mix of both within the same document.
- **Cassandra:** denormalization is not an exception here — it's the baseline modeling strategy. Cassandra data modeling starts from the queries the application needs to run, then builds one table per query, duplicating whatever data each query needs so it can be satisfied by reading a single partition with no join. Materialized views automate keeping a denormalized table in sync with a base table, but have known operational caveats (repair and consistency issues in some versions), so many teams instead maintain the duplication explicitly in application code or via a stream processor.
- **ScyllaDB:** same query-driven, denormalize-by-default posture as Cassandra. ScyllaDB materialized views have their own operational characteristics; many teams prefer explicit write-time duplication or a stream processor for fan-out updates.
- **DynamoDB:** single-table design is denormalization taken to its logical conclusion — related entities that would be separate, normalized tables in SQL are stored as items sharing a partition key (an "item collection") specifically so one `Query` can retrieve all of them without a join, and attributes needed by a read (e.g., a customer's name on every one of their order items) are copied onto each item rather than looked up. AWS's own guidance is explicit that this is the default, not a special case: design from access patterns first, and expect the same logical value to live in multiple items, keeping copies in sync via application code or DynamoDB Streams.

## Examples

- [examples/denormalization/postgres.sql](../examples/denormalization/postgres.sql)
- [examples/denormalization/mysql.sql](../examples/denormalization/mysql.sql)
- [examples/denormalization/sqlite.sql](../examples/denormalization/sqlite.sql)
- [examples/denormalization/mongodb.js](../examples/denormalization/mongodb.js)
- [examples/denormalization/cassandra.cql](../examples/denormalization/cassandra.cql)
- [examples/denormalization/scylladb.cql](../examples/denormalization/scylladb.cql)
- [examples/denormalization/dynamodb.md](../examples/denormalization/dynamodb.md)

## Related

- **Third Normal Form ([[third-normal-form]])** and **Fifth Normal Form ([[fifth-normal-form]])** describe the redundancy denormalization reintroduces on purpose — understanding the anomaly a form prevents is what lets you scope a denormalization to _only_ the read path that needs it, instead of losing the anomaly's protection everywhere.
- **First Normal Form ([[first-normal-form]])** — a deliberately-chosen array/JSON column for bag-of-values data is a narrow, single-column instance of the same trade discussed here.
