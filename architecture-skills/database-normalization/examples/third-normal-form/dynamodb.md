# Third Normal Form in DynamoDB

The relational anomaly is `orders.customer_name` depending transitively on `customer_id`, not on the order itself. DynamoDB's idiomatic answer denormalizes on purpose: copy the frequently-read, slow-changing `customerName` directly onto the order header item so reading an order never requires a second `GetItem` against the customer.

## Access Patterns

- Get an order header, showing the customer's name, in a single request.
- List a customer's recent orders with their name already attached, without joining back to a `Customer` item per row.

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
  "PK": "CUSTOMER#500",
  "SK": "CUSTOMER#500",
  "Type": "Customer",
  "customerName": "Alicia Moreno",
  "tier": "GOLD"
}
```

## Why This Shape

- `customerName` is copied onto every order item so the `Query`/`GetItem` that already fetches the order also returns the name — no second round trip against `PK: "CUSTOMER#500"` on a path that's read far more often than a name changes.
- `customerId` is kept alongside the copy so the source-of-truth customer item is still reachable when other, less frequently needed customer attributes are required.
- The trade this accepts: if Alicia changes her name, every order item that copied `customerName` is now stale until it's fixed. That's handled either by accepting the staleness (order history showing "the name at order time" is often fine) or by a DynamoDB Streams handler on the `Customer` item that fans the update out to affected `Order` items.
- This is the single-table-design version of the exact transitive-dependency trade 3NF names in SQL — DynamoDB just makes the opposite default choice, because it has no join to make the "correct" normalized read cheap.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// Get the order header, customer name included, with a single GetItem — no
// second lookup against the CUSTOMER# item.
const result = await docClient.send(new GetCommand({
  TableName: "AppTable",
  Key: { PK: "ORDER#1001", SK: "ORDER#1001" },
}));
```
