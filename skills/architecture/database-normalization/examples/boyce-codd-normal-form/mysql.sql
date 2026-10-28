-- Boyce-Codd Normal Form (BCNF)
-- Anomaly: instructor -> subject holds (each instructor teaches exactly one
-- subject) but instructor is not a superkey of enrollments -- a 3NF-legal
-- dependency that still violates BCNF.

-- ============================================================
-- BEFORE: single table with two overlapping candidate keys
-- ============================================================
CREATE TABLE enrollments (
    student_id INT UNSIGNED NOT NULL,
    subject    VARCHAR(50)  NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    -- Candidate keys: (student_id, subject) and (student_id, instructor).
    PRIMARY KEY (student_id, subject)
) ENGINE=InnoDB;

INSERT INTO enrollments VALUES
    (1, 'Algebra',  'Rivera'),
    (2, 'Algebra',  'Rivera'),   -- Rivera repeated: subject copied along
    (2, 'Geometry', 'Alvarez');

-- instructor -> subject holds (Rivera always teaches Algebra) but instructor
-- alone isn't a candidate key here, so this is BCNF-illegal even in 3NF.
-- Update anomaly: if Rivera switches to teaching Geometry, every row naming
-- Rivera must be updated, or rows disagree about what Rivera teaches.
-- Insertion anomaly: a newly hired instructor with no students yet has no
-- row to record which subject they teach.
-- Deletion anomaly: if the one student enrolled with an instructor drops the
-- course, the fact "this instructor teaches this subject" disappears too.

-- ============================================================
-- AFTER: split along the non-superkey determinant instructor -> subject
-- ============================================================
DROP TABLE enrollments;

CREATE TABLE instructor_subject (
    instructor VARCHAR(100) PRIMARY KEY,  -- PK enforces instructor -> subject
    subject    VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE student_instructor (
    student_id INT UNSIGNED NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    PRIMARY KEY (student_id, instructor),
    FOREIGN KEY (instructor) REFERENCES instructor_subject(instructor)
) ENGINE=InnoDB;

INSERT INTO instructor_subject VALUES
    ('Rivera', 'Algebra'),
    ('Alvarez', 'Geometry');

INSERT INTO student_instructor VALUES
    (1, 'Rivera'),
    (2, 'Rivera'),
    (2, 'Alvarez');

-- Reconstruct the "before" view; the instructor-subject fact now lives in
-- exactly one row regardless of how many students take lessons from them.
SELECT si.student_id, isu.subject, si.instructor
FROM student_instructor si
JOIN instructor_subject isu ON isu.instructor = si.instructor;
