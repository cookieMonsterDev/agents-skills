# Choosing a cache strategy

## Establish the benefit

Identify repeated work, the consumers sharing its result, and the acceptable age.
Measure the read path before adding another layer. Compare query/index improvements,
smaller payloads, batching, and reuse within one request. High-cardinality reads with
little reuse can cost more with a cache.

## Read and write ownership

- **Cache-aside:** the application loads on a miss and owns invalidation. Useful for
  selected expensive reads; cold misses and stale-fill races need explicit handling.
- **Read-through:** a cache abstraction owns loading. Check the actual library's
  coalescing, error, and expiration guarantees rather than inferring them from the name.
- **Write-through:** the write path updates the source and cache before reporting
  success according to a defined contract. Two independent writes are not an atomic
  transaction; specify partial failure, concurrent fills, and writers bypassing that path.
- **Write-behind:** acknowledge before the source write finishes. This is also a
  durability design: specify durable buffering, ordering, idempotent replay, backpressure,
  and recovery. If losing the cache loses acknowledged writes, it is not disposable.
- **Refresh-ahead:** refresh likely hot entries before expiry. Bound speculative work;
  refresh jobs for unused keys can cost more than the misses they avoid.

AWS describes lazy population, write-through, expiration, and warming trade-offs in
[Caching Best Practices](https://aws.amazon.com/caching/best-practices/).
These names describe ownership; none alone proves the required consistency.

## Placement

Local caches remove network hops but duplicate memory and fills per process. Shared
caches add a dependency and coordination costs. CDN/proxy caches require correct HTTP
representation and privacy semantics. Multiple layers multiply invalidation paths;
choose the fewest layers that meet the measured need.

An evictable cache must be reconstructible from an authoritative source. A durable
projection or historical snapshot can have a different ownership and recovery
contract. Decide which one the system actually needs before borrowing cache rules.

## Worked choice

A public catalog endpoint repeatedly performs an expensive aggregate; descriptions
may lag by 90 seconds. Compare an indexed query against cache-aside with a 60-second
fresh interval and at most 30 additional seconds of stale service. Include load time
and source lag when checking the 90-second end-to-end age limit. Refresh only hot
entries and coalesce fills. Checkout still obtains authoritative price and availability
under its own transaction contract; a fast catalog display does not authorize a sale.
