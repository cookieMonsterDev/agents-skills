-- Fourth Normal Form (4NF)
-- Anomaly: skills and languages are independent multivalued facts about an
-- employee, forced into a spurious cross-product by sharing one table.

-- ============================================================
-- BEFORE: independent multivalued facts crammed into one table
-- ============================================================
CREATE TABLE employee_skills_languages (
    employee_id INT UNSIGNED NOT NULL,
    skill       VARCHAR(50) NOT NULL,
    language    VARCHAR(50) NOT NULL,
    PRIMARY KEY (employee_id, skill, language)
) ENGINE=InnoDB;

-- Employee 1 has skills {SQL, Python} and speaks {English, Spanish} -- to
-- lose no information, every skill must be paired with every language.
INSERT INTO employee_skills_languages VALUES
    (1, 'SQL',    'English'),
    (1, 'SQL',    'Spanish'),
    (1, 'Python', 'English'),
    (1, 'Python', 'Spanish');  -- 4 rows for 2 + 2 unrelated facts, not 4 facts

-- Multivalued dependency: employee_id ->-> skill and employee_id ->-> language,
-- independent of each other -- no functional dependency is violated (this
-- table can already be in BCNF), yet the shape still forces this redundancy.
-- Insertion anomaly: adding a third skill means adding a row for every
-- existing language, or the table becomes inconsistent about which
-- skill/language pairs are "real."
-- Deletion anomaly: removing the last row pairing a skill with a language can
-- accidentally delete the only record that the employee has that skill at all.

-- ============================================================
-- AFTER: each independent multivalued fact gets its own table
-- ============================================================
DROP TABLE employee_skills_languages;

CREATE TABLE employee_skills (
    employee_id INT UNSIGNED NOT NULL,
    skill       VARCHAR(50) NOT NULL,
    PRIMARY KEY (employee_id, skill)
) ENGINE=InnoDB;

CREATE TABLE employee_languages (
    employee_id INT UNSIGNED NOT NULL,
    language    VARCHAR(50) NOT NULL,
    PRIMARY KEY (employee_id, language)
) ENGINE=InnoDB;

INSERT INTO employee_skills VALUES (1, 'SQL'), (1, 'Python');
INSERT INTO employee_languages VALUES (1, 'English'), (1, 'Spanish');

-- Reconstruct "all facts about this employee" -- note this join recreates the
-- same 2x2 cross-product rows as before, but only as a read-time view, not as
-- stored, independently-anomalous data.
SELECT es.employee_id, es.skill, el.language
FROM employee_skills es
JOIN employee_languages el ON el.employee_id = es.employee_id;
