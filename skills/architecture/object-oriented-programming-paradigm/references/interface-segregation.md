# Interface Segregation Principle

**Category:** SOLID Principles

## Intent

Keep interfaces small and shaped to what each client actually needs. No caller should be forced to depend on methods it never calls — split a fat contract into several focused ones so implementers provide only real behavior and clients see only the seam they use.

## Problem

- An `OfficeMachine` interface declares `print`, `scan`, and `fax`. A simple desk printer implements all three but `scan` and `fax` throw `NotSupported` — the contract lied about what the object can do, and every caller must guard against methods that exist only to satisfy the interface.
- A reporting service takes an `OfficeMachine` just to call `print`, yet its tests must stub `scan` and `fax` anyway — the fat interface leaks unrelated capabilities into code that has no business knowing they exist.
- Adding a fourth capability (`staple`) to the monolith interface forces every implementer — including the printer that will never staple — to compile against the new method, reimplement a stub, and ship a change it did not need.
- The `NotSupported` stubs are a Liskov smell in disguise: callers cannot treat every `OfficeMachine` as interchangeable for every operation, even though the type system says they can.

## Structure

- **Fat interface (the smell)** — one type listing every operation the *family* of devices might offer (`print`, `scan`, `fax`); clients and implementers are coupled to the union of all capabilities, not to what any one of them needs.
- **Segregated interfaces** — one contract per capability (`Printer`, `Scanner`, `FaxMachine`); each names only the methods relevant to that job.
- **Focused implementers** — `SimplePrinter` implements `Printer` only; `MultiFunctionDevice` implements all three interfaces because it genuinely supports all three — no stubs, no lies.
- **Client-specific dependencies** — the print queue depends on `Printer`; the document archive depends on `Scanner`; each client imports the smallest contract that covers its use case.

The principle applies at every boundary where code depends on an abstraction: public interfaces, base classes used as contracts, even the small interface a Go consumer declares — if a client uses one method, it should not be handed a type with ten.

## When to Use

- Implementers leave methods empty, return a sentinel, or throw `NotSupported`/`UnsupportedOperationException` to satisfy an interface they only partially support — the interface is wider than the object.
- Tests mock an interface and must stub methods the code under test never touches, because the type bundles unrelated operations.
- Different clients use different subsets of the same interface, and a change driven by one client's needs (adding `staple` for the binder) forces every other client and implementer to notice.
- An interface grew by accretion — each new device type added its unique method to the shared contract instead of getting its own.

## When Not to Use

- **Don't atomize into one-method interfaces everywhere.** A `Printer` with `print` and `getStatus` is one cohesive capability; splitting `print` and `getStatus` into separate interfaces serves no distinct client and just multiplies type noise.
- **A genuine multi-capability object used as a whole is fine.** A `MultiFunctionDevice` that truly prints, scans, and faxes can implement three small interfaces — segregation is about what *clients* depend on, not about forbidding objects that do several jobs.
- **Stable, complete contracts aren't fat by default.** `List` in the standard library has many methods because every list implementation genuinely supports them and every list client may need any of them — segregating `get` from `add` would serve no one.
- If the real problem is that one class serves too many *actors* rather than that one interface serves too many *clients*, that is **Single Responsibility** — fix the class first; the interface shape often follows.

## Trade-offs

- **Pros:** implementers ship only real behavior — no stub methods, no lying types; clients depend on the smallest surface, so unrelated API changes stop rippling into them; tests stub only what the code calls; new capabilities arrive as new interfaces without reopening existing ones.
- **Cons:** more types to name, file, and discover; a single physical object that implements several interfaces can be awkward to pass where one aggregate type used to suffice; drawing the split line wrongly produces a forest of tiny interfaces that are harder to navigate than one honest fat type; over-segregation can mirror the "anemic interface" failure mode of over-splitting classes.

## Language Notes

- **Java / C# / PHP / Swift:** the classic home — `interface`/`protocol` keywords make segregation explicit. C# interface segregation is idiomatic (`IReadOnlyList<T>` vs `IList<T>`); watch for "service interfaces" that mirror one concrete class one-to-one — segregate by *client need*, not by class file.
- **Python:** `typing.Protocol` (structural) lets each consumer declare the one-method protocol it needs (`class Printer(Protocol): def print(...): ...`) without touching implementers — segregation without a shared base. `abc.ABC` (nominal) behaves like Java; keep ABCs small.
- **JavaScript / TypeScript:** structural typing segregates naturally — a function that only calls `.print(doc)` accepts any object with `print`, no shared interface required. Explicit `interface` types help when you want a named, checkable contract shared across modules.
- **Go:** consumer-side interfaces are segregation by default — the HTTP handler declares `type Printer interface { Print([]byte) error }` with one method, and only types that print satisfy it. Resist declaring large interfaces in a shared package "for reuse"; let each consumer own its small need.
- **Rust:** traits are the contract; prefer several small traits (`Print`, `Scan`) over one `OfficeMachine` supertrait unless a client genuinely needs the bundle. Blanket impls and trait objects (`Box<dyn Printer>`) let you pass segregated seams at runtime.
- **C++:** abstract base classes with pure virtuals; a class forced to inherit a wide ABC stubs out unimplemented pure virtuals — the same smell as Java. Prefer several small ABCs or template constraints (`requires T.print(doc)`) over one kitchen-sink base.
- **C:** no interfaces — segregation is a struct of function pointers per capability (`PrinterVTable` with only `print`, `ScannerVTable` with only `scan`). A device that does both holds both vtables or exposes both through separate handles.

## Examples

- [examples/interface-segregation/interface-segregation.py](../examples/interface-segregation/interface-segregation.py)
- [examples/interface-segregation/interface-segregation.cpp](../examples/interface-segregation/interface-segregation.cpp)
- [examples/interface-segregation/interface-segregation.java](../examples/interface-segregation/interface-segregation.java)
- [examples/interface-segregation/interface-segregation.cs](../examples/interface-segregation/interface-segregation.cs)
- [examples/interface-segregation/interface-segregation.js](../examples/interface-segregation/interface-segregation.js)
- [examples/interface-segregation/interface-segregation.php](../examples/interface-segregation/interface-segregation.php)
- [examples/interface-segregation/interface-segregation.swift](../examples/interface-segregation/interface-segregation.swift)

## Related Concepts

- **[Single Responsibility](single-responsibility.md)** — SRP splits a class by *actor* (reason to change); ISP splits an interface by *client* (methods actually called). A god class often grows a god interface; fixing one frequently exposes the other.
- **[Dependency Inversion](dependency-inversion.md)** — the inverted abstraction should be consumer-shaped and minimal; ISP is how you keep that abstraction from swelling into a mirror of every implementation's full surface.
- **[Liskov Substitution](liskov-substitution.md)** — `NotSupported` stubs exist because a fat interface promises substitutability the implementations cannot deliver; segregated interfaces shrink the promise to what each type can honestly fulfill.
- **[Interfaces and Abstract Classes](interfaces-and-abstract-classes.md)** — the mechanics of declaring contracts; ISP is the sizing rule for those contracts once you decide to extract one.
- **[Coupling and Cohesion](coupling-and-cohesion.md)** — a fat interface couples every client to every method on it; segregation lowers coupling by letting each client depend only on the cohesive subset it uses.
