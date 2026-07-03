# {Item Name}

**Category:** {Category}

## Intent

{One or two sentences: what force this item resolves and how, at the level of "define X so that Y happens without Z."}

## Problem

- {A concrete situation where the absence of this item causes pain — a symptom, not just an abstract description.}
- {A second forcing scenario, phrased in terms a reader would recognize from their own code/system.}
- {A third, if there's a genuinely distinct pressure driving toward this item; delete if two is enough.}

## Structure

- **{Role A}** — {what it owns and does}.
- **{Role B}** — {what it owns and does, and how it relates to Role A}.
- **{Role C}** — {add or remove roles to match the actual shape of this item}.

## When to Use

- {A concrete signal that this item fits — not just a restatement of the intent.}
- {Another signal, ideally one you'd notice by reading code or a system diagram.}
- {A third, if applicable.}

## When Not to Use

- {The most common misapplication — when people reach for this item out of habit rather than need.}
- {A case where a simpler alternative wins; name the alternative.}
- {A case where a different item in this same catalog is the better fit; name it and cross-reference.}

## Trade-offs

- **Pros:** {2-4 concrete benefits, not generic praise.}
- **Cons:** {2-4 concrete costs — what gets harder, riskier, or more indirect as a result of adopting this item.}

<!--
  Rename "Language Notes" to fit the domain (e.g. "Platform Notes", "Team Notes",
  "Scale Notes") or delete the section entirely if this item doesn't vary by
  language/platform/context.
-->

## Language Notes

- **{Language/Context A}:** {the idiomatic form this item takes here, and any built-in language feature that replaces it outright.}
- **{Language/Context B}:** {ditto — call out where the textbook shape doesn't fit and what's used instead.}
- **Languages without examples:** when a language lacks the paradigm your skill teaches (e.g. no classes in Go for an OOP skill), document the mapping here instead of adding an example file.

<!--
  Delete the "Examples" section if this skill has no bundled code examples.
  Link only languages that actually have a file in examples/<item>/.
  Do not list every language your skill might ever support — list only what exists.
-->

## Examples

- [examples/example-item/example-item.py](../examples/example-item/example-item.py)
- [examples/example-item/example-item.cpp](../examples/example-item/example-item.cpp)
<!-- Add one line per language file that exists. Omit languages with no file. -->

## Related {Items}

- **{Related Item A}** {how it differs in intent or structure — the distinction a reader needs to pick the right one}.
- **{Related Item B}** {ditto}.
