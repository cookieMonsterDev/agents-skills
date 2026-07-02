---
name: phoenix-docs
description: Use when users ask how to build, explain, configure, route, secure, test, deploy, or troubleshoot Phoenix web applications and APIs, including routers, controllers, contexts, Ecto, LiveView, channels, plugs, HEEx templates, authentication, PubSub, generators, or Elixir releases, especially when they need official Phoenix documentation, exact links, or docs-grounded Elixir guidance.
---

Phoenix questions are easy to answer from stale memory or Rails/Django assumptions. Use this skill to ground answers in the official Phoenix documentation and return the closest authoritative page instead of generic Elixir or Plug advice.

## When to Use

Use this skill when the request is about:

- Phoenix concepts, project structure, endpoints, routers, and the request life-cycle
- Controllers, views, HEEx templates, function components, and layouts
- Routing, pipelines, scopes, and verified routes
- Plug middleware in endpoints, routers, and controllers
- Contexts, Ecto schemas, changesets, queries, and migrations
- LiveView, channels, PubSub, and real-time features
- Authentication and authorization (`mix phx.gen.auth`, scopes)
- Testing with `ConnTest`, `DataCase`, and channel tests
- Deployment, releases, assets, secrets, and production configuration
- Generators: `mix phx.new`, `mix phx.gen.html`, `mix phx.gen.live`, `mix phx.gen.auth`

Do not use this skill for:

- Raw Elixir language questions without Phoenix context. Prefer the Elixir guides.
- Ecto-only questions with no Phoenix web layer unless the docs page is linked from Phoenix guides.
- Django, Flask, or FastAPI patterns. Use `django-docs`, `flask-docs`, or `fastapi-docs` instead.
- Third-party packages not covered by Phoenix docs unless the question is about general Phoenix integration.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, installation, and project structure
- Request life-cycle, plug, routing, and controllers
- Templates, HEEx, components, and layouts
- Contexts, Ecto, and data modelling
- LiveView, channels, and real-time features
- Authentication, scopes, and authorization
- Testing and deployment
- Generators and how-to guides
- API reference (`Phoenix.Controller`, `Phoenix.Endpoint`, etc.)

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Phoenix docs first

- Treat `phoenix.hexdocs.pm` as the source of truth for Phoenix.
- Prefer pages under <https://phoenix.hexdocs.pm/>.
- Search with the user's exact terms plus focused Phoenix phrases such as `pipe_through`, `assign`, `LiveView`, `context`, `changeset`, or `mix phx.gen.auth`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For version-specific changes, check the changelog and migration notes before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish guides from API reference before recommending patterns.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Phoenix docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Phoenix docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Overview, Installation, and Up and Running before deep reference pages.
- For routing questions, prefer the Routing guide and note pipeline/scope behavior.
- For request flow questions, follow Endpoint → Router → Controller → View in the life-cycle guides.
- For data questions, prefer Contexts and Ecto guides before scattering logic in controllers.
- For real-time questions, distinguish LiveView from Channels and check PubSub clustering notes for production.
- For auth questions, start with `mix phx.gen.auth` and Scopes before inventing custom auth.
- For deployment questions, prefer Deployment and Releases guides over `mix phx.server` in production.
- For generator questions, check `mix help phx.new` and generator-specific docs for flags like `--no-ecto` or `--no-live`.

## Common Mistakes

- Answering from memory without verifying the current Phoenix docs
- Linking the Phoenix overview when a narrower guide or API page exists
- Treating Phoenix like Django (fat controllers instead of contexts)
- Confusing LiveView stateful processes with stateless controller actions
- Forgetting that plugs compose at endpoint, router pipeline, and controller levels
- Using the development server configuration in production without checking deployment docs
- Ignoring clustering/sticky-session requirements for LiveView or long-polling in multi-node deployments

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Phoenix docs as the final authority.
