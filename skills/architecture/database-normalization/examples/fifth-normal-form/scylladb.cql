-- Assumes a keyspace already exists and USE <keyspace>; has been run.
-- ScyllaDB uses CQL compatible with Apache Cassandra; these examples run as-is in cqlsh against ScyllaDB.

-- Fifth Normal Form: the relational anomaly is a genuine three-way join
-- dependency (C. J. Date's agent/company/product example) that can't be
-- losslessly split into two pairwise tables. ScyllaDB sidesteps the theory
-- by building one query table per pairwise question actually asked; it
-- cannot join the three back together at read time the way SQL can.

-- Query: which companies does this agent represent.
CREATE TABLE companies_by_agent (
    agent   text,
    company text,
    PRIMARY KEY ((agent), company)
);

INSERT INTO companies_by_agent (agent, company) VALUES ('agent_a', 'acme_corp');

SELECT * FROM companies_by_agent WHERE agent = 'agent_a';

-- Query: which products does this company make.
CREATE TABLE products_by_company (
    company text,
    product text,
    PRIMARY KEY ((company), product)
);

INSERT INTO products_by_company (company, product) VALUES ('acme_corp', 'widget');

SELECT * FROM products_by_company WHERE company = 'acme_corp';

-- Query: which products does this agent sell.
CREATE TABLE products_by_agent (
    agent   text,
    product text,
    PRIMARY KEY ((agent), product)
);

INSERT INTO products_by_agent (agent, product) VALUES ('agent_a', 'widget');

SELECT * FROM products_by_agent WHERE agent = 'agent_a';

-- If "which products does this agent sell from which company" becomes a
-- real, frequent query, it needs a fourth, denormalized table keyed for
-- that specific three-way lookup, written to redundantly at insert time --
-- ScyllaDB cannot reconstruct the ternary fact from the three binaries at
-- read time the way a relational JOIN could.
