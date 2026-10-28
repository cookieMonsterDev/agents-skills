# Fifth Normal Form in DynamoDB

The relational anomaly is C. J. Date's ternary join dependency: agent-represents-company, company-makes-product, and agent-sells-product are each independently true, but no two of the three pairings imply the third, so a two-way split loses information. DynamoDB's idiomatic answer models each binary relationship as its own item collection — and, because DynamoDB has no join to reconstruct a ternary fact from binaries, writes the three-way fact explicitly only when it's actually observed.

## Access Patterns

- Which companies does this agent represent?
- Which products does this company make?
- Which products does this agent sell (regardless of which company made them)?

## Item Design

```json
{
  "PK": "AGENT#A1",
  "SK": "COMPANY#C1",
  "Type": "AgentCompany"
}
```

```json
{
  "PK": "COMPANY#C1",
  "SK": "PRODUCT#P1",
  "Type": "CompanyProduct"
}
```

```json
{
  "PK": "AGENT#A1",
  "SK": "PRODUCT#P1",
  "Type": "AgentProduct"
}
```

Each item records one observed binary fact. The `AgentProduct` item for `(A1, P1)` is written because agent A1 was actually observed selling product P1 — never derived by rejoining `AgentCompany` and `CompanyProduct`, since that rejoin could assert combinations (like A1 selling a product from a company A1 doesn't represent) that were never true.

## Why This Shape

- Each pairing lives in its own item collection, keyed so it can be queried independently: `PK: "AGENT#A1"` with a `COMPANY#` sort-key prefix answers "which companies," a `PRODUCT#` sort-key prefix on the same partition answers "which products this agent sells."
- No item collection stores the three-way combination `(agent, company, product)` derived from the other two — DynamoDB has no join operator, so there is nothing that could safely "reconstruct" it without risking a false combination.
- If "which products does this agent sell from a specific company" becomes a real, named access pattern, it needs either a dedicated GSI (e.g., a GSI on `AgentProduct` items with `companyId` as an extra attribute, if that provenance is tracked) or a fourth explicit item type recording the observed triple directly — not a query-time join across the three pairwise collections.
- This keeps every stored fact independently true and independently maintainable: revoking an agent's relationship with a company doesn't silently invalidate or fabricate the agent's product-selling facts.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// Which products does this agent sell? (one of the three independent binary facts)
const result = await docClient.send(new QueryCommand({
  TableName: "AppTable",
  KeyConditionExpression: "PK = :pk AND begins_with(SK, :prefix)",
  ExpressionAttributeValues: { ":pk": "AGENT#A1", ":prefix": "PRODUCT#" },
}));
```
