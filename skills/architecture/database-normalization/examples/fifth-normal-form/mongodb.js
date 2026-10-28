// Fifth Normal Form (5NF) — C. J. Date's classic ternary join dependency: agent represents company,
// company makes product, agent sells product, but the valid three-way (agent, company, product)
// combinations aren't derivable from any two of the three pairwise relationships alone. This is one of
// the few cases where MongoDB's document model doesn't offer an obviously better shape than the
// relational one — embedding tends to reintroduce the exact false-combination risk 5NF avoids.

db.agentCompany.drop();
db.companyProduct.drop();
db.agentProduct.drop();

// Anti-pattern (not shown as data, described): embedding an agent's companies and products together on
// one agent document (e.g. agent -> [{company, products: [...]}, ...]) tempts a reader into assuming
// every product listed is sellable from every company listed for that agent — exactly the spurious
// rejoin 5NF prevents when the three pairwise facts are actually independently maintained.

// Chosen fix: three pairwise reference collections, each an independently-true binary fact, mirroring
// the relational decomposition — this is the right call because each pairing (who represents whom,
// who makes what, who sells what) is populated and maintained separately by different business events.
db.agentCompany.insertMany([
  { agent: "A1", company: "C1" },
  { agent: "A1", company: "C2" },
]);

db.companyProduct.insertMany([
  { company: "C1", product: "P1" },
  { company: "C2", product: "P2" },
]);

db.agentProduct.insertMany([
  { agent: "A1", product: "P1" },
  // Note: no (A1, P2) fact recorded — A1 represents C2 but has never actually sold P2.
]);

// Reconstruct the ternary relationship by joining all three collections; only combinations consistent
// with all three binary facts survive — exactly the valid set, no more, no less. A naive two-way rejoin
// of agentCompany and agentProduct alone would have wrongly implied A1 sells P2 (made by C2).
db.agentCompany.aggregate([
  {
    $lookup: {
      from: "companyProduct",
      localField: "company",
      foreignField: "company",
      as: "companyProducts",
    },
  },
  { $unwind: "$companyProducts" },
  {
    $lookup: {
      from: "agentProduct",
      let: { agent: "$agent", product: "$companyProducts.product" },
      pipeline: [
        { $match: { $expr: { $and: [{ $eq: ["$agent", "$$agent"] }, { $eq: ["$product", "$$product"] }] } } },
      ],
      as: "confirmedSale",
    },
  },
  { $match: { confirmedSale: { $ne: [] } } },
  { $project: { _id: 0, agent: 1, company: 1, product: "$companyProducts.product" } },
]);

// Still matters, the same way: this is a genuinely rare shape, and MongoDB gives no shortcut around it.
// The trade is identical to the relational one — three collections cost a three-way $lookup per read;
// storing only observed (agent, company, product) triples in one collection is the alternative when the
// ternary combination itself is the frequent query, at the cost of not separately tracking each binary fact.
