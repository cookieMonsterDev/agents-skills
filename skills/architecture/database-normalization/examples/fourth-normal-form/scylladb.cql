-- Assumes a keyspace already exists and USE <keyspace>; has been run.
-- ScyllaDB uses CQL compatible with Apache Cassandra; these examples run as-is in cqlsh against ScyllaDB.

-- Fourth Normal Form: the relational anomaly is forcing two independent
-- multivalued facts (skills, languages) into one table, producing a
-- spurious cross-product of every skill with every language. ScyllaDB's
-- answer is to give each independent fact its own collection column on the
-- same partition, not to pair them into rows -- pairing them would be the
-- ScyllaDB-specific version of the same anomaly, with no query it serves.

-- Query: get an employee's skills and languages.
CREATE TABLE employees (
    employee_id uuid PRIMARY KEY,
    skills      set<text>,
    languages   set<text>
);

INSERT INTO employees (employee_id, skills, languages)
VALUES (
    55555555-5555-5555-5555-555555555555,
    {'sql', 'python'},
    {'english', 'spanish'}
);

SELECT skills, languages FROM employees WHERE employee_id = 55555555-5555-5555-5555-555555555555;

-- If "find all employees with skill X" becomes a real query, that's a
-- separate query table (employees_by_skill(skill, employee_id, ...)), not a
-- reason to pair skills with languages.
