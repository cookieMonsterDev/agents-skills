-- Fifth Normal Form (5NF)
-- Anomaly: C. J. Date's classic ternary join dependency -- a combination
-- (agent, company, product) is valid only when all three pairwise facts
-- hold, so no two-way split reconstructs it losslessly.

-- ============================================================
-- BEFORE: one flat table for a genuine three-way relationship
-- ============================================================
CREATE TABLE agent_company_product (
    agent   VARCHAR(50) NOT NULL,
    company VARCHAR(50) NOT NULL,
    product VARCHAR(50) NOT NULL,
    PRIMARY KEY (agent, company, product)
) ENGINE=InnoDB;

-- Agent A1 represents C1 and C2, sells P1 (from C1) and P2 (from C2). A1
-- does NOT sell P1-from-C2 or P2-from-C1 -- those combinations are invalid.
INSERT INTO agent_company_product VALUES
    ('A1', 'C1', 'P1'),
    ('A1', 'C2', 'P2');

-- Join dependency, not a simpler functional/multivalued one: splitting into
-- agent_company(agent, company) and agent_product(agent, product) and
-- rejoining would also assert A1 sells P1-from-C2, which was never a fact.
-- Insertion anomaly: recording that C1 now also makes product P3, before any
-- agent has sold it, has nowhere to go in this flat table.
-- Deletion anomaly: removing the one row for (A1, C1, P1) can silently erase
-- the independently true fact "A1 represents C1" if no other row expresses it.

-- ============================================================
-- AFTER: three pairwise tables, each an independently maintained binary fact
-- ============================================================
DROP TABLE agent_company_product;

CREATE TABLE agent_company (
    agent   VARCHAR(50) NOT NULL,
    company VARCHAR(50) NOT NULL,
    PRIMARY KEY (agent, company)
) ENGINE=InnoDB;

CREATE TABLE company_product (
    company VARCHAR(50) NOT NULL,
    product VARCHAR(50) NOT NULL,
    PRIMARY KEY (company, product)
) ENGINE=InnoDB;

CREATE TABLE agent_product (
    agent   VARCHAR(50) NOT NULL,
    product VARCHAR(50) NOT NULL,
    PRIMARY KEY (agent, product)
) ENGINE=InnoDB;

INSERT INTO agent_company  VALUES ('A1', 'C1'), ('A1', 'C2');
INSERT INTO company_product VALUES ('C1', 'P1'), ('C2', 'P2');
INSERT INTO agent_product  VALUES ('A1', 'P1'), ('A1', 'P2');

-- Reconstruct the ternary fact: only combinations consistent with all three
-- binary tables survive this three-way join -- exactly the valid set, no more.
-- If this join is on a hot path, a maintained summary table is the MySQL
-- substitute for a materialized view (see [[denormalization]]).
SELECT ac.agent, ac.company, cp.product
FROM agent_company ac
JOIN company_product cp ON cp.company = ac.company
JOIN agent_product ap ON ap.agent = ac.agent AND ap.product = cp.product;
