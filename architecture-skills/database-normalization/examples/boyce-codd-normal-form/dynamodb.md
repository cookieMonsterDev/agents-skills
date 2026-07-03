# Boyce-Codd Normal Form in DynamoDB

The relational anomaly is `enrollments(student_id, subject, instructor)` storing `subject` even though `instructor → subject` holds and `instructor` isn't a candidate key — every enrollment row for that instructor has to agree on `subject`, or the data disagrees with itself. DynamoDB's answer here is the mirror image of the 2NF/3NF trade: store `subject` once, on the instructor, and look it up rather than copy it — because unlike a product price or a customer name, this is a fact that's cheap to fetch and rarely read at the same volume as the enrollment itself.

## Access Patterns

- Look up what subject a given instructor teaches.
- List a student's enrollments (by instructor) without needing `subject` on every row.
- Change an instructor's subject assignment in exactly one place.

## Item Design

```json
{
  "PK": "INSTRUCTOR#77",
  "SK": "INSTRUCTOR#77",
  "Type": "Instructor",
  "name": "R. Rivera",
  "subject": "Algebra"
}
```

```json
{
  "PK": "STUDENT#42",
  "SK": "INSTRUCTOR#77",
  "Type": "Enrollment",
  "enrolledOn": "2026-01-15"
}
```

Note what's absent: the `Enrollment` item does not carry `subject`. If Rivera switches from teaching Algebra to Geometry, exactly one item (`INSTRUCTOR#77`) changes.

## Why This Shape

- `subject` is stored once, on the item it's actually a fact about (`INSTRUCTOR#77`), instead of being copied onto every enrollment item that references that instructor.
- This is a deliberate *non*-copy, unlike the 2NF (`productName`/`priceAtPurchase`) and 3NF (`customerName`) examples in this same scenario, where copying onto the frequently-read item was the right call.
- The difference is access pattern and volatility: order line items and order headers are read far more often, per source-item, than a product or customer record changes — copying pays for itself. An instructor's subject is looked up relatively rarely per read of the enrollment (a schedule view can batch-fetch a handful of distinct instructors), and instructor-subject reassignments, while infrequent, would require an application-level or DynamoDB Streams fan-out across every enrollment item if the value were copied — a cost not justified here.
- DynamoDB has no declarative way to enforce "this attribute is determined by that other item" (no cross-item constraint), so keeping the fact in one place, rather than copying it and hoping application code keeps every copy in sync, is also the simpler failure mode.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// Look up what subject this instructor teaches — a single GetItem, not a
// value copied onto every enrollment.
const result = await docClient.send(new GetCommand({
  TableName: "AppTable",
  Key: { PK: "INSTRUCTOR#77", SK: "INSTRUCTOR#77" },
}));
```
