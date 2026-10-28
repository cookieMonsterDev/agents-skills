---
name: gitlab-ci-docs
description: Official GitLab CI/CD documentation, answered with links to the exact pages. Use for any GitLab CI/CD question, including `.gitlab-ci.yml` syntax, runners, variables and inputs, artifacts and caches, environments and deployments, or CI/CD components.
---

# GitLab CI/CD Docs

GitLab CI/CD answers drift toward stale keywords and GitHub Actions habits, so ground each answer in the live docs at <https://docs.gitlab.com/ci/>, not memory, and link the exact page behind every claim.

Route GitHub Actions workflows, runners or YAML to `github-actions-docs`. GitLab repository, merge request or project administration outside CI/CD lives in the rest of `docs.gitlab.com`.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.gitlab.com` with the user's exact terms plus GitLab CI/CD vocabulary such as `gitlab-ci.yml`, `rules`, `needs`, `include:component`, `CI/CD inputs`, or `self-managed runners`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and `.gitlab-ci.yml` examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Syntax: the CI/CD YAML syntax reference, at the specific keyword section.
- Variables: tell CI/CD variables, predefined variables, inputs and secrets apart before recommending a pattern.
- Secrets: the pipeline security, secrets management and external secrets docs, before masked variables alone.
- Runners: the runner overview and registration docs, before executor settings.
- Reusable configuration: the CI/CD components and `include` docs, before copy-paste templates.
- Beginner walkthroughs: the first-pipeline tutorial, before the full YAML reference.

## Gotchas

- Use GitLab CI/CD keywords; GitHub Actions syntax and concepts do not carry over.
- Use CI/CD inputs for pipeline parameters, as the docs recommend; CI/CD variables are a separate mechanism.
- Keep credentials in secrets management or external secrets rather than long-lived plain variables.
- State the tier or offering for Premium or Ultimate features such as merge trains and external secrets.
