# Behavioral review scenarios

Use these synthetic prompts to evaluate the skill. Give the prompt and skill to an
agent, then assess the result against the criterion. These are evaluation fixtures,
not evidence that an implementation was load-tested.

## Hot-key expiry

**Prompt:** A public catalog description has a 60-second Redis TTL. On a miss every
request loads the database. There are 12 app replicas. Descriptions may be served
for at most 90 seconds from the source snapshot. Review and propose a fix.

**Criterion:** identifies per-key stampede; preserves a bounded stale copy, coalesces
refresh at an appropriate scope, includes source/load age in the bound, and covers
cold misses, failed refresh, and lease expiry. Jitter alone is insufficient.

## Strict freshness

**Prompt:** We cache whether an account can approve payments. Revocation must take
effect before any later approval. Can stale-while-revalidate solve expiry spikes?

**Criterion:** preserves the revocation requirement; does not propose stale permission
reuse. Names the authoritative consistency boundary and a bounded overload outcome.

## Write race

**Prompt:** A reader loads v1 and pauses. A writer commits v2 and deletes the cache.
The reader resumes and caches v1. We already delete after commit. Review the fix.

**Criterion:** identifies delayed publication; requires a retained generation/version
guard or authoritative reads according to the consistency contract. Does not claim
that another fixed-delay deletion proves correctness.

## Cache outage

**Prompt:** 10,000 requests/second, 99% hits, origin tested for 500 requests/second.
On a Redis timeout we immediately retry twice, then read the database. Improve it.

**Criterion:** quantifies loss of the hit shield, bounds origin traffic and retry work,
defines fallback/rejection, and tests cold/recovery conditions. Increasing TTL alone
does not address the failure.

## Review scope and simpler alternative

**Prompt:** Review a proposed cache for unique export requests with no result reuse.
Do not change files. The database query has no index for its filter.

**Criterion:** stays read-only, investigates the query plan/index, and allows no cache
as the outcome. Does not force a caching pattern or invent performance measurements.
