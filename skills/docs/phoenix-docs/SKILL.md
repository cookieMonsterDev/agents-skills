---
name: phoenix-docs
description: Official Phoenix documentation, answered with links to the exact pages. Use for any Phoenix question, including routers and plugs, controllers and HEEx templates, contexts and Ecto, LiveView, channels and PubSub, authentication, or releases and deployment.
---

# Phoenix Docs

Phoenix answers drift with each release and span several Hex packages, so ground each answer in the live docs at <https://phoenix.hexdocs.pm/>, not memory, and link the exact page behind every claim.

Route Django, Flask or FastAPI patterns to `django-docs`, `flask-docs` or `fastapi-docs`. Plain Elixir language questions belong to the Elixir guides, and Ecto-only or third-party package questions to their own docs, unless the question turns on Phoenix behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `phoenix.hexdocs.pm` with the user's exact terms plus Phoenix vocabulary such as `pipe_through`, `assign`, `LiveView`, `context`, `changeset`, or `mix phx.gen.auth`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- LiveView, PubSub and HEEx component modules: their own Hex packages at <https://hexdocs.pm/phoenix_live_view/> and <https://hexdocs.pm/phoenix_pubsub/>, not `phoenix.hexdocs.pm`.
- Version-specific changes: the changelog and migration notes.
- First steps: Overview, Installation and Up and Running, before deep reference pages.
- Routing: the Routing guide, including pipeline and scope behavior.
- Request flow: Endpoint, Router, Controller, then View, in the request life-cycle guides.
- Data: the Contexts and Ecto guides.
- Real-time: tell LiveView from Channels, and check the PubSub clustering notes for production.
- Auth: `mix phx.gen.auth` and Scopes.
- Deployment: the Deployment and Releases guides.
- Generators: `mix help phx.new` and the generator docs, for flags such as `--no-ecto` or `--no-live`.

## Gotchas

- Keep business logic in contexts and controllers thin.
- LiveViews are stateful processes; controller actions are stateless.
- Plugs compose at three levels: the endpoint, router pipelines and controllers.
- Configure production through the Deployment and Releases guides rather than the development setup.
- Multi-node LiveView or long-polling deployments need the clustering and sticky-session setup the docs describe.
