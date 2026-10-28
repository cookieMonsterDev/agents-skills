# Fourth Normal Form in DynamoDB

The relational anomaly is forcing two independent multivalued facts (an employee's skills, an employee's languages) into one paired table, producing a spurious cross-product of every skill with every language. DynamoDB's idiomatic answer is to store each independent fact as its own attribute — two sibling `List`/`String Set` attributes on the employee item — never as a list of `{skill, language}` pairs.

## Access Patterns

- Get an employee's full profile, including all skills and all languages, in one read.
- Add or remove a single skill or a single language without touching the other attribute.

## Item Design

```json
{
  "PK": "EMPLOYEE#900",
  "SK": "EMPLOYEE#900",
  "Type": "Employee",
  "name": "Devon Clarke",
  "skills": ["SQL", "Python"],
  "languages": ["English", "Spanish"]
}
```

The anti-pattern this avoids — a single `skillLanguagePairs` list forcing a false cross-product:

```json
{
  "skillLanguagePairs": [
    { "skill": "SQL", "language": "English" },
    { "skill": "SQL", "language": "Spanish" },
    { "skill": "Python", "language": "English" },
    { "skill": "Python", "language": "Spanish" }
  ]
}
```

Four pairs to represent two independent facts, with no query this shape actually serves — adding a third skill would mean adding two more pairs just to keep the cross-product "complete."

## Why This Shape

- `skills` and `languages` are modeled as two separate `String Set`/`List` attributes on the same item because they're independent facts about the employee — exactly the 4NF tell of "does the set of skills have anything to do with the set of languages? No."
- Keeping them as sibling attributes (rather than pairing them) means adding a skill is a single `UPDATE` with `ADD skills :s`, untouched by how many languages the employee speaks.
- If either set became large or needed to be queried independently — "find all employees with skill X" — it would graduate from an attribute to its own item collection (`EMPLOYEE#900` / `SKILL#SQL` items, or a GSI on a `skill` attribute), the same escalation path described for 1NF's List-vs-item-collection decision.
- No cross-product item collection is created, because there's no access pattern ("find employees by skill+language pair") that would justify one.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const docClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

// Get the employee item — skills and languages both come back as independent
// attributes, no cross-product to unpack.
const result = await docClient.send(new GetCommand({
  TableName: "AppTable",
  Key: { PK: "EMPLOYEE#900", SK: "EMPLOYEE#900" },
}));
```
