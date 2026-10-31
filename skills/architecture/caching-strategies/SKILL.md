---
name: caching-strategies
description: Review, diagnose, and improve application and HTTP caching. Use when designing a cache, investigating stampedes or stale reads, reviewing cache isolation and invalidation, or reducing cache-related origin load. For command syntax alone, use the cache product's documentation.
---

# Caching Strategies

Treat a cache as a replica with a freshness contract and a failure mode. Recommend
it for a demonstrated reuse or latency benefit; a simpler query, index, or no cache
can be the right outcome.

## Workflow

1. **Establish the contract.** For the affected read path, identify the authoritative
   store, cache layers, key dimensions, readers and writers, deployment topology,
   tolerated staleness, and origin capacity. Trace actual code and configuration;
   separate measured facts from assumptions. Ask only for unknown requirements
   that change the design, such as whether stale authorization decisions are allowed.
2. **Trace the lifecycle.** Follow a fresh hit, stale hit, absent/evicted entry,
   concurrent fill, committed write, and dependency failure across the affected
   layers. Include background jobs and other services that write the same data.
   Finish when each transition has an owner and observable behavior, or a named gap.
3. **Read the matching references** below. For a broad caching review, cover every
   applicable branch; for a focused incident, follow its causal path. Verify
   version-specific commands and library guarantees in official product docs.
4. **Choose the smallest correction.** Explain the failure sequence, the invariant
   the change restores, and its latency, freshness, capacity, and complexity costs.
   A review produces findings; implement only when the request includes changes.
5. **Verify the contract.** Exercise the affected interleavings with controlled
   clocks/barriers and representative concurrency. Compare origin calls, tail
   latency, stale age, refresh errors, and rejected requests against explicit bounds.
   Distinguish proposed tests from checks actually run; a warm-cache hit ratio alone
   does not demonstrate correctness or outage tolerance.

## Routing

- **Choosing cache placement or write policy:** read
  [strategies](references/strategies.md).
- **One hot key expires, concurrent cold misses, or refresh owners fail:** read
  [stampede prevention](references/stampede.md).
- **Old values reappear after writes, missed invalidations, or several cache layers:**
  read [invalidation and consistency](references/invalidation.md).
- **Wrong user's result, ambiguous keys, personalized HTTP responses, or repeated
  lookups of missing records:** read [keys and isolation](references/keys-and-isolation.md).
- **Many keys expire, cache outage, eviction churn, or a hot shard:** read
  [capacity and failure](references/capacity-and-failure.md).
- **Checking whether an agent applies these rules correctly:** use the synthetic
  [review scenarios](references/review-scenarios.md).

## Findings and completion

For each actionable finding, provide: severity and impact, file/configuration
evidence, a concrete request or event sequence, the smallest fix with its trade-off,
and a verification criterion. Mark unverified hypotheses as validation gaps.

For an implementation, also report the changed contract, checks actually run, and
rollout/recovery implications. Account for old cache payloads and mixed application
versions; changing a key namespace can create a cold-cache traffic surge.
Finish when every in-scope failure has a supported finding, a verified correction,
or an explicit remaining limitation.
