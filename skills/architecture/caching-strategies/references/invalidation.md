# Invalidation and consistency

## Symptom and rule

A user updates a record, sees the new value, then sees the old value again. **Fix:**
trace writer/reader ordering and protect cache publication, not just deletion.

Cache-aside does not by itself guarantee cache/store consistency. Committing the
authoritative write before invalidating avoids a reader refilling from the old
database state during a pre-commit deletion, but leaves other races. See
[Microsoft's cache-aside guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside).

## Reproduce the stale-fill race

```text
reader A: cache miss; reads database version 7; pauses before cache publication
writer B: commits version 8; deletes cache entry
reader A: publishes version 7 after deletion
reader C: sees version 7 until another invalidation or expiration
```

Choose a correction for the required consistency:

- **Bounded staleness is acceptable:** state the actual maximum age and use finite
  freshness limits. Account for read-replica lag, load duration, delayed publication,
  and stale-serving windows; a TTL measured from a delayed fill is not automatically
  a bound on age since the source changed.
- **Old fills must be rejected:** use a retained generation/tombstone or authoritative
  source version. A fill captures the generation before loading and publishes only
  if it still matches, atomically with the write. Invalidation advances the generation.
  Comparing only against the cached payload fails when deletion removes that payload.
- **Strict read-after-write is required:** route affected reads to the authoritative
  source or require at least the writer's committed version. Define the guarantee
  across clients and replicas. Cache-aside plus a deletion cannot establish linearizability.

Where the database commit and cache invalidation are separate operations, cover the
crash between them. A durable outbox/change stream can make delivery recoverable;
handlers must tolerate duplicate and out-of-order events. Event delivery remains
asynchronous unless the read protocol supplies a stronger guarantee. A delayed
second deletion can reduce a race window, but cannot prove correctness for
unbounded read delays.

## Layers, deletions, and deployment

Inventory process caches, shared caches, response caches, CDN/browser caches, and
derived lists or aggregates. Updating an entity can invalidate several query results.
Give each dependency an invalidation owner or explicit freshness bound.

L1 hits can bypass an invalidated L2. On a lost invalidation connection, discard or
revalidate the affected local entries before trusting them again. Server-assisted
tracking is product-specific; see [Redis client-side caching](https://redis.io/docs/latest/develop/reference/client-side-caching/).

Carry the original age budget through layers instead of restarting it at every copy.
For deletion or permission changes, establish whether any stale copy remains usable.
Version serialized payloads/keys when readers cannot safely interpret both schemas;
budget the resulting misses and keep rollback readers compatible with retained data.

## Verification

Use barriers to reproduce the interleaving above, then assert the selected consistency
contract. Also exercise commit-success/invalidation-failure, duplicate and reordered
events, L1 disconnect, deletion during a fill, and mixed-version readers. Check the
observed value or age, not merely that a delete command was called.
