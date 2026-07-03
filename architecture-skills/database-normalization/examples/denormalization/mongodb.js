// Denormalization — a fully normalized (referenced) schema answers "this order, with product names
// and the customer's name" only via multiple $lookups; MongoDB's join only works within a database and
// costs a round trip per referenced collection. The Extended Reference Pattern combines the 2NF and
// 3NF fixes into one read-optimized document: embed the small, frequently-needed, rarely-changing
// subset of each related entity, reference the rest.

db.customers.drop();
db.products.drop();
db.orders.drop();

db.customers.insertMany([{ _id: "CUST-77", name: "Priya Nair", city: "Austin" }]);
db.products.insertMany([
  { _id: "PROD-1", name: "Widget", price: 9.99, stock: 500 },
  { _id: "PROD-2", name: "Gadget", price: 19.99, stock: 120 },
]);

// Fully normalized shape (reference-only) — correct, but reading an order's summary costs two
// $lookups (customer, products) every time, which is the join-per-read cost this pattern trades away.
db.orders.insertOne({
  orderId: "ORD-4001",
  customerId: "CUST-77",
  orderItems: [
    { productId: "PROD-1", quantity: 2 },
    { productId: "PROD-2", quantity: 1 },
  ],
});

db.orders.deleteMany({});

// Idiomatic denormalized shape: embed a frozen subset of the customer (name) and of each product
// (name, price at purchase) directly on the order, alongside the ids for anything that still needs the
// live record. This is the MongoDB default, not a violation, because these are exactly the fields an
// order confirmation, receipt, or history list reads together and rarely need to reflect live changes —
// name/price drift after the fact is expected and desired here, not an anomaly.
db.orders.insertMany([
  {
    orderId: "ORD-4001",
    customerId: "CUST-77",
    customerName: "Priya Nair",
    orderItems: [
      { productId: "PROD-1", productName: "Widget", priceAtPurchase: 9.99, quantity: 2 },
      { productId: "PROD-2", productName: "Gadget", priceAtPurchase: 19.99, quantity: 1 },
    ],
  },
]);

// One-document read serves the common case with zero joins.
db.orders.find({ orderId: "ORD-4001" });

// The reference ids are kept for the rare read that needs the live record (current stock, updated
// address) — a $lookup is still available, it's just no longer on the hot path.
db.orders.aggregate([
  { $match: { orderId: "ORD-4001" } },
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "liveCustomer",
    },
  },
]);

// Still applies, and is idiomatic by default here: unlike a relational OLTP schema (where
// denormalizing up front is premature optimization), MongoDB's own documented patterns (Extended
// Reference, Subset) treat this embed-what's-read-together/reference-what's-shared-or-large split as
// the normal starting design, with the synchronization cost (updating copies on the rare write) as the
// explicit, accepted trade — not a violation of anything MongoDB enforces.
