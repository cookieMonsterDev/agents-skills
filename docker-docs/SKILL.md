---
name: docker-docs
description: Use when users ask how to install, configure, build, run, network, secure, compose, orchestrate, or troubleshoot Docker containers, images, volumes, networks, registries, Docker Engine, Docker Compose, Buildx, Swarm, or the Docker Engine API, including Dockerfile syntax, Compose file format, CLI flags, daemon configuration, and Docker Desktop, especially when they need official Docker documentation, exact links, or docs-grounded guidance.
---

Docker questions are easy to answer from stale memory or pre-Compose-v2 patterns. Use this skill to ground answers in the official Docker documentation and return the closest authoritative page instead of generic container advice.

## When to Use

Use this skill when the request is about:

- Docker concepts, architecture, containers, images, and the Docker Engine daemon
- Installing or configuring Docker Engine, Docker Desktop, or Docker Compose
- Dockerfile syntax, image builds, multi-stage builds, and Buildx
- Compose file format, `docker compose` workflows, profiles, and overrides
- Container lifecycle: run, exec, logs, inspect, stop, restart, and resource limits
- Images: pull, push, tag, prune, and registry authentication
- Networking: bridge, host, overlay, published ports, and DNS
- Volumes, bind mounts, tmpfs, and storage drivers
- Docker Engine API, SDKs, and API version negotiation
- Swarm mode: services, stacks, secrets, configs, and nodes
- Security: rootless mode, content trust, Scout, and hardened images
- Troubleshooting daemon, build, networking, or registry errors

Do not use this skill for:

- Kubernetes cluster operations or `kubectl` usage. Use `kubernetes-docs` instead.
- AWS CLI commands for ECS, ECR, or Fargate. Use `aws-cli-docs` instead.
- Third-party orchestrators (Nomad, Podman docs) unless the question is about Docker compatibility or migration covered in Docker docs.
- Application framework questions unrelated to Docker (NestJS, Express, etc.) unless the user is asking about containerizing that stack per Docker docs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Installation and platform setup (Engine, Desktop, Compose)
- Dockerfile and image builds
- Compose file format and multi-container apps
- CLI reference (docker, compose, buildx)
- Networking, storage, and runtime configuration
- Registries, distribution, and image security
- Engine API and SDKs
- Swarm and orchestration
- Security, rootless, and supply chain
- Troubleshooting and diagnostics

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Docker docs first

- Treat `docs.docker.com` as the source of truth for Docker.
- Prefer the reference section at <https://docs.docker.com/reference/> for CLI syntax, file formats, and APIs.
- Prefer manuals at <https://docs.docker.com/manuals/> for install, configure, and operate workflows.
- Prefer guides at <https://docs.docker.com/guides/> for task-focused walkthroughs.
- Search with the user's exact terms plus focused Docker phrases such as `compose.yaml`, `HEALTHCHECK`, `buildx`, `--mount`, `overlay2`, or `DOCKER_HOST`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Compose questions, check Compose Specification and `docker compose` CLI docs before answering from legacy `docker-compose` v1 behavior.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For CLI flags, open the specific command reference page (for example `docker run`, `docker compose up`).
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Docker docs links, not just the docs homepage.
- Only provide Dockerfile, Compose, or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Docker docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example Dockerfile, Compose, or CLI commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer Get Started and Engine overview before CLI reference pages.
- For install questions, prefer Engine install or Desktop install manuals before troubleshooting.
- For build questions, prefer Dockerfile reference and `docker build` / Buildx docs before improvising layer caching advice.
- For Compose questions, distinguish Compose file reference (schema) from `docker compose` CLI (commands).
- For networking questions, check network driver docs and port publishing before guessing DNS or firewall behavior.
- For storage questions, distinguish volumes, bind mounts, and tmpfs in the manuals before recommending host paths.
- For API questions, check Engine API version matrix and `docker version` output semantics before hardcoding endpoints.
- Default to Compose v2 (`docker compose`) unless the user explicitly needs legacy `docker-compose` v1.

## Common Mistakes

- Answering from memory without verifying the current Docker docs
- Linking the Docker docs landing page when a narrower reference or manual page exists
- Mixing legacy `docker-compose` (v1, hyphenated) with `docker compose` (v2, plugin) syntax or behavior
- Confusing bind mounts with named volumes when persistence or permissions matter
- Recommending `latest` tags or root-in-container defaults without checking security guidance
- Treating Swarm stack deploy syntax as equivalent to Compose file features without checking compatibility notes
- Quoting deprecated Dockerfile instructions without checking the current Dockerfile reference

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Docker docs as the final authority.
