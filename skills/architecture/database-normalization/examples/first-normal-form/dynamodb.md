# First Normal Form in DynamoDB

The relational anomaly is cramming a repeating fact into one delimited column (`products: "Widget,Gadget,Gizmo"`) so it can't be queried, indexed, or paginated by element. DynamoDB's idiomatic answer is the same one 1NF gives SQL: if the list is its own access pattern, give it its own item collection — one item per element, sharing a partition key — rather than a single `List` attribute.

## Access Patterns

- Get an order and all its line items in one query.
- Add a line item to an order without rewriting the whole order.
- Page through an order's line items independently of the order header.

## Item Design

```json
{
  "PK": "ORDER#1001",
  "SK": "ORDER#1001",
  "Type": "Order",
  "orderDate": "2026-06-30",
  "status": "SHIPPED"
}
```

```json
{
  "PK": "ORDER#1001",
  "SK": "ITEM#1",
  "Type": "OrderItem",
  "productId": "P-100",
  "quantity": 2
}
```

```json
{
  "PK": "ORDER#1001",
  "SK": "ITEM#2",
  "Type": "OrderItem",
  "productId": "P-200",
  "quantity": 1
}
```

Anti-pattern this replaces — a single order item with `"products": "Widget,Gadget,Gizmo"` baked into one attribute: nothing can `Query` for "just the Gizmo line," update one line's quantity without a read-modify-write of the whole string, or bound how many products a single item can hold before hitting the 400 KB item-size limit.

## Why This Shape

- Line items live in the same item collection as the order header (`PK = "ORDER#1001"`), so one `Query` returns the header plus every line item, ordered by `SK`.
- Each line item is independently writable — adding `ITEM#3` or updating `ITEM#1`'s quantity touches one item, not a shared attribute every other line item also lives inside.
- A `List` attribute is still the right call for data that's always read and written as a whole and never queried by individual element — e.g., a small `tags: ["fragile", "gift"]` attribute on the order header is fine as a `List`, because nothing ever asks "give me just the orders tagged `fragile`" as a DynamoDB query against that attribute.
- The line becomes its own item collection specifically because "give me one line item" and "page through all line items" are real, named access patterns — a `List` attribute has no way to be queried or paginated into on its own.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// Get the order header and all of its line items in one request.
const result = await docClient.send(new QueryCommand({
  TableName: "AppTable",
  KeyConditionExpression: "PK = :pk",
  ExpressionAttributeValues: { ":pk": "ORDER#1001" },
}));
```
