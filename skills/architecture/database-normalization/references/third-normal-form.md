# Third Normal Form (3NF)

**Category:** Core Form

## Intent

Require every non-key attribute to depend on the key, the whole key, and nothing but the key. 3NF eliminates **transitive dependencies**: a non-key attribute that depends on another non-key attribute rather than depending on the key directly.

## Problem

- `orders(order_id PK, customer_id, customer_name, customer_city, customer_zip)` — `customer_name`, `customer_city`, and `customer_zip` depend on `customer_id`, which is itself a non-key attribute of `orders`. They depend on the key only _transitively_, through `customer_id`.
- **Update anomaly:** a customer moving to a new city requires updating every order row they've ever placed, or the rows disagree about where the customer lives.
- **Insertion anomaly:** a new customer with no orders yet has nowhere to record their name or address.
- **Deletion anomaly:** deleting a customer's one and only order deletes their contact information along with it.

## Structure

- **Split by the transitive source** — attributes that depend on a non-key attribute move into a table keyed by that attribute (`customers(customer_id PK, name, city, zip)`).
- **A foreign key replaces the copied attributes** — `orders` keeps `customer_id` as a foreign key and drops the columns that only described the customer, not the order.

## When to Use

- Any table where a non-key column's value is fully determined by another non-key column, not by the primary key itself — a strong signal is a column whose meaning has nothing to do with the table's own subject (customer address data sitting in an orders table).
- Whenever "if I update column A, do I also need to update column B on this same row and every other row that shares A's value?" is true.

## When Not to Use

- If the "dependent" attribute is actually a fact about the row itself, not a copy of a fact from elsewhere, it's not transitive — e.g., `shipped_at` on `orders` depends on the order, not on the customer, even though shipping speed correlates with the customer's region.
- A deliberate, named denormalization (a reporting table joining orders and customers ahead of time for a read-heavy dashboard) is not a 3NF violation in the OLTP schema — it's a separate derived structure; see [[denormalization]].

## Trade-offs

- **Pros:** each entity's facts live in exactly one place; updating a customer's address is one write, and it's immediately correct everywhere that customer is referenced.
- **Cons:** reading "this order with the customer's name and city" costs a join instead of a single-table read; this is the most common point where the normalization/read-latency trade-off starts to matter and where teams start reaching for a cache, a materialized view, or a denormalized read model.

## Database Notes

- **PostgreSQL:** `CREATE TABLE customers (...)` plus a `FOREIGN KEY (customer_id) REFERENCES customers(customer_id)` on `orders` is the direct fix. A materialized view (`CREATE MATERIALIZED VIEW`) is PostgreSQL's built-in way to get the read-side benefit of the pre-3NF flat table back, refreshed on a schedule, without keeping the base tables denormalized.
- **MySQL:** same fix, same `FOREIGN KEY` mechanism (InnoDB only — `MyISAM` does not enforce foreign keys). MySQL has no built-in materialized view; the common substitute is a summary table maintained by a trigger or a scheduled `INSERT ... ON DUPLICATE KEY UPDATE ... SELECT`.
- **SQLite:** same `FOREIGN KEY` split as PostgreSQL/MySQL with `PRAGMA foreign_keys = ON`. No materialized view — use a summary table kept in sync by triggers or application code for read-heavy denormalized paths.
- **MongoDB:** this is the canonical embedding-versus-referencing decision. Embedding customer name/city directly in every order document reintroduces the transitive-dependency anomaly (the customer's data is now copied into every one of their orders and must be kept in sync on every change). MongoDB's guidance is to _reference_ the customer (store `customer_id`, `$lookup` when needed) when customer data changes independently and is shared across many orders, and to embed only a small, intentionally-frozen subset (the Extended Reference Pattern, same as in [[second-normal-form]]) for fields that should reflect the value _at order time_ rather than the live value.
- **Cassandra / ScyllaDB:** because a CQL query can't join `orders` to `customers`, any table built to answer "show me this order with the customer's name" must duplicate the customer's name into that table on write. This isn't a mistake, it's the model — but it means an update to a customer's name requires writing to every denormalized table that copied it (materialized views automate exactly this fan-out for a single source table, with operational caveats, so many teams maintain the fan-out in application code instead).
- **DynamoDB:** the transitive-dependency shape maps directly onto the single-table design decision of whether to store customer attributes on the order item. AWS's own guidance is to denormalize the frequently-read, slowly-changing customer fields (name, tier) onto the order item to avoid a second `GetItem` round trip, and to accept that a customer name change requires updating (or accepting staleness in) every order item that copied it — see [[denormalization]] for the general trade this reflects.

## Examples

- [examples/third-normal-form/postgres.sql](../examples/third-normal-form/postgres.sql)
- [examples/third-normal-form/mysql.sql](../examples/third-normal-form/mysql.sql)
- [examples/third-normal-form/sqlite.sql](../examples/third-normal-form/sqlite.sql)
- [examples/third-normal-form/mongodb.js](../examples/third-normal-form/mongodb.js)
- [examples/third-normal-form/cassandra.cql](../examples/third-normal-form/cassandra.cql)
- [examples/third-normal-form/scylladb.cql](../examples/third-normal-form/scylladb.cql)
- [examples/third-normal-form/dynamodb.md](../examples/third-normal-form/dynamodb.md)

## Related Forms

- **Second Normal Form ([[second-normal-form]])** eliminates dependency on _part_ of a composite key; 3NF eliminates dependency on _another non-key attribute_ — the two are the composite-key and single-key versions of the same underlying problem.
- **Boyce-Codd Normal Form ([[boyce-codd-normal-form]])** is a stricter version of 3NF that closes a gap 3NF leaves open when a table has more than one candidate key.
