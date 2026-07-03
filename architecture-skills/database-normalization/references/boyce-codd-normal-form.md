# Boyce-Codd Normal Form (BCNF)

**Category:** Advanced Form

## Intent

Require that for every non-trivial functional dependency `X → Y` in the table, `X` is a superkey — i.e., every determinant is a candidate key. BCNF is a strictly stronger version of 3NF that only differs from it when a table has two or more overlapping candidate keys.

## Problem

- `enrollments(student_id, subject, instructor)` where the business rule is: each instructor teaches exactly one subject, but a subject can be taught by several instructors, and a student can take a subject from more than one instructor over time. Candidate keys are `(student_id, subject)` and `(student_id, instructor)`.
- The functional dependency `instructor → subject` holds (each instructor implies exactly one subject), but `instructor` alone is *not* a candidate key of this table (it doesn't determine `student_id`). This dependency is 3NF-legal — `subject` is not transitively dependent through a non-key attribute chain in the classic sense — but it still violates BCNF, because its determinant (`instructor`) isn't a superkey.
- **Update anomaly:** if instructor Rivera switches from teaching Algebra to teaching Geometry, every row naming Rivera must be updated, or some rows will disagree about what Rivera teaches.
- **Insertion anomaly:** a newly hired instructor with no students yet assigned has no row to record which subject they teach.
- **Deletion anomaly:** if the one student enrolled with a given instructor drops the course, the fact "this instructor teaches this subject" disappears with that row.

## Structure

- **Split along the non-superkey determinant** — pull the dependency `instructor → subject` into its own table (`instructor_subject(instructor PK, subject)`), leaving the original table with only the attributes that depend on a full candidate key.
- **The remaining junction table drops the redundant attribute** — `student_instructor(student_id, instructor)` records who's taking lessons from whom; `subject` is looked up via `instructor_subject`.

## When to Use

- A table has more than one candidate key, and at least one non-key-derived functional dependency exists between attributes that overlap those candidate keys — this is the specific, narrow shape BCNF targets, and it's uncommon compared to 2NF/3NF violations.
- The classic tell: describing the business rule out loud requires saying "each X has exactly one Y" about something that isn't the table's primary identifier.

## When Not to Use

- Most 3NF tables are already in BCNF; don't go looking for overlapping candidate keys where none exist.
- BCNF decomposition can occasionally make a functional dependency non-enforceable by simple keys/constraints alone (a known theoretical limitation — some BCNF decompositions lose the ability to check a dependency without a join). If enforcing the original constraint matters more than eliminating the last redundancy, staying at 3NF and enforcing the rule with a trigger or check can be the pragmatic choice.

## Trade-offs

- **Pros:** removes every redundancy traceable to a non-superkey determinant; the instructor-subject fact is recorded exactly once regardless of how many students take lessons from that instructor.
- **Cons:** an extra join to answer "what does this student's schedule look like with subjects" instead of one table scan; in the rare case mentioned above, the decomposition can make a business rule harder to enforce declaratively.

## Database Notes

- **PostgreSQL:** enforce `instructor → subject` on the split table with a `UNIQUE (instructor)` constraint (or make `instructor` the primary key of `instructor_subject` outright) — that's what turns the informal rule "each instructor teaches one subject" into something the database rejects violations of.
- **MySQL / SQLite:** identical approach — `PRIMARY KEY (instructor)` on the split table. MySQL's foreign keys require InnoDB; SQLite requires `PRAGMA foreign_keys = ON`.
- **MongoDB:** this shape usually surfaces as "should `subject` be embedded on the enrollment document or looked up from an `instructors` collection." Because the rule is about the *instructor*, not the enrollment, model it as a field on the instructor document and reference the instructor from the enrollment — embedding `subject` on every enrollment reintroduces the exact redundancy BCNF removes, with the same update-anomaly cost.
- **Cassandra / ScyllaDB:** query-driven tables sidestep the BCNF question entirely by asking "what do I query by" instead of "what determines what." An `instructor_subject` table keyed by `instructor` is the natural way to answer "what does this instructor teach," and a separate `enrollments_by_student` table duplicates `subject` for read speed — consistent with the default of denormalizing on purpose (see [[denormalization]]) rather than avoiding the redundancy BCNF targets.
- **DynamoDB:** model the `instructor → subject` fact as its own item (or as an attribute on an `INSTRUCTOR#<id>` item), and treat any copy of `subject` on enrollment items as an explicit denormalization requiring an application-level or DynamoDB Streams-driven fan-out update when an instructor's subject changes — DynamoDB has no declarative way to express "this attribute is determined by that other item," so the constraint BCNF describes has to be enforced in application code.

## Examples

- [examples/boyce-codd-normal-form/postgres.sql](../examples/boyce-codd-normal-form/postgres.sql)
- [examples/boyce-codd-normal-form/mysql.sql](../examples/boyce-codd-normal-form/mysql.sql)
- [examples/boyce-codd-normal-form/sqlite.sql](../examples/boyce-codd-normal-form/sqlite.sql)
- [examples/boyce-codd-normal-form/mongodb.js](../examples/boyce-codd-normal-form/mongodb.js)
- [examples/boyce-codd-normal-form/cassandra.cql](../examples/boyce-codd-normal-form/cassandra.cql)
- [examples/boyce-codd-normal-form/scylladb.cql](../examples/boyce-codd-normal-form/scylladb.cql)
- [examples/boyce-codd-normal-form/dynamodb.md](../examples/boyce-codd-normal-form/dynamodb.md)

## Related Forms

- **Third Normal Form ([[third-normal-form]])** is what BCNF strengthens; every BCNF table is in 3NF, but not every 3NF table is in BCNF.
- **Fourth Normal Form ([[fourth-normal-form]])** targets a different kind of dependency (multivalued, not functional) that BCNF doesn't address at all.
