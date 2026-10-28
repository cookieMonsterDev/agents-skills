---
name: github-actions-docs
description: Official GitHub Actions documentation, answered with links to the exact pages. Use for any GitHub Actions question, including workflow syntax and triggers, runners, reusable workflows and custom actions, secrets and OIDC, or deployments and environments.
---

# GitHub Actions Docs

GitHub Actions answers drift with every platform change, so ground each answer in the live docs at <https://docs.github.com/en/actions>, not memory, and link the exact page behind every claim.

Route GitLab CI/CD pipelines to `gitlab-ci-docs`. Pull request, branch and repository operations, CodeQL code scanning, and Dependabot configuration belong to their own sections of `docs.github.com` unless the question turns on GitHub Actions behavior; triage of a specific failing check starts from that run's logs rather than the docs.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.github.com/en/actions` with the user's exact terms plus GitHub Actions vocabulary such as `workflow syntax`, `OIDC`, `reusable workflows`, or `self-hosted runners`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and workflow YAML only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Syntax: the workflow syntax, events, contexts, variables or expressions reference pages.
- Security: the `Secure use`, `Secrets`, `GITHUB_TOKEN`, `OpenID Connect` and artifact attestation docs.
- Deployments: the environments and deployment protection docs, before cloud-specific examples.
- Migration: the migration hub page first, then the platform-specific migration guide.

## Gotchas

- Reusable workflows and composite actions are different mechanisms; name the one the answer uses.
- Authenticate to cloud providers with OIDC, the documented path, rather than long-lived cloud credentials.
