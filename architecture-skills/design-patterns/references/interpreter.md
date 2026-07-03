# Interpreter

**Category:** Behavioral

## Intent

Given a small language, define a class (or type) per grammar rule and an `interpret` operation on each, so sentences in the language are represented as syntax trees that evaluate themselves.

## Problem

- The application keeps re-implementing ad-hoc parsing and evaluation for the same kind of input: filter expressions, pricing rules, feature-flag conditions, spreadsheet formulas.
- Rules must be composed, stored, and evaluated against varying contexts (an expression like `(x + y) * 2 - z` evaluated with different variable bindings).
- The grammar is small and stable enough that a hand-built object tree is simpler than pulling in a parser generator or embedding a scripting engine.

## Structure

- **Abstract expression** — declares `interpret(context)`.
- **Terminal expression** — leaf rules of the grammar (a number literal, a variable reference).
- **Non-terminal expression** — composite rules holding sub-expressions (addition, multiplication); interpretation recurses into children.
- **Context** — the data interpretation runs against (typically a map of variable bindings).
- **Client** — builds (or parses input into) the expression tree, then calls `interpret` on the root.

## When to Use

- A recurring family of problems can be expressed as sentences in a small grammar (queries, rules, formulas).
- Expressions must be built at runtime, stored, inspected, or evaluated repeatedly against different contexts.
- The grammar is small; each rule maps cleanly to one class or enum variant.

## When Not to Use

- The grammar is large or evolving quickly — the class-per-rule approach explodes; use a parser generator (ANTLR, yacc) or an existing expression engine instead.
- The host language can express the rules directly: a closure `(ctx) => ctx.x + ctx.y` often replaces an entire expression tree when trees never need to be inspected or serialized.
- Performance is critical: tree-walking interpretation is the slowest evaluation strategy (consider compiling to closures or bytecode).

## Trade-offs

- **Pros:** each grammar rule is isolated and testable, trees are inspectable and serializable data, new rules are added as new node types without touching existing ones.
- **Cons:** one type per rule is verbose for anything beyond small grammars, tree-walking is slow, and the pattern says nothing about parsing — building the tree from text is a separate (often harder) problem.

## Language Notes

- **Rust / Swift:** an enum with a recursive/`indirect` variant per rule plus one `match`/`switch` in `eval` is the idiomatic form — no trait objects or class hierarchy needed.
- **Python / PHP / Java / C# / C++:** the classic form with an expression interface and one class per rule; Java `sealed` interfaces and C# records reduce the boilerplate.
- **JavaScript:** functions composing functions (`add(variable("x"), literal(2))` returning `env => ...`) express the tree without classes and evaluate faster.
- **Go:** a small `Expr` interface with `Eval(env)` implemented by one struct per rule.
- **C:** emulated with a tagged struct (node kind + children) and a recursive `eval` switching on the kind, or function pointers per node.
- Real-world incarnations: regular expression engines, SQL `WHERE` clause evaluators, spreadsheet formulas, and rule engines.

## Examples

- [examples/interpreter/interpreter.py](../examples/interpreter/interpreter.py)
- [examples/interpreter/interpreter.c](../examples/interpreter/interpreter.c)
- [examples/interpreter/interpreter.cpp](../examples/interpreter/interpreter.cpp)
- [examples/interpreter/interpreter.java](../examples/interpreter/interpreter.java)
- [examples/interpreter/interpreter.cs](../examples/interpreter/interpreter.cs)
- [examples/interpreter/interpreter.js](../examples/interpreter/interpreter.js)
- [examples/interpreter/interpreter.rs](../examples/interpreter/interpreter.rs)
- [examples/interpreter/interpreter.go](../examples/interpreter/interpreter.go)
- [examples/interpreter/interpreter.php](../examples/interpreter/interpreter.php)
- [examples/interpreter/interpreter.swift](../examples/interpreter/interpreter.swift)

## Related Patterns

- **Composite** — the expression tree *is* a composite; Interpreter adds the evaluation operation to it.
- **Visitor** keeps the tree pure data and moves `interpret` (and other operations like pretty-printing) into visitor classes.
- **Flyweight** can share terminal nodes (the same literal or variable appearing many times).
- **Iterator** can traverse the tree without evaluating it.
