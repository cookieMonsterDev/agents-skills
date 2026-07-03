---
name: {skill-name}
description: Use when users ask how to {primary-capabilities}, especially when they need official {Product Name} documentation, exact links, or docs-grounded guidance.
---

{Product Name} questions are easy to answer from stale memory. Use this skill to ground answers in official {Product Name} documentation and return the closest authoritative page instead of generic advice.

## When to Use

Use this skill when the request is about:

- {Topic area 1}
- {Topic area 2}
- {Topic area 3}
- Troubleshooting when the user needs documentation, syntax guidance, or official references

Do not use this skill for:

- {Adjacent domain 1}. Use `{other-skill-name}` instead.
- {Adjacent domain 2}. Use `{other-skill-name}` instead.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- {Category 1}
- {Category 2}
- {Category 3}
- {Category 4}

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official docs first

- Treat `{docs.example.com}` as the source of truth.
- Prefer pages under <{https://docs.example.com/base-path}>.
- Search with the user's exact terms plus a focused phrase such as `{keyword-1}`, `{keyword-2}`, or `{keyword-3}`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact docs links, not just the docs homepage.
- Only provide examples or step-by-step instructions when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to {Product Name} docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example or steps, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer overview or getting-started pages before deep reference pages.
- For syntax questions, prefer reference pages over tutorials.
- For security questions, prefer dedicated security docs before generic configuration pages.
- If the user asks for a beginner walkthrough, start with a tutorial or quickstart instead of a raw reference page.

## Common Mistakes

- Answering from memory without verifying the current docs
- Linking the docs landing page when a narrower page exists
- {Product-specific mistake 1}
- {Product-specific mistake 2}
- Letting adjacent domains absorb the request when another skill is the sharper fit

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live docs as the final authority.
