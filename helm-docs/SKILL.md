---
name: helm-docs
description: Use when users ask how to install, search, deploy, upgrade, rollback, uninstall, template, lint, package, or troubleshoot Helm charts and releases on Kubernetes, including chart development, values, repositories, hooks, plugins, OCI registries, Helm 4 changes, or the Helm Go SDK, especially when they need official Helm documentation, exact links, or docs-grounded guidance.
---

Helm questions are easy to answer from stale memory or Helm 3 assumptions that no longer apply in Helm 4. Use this skill to ground answers in the official Helm documentation and return the closest authoritative page instead of generic Kubernetes packaging advice.

## When to Use

Use this skill when the request is about:

- Helm concepts: charts, releases, repositories, and values
- Installing, upgrading, rolling back, and uninstalling Helm releases
- Searching charts on Artifact Hub or configured repositories
- Chart development, templating, linting, and packaging
- Values files, `--set`, `--set-json`, and override precedence
- Helm plugins and the Go SDK
- Helm 4 overview, breaking changes, and migration from Helm 3
- Helm CLI command reference and flags

Do not use this skill for:

- Core Kubernetes API resources, kubectl, or cluster administration without Helm context. Use `kubernetes-docs` instead.
- Raw Docker image builds or Compose files. Use `docker-docs` instead.
- Terraform Helm provider configuration unless the question is specifically about Helm chart behavior documented on helm.sh.
- Argo CD, Flux, or other GitOps tools unless the question is about Helm chart mechanics documented by Helm.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Introduction and core concepts
- Installing and using Helm day to day
- Chart development and templating
- Best practices and chart design
- Plugins and extensibility
- Helm CLI command reference
- Helm 4 migration and version differences

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Helm docs first

- Treat `helm.sh/docs` as the source of truth for Helm.
- Prefer pages under <https://helm.sh/docs/>.
- Default to the current documentation version (4.2.2) unless the user specifies another supported version.
- Search with the user's exact terms plus focused Helm phrases such as `helm upgrade`, `values.yaml`, `chart hooks`, `helm template`, `OCI`, or `Artifact Hub`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Helm 4 questions, check the Helm 4 Overview before answering from Helm 3 knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For CLI flags, open the specific subcommand reference page.
- If a page appears renamed, moved, or not yet updated for Helm 4, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Helm docs links, not just the docs homepage.
- Only provide chart YAML or Helm command examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Helm docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example Helm commands or chart snippets, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Introduction and Using Helm before the full command reference.
- For chart authoring questions, prefer Chart Template Guide and Best Practices before guessing template patterns.
- For release lifecycle questions, distinguish install, upgrade, rollback, and uninstall docs.
- For values override questions, open Using Helm sections on `--values` and `--set` precedence.
- For Helm 4 questions, start with Helm 4 Overview and verify whether older pages are marked outdated.
- For command syntax questions, open the generated subcommand page under Helm Commands.

## Common Mistakes

- Answering from Helm 3 memory without checking Helm 4 docs
- Linking the Helm docs homepage when a narrower command or guide page exists
- Confusing chart version with app version in release output
- Assuming a default chart repository exists in Helm 3+ without `helm repo add`
- Recommending `--recreate-pods` without noting deprecation in current Helm versions
- Treating Artifact Hub search results as installed local repositories

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Helm docs as the final authority.
