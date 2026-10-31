---
name: {skill-name}
description: {Domain, e.g. "Gang of Four (GoF) design patterns"}, with a reference{ and runnable examples} per {item}. Use when a question names {an item} ({item-1}, {item-2}...), describes a problem {an item} might solve, compares {items}, or asks to review or refactor toward one.
---

<!--
  The description is always loaded: keep it to what the skill is plus one trigger per
  distinct case. Leave language lists and other details the body carries out of it.
-->

# {Skill Title}

Ground every {domain} answer in this skill's reference files, not in improvised definitions. {One sentence on when an item earns its place, e.g. "A pattern is the answer to specific forces: recommend one only when the user's problem shows them."}

## Workflow

For reviews, trace the user's implementation and callers before selecting catalog
items. Report evidence, a concrete failure/change scenario, impact, the smallest
correction, and a verification criterion. Separate defects from optional design
choices. For implementation requests, preserve supported contracts and validate
observable behavior. Keep detailed domain-specific review rules in a linked
reference when they would obscure the shared workflow.

1. **Identify the {item(s)}** in the catalog below, by name or by the symptoms in the user's problem. Done when every {item} the question names or implies is listed, or when none fits; then answer with the simpler solution that does.
2. **Read each identified reference** at `references/<item>.md` in full. When comparing {items}, read every one compared and contrast their intent, not their structure.
3. **Read the language example** at `examples/<item>/<item>.<ext>` for the user's language. For a language without an example, use the reference's Language Notes. _(Delete this step if the skill has no code examples.)_
4. **Answer** with what the {item} does, when it applies, the simpler alternative and when it wins, and {code/guidance} adapted to the user's domain in the language's idiomatic form. Done when every identified {item} has all four parts.

## {Domain} Catalog

Group {items} into the categories that make sense for this domain (creational/structural/behavioral, principle/practice, layer/tier, etc.). One table per category.

### {Category 1}

{One-line description of what this category of items has in common.}

| {Item}   | Intent               | Reference                                    |
| -------- | --------------------- | --------------------------------------------- |
| {Item A} | {What it does, in one line} | [references/{item-a}.md](references/{item-a}.md) |
| {Item B} | {What it does, in one line} | [references/{item-b}.md](references/{item-b}.md) |

### {Category 2}

{One-line description of what this category of items has in common.}

| {Item}   | Intent               | Reference                                    |
| -------- | --------------------- | --------------------------------------------- |
| {Item C} | {What it does, in one line} | [references/{item-c}.md](references/{item-c}.md) |

<!--
  Delete the "Examples" section below if this skill has no bundled code examples
  (e.g. a skill about system-design trade-offs or architectural principles may not need one).
-->

## Examples

Examples are self-contained and runnable, in {Language A, Language B, ...}. {Any idiomatic substitution, e.g. "C emulates objects with structs and function pointers."}

### Choosing languages

_Maintainer guidance: delete this subsection from a new skill._

**Only add an example file when the language genuinely supports the skill's concepts** — do not ship a file in every language for completeness.

| Skill type | Include | Omit | Rule |
| ---------- | ------- | ---- | ---- |
| OOP paradigm (classes, inheritance, pillars, SOLID) | Python, C++, Java, C#, JavaScript, PHP, Swift | C, Go, Rust | Requires first-class classes. Note idiomatic mappings in reference Language Notes only. |
| Design patterns (GoF, composable techniques) | Python, C, C++, Java, C#, JavaScript, Rust, Go, PHP, Swift | — | Patterns are idiomatically adapted (C emulates with structs/function pointers; Go/Rust use interfaces/traits). |
| Other catalog skills | Pick per item | — | Omit a language when the item is built into the language or has no honest mapping. |

List only the languages the skill actually ships. A language file may be absent per item
when it does not translate meaningfully; the item's reference notes the gap and the
idiomatic alternative in Language Notes.

<!--
  Cross-references between reference files use relative Markdown links, e.g.
  [Builder](builder.md), so agents can follow them and scripts/lint.sh can check them.
-->
