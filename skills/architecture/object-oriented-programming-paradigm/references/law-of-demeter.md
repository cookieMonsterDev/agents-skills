# Law of Demeter

**Category:** Design Qualities

## Intent

A method should talk only to its immediate collaborators — call methods on itself, its own fields, its parameters, and objects it creates — never on objects fished out of another call's return value. Knowledge of any object's internals then stays within one hop, so a representation change ripples to its neighbors, not across the codebase.

## Problem

- Checkout code reads `order.getCustomer().getWallet().deduct(total)` — a "train wreck". Checkout now knows that orders have customers, customers keep wallets, and wallets have a `deduct`. When customers switch to stored payment cards, every such chain in the codebase breaks, not just `Customer`.
- A rule like "a wallet never goes negative" cannot be enforced anywhere, because callers reach past `Customer` and mutate the `Wallet` directly — the object that owns the rule never gets a say (the classic paperboy who digs into `customer.wallet.cash` instead of asking the customer to pay).
- Unit tests need mocks that return mocks that return mocks: to test the paperboy you must build a customer holding a wallet holding cash, because the code under test traverses that whole graph instead of asking one collaborator for one thing.

## Structure

The "law" is a whitelist. Inside a method of class `C`, you may call methods on exactly these collaborators:

- **`this`/`self`** — other methods of `C` itself.
- **Fields of `C`** — the components the object directly owns.
- **Parameters** — collaborators explicitly handed to the method.
- **Objects the method creates** — locals it instantiated itself (plus, in the original formulation, globals).

Everything else — above all the *result of calling a method on one of the above* — is a "stranger": a friend of a friend you should not talk to. The fix is **tell, don't ask**: instead of asking a collaborator for its parts and operating on them (`customer.getWallet().deduct(due)`), tell the collaborator what you need done (`customer.pay(due)`) and let it forward to its own parts. The knowledge of *how* a customer pays moves next to the data it needs.

## When to Use

- Chains of two or more getters that cross object boundaries (`a.getB().getC().doX()`), especially when the same chain appears at several call sites — each occurrence is a copy of someone else's structure.
- A rule about an inner object (never negative, must stay sorted, must be logged) keeps getting violated because outsiders mutate it directly; routing every touch through the owner is the only place the rule can live.
- Test setup requires building or mocking a deep object graph just to exercise one method — the method is coupled to the graph's shape, not to what it actually needs.
- A refactor of one class's internals (renaming a field, splitting a wallet into cash plus cards) forces edits in files that never mention that class by name.

## When Not to Use

- **Fluent APIs, builders, streams, and optional chains** — `builder.name("x").age(3).build()` or `list.stream().filter(...).map(...)` chains many dots, but each call returns the *same* object or the next stage of one deliberate pipeline. The law counts hops through *different objects' internals*, not dots on a line.
- **Plain data structures, DTOs, and config trees** — `config.server.port` or reaching through a parsed JSON payload is fine: these are data with no behavior or invariants, and exposing their shape is their entire job. The law governs objects that encapsulate decisions, not records (see Encapsulation's "plain data carriers" caveat).
- **Don't mechanically wrap every hop in a delegating getter.** Replacing `customer.getWallet().balance()` with `customer.getWalletBalance()` complies with the letter of the law while keeping the coupling; do it for every inner field and the owner grows a wide, shallow forwarding interface. Prefer moving the *operation* (`customer.pay(due)`) over forwarding the *query*.

## Trade-offs

- **Pros:** representation changes stay local — only direct neighbors of a class notice its refactors; invariants become enforceable because every touch goes through the owner; tests need one collaborator, not a graph of stubs; call sites read as intent (`customer.pay`) rather than mechanism (`wallet.deduct`).
- **Cons:** over-applied, it produces the "wide shallow interface" — dozens of one-line delegation methods that exist only to satisfy the rule, bloating the owner and hiding the few methods that matter; each tell-don't-ask move adds a level of indirection to step through when debugging; drawing the line between "object with behavior" (law applies) and "plain data" (it doesn't) takes judgment the rule itself won't give you.

## Language Notes

- **Java / C# / PHP:** getter-culture languages are where the law was coined and where train wrecks flourish; C#'s null-conditional `?.` and PHP's `?->` make long chains null-safe and therefore even easier to leave in place. Records (`record` in Java/C#, readonly classes in PHP) mark the plain-data case where chaining is fine.
- **JavaScript / TypeScript & Swift:** optional chaining (`order?.customer?.wallet?.cash`) and Swift key paths make deep reaching one expression that silently yields `undefined`/`nil` as shapes drift — the chain keeps compiling while quietly doing nothing. The tell-don't-ask fix is identical; reserve chaining for data payloads.
- **Python:** nothing is truly private, so `customer._wallet.cash` always works — the law here is pure discipline. Properties don't help by themselves; they rename the reach without removing it. Dataclasses mark the exempt plain-data case.
- **C:** the train wreck is a pointer chain, `order->customer->wallet->cash`. The opaque-pointer idiom (struct body hidden in the `.c` file) makes the law physically enforceable: callers cannot dereference fields they cannot see, so they *must* call `customer_pay`.
- **C++:** same struct chains plus getters; a getter returning a reference to a member (`Wallet& wallet()`) is an open invitation to violate the law. Return values, take parameters, or move the operation onto the owner.
- **Rust:** ownership already leans this way — `customer.wallet_mut().deduct(due)` holds a mutable borrow of the whole customer, and module-level privacy hides fields by default, so handing out `&mut` to internals is both awkward and un-idiomatic. Methods on the owning type (`customer.pay(due)`) are the path of least resistance.
- **Go:** no getter culture, but exported struct fields make `o.Customer.Wallet.Cash` easy across packages. Unexported fields plus methods on the owner restore the boundary; accepting small interfaces ("hand a function only what it needs") is Go's idiom for the same idea.

## Examples

- [examples/law-of-demeter/law-of-demeter.py](../examples/law-of-demeter/law-of-demeter.py)
- [examples/law-of-demeter/law-of-demeter.cpp](../examples/law-of-demeter/law-of-demeter.cpp)
- [examples/law-of-demeter/law-of-demeter.java](../examples/law-of-demeter/law-of-demeter.java)
- [examples/law-of-demeter/law-of-demeter.cs](../examples/law-of-demeter/law-of-demeter.cs)
- [examples/law-of-demeter/law-of-demeter.js](../examples/law-of-demeter/law-of-demeter.js)
- [examples/law-of-demeter/law-of-demeter.php](../examples/law-of-demeter/law-of-demeter.php)
- [examples/law-of-demeter/law-of-demeter.swift](../examples/law-of-demeter/law-of-demeter.swift)

## Related Concepts

- **Encapsulation** protects one object's state behind its interface; the Law of Demeter is encapsulation applied across object graphs — `a.getB().getC().setX()` leaks B's and C's internals exactly as a public field leaks A's.
- **Coupling and Cohesion** name what the law optimizes: it is a concrete coupling rule ("know only your neighbors, one hop deep"), and tell-don't-ask raises cohesion by moving behavior into the class that owns the data it operates on.
- **Single Responsibility** explains why the paperboy digging through wallets is wrong twice over: managing the customer's money is the customer's job, and code that traverses another object's structure has quietly taken on that object's responsibilities.
- **Interface Segregation** guards against the failure mode of over-compliance: if satisfying the law means growing dozens of forwarding getters, the owner's interface is getting wide and shallow — move operations instead of delegating queries.
