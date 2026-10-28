---
name: fastapi-docs
description: Official FastAPI documentation, answered with links to the exact pages. Use for any FastAPI question, including path operations, dependencies, Pydantic models and validation, security and OAuth2, OpenAPI docs, WebSockets and background tasks, testing, or deployment.
---

# FastAPI Docs

FastAPI answers drift with its releases and the move from Pydantic v1 to v2, so ground each answer in the live docs at <https://fastapi.tiangolo.com/>, not memory, and link the exact page behind every claim.

Route Django ORM, admin or URLconf patterns to `django-docs`, and Flask blueprints, WSGI context or Jinja-first apps to `flask-docs`. Starlette internals and standalone Pydantic belong to their own docs unless the question turns on FastAPI's documented integration.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `fastapi.tiangolo.com` with the user's exact terms plus FastAPI vocabulary such as `Depends`, `APIRouter`, `response_model`, `HTTPException`, `lifespan`, or `TestClient`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Pydantic v2 migration: the Pydantic v1 to v2 recipe.
- First steps: First Steps and the Tutorial - User Guide, before deep reference pages.
- Recommended patterns: the tutorial; exact signatures: the API reference.
- Validation: the tutorial sections on parameters and bodies, before Pydantic config.
- Dependencies: `Depends`, sub-dependencies, and dependencies with `yield`.
- Security: Security - First Steps and the OAuth2 guides.
- Async: Concurrency and async/await, for whether a route needs `def` or `async def`.
- Deployment: the Deployment section and its Uvicorn and Docker guides.
- OpenAPI: Metadata and Docs URLs, or the advanced OpenAPI guides.

## Gotchas

- FastAPI hands request data to handlers through parameters and dependencies rather than a Flask-style global request object, and handlers can be `async def`.
- Write Pydantic v2 models, which the docs recommend; v1 patterns differ.
- Choose `def` or `async def` per the Concurrency and async/await page, matching I/O-bound and CPU-bound work to the guidance there.
- FastAPI generates the OpenAPI schema from type hints; customize it through the OpenAPI guides rather than writing it by hand.
- Use FastAPI dependency injection, kept separate from Django REST Framework or Flask patterns.
