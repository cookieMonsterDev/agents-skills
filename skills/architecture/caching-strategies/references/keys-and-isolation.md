# Keys, isolation, and negative caching

## Wrong-result rule

Two requests share an entity ID but differ by tenant, permissions, locale, currency,
filters, or representation. A key using only the ID returns the wrong result.
**Fix:** include every dimension that changes the reusable result and enforce access
checks on cache hits as well as misses. A key is not an authorization check.

Example application key, using unambiguous encoding for each component:

```text
product:v3:tenant=17:id=42:locale=uk:currency=UAH:audience=public
```

Derive tenant and permission scope from trusted request context. Canonicalize query
inputs only when they are semantically equivalent. Limit key length/cardinality and
payload size. Keep tokens and personal data out of raw keys and metric labels;
hashing a key does not make the cached value safe to share. Validate decoded payloads
and fail safely on corruption or an unsupported schema.

## HTTP rule

Check the whole browser/CDN/proxy path. URL equality does not mean two authenticated
responses are interchangeable. Use `Vary` for relevant request-header dimensions,
and confirm the cache actually includes them in selection. `private` restricts shared
cache storage, `no-store` prohibits storage, and `no-cache` requires validation before
reuse; those directives have distinct meanings. Review rules for `Authorization`
and personalized responses explicitly. See
[RFC 9111, sections 3–5](https://www.rfc-editor.org/rfc/rfc9111.html).

## Negative-cache rule

Repeated lookups of an absent record miss the cache and hammer the origin. **Fix:**
cache a confirmed not-found outcome for a short, explicit interval when the domain
allows delayed visibility, and clear or supersede it on creation.

Represent not-found separately from a valid empty list, null-valued field, permission
denial, timeout, and dependency failure. Never turn a transient failure into a cached
absence. A Bloom filter can avoid some absent-key reads, but positive results still
require lookup and the update/rebuild path must preserve visibility of new records.
For mostly unique random keys, negative entries alone may just exhaust memory;
combine admission/rate limits with an origin budget.

## Verification

- Same ID under different tenants and roles returns only each caller's allowed data.
- Logout or permission revocation cannot reuse a now-forbidden response.
- Equivalent query inputs share a key; meaningfully different inputs do not.
- A confirmed miss followed by creation becomes visible within the stated bound.
- Origin errors remain distinguishable from not-found and do not poison future hits.
- Test HTTP headers and cache behavior end to end, including a second user and a
  shared proxy; unit tests for key construction alone cannot verify that path.
