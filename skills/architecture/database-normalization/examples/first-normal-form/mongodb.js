// First Normal Form (1NF) — MongoDB has no 1NF, but it has the same atomicity question one level down.
// The relational anomaly: cramming a variable-length fact (an order's line items) into one delimited
// string or numbered columns makes it unindexable and unparseable by the database itself.
// MongoDB's answer: arrays of embedded values are idiomatic, but each array *element* must still be
// an atomic, well-structured value — not another delimited string standing in for a hidden sub-table.

db.orders.drop();

// Anti-pattern: a comma-joined string reintroduces the exact 1NF anomaly inside a single field.
// Nothing here is queryable by individual product, indexable, or safely updatable one item at a time —
// the application has to split() the string back out on every read and re-join it on every write.
db.orders.insertOne({
  orderId: "ORD-1001",
  customerId: "CUST-77",
  products: "Widget,Gadget,Gizmo",
});

db.orders.deleteMany({});

// Idiomatic fix: products as an array of sub-documents, each element atomic and independently meaningful.
// $elemMatch, positional updates ($), and multikey indexes all work against this shape; none of them
// work against a delimited string.
db.orders.insertMany([
  {
    orderId: "ORD-1001",
    customerId: "CUST-77",
    products: [
      { name: "Widget", qty: 2 },
      { name: "Gadget", qty: 1 },
      { name: "Gizmo", qty: 5 },
    ],
  },
  {
    orderId: "ORD-1002",
    customerId: "CUST-88",
    products: [{ name: "Widget", qty: 1 }],
  },
]);

db.orders.createIndex({ "products.name": 1 });

// Query one order's items directly, no string parsing.
db.orders.find({ orderId: "ORD-1001" }, { products: 1, _id: 0 });

// Find every order that contains a specific product — a multikey index makes this an index seek,
// impossible against a delimited string without a full collection scan plus in-app parsing.
db.orders.find({ "products.name": "Gizmo" });

// Update a single line item's quantity in place via the array filter positional operator.
db.orders.updateOne(
  { orderId: "ORD-1001", "products.name": "Widget" },
  { $set: { "products.$.qty": 3 } }
);

// Still matters, differently: MongoDB never enforces atomic fields, so this discipline is self-imposed.
// The rule survives as "keep each array element atomic and structured," not "eliminate repeating groups" —
// a deliberate whole-array JSON-like blob that's always read/written as a unit is a separate, named
// denormalization choice (see denormalization.md), not an accidental 1NF violation.
