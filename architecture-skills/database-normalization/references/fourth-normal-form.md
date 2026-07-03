# Fourth Normal Form (4NF)

**Category:** Advanced Form

## Intent

Require that a table have no non-trivial **multivalued dependency** unless that dependency is on a candidate key. A multivalued dependency exists when one attribute determines a _set_ of values for another attribute, independently of a third attribute — forcing two independent one-to-many facts into a single table produces a spurious many-to-many cross-product.

## Problem

- `employee_skills_languages(employee_id, skill, language)` records that employee E1 has skills {SQL, Python} and speaks languages {English, Spanish} — but skills and languages are independent facts about the employee, unrelated to each other.
- To represent this in one table without losing information, every skill must be paired with every language: (E1, SQL, English), (E1, SQL, Spanish), (E1, Python, English), (E1, Python, Spanish) — four rows to represent 2 + 2 = 4 independent facts, not because SQL relates to English but because the table's shape forces a cross-product.
- **Insertion anomaly:** adding a third skill means adding a row for every existing language, or the table becomes inconsistent about which skill/language pairs are "real."
- **Deletion anomaly:** removing the last row that happens to pair a given skill with a given language can accidentally delete the only record that the employee has that skill at all, even though the skill and the language deletion were unrelated.
- This can be in BCNF already — every functional dependency's determinant can be a superkey (there may be no non-trivial _functional_ dependency at all) — and still have this anomaly, because the problem is a multivalued dependency, which functional-dependency-based forms (1NF–BCNF) don't address.

## Structure

- **Split each independent multivalued fact into its own table** — `employee_skills(employee_id, skill)` and `employee_languages(employee_id, language)`, each a simple one-to-many table.
- **No cross-product table remains** — querying "all skills and languages for employee E1" becomes two independent queries (or two joins), not one table with redundant combinations.

## When to Use

- A table has two or more independent, multivalued attributes tied to the same entity — the tell is when you can ask "does the set of X values for this key have anything to do with the set of Y values for the same key?" and the honest answer is no.
- The table is already in BCNF (no problematic functional dependencies) but still exhibits redundancy driven by combinatorics rather than by any single functional dependency.

## When Not to Use

- If the two multivalued facts are _not_ independent (e.g., "which language each skill is taught in" is a genuine pairing, not a cross-product), there's no multivalued dependency to eliminate — that's a legitimate three-way relationship, and forcing it apart loses information (this is closer to the [[fifth-normal-form]] territory of join dependencies).
- Two multivalued facts with genuinely small, fixed cardinality and no independent growth (rare) may not be worth splitting if the redundancy is trivial and the combined table is never a bottleneck — judge against the actual anomaly, not the rule.

## Trade-offs

- **Pros:** each independent multivalued fact is recorded once per (entity, value) pair; no combinatorial row explosion as more skills or languages are added.
- **Cons:** an "all facts about this employee" view now unions results from multiple tables instead of reading one; the cross-product was at least trivially easy to `SELECT *` from.

## Database Notes

- **PostgreSQL / MySQL / SQLite:** the classic fix is exactly the two-table split above, with `UNIQUE (employee_id, skill)` and `UNIQUE (employee_id, language)` to prevent duplicate facts. PostgreSQL's array columns (`skills text[]`, `languages text[]` directly on `employees`) are a legitimate alternative for read-heavy, rarely-queried-by-individual-value cases — but that trade is the same one discussed in [[first-normal-form]], made deliberately rather than as a byproduct of avoiding a join.
- **MongoDB:** this maps directly to modeling two independent arrays as two separate array fields on the employee document (`skills: [...]`, `languages: [...]`) rather than one array of `{skill, language}` pairs — the pairs array would force the same false cross-product 4NF eliminates. Two sibling arrays on one document are the idiomatic, non-anomalous MongoDB shape here, since a document has no dependency-theory concept to violate.
- **Cassandra / ScyllaDB:** model each independent multivalued fact as its own `set` or `list` column on the employee's row (`skills set<text>`, `languages set<text>`), or as separate query tables if either set is queried independently (`employees_by_skill`). Combining them into paired rows in one table would be the CQL-specific version of the same anomaly — an unnecessary cross-product with no query it actually serves.
- **DynamoDB:** store each independent multivalued fact as its own `List` or `String Set` attribute on the employee item, or — if either set is large or independently queried (e.g., "find all employees with skill X") — as its own item collection (`EMPLOYEE#<id>` / `SKILL#<name>` items) so it can be queried without scanning. Pairing skills and languages into single items would create the same spurious combinations 4NF targets, with no access pattern to justify it.

## Examples

- [examples/fourth-normal-form/postgres.sql](../examples/fourth-normal-form/postgres.sql)
- [examples/fourth-normal-form/mysql.sql](../examples/fourth-normal-form/mysql.sql)
- [examples/fourth-normal-form/sqlite.sql](../examples/fourth-normal-form/sqlite.sql)
- [examples/fourth-normal-form/mongodb.js](../examples/fourth-normal-form/mongodb.js)
- [examples/fourth-normal-form/cassandra.cql](../examples/fourth-normal-form/cassandra.cql)
- [examples/fourth-normal-form/scylladb.cql](../examples/fourth-normal-form/scylladb.cql)
- [examples/fourth-normal-form/dynamodb.md](../examples/fourth-normal-form/dynamodb.md)

## Related Forms

- **Boyce-Codd Normal Form ([[boyce-codd-normal-form]])** can hold on a table that still violates 4NF — 4NF targets multivalued dependencies, a distinct class from the functional dependencies BCNF governs.
- **Fifth Normal Form ([[fifth-normal-form]])** targets the case 4NF's "independent facts" assumption doesn't cover: three or more facts that _are_ genuinely interrelated and can't be losslessly split into independent pairs at all.
