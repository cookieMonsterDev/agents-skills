# Capacity and dependency failure

## Many keys expire together: cache avalanche

**Symptom:** a bulk fill, deployment, or namespace change synchronizes expiry of many
keys. **Fix:** spread refresh/expiration times within the permitted freshness budget,
rate-limit warming, and bound total concurrent origin work. Per-key coalescing does
not limit the aggregate work of thousands of distinct keys. Jitter changes timing,
not origin capacity.

## Cache unavailable: fallback overload

**Symptom:** every cache error falls through to the database, exhausting its pool.
**Fix:** define a finite origin request/concurrency budget, short cache deadlines,
bounded retries, and a fallback or load-shedding policy. Serve stale only where
allowed and still available; a stale copy stored exclusively in the failed cache
cannot be used. A circuit breaker avoids repeated calls to a failed cache but does
not itself limit database traffic. AWS describes this cache dependency and recommends
testing the service with caching disabled in
[Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/).

Illustrative capacity calculation: with 10,000 eligible reads/second and a 99% hit
ratio, about 100 misses/second reach the origin before refresh and retry work. A cold
cache can expose all 10,000. If the measured origin budget is 500/second, state how
requests above it are coalesced, deferred, served an allowed fallback, or rejected.
Budget concurrency separately when origin latency grows.

## Hot key and eviction churn

**Hot key:** one shard is saturated even though the hit ratio is high. Trace per-shard
request volume, payload bytes, serialization, and network cost. More shards do not
split one key automatically. Consider a bounded local read cache or replicated read
path only with an explicit coherence/staleness policy.

**Churn:** useful values are evicted before reuse. Measure working-set bytes,
cardinality, object sizes, evictions, and misses by operation. Limit oversized or
one-use entries and choose an eviction/admission policy that matches the workload.
TTL bounds age; it does not reserve space. Redis documents how memory limits and
eviction policies interact in [Key eviction](https://redis.io/docs/latest/develop/reference/eviction/).
Separate disposable cache data from durable state and coordination metadata whose
eviction would invalidate the protocol.

## Verification and rollout

Load-test representative skew and payload sizes in a controlled environment:
one hot key, many cold keys, synchronized expiry, slow/failed cache calls, and
recovery. Assert bounds on origin QPS/concurrency, queue size, tail latency, error
rate, and served age. Track refresh failures and rejected work alongside hits.
Use bounded metric dimensions, not raw cache keys.

Roll out by a limited traffic cohort, compare against a baseline, and define stop
thresholds from service objectives. A cache-bypass switch is safe only if the origin
budget remains enforced. Recovery and rollback should avoid a fleet-wide flush or
unlimited warm-up that recreates the incident.
