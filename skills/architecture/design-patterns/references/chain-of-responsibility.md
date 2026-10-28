# Chain of Responsibility

**Category:** Behavioral

## Intent

Pass a request along a chain of handlers; each handler either processes the request or forwards it to the next handler. The sender does not know (or care) which handler ends up responding.

## Problem

- Several objects can handle a request, and the right one is only known at runtime (`if severity <= 2 then frontline else if ...` scattered through the caller).
- The sender should be decoupled from the set of receivers, so handlers can be added, removed, or reordered without touching client code.
- Processing steps should be composable, as in HTTP middleware where each layer may short-circuit (auth failure) or pass the request on.

## Structure

- **Handler** — declares the handling interface and usually holds a reference to the next handler in the chain.
- **Concrete handler** — decides whether it can process the request; if not, it delegates to the next handler.
- **Client** — assembles the chain and sends requests to the first handler only.
- The end of the chain defines the fallback behavior: reject, log, or silently drop the request.

## When to Use

- More than one object may handle a request and the handler should be picked dynamically.
- You want to issue a request without naming the receiver explicitly (support escalation, event bubbling, middleware).
- The set or order of handlers must be configurable at runtime.

## When Not to Use

- Exactly one known object always handles the request; a direct call is simpler.
- Every handler must always run; that is a pipeline (or Decorator), not a chain that stops at the first match.
- A simple lookup (dict/map from request kind to handler) expresses the dispatch more directly than a linear scan.

## Trade-offs

- **Pros:** decouples sender from receivers, handlers stay single-purpose, chains can be built and reordered at runtime.
- **Cons:** no guarantee any handler responds (needs an explicit fallback); long chains are harder to debug and add per-hop overhead; the flow of a request is implicit rather than visible at the call site.

## Language Notes

- **Python / PHP:** a linked-handler class works, but a plain list of callables tried in order is often the lighter idiom; frameworks (Django middleware, PSR-15) are this pattern in production form.
- **Java / C#:** the classic OO form with an abstract handler base class; servlet filters and ASP.NET Core middleware are built-in incarnations.
- **JavaScript:** middleware functions of the form `(request, next) => ...` (Express, Koa) are the native shape of the pattern; a class hierarchy is rarely needed.
- **Rust:** linked `Option<Box<dyn Handler>>` chains fight the borrow checker; iterating a `Vec<Box<dyn Handler>>` until one handles the request is the idiomatic form.
- **Go:** handlers as functions or small interfaces in a slice; `net/http` middleware wrapping (`func(next http.Handler) http.Handler`) is the same idea.
- **C:** emulated with a struct holding a function pointer and a `next` pointer.
- **Swift:** protocol-based chains work well; UIKit's responder chain is the canonical platform example.

## Examples

- [examples/chain-of-responsibility/chain-of-responsibility.py](../examples/chain-of-responsibility/chain-of-responsibility.py)
- [examples/chain-of-responsibility/chain-of-responsibility.c](../examples/chain-of-responsibility/chain-of-responsibility.c)
- [examples/chain-of-responsibility/chain-of-responsibility.cpp](../examples/chain-of-responsibility/chain-of-responsibility.cpp)
- [examples/chain-of-responsibility/chain-of-responsibility.java](../examples/chain-of-responsibility/chain-of-responsibility.java)
- [examples/chain-of-responsibility/chain-of-responsibility.cs](../examples/chain-of-responsibility/chain-of-responsibility.cs)
- [examples/chain-of-responsibility/chain-of-responsibility.js](../examples/chain-of-responsibility/chain-of-responsibility.js)
- [examples/chain-of-responsibility/chain-of-responsibility.rs](../examples/chain-of-responsibility/chain-of-responsibility.rs)
- [examples/chain-of-responsibility/chain-of-responsibility.go](../examples/chain-of-responsibility/chain-of-responsibility.go)
- [examples/chain-of-responsibility/chain-of-responsibility.php](../examples/chain-of-responsibility/chain-of-responsibility.php)
- [examples/chain-of-responsibility/chain-of-responsibility.swift](../examples/chain-of-responsibility/chain-of-responsibility.swift)

## Related Patterns

- **Command** objects often travel along a chain; the two combine naturally (a chain of handlers processing command objects).
- **Decorator** has the same linked structure, but decorators always delegate onward and add behavior, while chain handlers may stop the request.
- **Composite** parent links form an implicit chain: a child forwards requests up the tree (event bubbling).
