# Reviewing and changing schemas

## Establish dependencies from the domain

Read schema constraints, writes, important queries, and representative data. List
candidate keys and the functional/multivalued/join dependencies that the domain
actually requires. Sample uniqueness alone cannot prove a dependency: two customers
can share a name even if today's rows do not. Mark unknown business rules explicitly.

For each finding, name the affected relation, a concrete insertion/update/deletion
sequence, the resulting anomaly, the dependency behind it, and the smallest fix.
Read the relevant form's reference before proposing decomposition.

## Normalization: verify reconstruction and enforcement

**Symptom:** every order row repeats the customer's current contact email; changing
one row leaves contradictory current addresses. **Fix:** store the current email
with its owning customer and reference that customer from orders, if that matches
the business rule. **Verify:** the join reconstructs valid original facts without
spurious rows, and required dependencies remain enforceable. Document any dependency
not preserved by the decomposition and how it will be enforced.

A historical `email_at_order` or `price_at_purchase` is a separate fact, not necessarily
an anomaly. Preserve snapshot semantics instead of replacing historical values with
today's data. Check nullability, foreign keys, uniqueness, and deletion behavior in
the actual database.

## Denormalization: own the synchronization

**Symptom:** an aggregate endpoint is slow. **Fix:** inspect its query plan, indexes,
cardinality, and workload first. If a projection or cache is warranted, identify the
source of truth, readers, update owner, acceptable lag, rebuild procedure, and storage
cost. **Verify:** concurrent updates, duplicates, missed/reordered events, and rebuilds
meet the stated contract; compare representative query latency and write overhead.

A disposable cache can be evicted and reconstructed. A durable projection or retained
historical fact may require stronger recovery guarantees. If TTLs, refresh contention,
or cache outages are the problem, perform a caching-specific review rather than
treating normalization as the repair.

## Migrate supported consumers

For a requested schema change, define how old/new readers and writers coexist.
Expand the schema, backfill with resumable/idempotent work, reconcile concurrent writes,
validate constraints and reconstruction, then switch consumers. Retire old storage
only after its readers, writers, and rollback versions no longer need it.

Keep review-only requests read-only. An implementation is complete when the anomaly
and migration behavior are checked, measured performance claims have evidence, and
remaining rollout/recovery limits are explicit.
