// Boyce-Codd Normal Form (BCNF) — the relational anomaly is a non-superkey determinant: instructor
// determines subject (each instructor teaches exactly one subject) even though instructor alone isn't
// a candidate key of enrollments. In MongoDB this surfaces as "should subject live on the enrollment
// document or be looked up from the instructor's own document?" Because the rule is about the
// instructor, it belongs on the instructor document.

db.instructors.drop();
db.enrollments.drop();

// Anti-pattern: subject copied onto every enrollment. If instructor Rivera switches from Algebra to
// Geometry, every enrollment document naming Rivera must be updated, or they disagree about what
// Rivera teaches — the same update anomaly BCNF targets, just expressed as documents instead of rows.
db.enrollments.insertMany([
  { studentId: "STU-1", subject: "Algebra", instructor: "Rivera" },
  { studentId: "STU-2", subject: "Algebra", instructor: "Rivera" },
]);

db.enrollments.deleteMany({});

// Idiomatic fix: instructors is its own collection keyed by instructor, holding the one fact that's
// actually determined by instructor. Enrollments reference the instructor and never copy subject.
db.instructors.insertMany([
  { _id: "Rivera", subject: "Algebra" },
  { _id: "Chen", subject: "Geometry" },
]);

db.enrollments.insertMany([
  { studentId: "STU-1", instructor: "Rivera" },
  { studentId: "STU-2", instructor: "Rivera" },
  { studentId: "STU-3", instructor: "Chen" },
]);

// A student's schedule, subject included, is read by looking the subject up once from the instructor
// document — instructor is the instructors collection's _id, so this is a single indexed lookup.
db.enrollments.aggregate([
  {
    $lookup: {
      from: "instructors",
      localField: "instructor",
      foreignField: "_id",
      as: "instructorInfo",
    },
  },
  { $unwind: "$instructorInfo" },
  {
    $project: {
      _id: 0,
      studentId: 1,
      instructor: 1,
      subject: "$instructorInfo.subject",
    },
  },
]);

// Rivera switches to teaching Geometry: one write, on one document, fixes every enrollment's view of it.
db.instructors.updateOne({ _id: "Rivera" }, { $set: { subject: "Geometry" } });

// Still matters, the same way: MongoDB has no functional-dependency enforcement, so nothing stops a
// developer from embedding subject on enrollments anyway — the redundancy and update-anomaly cost is
// identical to the relational case; the fix is the same "model the fact where it's actually determined."
