---
name: docker-docs
description: Official Docker documentation, answered with links to the exact pages. Use for any Docker question, including Dockerfiles and Buildx, Docker Compose, Engine networking and storage, registries, the Engine API, Swarm, or Docker Desktop.
---

# Docker Docs

Docker answers drift toward legacy `docker-compose` v1 patterns and stale Dockerfile syntax, so ground each answer in the live docs at <https://docs.docker.com/>, not memory, and link the exact page behind every claim.

Route Kubernetes clusters and `kubectl` to `kubernetes-docs`, ECS and Fargate to `aws-ecs-docs`, and AWS CLI commands for ECR to `aws-cli-docs`. Nomad, Podman and application frameworks belong to their own docs unless the question turns on Docker compatibility, migration, or containerizing that stack.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.docker.com` with the user's exact terms plus Docker vocabulary such as `compose.yaml`, `HEALTHCHECK`, `buildx`, `--mount`, `overlay2`, or `DOCKER_HOST`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and Dockerfile, Compose or CLI examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- CLI syntax, file formats and APIs: the reference section at <https://docs.docker.com/reference/>, down to the specific command page such as `docker run` or `docker compose up`.
- Install, configure and operate: the manuals at <https://docs.docker.com/manuals/>, starting with the Engine or Desktop install manual for install questions.
- Task walkthroughs: the guides at <https://docs.docker.com/guides/>.
- Concepts: Get Started and the Engine overview, before CLI reference pages.
- Compose: the Compose Specification for `compose.yaml` keys, and the `docker compose` CLI reference for commands.
- Builds: the Dockerfile reference and the `docker build` / Buildx docs, before layer-caching advice.
- Networking: the network driver and port publishing docs, before DNS or firewall advice.
- Storage: the volumes, bind mounts and tmpfs manuals, before recommending host paths.
- Engine API: the Engine API version matrix and `docker version` output semantics, before hardcoding endpoints.

## Gotchas

- Default to Compose v2 (`docker compose`, the plugin); use legacy `docker-compose` v1 (hyphenated) syntax and behavior only when the user needs it.
- Named volumes and bind mounts differ on persistence and permissions; name which one the answer uses.
- Check the security guidance before recommending `latest` tags or root-in-container defaults.
- Check the Swarm compatibility notes before carrying Compose file features into a stack deploy.
- Confirm each Dockerfile instruction against the current Dockerfile reference, which marks deprecated ones.
