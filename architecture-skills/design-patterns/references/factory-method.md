# Factory Method

**Category:** Creational

## Intent

Define an interface for creating an object, but let subclasses decide which class to instantiate. The creator's shared workflow calls an overridable creation step, so new product types plug in without touching the workflow.

## Problem

- A class contains useful logic (planning a delivery, running an import, rendering a document) but hard-codes `new Truck()` somewhere inside it, so reusing the logic with a different product means copy-paste or conditionals.
- `switch (type) { case "road": ...; case "sea": ... }` blocks appear wherever products are created, and each new type means editing all of them.
- Client code should work with products through a common interface and not know which concrete class it received.

## Structure

- **Product** — the common interface of the objects being created (`Transport`).
- **Concrete products** — the actual classes (`Truck`, `Ship`).
- **Creator** — declares the factory method (`createTransport()`) and usually contains business logic that calls it (`planDelivery()`).
- **Concrete creators** — override the factory method to return a specific product (`RoadLogistics` → `Truck`).

## When to Use

- A shared workflow needs one customizable creation step (the classic Template Method + creation combo).
- You don't know ahead of time the exact types your code must work with, and want new types added by adding a subclass, not by editing existing code.
- You want to give library users a documented hook for substituting the objects your framework creates.

## When Not to Use

- There is exactly one product and no variation is expected; call the constructor.
- Only the created object varies and there is no surrounding workflow — passing a constructor reference, closure, or callable as a parameter is simpler in most modern languages.
- The variation is data, not behavior; a lookup table or configuration usually beats a subclass per variant.

## Trade-offs

- **Pros:** creation is decoupled from use, new products don't require editing the creator's workflow, single obvious place per product for construction logic.
- **Cons:** a subclass per product can balloon the class count; trivial cases end up with ceremony a first-class function would avoid.

## Language Notes

- **Python / JavaScript / PHP:** classes and functions are first-class values, so passing the class or a closure directly often replaces the pattern; a full creator hierarchy pays off only when the creator has substantial shared logic.
- **Java / C#:** the pattern's natural habitat — abstract creator classes with protected factory methods are everywhere in the standard libraries (`Calendar.getInstance`, collection `Iterator`s).
- **Rust:** a trait with a creation method returning `Box<dyn Product>` mirrors the pattern; for a closed set of products, enums with a constructor `match` are usually preferred over trait objects.
- **Go:** no inheritance, so the "creator" is an interface the workflow function accepts; concrete creators are small structs satisfying it.
- **C:** emulated with function pointers: the creator is a struct holding a `create` function pointer used by the shared workflow function.
- **Swift:** protocols with default implementations in extensions give you the shared workflow; conforming types supply only the factory method.

## Examples

- [examples/factory-method/factory-method.py](../examples/factory-method/factory-method.py)
- [examples/factory-method/factory-method.c](../examples/factory-method/factory-method.c)
- [examples/factory-method/factory-method.cpp](../examples/factory-method/factory-method.cpp)
- [examples/factory-method/factory-method.java](../examples/factory-method/factory-method.java)
- [examples/factory-method/factory-method.cs](../examples/factory-method/factory-method.cs)
- [examples/factory-method/factory-method.js](../examples/factory-method/factory-method.js)
- [examples/factory-method/factory-method.rs](../examples/factory-method/factory-method.rs)
- [examples/factory-method/factory-method.go](../examples/factory-method/factory-method.go)
- [examples/factory-method/factory-method.php](../examples/factory-method/factory-method.php)
- [examples/factory-method/factory-method.swift](../examples/factory-method/factory-method.swift)

## Related Patterns

- **Abstract Factory** is usually implemented as a set of factory methods, one per product kind.
- **Template Method**: the factory method is a customizable step inside a template method's fixed workflow.
- **Prototype** avoids the creator subclass hierarchy by cloning a configured instance instead of instantiating a class.
