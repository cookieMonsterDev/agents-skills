# Second Normal Form in DynamoDB

The relational anomaly is a junction row keyed by `(order_id, product_id)` storing `product_name`/`product_price`, which really depend only on `product_id` — a partial dependency. DynamoDB's idiomatic answer leans the other way from SQL: copy the commonly-needed, slow-changing product attributes onto the line-item item so reading an order never needs a second lookup against a `Product` item.

## Access Patterns

- Get an order and all its line items — including product name and the price actually charged — in one query.
- Render an order confirmation or invoice without any per-line-item follow-up read.

## Item Design

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
  "PK": "PRODUCT#P-100",
  "SK": "PRODUCT#P-100",
  "Type": "Product",
  "productName": "Widget",
  "currentPrice": 11.49
}
```

A naive design that stayed "normalized" would store only `PK: "ORDER#1001", SK: "ITEM#P-100", quantity: 2` and require a separate `GetItem` against `PK: "PRODUCT#P-100"` for every line item just to render a name and price — one order with five line items becomes six requests instead of one.

## Why This Shape

- `productName` and `priceAtPurchase` are copied onto the order-item so the single `Query` on `PK = "ORDER#1001"` from 1NF already returns everything an order confirmation needs — no fan-out `GetItem` per line.
- `priceAtPurchase` is a deliberate point-in-time snapshot, not a stale copy: it's meant to diverge from the product's `currentPrice` over time, so there's nothing to "fix" if they disagree later.
- `productName` is genuinely denormalized, though: if a product gets renamed, every existing order-item that copied the old name stays as-is (or is fixed up via a DynamoDB Streams handler) — that's an accepted trade, not a bug, because product names change rarely and orders are read far more often than products are renamed.
- This mirrors AWS's own single-table design guidance: copy what a hot read path needs onto the item that path already touches, rather than optimizing for a "single source of truth" that costs an extra round trip on every read.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// One query returns every line item with its name and price snapshot already attached.
const result = await docClient.send(new QueryCommand({
  TableName: "AppTable",
  KeyConditionExpression: "PK = :pk AND begins_with(SK, :prefix)",
  ExpressionAttributeValues: { ":pk": "ORDER#1001", ":prefix": "ITEM#" },
}));
```
