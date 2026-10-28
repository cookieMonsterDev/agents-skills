// Fourth Normal Form (4NF) — the relational anomaly is a false cross-product: pairing two independent
// multivalued facts (skills, languages) into one table forces every skill to be paired with every
// language just to represent both sets. A document has no dependency theory to violate, but the same
// false-pairing shape reappears if the two independent facts are modeled as one array of pairs.

db.employees.drop();

// Anti-pattern: one array of {skill, language} pairs forces the same spurious cross-product 4NF
// eliminates. Representing "SQL, Python" and "English, Spanish" without implying a skill-language
// pairing requires four sub-documents for two independent facts, and adding a third skill means adding
// a pair for every existing language or leaving the set inconsistent about which pairs are "real."
db.employees.insertOne({
  employeeId: "EMP-1",
  skillLanguagePairs: [
    { skill: "SQL", language: "English" },
    { skill: "SQL", language: "Spanish" },
    { skill: "Python", language: "English" },
    { skill: "Python", language: "Spanish" },
  ],
});

db.employees.deleteMany({});

// Idiomatic fix: two independent sibling arrays on the same document. No cross-product is implied or
// possible — a document has no notion of "these two arrays must be paired," so this is simply the
// natural shape for two unrelated one-to-many facts about the same employee.
db.employees.insertMany([
  {
    employeeId: "EMP-1",
    skills: ["SQL", "Python"],
    languages: ["English", "Spanish"],
  },
  {
    employeeId: "EMP-2",
    skills: ["Go"],
    languages: ["English"],
  },
]);

db.employees.createIndex({ skills: 1 });
db.employees.createIndex({ languages: 1 });

// Adding a third skill touches one array element, not a cross-product of rows/sub-documents.
db.employees.updateOne({ employeeId: "EMP-1" }, { $push: { skills: "Go" } });

// Independently queryable: employees with a given skill, regardless of language, and vice versa —
// exactly the independence the two-table relational split preserves.
db.employees.find({ skills: "Python" }, { employeeId: 1, _id: 0 });
db.employees.find({ languages: "Spanish" }, { employeeId: 1, _id: 0 });

// Still matters, differently: MongoDB can't stop a developer from choosing the paired-array shape, and
// doing so reintroduces the exact false cross-product 4NF targets. The fix isn't a table split — it's
// choosing two sibling arrays instead of one array of pairs, since the facts are genuinely independent.
