# Second Normal Form (2NF)

**Category:** Core Form

## Intent

Require every non-key attribute to depend on the _whole_ primary key, not just part of it. 2NF only has teeth when the primary key is composite (two or more columns) — a table with a single-column key is automatically in 2NF once it's in 1NF.

## Problem

- A table keyed by `(order_id, product_id)` also stores `product_name` and `product_price` — but those depend only on `product_id`, not on the pair. This is a **partial dependency**: a non-key attribute depends on part of the key rather than the whole key.
- **Update anomaly:** if a product's name changes, every order line that ever ordered it needs the same update, or the data disagrees with itself across rows.
- **Insertion anomaly:** a new product with no orders yet has no `(order_id, product_id)` row to attach its name and price to, so it can't be recorded at all.
- **Deletion anomaly:** deleting the last order line for a product deletes the only place its name and price were recorded.

## Structure

- **Split by dependency source** — attributes that depend on the whole composite key stay in the original (junction/associative) table; attributes that depend on only part of the key move to a table keyed by that part.
- **A junction table with only true line-specific facts** — after the split, the composite-keyed table holds only attributes that genuinely vary per combination (e.g., `quantity`, `unit_price_at_purchase` if price is meant to be captured historically), plus foreign keys to the split-out tables.

## When to Use

- Any table with a composite primary key where some non-key column's value is fully determined by only one part of that key.
- Classic shape: an order/line-item, enrollment, or any many-to-many junction table that has grown extra descriptive columns belonging to one side of the relationship.

## When Not to Use

- Tables with a single-column (non-composite) primary key are already in 2NF by definition once in 1NF — there's no partial dependency to have.
- If an attribute is deliberately a point-in-time snapshot (e.g., `unit_price_at_purchase` capturing the price _as charged_, independent of the current product price), it is not a 2NF violation — it's a distinct fact that happens to share a name with a fact in another table. Don't "fix" a historical snapshot into a live foreign-key lookup; that changes its meaning.

## Trade-offs

- **Pros:** each fact is stored exactly once at the granularity it actually varies at; updates to a product's name or price touch one row, not every order line that ever referenced it.
- **Cons:** reading "order line with product name and price" now requires a join back to the products table instead of reading one row.

## Database Notes

- **PostgreSQL / MySQL / SQLite:** 2NF is enforced by schema design, not by the engine — nothing stops you from creating a composite-keyed table with partially-dependent columns. `NOT NULL` and `UNIQUE` constraints on the split-out table (e.g., `products(product_id) PRIMARY KEY`) are how the fix is expressed; a `FOREIGN KEY` from the junction table enforces that only real products can be referenced. SQLite requires `PRAGMA foreign_keys = ON` per connection for FK enforcement.
- **MongoDB:** the partial-dependency problem shows up as "which fields belong on the embedded line-item sub-document versus the referenced product document." The Extended Reference Pattern is MongoDB's answer: embed only the small, mostly-static subset of product fields the order actually needs at read time (name, price-at-purchase) directly in the order document, and keep a reference (`product_id`) to the full product document for anything else — this is a deliberate, named partial denormalization, not an accidental 2NF violation, because the embedded copy is expected to diverge from the live product over time (that's the point for `price_at_purchase`).
- **Cassandra / ScyllaDB:** there is no composite-key partial-dependency concept to violate, because tables are built per query, not per entity. The equivalent design decision is which columns to duplicate into a query table: an `orders_by_product` table built to answer "all orders for this product" will duplicate `product_name` into every row for that product on purpose, because a CQL `SELECT` cannot join back to a `products` table — consistency of that duplicated name across all its copies becomes the application's job (or an idempotent batch update).
- **DynamoDB:** the partial-dependency shape maps to a modeling question: does an item (say, an `ORDER#<id>#PRODUCT#<id>` line-item item) need a copy of product attributes, or should the application issue a second `GetItem` for the product? DynamoDB's answer leans toward copying commonly-needed, slow-changing attributes (name, price) onto the line-item item to avoid a second request, which is the same trade AWS's own guidance makes for single-table design — see [[denormalization]].

## Examples

- [examples/second-normal-form/postgres.sql](../examples/second-normal-form/postgres.sql)
- [examples/second-normal-form/mysql.sql](../examples/second-normal-form/mysql.sql)
- [examples/second-normal-form/sqlite.sql](../examples/second-normal-form/sqlite.sql)
- [examples/second-normal-form/mongodb.js](../examples/second-normal-form/mongodb.js)
- [examples/second-normal-form/cassandra.cql](../examples/second-normal-form/cassandra.cql)
- [examples/second-normal-form/scylladb.cql](../examples/second-normal-form/scylladb.cql)
- [examples/second-normal-form/dynamodb.md](../examples/second-normal-form/dynamodb.md)

## Related Forms

- **First Normal Form ([[first-normal-form]])** is a prerequisite — 2NF assumes atomic values and a real key already exist.
- **Third Normal Form ([[third-normal-form]])** closes the parallel gap for tables with a single-column key: a non-key attribute depending on _another non-key attribute_ rather than on part of a composite key.
