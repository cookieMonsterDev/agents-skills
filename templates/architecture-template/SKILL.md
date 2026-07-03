---
name: {skill-name}
description: Explains and applies {domain, e.g. "the Gang of Four design patterns" / "the 12-factor app principles"} with idiomatic {guidance/examples} in {context, e.g. "Python, Java, Go, and Rust" or "system design"}. Use when users ask about {topic-1}, {topic-2}, {topic-3}, when they need help choosing {an item} for a design problem, when refactoring toward {an item}, or when they want {an item} example in a specific {language/context}.
---

# {Skill Title}

Ground {domain} answers in the reference files bundled with this skill instead of improvising definitions. Each {item, e.g. "pattern" / "principle"} has a reference file explaining it{, and a folder of runnable examples in popular languages — delete this clause if the skill has no code examples}.

## When to Use

- The user names {an item} directly ("show me the {item} in {language}")
- The user describes a problem that maps to {an item} ("{example problem phrasing}")
- The user asks to compare {items} ("{item A} vs {item B}?")
- The user wants existing code or design refactored toward {an item}

## Workflow

1. **Identify the {item(s)}** from the user's question using the catalog below.
2. **Read the reference file** at `references/<item>.md` for the explanation, applicability, trade-offs, and related {items}.
3. **Read the language example** at `examples/<item>/<item>.<ext>` when the user works in (or asks for) a specific language. Adapt it to their domain rather than pasting the generic example verbatim. _(Delete this step if the skill has no code examples.)_
4. **Answer** with: what the {item} does, when to use it (and when not to), and {code/guidance} adapted to the user's context.

If the user's problem does not match any {item} cleanly, say so — do not force {an item} where a simpler solution fits.

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

Each {item} has a folder `examples/<item>/` with self-contained, runnable examples named `<item>.<ext>`:

| Language   | File            | Notes                                            |
| ---------- | --------------- | ------------------------------------------------- |
| {Language} | `<item>.{ext}`  | {Any gap or idiomatic substitution for this language} |

A language file may be absent when {an item} does not translate meaningfully to that language; the {item}'s reference file notes such gaps and idiomatic alternatives.

## Answering Guidelines

- Prefer the language's/domain's idiomatic form over a literal textbook description.
- Mention trade-offs and simpler alternatives, not just the mechanics.
- When comparing {items}, read both reference files and contrast intent, not structure.
- Do not recommend {a commonly-overused item}, or any {item}, as a default; {items} are solutions to specific forces, not style goals.
