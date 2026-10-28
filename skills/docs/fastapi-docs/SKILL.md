---
name: fastapi-docs
description: Use when users ask how to build, explain, configure, validate, secure, test, deploy, or troubleshoot FastAPI applications and APIs, including path operations, dependencies, Pydantic models, OpenAPI docs, middleware, background tasks, WebSockets, lifespan events, SQL databases, authentication, or async Python, especially when they need official FastAPI documentation, exact links, or docs-grounded Python guidance.
---

FastAPI questions are easy to answer from stale memory or Flask/Django assumptions. Use this skill to ground answers in the official FastAPI documentation and return the closest authoritative page instead of generic Python web advice.

## When to Use

Use this skill when the request is about:

- FastAPI concepts, path operations, routing, and application structure
- Request parameters, body models, response models, and validation with Pydantic
- Dependencies (`Depends`, `Security`), sub-dependencies, and dependency injection
- Authentication, OAuth2, JWT, HTTP Basic, and security utilities
- Middleware, CORS, exception handlers, and custom responses
- Background tasks, lifespan events, WebSockets, and streaming/SSE
- SQL databases, testing with `TestClient`, and deployment with Uvicorn
- OpenAPI schema, Swagger UI, ReDoc, and API metadata
- Advanced topics: mounts, proxies, templates, static files, and async tests

Do not use this skill for:

- Django ORM, admin, or URLconf patterns. Use `django-docs` instead.
- Flask blueprints, WSGI context, or Jinja-first apps. Use `flask-docs` instead.
- Starlette internals unless the question is about FastAPI's documented Starlette integration.
- Pydantic-only questions with no FastAPI context unless the docs page is linked from FastAPI guides.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, installation, and first steps
- Tutorial: parameters, bodies, validation, and responses
- Dependencies and security
- Middleware, CORS, and error handling
- Databases, testing, and deployment
- Advanced: WebSockets, lifespan, mounts, proxies, templates
- API reference (`FastAPI`, `APIRouter`, `Depends`, etc.)
- How-to recipes and migration guides

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official FastAPI docs first

- Treat `fastapi.tiangolo.com` as the source of truth for FastAPI.
- Prefer pages under <https://fastapi.tiangolo.com/>.
- Search with the user's exact terms plus focused FastAPI phrases such as `Depends`, `APIRouter`, `response_model`, `HTTPException`, `lifespan`, or `TestClient`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Pydantic v2 migration questions, check the Pydantic v1 to v2 recipe before answering from older patterns.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish tutorial guidance from API reference before recommending patterns.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact FastAPI docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to FastAPI docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer First Steps and the Tutorial before deep reference pages.
- For validation questions, prefer tutorial sections on parameters and bodies before guessing Pydantic config.
- For dependency questions, map to `Depends`, sub-dependencies, or `yield` dependencies as documented.
- For security questions, start with Security - First Steps and OAuth2 guides before inventing auth flows.
- For async questions, check Concurrency and async/await and whether `def` vs `async def` matters for the route.
- For deployment questions, prefer Deployment and Uvicorn/Docker guides over ad hoc server advice.
- For OpenAPI questions, prefer Metadata and Docs URLs or OpenAPI advanced guides.

## Common Mistakes

- Answering from memory without verifying the current FastAPI docs
- Linking the FastAPI homepage when a narrower tutorial or reference page exists
- Treating FastAPI like Flask (global request objects, sync-only handlers by default)
- Confusing Pydantic v1 patterns with v2 when the docs recommend v2 models
- Using `def` for I/O-bound async code or `async def` for CPU-bound work without checking async guidance
- Recommending manual OpenAPI schema when FastAPI generates it from type hints
- Mixing Django REST Framework or Flask patterns with FastAPI dependency injection

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live FastAPI docs as the final authority.
