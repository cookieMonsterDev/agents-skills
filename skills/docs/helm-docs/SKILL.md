---
name: helm-docs
description: Official Helm documentation, answered with links to the exact pages. Use for any Helm question, including chart development and templates, releases and upgrades, values, repositories and OCI registries, plugins and the Go SDK, or Helm 4 migration.
---

# Helm Docs

Helm 3 assumptions no longer hold in Helm 4, so ground each answer in the live docs at <https://helm.sh/docs/>, not memory, and link the exact page behind every claim.

Route core Kubernetes resources, `kubectl` or cluster administration to `kubernetes-docs`, Docker image builds or Compose files to `docker-docs`, and Terraform Helm provider configuration to `terraform-docs`. Argo CD, Flux and other GitOps tools belong to their own docs unless the question turns on Helm chart behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `helm.sh/docs` with the user's exact terms plus Helm vocabulary such as `helm upgrade`, `values.yaml`, `chart hooks`, `helm template`, `OCI`, or `Artifact Hub`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and Helm commands or chart snippets only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: default to the current docs version (4.3.1) unless the user names another supported version.
- Helm 4 or migration from Helm 3: the Helm 4 Overview first, then check whether older pages are marked outdated or not yet updated for Helm 4.
- Beginner questions: Introduction and Using Helm, before the full command reference.
- Chart authoring: the Chart Template Guide and Best Practices, before improvising template patterns.
- Values overrides: the Using Helm sections on `--values` and `--set` precedence.
- Command syntax and flags: the generated subcommand page under Helm Commands.

## Gotchas

- Chart version and app version are separate fields in release output.
- Helm 3 and later ship with no default chart repository; add one with `helm repo add`.
- Note that `--recreate-pods` is deprecated in current Helm versions whenever it comes up.
- Artifact Hub search results are hub listings, separate from the repositories configured locally.
