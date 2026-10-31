# Reviewing and refactoring patterns

## Inspect the forces before selecting a pattern

Trace the affected callers, implementations, state ownership, and failure paths.
Name the concrete change pressure: duplicated algorithm selection, incompatible
interfaces, coupled construction, or another observable cost. A missing pattern
name is not a defect. Compare the smallest function/data change with the pattern.

For each finding, give the location, triggering scenario, behavioral or maintenance
impact, minimal correction, and a check proving the intended result. Distinguish a
demonstrated defect from a design option. A review stays read-only; a refactoring
request authorizes changes within its scope.

## Rules with examples

### Strategy: duplicated decisions

**Symptom:** adding a shipping method requires updating the same algorithm-selection
switch in pricing, dispatch, and quoting. **Fix:** centralize the shared decision and
its contract; use functions or strategies where independent behavior varies.
Keep one small stable switch when it is already the single source of truth.
**Verify:** each existing shipping method preserves prices/errors, and adding a
method changes the intended registration/implementation rather than scattered callers.

### Proxy: preserve the caller's contract

**Symptom:** a caching proxy returns a shared mutable object, so one caller's mutation
changes another caller's result. **Fix:** use immutable values or an intentional
copy/ownership boundary. A matching method signature does not prove transparent behavior.
**Verify:** mutation, authorization, freshness, errors, and cancellation match the
contract the proxy promises. A caching proxy also needs an explicit invalidation and
concurrent-fill policy; the GoF structure does not supply one. Use a caching-specific
review when those behaviors are in scope.

### Singleton: distinguish lifetime from distributed ownership

**Symptom:** a singleton refresh service is assumed to elect one owner across app
replicas. **Fix:** state the actual process lifetime and coordination boundary;
inject a shared instance for local resource reuse, and use appropriate coordination
when multiple processes must cooperate. **Verify:** a multi-process scenario rather
than only repeated construction in one process.

## Implementing a refactor

Read the selected catalog references and actual language examples. Preserve public
behavior, ordering, resource cleanup, and supported consumers unless a behavior
change is requested. Characterize the observable contract before moving code, make
one coherent change, and run affected checks. Report the simplified boundary and
remaining trade-offs; count reduced change sites or coupling only when observed.
