# Reviewing class designs

Trace real callers, construction, mutable state, and resource lifetimes before
diagnosing a principle violation. Identify the invariant or change pressure, then
read its catalog reference. Class size and naming alone are weak evidence.

For each finding, report its location, a concrete caller/change scenario, impact,
the smallest correction, and a behavioral check. Separate demonstrated defects
from optional design improvements. Implement only for a request that includes changes.

## Encapsulation: preserve invariants at every boundary

**Symptom:** `order.items` exposes a mutable collection that callers modify without
recalculating totals. **Fix:** expose a read-only view/copy and mutations that preserve
the order invariant. **Verify:** callers cannot bypass validation through aliases;
valid modifications still update totals correctly. Adding getters and setters that
leak the same mutable state does not establish encapsulation.

## Liskov substitution: test the consumer's expectations

**Symptom:** `ReadOnlyStore` inherits `Store` but throws for `save`, while clients of
`Store` legitimately depend on saving. **Fix:** split the read and write contracts
or use composition, keeping existing consumers supported during migration.
**Verify:** each implementation satisfies the preconditions, postconditions, and
error/lifecycle semantics of the interface its callers use. A base type explicitly
documenting optional writes would require a different assessment.

## Single responsibility: separate actual reasons to change

**Symptom:** pricing policy changes and file-format changes repeatedly touch the
same invoice class. **Fix:** separate calculation from serialization at a coherent
boundary. Keep closely related operations together; one method per class adds
indirection without necessarily improving cohesion. **Verify:** a format change
leaves pricing behavior intact and existing exports remain compatible.

## Dependency inversion: expose a useful boundary

**Symptom:** domain decisions instantiate a concrete network client, preventing
deterministic tests of timeout and failure outcomes. **Fix:** inject the narrow
capability the domain needs, with explicit errors and ownership. A function can be
enough; an interface for every class is not the objective. **Verify:** production
wiring and a controlled failure implementation both satisfy the same contract.

## Completion for refactoring

Preserve supported construction, serialization, public methods, identity, and resource
cleanup unless changing them is part of the request. Use behavior/contract tests at
the changed boundary, not assertions about class counts or inheritance depth.
Report the change pressure removed, checks run, and any consumer migration still needed.
