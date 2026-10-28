-- Assumes a keyspace already exists and USE <keyspace>; has been run.

-- Boyce-Codd Normal Form: the relational anomaly is a determinant
-- (instructor -> subject) that isn't a candidate key of the enrollments
-- table. Cassandra sidesteps the "what determines what" question entirely
-- and asks "what do I query by" instead -- there's no overlapping-candidate-
-- key case to detect, only a duplication trade to make.

-- Query: what subject does this instructor teach.
CREATE TABLE instructor_subject (
    instructor text PRIMARY KEY,
    subject    text
);

INSERT INTO instructor_subject (instructor, subject) VALUES ('rivera', 'geometry');

SELECT * FROM instructor_subject WHERE instructor = 'rivera';

-- Query: this student's enrollments.
-- subject is denormalized in so the student's schedule reads from one
-- partition. If Rivera switches subjects, both this table and
-- instructor_subject must be updated together, or the two disagree about
-- what Rivera teaches -- consistent with Cassandra's default of
-- denormalizing on purpose rather than avoiding the redundancy BCNF targets.
CREATE TABLE enrollments_by_student (
    student_id uuid,
    instructor text,
    subject    text,
    PRIMARY KEY ((student_id), instructor)
);

INSERT INTO enrollments_by_student (student_id, instructor, subject)
VALUES (44444444-4444-4444-4444-444444444444, 'rivera', 'geometry');

SELECT * FROM enrollments_by_student WHERE student_id = 44444444-4444-4444-4444-444444444444;
