// Second Normal Form (2NF) — the relational partial-dependency anomaly (order-line columns that
// depend only on productId, not on the whole composite key) becomes a modeling question in MongoDB:
// which fields belong on the embedded line item versus the referenced product document?
// MongoDB's answer is the Extended Reference Pattern: embed a small, intentionally-frozen subset
// (name, price-at-purchase) and reference the rest.

db.products.drop();
db.orders.drop();

db.products.insertMany([
  { _id: "PROD-1", name: "Widget", price: 9.99, description: "A standard widget", stock: 500 },
  { _id: "PROD-2", name: "Gadget", price: 19.99, description: "A fancier gadget", stock: 120 },
]);

// Anti-pattern: full product fields duplicated onto every line item. This is the partial-dependency
// anomaly in document form — productName/productPrice depend only on productId, not on the order,
// so a product rename requires a fan-out update across every order that ever referenced it, and a
// stale description/stock copy drifts from the source of truth for no reason (those fields aren't
// even meant to be a point-in-time snapshot).
db.orders.insertOne({
  orderId: "ORD-2001",
  orderItems: [
    { productId: "PROD-1", productName: "Widget", productPrice: 9.99, productDescription: "A standard widget", quantity: 2 },
  ],
});

db.orders.deleteMany({});

// Idiomatic fix: Extended Reference Pattern. Only the fields the order actually needs at read time —
// name and price *as charged* — are embedded; everything else (description, live stock) is looked up
// via productId when actually needed. priceAtPurchase is a deliberate snapshot, not meant to track
// the live product price, so it is not "fixed" into a lookup.
db.orders.insertMany([
  {
    orderId: "ORD-2001",
    orderItems: [
      { productId: "PROD-1", productName: "Widget", priceAtPurchase: 9.99, quantity: 2 },
      { productId: "PROD-2", productName: "Gadget", priceAtPurchase: 19.99, quantity: 1 },
    ],
  },
]);

// Fast, join-free read for the common case: order confirmation, receipts, order history lists.
db.orders.find({ orderId: "ORD-2001" }, { orderItems: 1, _id: 0 });

// Only when something beyond the frozen subset is needed (current stock, full description) does the
// read pay a $lookup back to the full products collection.
db.orders.aggregate([
  { $match: { orderId: "ORD-2001" } },
  { $unwind: "$orderItems" },
  {
    $lookup: {
      from: "products",
      localField: "orderItems.productId",
      foreignField: "_id",
      as: "productDetail",
    },
  },
  { $unwind: "$productDetail" },
  {
    $project: {
      _id: 0,
      productName: "$orderItems.productName",
      priceAtPurchase: "$orderItems.priceAtPurchase",
      currentStock: "$productDetail.stock",
    },
  },
]);

// Still matters, differently: the partial-dependency concept doesn't apply to a document that has no
// composite key, but the underlying question — "which fields should live where" — resurfaces as the
// embed-vs-reference decision, resolved by the Extended Reference Pattern rather than by a table split.
