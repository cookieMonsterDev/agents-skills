// Third Normal Form (3NF) — the relational transitive-dependency anomaly (customer name/city copied
// onto every order, depending on customerId rather than the order itself) is MongoDB's canonical
// embedding-versus-referencing decision. Embedding full, mutable customer data reintroduces the
// anomaly; referencing (with a $lookup) or embedding a small frozen subset are the two real answers.

db.customers.drop();
db.orders.drop();

db.customers.insertMany([
  { _id: "CUST-77", name: "Priya Nair", city: "Austin", zip: "78701" },
]);

// Anti-pattern: full, live-mutable customer fields copied onto every order. If Priya moves to Dallas,
// every one of her past orders needs to be updated too, or they disagree about where she lived — the
// exact transitive-dependency update anomaly 3NF eliminates, just inside a document instead of a row.
db.orders.insertOne({
  orderId: "ORD-3001",
  customerId: "CUST-77",
  customerName: "Priya Nair",
  customerCity: "Austin",
  customerZip: "78701",
});

db.orders.deleteMany({});

// Fix, option A — reference: customerId only, $lookup when the order needs customer data.
// Right choice when customer data changes independently and many orders need the current, live value.
db.orders.insertOne({ orderId: "ORD-3001", customerId: "CUST-77" });

db.orders.aggregate([
  { $match: { orderId: "ORD-3001" } },
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer",
    },
  },
  { $unwind: "$customer" },
]);

// Fix, option B — Extended Reference Pattern: embed only a small, intentionally-frozen subset
// (the name *as of order time*) alongside the reference. Reasonable when the field is meant to read
// as a historical snapshot (a shipping label, an invoice) rather than track the customer's live record —
// the same trade as priceAtPurchase in second-normal-form.md, applied to the customer side.
db.orders.updateOne(
  { orderId: "ORD-3001" },
  { $set: { customerNameAtOrderTime: "Priya Nair" } }
);

db.orders.find({ orderId: "ORD-3001" });

// Still matters, differently: the anomaly is real in MongoDB too — full customer data embedded on
// every order goes stale on every address change. Reference live, shared, independently-changing data;
// embed only a named, frozen subset meant to freeze at a point in time.
