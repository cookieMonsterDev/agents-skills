# Stampede prevention

## Symptom and rule

A hot key expires. Every request that wanted it misses at the same moment and slams
the database together. **Fix:** let one refresh owner rebuild it while other callers
receive a still-permitted stale copy. This combines request coalescing with
stale-while-revalidate; neither feature implies the other.

## Freshness states

Keep the payload until the end of the allowed stale window, rather than deleting it
at its freshness deadline. Store `freshUntil` and `serveUntil`, with
`freshUntil <= serveUntil`:

- Before `freshUntil`: return the cached value.
- From `freshUntil` to `serveUntil`: return stale if the data contract permits it;
  elect one refresh owner for the key.
- At/after `serveUntil`, or when absent: coalesce callers behind a bounded fill or
  return the defined unavailable response. There is no usable stale fallback.

For example, a public product description might be fresh for 60 seconds and usable
for another 30. These are illustrative values, not defaults for prices, inventory,
permissions, or revocations. HTTP SWR explicitly bounds how long stale responses
can be reused; stale-if-error is a separate policy. See
[RFC 5861, sections 3–4](https://www.rfc-editor.org/rfc/rfc5861.html).

## Coordination rules

1. Scope coalescing to the callers creating the overload. An in-process single-flight
   map permits one fill per process; 40 replicas can still issue 40 fills. Use shared
   coordination when the origin budget requires it, or document that bound as acceptable.
2. After acquiring ownership, reread the entry: another owner may already have filled
   it between the initial miss and acquisition.
3. Give origin calls, lock acquisition, waiting, and retries explicit deadlines.
   Bound the number of waiters and concurrent fills across different keys as well.
   A cancelled waiter should detach without cancelling work still needed by others.
4. Use a bounded lease with a unique owner token. Release or renew it atomically only
   when the stored token matches. Redis documents `SET ... NX PX` acquisition and
   conditional release; confirm supported commands for the deployed version.
   Plain `DEL` can remove a successor's lock. See
   [Redis distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/).
5. Lease expiry or failover can allow overlapping loaders. Safe release alone does
   not make publication safe. Atomically reject publication by an expired owner and
   guard against older source versions overwriting newer data. Keep invalidation
   generations or version high-water marks long enough to reject delayed writers.
   Describe the consistency guarantee of the store enforcing that check.
6. On refresh failure, preserve the old payload and its original `serveUntil`.
   Apply bounded retry backoff so each subsequent request does not start another
   failed refresh. Observe errors from background work and use a task lifetime the
   runtime supports; serverless request completion may stop detached work.

Lease coordination limits duplicate work under stated assumptions; it is not an
exactly-once guarantee. Side effects in a loader need their own idempotency contract.
For write races, also read [invalidation](invalidation.md).

## Worked request flow

This is design pseudocode, not a runnable distributed-lock implementation. The
coordination API must implement the ownership, publication, and retry rules above.

```text
entry = cache.read(key)
if entry exists and now < entry.freshUntil:
    return entry.value

if entry exists and now < entry.serveUntil and staleAllowed:
    refreshCoordinator.tryScheduleOne(key)  # bounded queue; cooldown on failure
    return entry.value

return refreshCoordinator.joinOrStartFill(key, requestDeadline)
    # owner rereads cache, loads with an origin deadline, publishes conditionally
    # waiters receive fresh data, a bounded error, or detach on cancellation
```

TTL jitter spreads expirations across different keys. It does not coalesce requests
for the same key. Early refresh can reduce hard expirations, but still needs a work
budget and a policy for duplicate refreshes.

## Verification

- Hold one origin read behind a barrier and send 100 requests for one stale key.
  They return the permitted old value; only one loader runs per coordination scope.
- Repeat with an empty cache: callers join the fill, meet a deadline, or receive the
  defined overload result. None receives a nonexistent stale value.
- Pause owner A past its lease, let B publish a newer result, then resume A. A can
  neither remove B's lease nor overwrite B's value.
- Make refresh fail repeatedly and advance the clock beyond `serveUntil`: retries
  are bounded and stale data stops being served at the contractual deadline.

Where a proxy owns caching, prefer its supported mechanisms after checking their
scope and timeout behavior. NGINX exposes separate cache lock, background update,
and stale-use controls; enabling one is not enabling all three. See
[NGINX proxy cache directives](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_lock).
