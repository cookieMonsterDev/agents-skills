# Fifth Normal Form (5NF)

**Category:** Advanced Form

## Intent

Require that a table have no join dependency that isn't implied by its candidate keys — i.e., the table cannot be losslessly reconstructed by joining two or more smaller projections of it unless that decomposition was already forced by a key. 5NF (also called Project-Join Normal Form) is the point past which no further lossless decomposition based on join dependencies is possible.

## Problem

- The classic example (C. J. Date): `agent_company_product(agent, company, product)` records that agent A sells product P made by company C — but only under a three-way business rule: _if_ agent A represents company C, _and_ company C makes product P, _and_ agent A sells product P, _then_ the combination (A, C, P) is valid.
- This looks like it might split into two tables the way [[fourth-normal-form]] would suggest — but a two-way split loses information here. Splitting into `agent_company(agent, company)` and `agent_product(agent, product)` and rejoining them produces combinations that were never actually true: if agent A represents companies C1 and C2, and sells products P1 (from C1) and P2 (from C2), rejoining the two binary tables would also assert that A sells P1-from-C2, which was never a fact.
- This is a genuine **three-way join dependency**: the table can only be losslessly decomposed into _three_ pairwise tables (`agent_company`, `company_product`, `agent_product`) together — no two of the three suffice, and all three must be rejoined to reconstruct exactly the original valid combinations, no more and no less.
- The anomaly this prevents: without the three-way split, adding a new company-product relationship (company C now makes product P) that hasn't yet been sold by any agent has nowhere to go in the single flat table, and removing the one row recording an agent-company-product fact can silently destroy the independently true company-product or agent-company facts it happened to be the last row expressing.

## Structure

- **Three pairwise tables replace the ternary table** — `agent_company(agent, company)`, `company_product(company, product)`, `agent_product(agent, product)` — each recording one binary relationship as its own independently-true fact.
- **The original ternary combination is reconstructed by joining all three**, and only combinations consistent with all three binary facts survive the join — which is exactly the set of valid combinations, no more.

## When to Use

- Extremely rare in practice: a genuine ternary (or higher) relationship where the binary projections are each independently meaningful and the combined constraint can't be expressed as a simpler functional or multivalued dependency.
- A strong signal: the entity has three or more roles in a relationship, each pairwise combination of which is separately meaningful and separately maintained (agents represent companies regardless of products; companies make products regardless of agents; agents sell products regardless of which company made them), yet the _three-way_ combination carries a business rule beyond either pairing alone.

## When Not to Use

- If the three attributes are already governed by a functional or multivalued dependency (e.g., "each agent works for exactly one company"), the problem is 2NF/3NF/4NF, not 5NF — check those first, since 5NF violations without any of the simpler dependency violations already present are uncommon.
- Almost never worth pursuing as a checklist item. Most schema designers never deliberately design for 5NF; they arrive there (or don't need to) because the simpler forms already resolved the actual anomalies present. Treat 5NF as a diagnostic for one specific, rare shape of anomaly, not a rung to climb by default.

## Trade-offs

- **Pros:** eliminates the very specific redundancy and update anomaly caused by a ternary relationship being stored as one flat table; each binary fact is recorded, and maintained, independently.
- **Cons:** reconstructing "does agent A sell product P from company C" now requires a three-way join across all three tables instead of a single-table lookup — for a relationship this rare, the join cost is usually a bigger practical concern than the anomaly was.

## Database Notes

- **PostgreSQL / MySQL / SQLite:** implement the three pairwise tables with composite primary keys (`PRIMARY KEY (agent, company)`, etc.) and foreign keys back to `agents`/`companies`/`products`. Query the three-way relationship with a three-table `JOIN`; if that join is on a hot path, consider a materialized view (PostgreSQL), a maintained summary table (MySQL/SQLite), rather than denormalizing the base tables.
- **MongoDB:** a ternary join-dependency relationship is one of the few cases where MongoDB's document model doesn't offer an obviously better shape than the relational one — embedding tends to reintroduce exactly the false-combination risk 5NF avoids. Modeling it as three reference collections (or one `agent_company_product` collection storing only combinations that have actually occurred, treated as observed facts rather than a derived cross-product) both work; pick based on whether the ternary combination is itself frequently queried as a unit.
- **Cassandra / ScyllaDB:** because tables are built per query, the natural approach sidesteps 5NF theory: build `agent_company`, `company_product`, and `agent_product` query tables for each pairwise question that's actually asked, and — only if "which products does this agent sell from which company" is itself a real, frequent query — maintain a fourth denormalized table keyed for that specific three-way lookup, written to redundantly at insert time.
- **DynamoDB:** model each binary relationship as its own item collection (e.g., `AGENT#<id>` items with a `COMPANY#<id>` sort key, and so on for the other two pairings) so each can be queried independently via the partition key. If the three-way combination is a named access pattern, add it as an explicit denormalized item (or a Global Secondary Index) rather than trying to derive it at read time — DynamoDB has no join operator to reconstruct the ternary fact from the three binaries.

## Examples

- [examples/fifth-normal-form/postgres.sql](../examples/fifth-normal-form/postgres.sql)
- [examples/fifth-normal-form/mysql.sql](../examples/fifth-normal-form/mysql.sql)
- [examples/fifth-normal-form/sqlite.sql](../examples/fifth-normal-form/sqlite.sql)
- [examples/fifth-normal-form/mongodb.js](../examples/fifth-normal-form/mongodb.js)
- [examples/fifth-normal-form/cassandra.cql](../examples/fifth-normal-form/cassandra.cql)
- [examples/fifth-normal-form/scylladb.cql](../examples/fifth-normal-form/scylladb.cql)
- [examples/fifth-normal-form/dynamodb.md](../examples/fifth-normal-form/dynamodb.md)

## Related Forms

- **Fourth Normal Form ([[fourth-normal-form]])** handles independent multivalued facts that split cleanly into pairs; 5NF handles the case where three (or more) facts are genuinely interdependent and no pairwise split suffices alone.
- **Denormalization ([[denormalization]])** is often the practical answer once a 5NF-shaped relationship is identified but the three-way join is too costly for a hot query path — the pairwise tables stay as the source of truth, and a denormalized read table serves the hot path.
