-- Fourth Normal Form (4NF)
-- Problem: an employee's skills and languages are independent facts, but
-- storing them in one table forces a spurious cross-product of every skill
-- with every language -- a multivalued dependency, not a functional one.

PRAGMA foreign_keys = ON;

-- ============ BEFORE: independent multivalued facts forced into a cross-product ============
CREATE TABLE employee_skills_languages (
    employee_id INTEGER NOT NULL,
    skill       TEXT NOT NULL,
    language    TEXT NOT NULL,
    PRIMARY KEY (employee_id, skill, language)
);

INSERT INTO employee_skills_languages VALUES
    (1, 'SQL', 'English'),
    (1, 'SQL', 'Spanish'),
    -- SQL has nothing to do with Spanish specifically -- these four rows
    -- exist only because the table's shape forces every skill x language
    -- combination, not because any pairing is itself a fact.
    (1, 'Python', 'English'),
    (1, 'Python', 'Spanish');

-- Insertion anomaly: adding a third skill means adding a row for every
-- existing language, or the table becomes inconsistent about which
-- skill/language pairs are "real."
-- Deletion anomaly: removing the last row pairing a given skill with a given
-- language can accidentally delete the only record that the employee has
-- that skill at all, even though skill and language deletion were unrelated.

-- ============ AFTER: each independent multivalued fact gets its own table ============
DROP TABLE employee_skills_languages;

CREATE TABLE employee_skills (
    employee_id INTEGER NOT NULL,
    skill       TEXT NOT NULL,
    PRIMARY KEY (employee_id, skill)
);

CREATE TABLE employee_languages (
    employee_id INTEGER NOT NULL,
    language    TEXT NOT NULL,
    PRIMARY KEY (employee_id, language)
);

INSERT INTO employee_skills (employee_id, skill) VALUES
    (1, 'SQL'),
    (1, 'Python');

INSERT INTO employee_languages (employee_id, language) VALUES
    (1, 'English'),
    (1, 'Spanish');

-- Reconstructs the original cross-product view on demand, but the base
-- tables no longer store the redundant combinations -- adding a third skill
-- is one row, not one row per existing language.
SELECT s.employee_id, s.skill, l.language
FROM employee_skills s
JOIN employee_languages l ON l.employee_id = s.employee_id
ORDER BY s.employee_id, s.skill, l.language;
