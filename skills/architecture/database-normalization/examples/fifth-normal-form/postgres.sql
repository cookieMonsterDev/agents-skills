-- Fifth Normal Form (5NF)
-- Problem (C. J. Date's classic example): agent_company_product is valid
-- only when agent represents company, company makes product, AND agent
-- sells product -- a genuine three-way join dependency. A two-way split
-- would rejoin into combinations that were never actually true.

-- ============ BEFORE: a ternary relationship stored as one flat table ============
CREATE TABLE agent_company_product (
    agent   text NOT NULL,
    company text NOT NULL,
    product text NOT NULL,
    PRIMARY KEY (agent, company, product)
);

INSERT INTO agent_company_product VALUES
    ('Smith', 'Acme', 'Widget'),
    ('Smith', 'Zenith', 'Gadget'),
    -- Smith represents both Acme and Zenith, and sells both Widget and
    -- Gadget, but never sells a Zenith Widget or an Acme Gadget -- splitting
    -- this into two binary tables and rejoining would falsely assert those
    -- combinations exist.
    ('Jones', 'Acme', 'Widget');

-- Insertion anomaly: a new company-product relationship (company now makes a
-- product) that hasn't yet been sold by any agent has nowhere to go in this
-- single flat table.
-- Deletion anomaly: removing the one row recording an agent-company-product
-- fact can silently destroy the independently true company-product or
-- agent-company facts it happened to be the last row expressing.

-- ============ AFTER: three pairwise tables replace the ternary table ============
DROP TABLE agent_company_product;

CREATE TABLE agent_company (
    agent   text NOT NULL,
    company text NOT NULL,
    PRIMARY KEY (agent, company)
);

CREATE TABLE company_product (
    company text NOT NULL,
    product text NOT NULL,
    PRIMARY KEY (company, product)
);

CREATE TABLE agent_product (
    agent   text NOT NULL,
    product text NOT NULL,
    PRIMARY KEY (agent, product)
);

INSERT INTO agent_company VALUES
    ('Smith', 'Acme'),
    ('Smith', 'Zenith'),
    ('Jones', 'Acme');

INSERT INTO company_product VALUES
    ('Acme', 'Widget'),
    ('Zenith', 'Gadget');

INSERT INTO agent_product VALUES
    ('Smith', 'Widget'),
    ('Smith', 'Gadget'),
    ('Jones', 'Widget');

-- Reconstructs exactly the valid original combinations, no more and no less
-- -- only rows consistent with all three independently-maintained binary
-- facts survive the three-way join.
SELECT ac.agent, ac.company, cp.product
FROM agent_company ac
JOIN company_product cp ON cp.company = ac.company
JOIN agent_product ap ON ap.agent = ac.agent AND ap.product = cp.product
ORDER BY ac.agent, ac.company, cp.product;
