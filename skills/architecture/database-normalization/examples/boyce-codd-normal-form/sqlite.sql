-- Boyce-Codd Normal Form (BCNF)
-- Problem: each instructor teaches exactly one subject, but a subject can
-- have several instructors, and a student can take a subject from more than
-- one instructor over time. Candidate keys are (student_id, subject) and
-- (student_id, instructor); instructor -> subject holds, but instructor is
-- not a superkey, so this is 3NF-legal yet BCNF-violating.

PRAGMA foreign_keys = ON;

-- ============ BEFORE: a non-superkey determinant (instructor -> subject) ============
CREATE TABLE enrollments_flat (
    student_id INTEGER NOT NULL,
    subject    TEXT NOT NULL,
    instructor TEXT NOT NULL,
    PRIMARY KEY (student_id, subject)
);

INSERT INTO enrollments_flat VALUES
    (1, 'Algebra', 'Rivera'),
    -- Rivera teaching Algebra is repeated for every student in the class --
    -- instructor determines subject, but instructor isn't this table's key.
    (2, 'Algebra', 'Rivera'),
    (2, 'Geometry', 'Chen');

-- Update anomaly: if Rivera switches from teaching Algebra to Geometry,
-- every row naming Rivera must be updated, or rows disagree about what
-- Rivera teaches.
-- Insertion anomaly: a newly hired instructor with no students yet assigned
-- has no row to record which subject they teach.
-- Deletion anomaly: if the one student enrolled with an instructor drops the
-- course, the fact "this instructor teaches this subject" disappears too.

-- ============ AFTER: split along the non-superkey determinant ============
DROP TABLE enrollments_flat;

CREATE TABLE instructor_subject (
    instructor TEXT PRIMARY KEY,
    subject    TEXT NOT NULL
);

CREATE TABLE student_instructor (
    student_id INTEGER NOT NULL,
    instructor TEXT NOT NULL REFERENCES instructor_subject (instructor),
    PRIMARY KEY (student_id, instructor)
);

INSERT INTO instructor_subject (instructor, subject) VALUES
    ('Rivera', 'Algebra'),
    ('Chen', 'Geometry');

INSERT INTO student_instructor (student_id, instructor) VALUES
    (1, 'Rivera'),
    (2, 'Rivera'),
    (2, 'Chen');

-- Reconstructs the original flat view; the instructor-subject fact is now
-- recorded exactly once, regardless of how many students take lessons from
-- that instructor.
SELECT si.student_id, ins.subject, si.instructor
FROM student_instructor si
JOIN instructor_subject ins ON ins.instructor = si.instructor
ORDER BY si.student_id, si.instructor;
