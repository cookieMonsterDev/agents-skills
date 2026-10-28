# First Normal Form (1NF)

**Category:** Core Form

## Intent

Require every column to hold a single, atomic value from its domain, and require every row to be uniquely identifiable, with no repeating groups of columns standing in for a list. 1NF turns "a cell can hold a list" into "a list is its own rows."

## Problem

- A table stores a variable-length fact (a customer's phone numbers, an order's line items) by either cramming multiple values into one delimited string (`"555-1234,555-5678"`) or by adding numbered columns (`phone_1`, `phone_2`, `phone_3`).
- Delimited strings can't be indexed, filtered, or aggregated by the database without parsing them back out in application code every time.
- Numbered columns cap the list at a guess (what happens at `phone_4`?) and every query that wants "all phone numbers" has to name every column and `UNION` or `COALESCE` them.
- Without a clear key, duplicate or ambiguous rows creep in because nothing prevents two rows from describing the same real-world entity.

## Structure

- **Atomic columns** — each column holds one value of one type; no arrays, no comma-joined lists, no JSON blobs standing in for a hidden sub-table (using a JSON/array column type deliberately, with the database's own operators to query inside it, is a separate design choice — see Database Notes).
- **A row per fact instance** — a repeating fact (line items, phone numbers) becomes its own table with a foreign key back to the parent, one row per instance.
- **A primary key** — every row is identifiable by a key so "the same row twice" is a detectable, preventable state.

## When to Use

- Always, as the floor for a relational schema — every subsequent normal form assumes 1NF already holds.
- Any time a column's name has a trailing number (`item_1`, `item_2`) or a column's values contain a delimiter that the application splits on.
- Any time "how many can there be?" doesn't have a fixed answer but the schema has already picked one.

## When Not to Use

- Never skip 1NF in an OLTP relational schema; every anomaly the higher forms fix presupposes atomic values and a real key.
- A single JSON/array column can be the _right_ denormalized choice for a value that is always read and written as a whole and never queried by its individual elements — that is a deliberate exception made by name (see [[denormalization]]), not an accidental 1NF violation.

## Trade-offs

- **Pros:** every value is independently queryable, indexable, and constrainable; row counts reflect real cardinality; no application-side parsing of encoded lists.
- **Cons:** a repeating fact becomes a join; "give me this order and all its items" now costs a second table (or a join) instead of one row.

## Database Notes

- **PostgreSQL:** supports native array and `jsonb` columns, which can hold non-atomic values without an error — a schema can _look_ 1NF-violating and still be queryable via `ANY()`, `unnest()`, or `jsonb` operators. This is a legitimate design choice for genuinely bag-of-values data (tags, feature flags), but it forfeits foreign keys, per-element constraints, and join-based aggregation on that data; default to a child table when the values relate to other tables or need per-value constraints.
- **MySQL:** has JSON columns but no native array type; a comma-separated `VARCHAR` or a JSON array are the two ways to accidentally violate 1NF, and MySQL will not stop either. `JSON_TABLE()` can query into a JSON array, but a child table with a foreign key is still the normalized answer when the values need indexing or referential integrity.
- **SQLite:** enforces neither atomicity nor foreign keys by default (`PRAGMA foreign_keys = ON` is required per connection). A comma-separated `TEXT` column is the most common accidental 1NF violation in embedded/mobile apps; the fix is the same child-table split as PostgreSQL/MySQL, using `INTEGER PRIMARY KEY AUTOINCREMENT` for surrogate keys.
- **MongoDB:** documents are schema-flexible by design, and arrays of embedded values are idiomatic (`{ "phones": ["555-1234", "555-5678"] }`) rather than a violation — MongoDB has no notion of 1NF. The atomicity concern still exists one level down: keep each array _element_ a well-structured, independently meaningful value (an object with typed fields) rather than another delimited string, so `$unwind`, array filters, and indexes on array fields keep working.
- **Cassandra:** collection types (`list`, `set`, `map`) let a column hold multiple values natively; this is the idiomatic way to store an unbounded-but-small list, not a 1NF violation, because Cassandra has no normal forms — the schema is defined by queries, not by dependency theory. Large or fast-growing collections still cause performance issues (they're read/written whole in older versions, and the values live in one partition), so a child table (a second CQL table keyed for the "list items" query) is still the right call once the collection can grow without bound.
- **ScyllaDB:** same CQL collection types and query-driven modeling posture as Cassandra. An unbounded list belongs in a separate query table keyed for the access pattern, not in a `list`/`set` column that grows without bound on one partition.
- **DynamoDB:** items support `List` and `Map` attribute types natively, so storing structured, nested data in one item is normal, not a violation. The 1NF-shaped question DynamoDB actually asks is different: is this list ever an _access pattern_ on its own (query for one item within it, page through it, update one element concurrently)? If so, model it as its own item collection (separate items sharing a partition key) instead of a single attribute, because DynamoDB has no way to index into or paginate a `List` attribute directly.

## Examples

- [examples/first-normal-form/postgres.sql](../examples/first-normal-form/postgres.sql)
- [examples/first-normal-form/mysql.sql](../examples/first-normal-form/mysql.sql)
- [examples/first-normal-form/sqlite.sql](../examples/first-normal-form/sqlite.sql)
- [examples/first-normal-form/mongodb.js](../examples/first-normal-form/mongodb.js)
- [examples/first-normal-form/cassandra.cql](../examples/first-normal-form/cassandra.cql)
- [examples/first-normal-form/scylladb.cql](../examples/first-normal-form/scylladb.cql)
- [examples/first-normal-form/dynamodb.md](../examples/first-normal-form/dynamodb.md)

## Related Forms

- **Second Normal Form ([[second-normal-form]])** assumes 1NF already holds and additionally requires non-key attributes to depend on the _whole_ key, not part of it.
- **Denormalization ([[denormalization]])** is the informed, named exception to storing atomic values in separate rows — not the same as an accidental 1NF violation, which happens without anyone deciding it should.
