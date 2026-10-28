# Denormalization in DynamoDB

The relational baseline needs four lookups — `orders`, `order_items`, `products`, `customers` — joined together to answer "this order, its items, the customer's name, and each product's name and price." DynamoDB's single-table design collapses all four into one item collection: one `Query` on the order's partition key returns the header (with the customer's name already copied on) and every line item (with product name and price-at-purchase already copied on).

## Access Patterns

- Get an order, its customer's name, and every line item with product name and price — in one request.
- Add a line item to an order without touching the customer or product source-of-truth items.

## Item Design

```json
{
  "PK": "ORDER#1001",
  "SK": "ORDER#1001",
  "Type": "Order",
  "customerId": "CUST#500",
  "customerName": "Alicia Moreno",
  "orderTotal": 42.97
}
```

```json
{
  "PK": "ORDER#1001",
  "SK": "ITEM#P-100",
  "Type": "OrderItem",
  "productName": "Widget",
  "priceAtPurchase": 9.99,
  "quantity": 2
}
```

```json
{
  "PK": "ORDER#1001",
  "SK": "ITEM#P-200",
  "Type": "OrderItem",
  "productName": "Gadget",
  "priceAtPurchase": 14.99,
  "quantity": 1
}
```

## Why This Shape

- The order header, its line items, the customer's name, and each product's name/price-at-purchase all live in one item collection (`PK = "ORDER#1001"`) — the same collection built up across the 1NF, 2NF, and 3NF examples in this scenario — so a single `Query` replaces four relational-style lookups.
- `customerName` and `productName` are copied rather than referenced; keeping them in sync when a customer renames or a product is renamed is an explicit job for application code or a DynamoDB Streams handler, not something the database enforces.
- `priceAtPurchase` is a snapshot, not a stale copy — it's supposed to diverge from a product's live price over time, so there's no "correct" value to reconcile it against.
- This is DynamoDB's default posture per AWS's own single-table design guidance, not a special case reached only under load: design from access patterns first, expect the same logical value to live in multiple items, and treat keeping those copies in sync as ordinary application or Streams work rather than as evidence something went wrong.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// One Query returns the order header (with customer name) and every line
// item (with product name and price) — no joins across four tables.
const result = await docClient.send(new QueryCommand({
  TableName: "AppTable",
  KeyConditionExpression: "PK = :pk",
  ExpressionAttributeValues: { ":pk": "ORDER#1001" },
}));
```
