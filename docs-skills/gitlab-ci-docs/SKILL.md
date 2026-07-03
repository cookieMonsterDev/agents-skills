---
name: gitlab-ci-docs
description: Use when users ask how to write, explain, configure, secure, optimize, or troubleshoot GitLab CI/CD pipelines, `.gitlab-ci.yml` syntax, stages, jobs, runners, variables, inputs, expressions, artifacts, caches, environments, deployments, CI/CD components, parent-child pipelines, merge request pipelines, or pipeline schedules, especially when they need official GitLab documentation, exact links, or docs-grounded YAML guidance.
---

GitLab CI/CD questions are easy to answer from stale memory or GitHub Actions assumptions. Use this skill to ground answers in official GitLab documentation and return the closest authoritative page instead of generic CI/CD advice.

## When to Use

Use this skill when the request is about:

- GitLab CI/CD concepts, terminology, or product boundaries
- `.gitlab-ci.yml` syntax, stages, jobs, rules, needs, extends, include, or workflow keywords
- GitLab-hosted runners, self-managed runners, project runners, or runner configuration
- CI/CD variables, predefined variables, inputs, expressions, or pipeline-level configuration
- Artifacts, caches, reports, dependencies, and job outputs
- Environments, deployments, review apps, and deployment tiers
- CI/CD components, the CI/CD Catalog, reusable pipeline configuration, or `include:component`
- Parent-child pipelines, multi-project pipelines, merge request pipelines, merge trains, or pipeline schedules
- Pipeline security, secrets management, external secrets, masked/protected variables, or ID tokens
- Migrating to or from GitLab CI/CD, or comparing GitLab CI/CD with other CI systems
- Troubleshooting pipeline behavior when the user needs documentation, syntax guidance, or official references

Do not use this skill for:

- GitHub Actions workflows, runners, or YAML. Use `github-actions-docs`.
- GitLab repository, merge request, or project administration unrelated to CI/CD. Search GitLab docs outside the CI/CD section.
- A specific failing pipeline log or CI failure triage in this repository when another skill such as `gh-fix-ci` is the sharper fit for GitHub-hosted checks.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, tutorials, and pipeline concepts
- YAML syntax and pipeline configuration
- Runners and execution environment
- Variables, inputs, and expressions
- Artifacts, caches, and job dependencies
- Environments and deployments
- CI/CD components and reusable configuration
- Security, secrets, and pipeline hardening
- Advanced pipeline types and orchestration
- Monitoring, debugging, and troubleshooting

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official GitLab docs first

- Treat `docs.gitlab.com` as the source of truth.
- Prefer pages under <https://docs.gitlab.com/ci/>.
- Search with the user's exact terms plus a focused GitLab CI phrase such as `gitlab-ci.yml`, `rules`, `needs`, `include:component`, `CI/CD inputs`, or `self-managed runners`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or tier-gated, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact GitLab docs links, not just the CI/CD homepage.
- Only provide YAML or step-by-step examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to GitLab docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example YAML or steps, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer overview or getting-started pages before the YAML reference.
- For syntax questions, prefer the CI/CD YAML syntax reference and the specific keyword section.
- For variable questions, distinguish CI/CD variables, predefined variables, inputs, and secrets before recommending a pattern.
- For security questions, prefer pipeline security, secrets management, and external secrets docs before suggesting masked variables alone.
- For runner questions, prefer runner overview and registration docs before guessing executor settings.
- For reusable configuration, prefer CI/CD components and `include` docs before inventing copy-paste templates.
- If the user asks for a beginner walkthrough, start with the first-pipeline tutorial instead of the full YAML reference.

## Common Mistakes

- Answering from memory without verifying the current docs
- Linking the GitLab CI/CD landing page when a narrower page exists
- Mixing GitHub Actions syntax or concepts with GitLab CI/CD keywords
- Treating CI/CD variables and CI/CD inputs as interchangeable when the docs recommend inputs for pipeline parameters
- Suggesting long-lived credentials in plain variables when secrets management or external secrets are documented
- Ignoring tier or offering limits for Premium or Ultimate features such as merge trains or external secrets
- Letting adjacent domains absorb the request when `github-actions-docs` or another skill is the sharper fit

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live GitLab docs as the final authority.
