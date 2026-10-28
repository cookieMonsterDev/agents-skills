---
name: flask-docs
description: Official Flask documentation, answered with links to the exact pages. Use for any Flask question, including routing and blueprints, application factories, templates, sessions, the application and request contexts, testing and the CLI, or deployment.
---

# Flask Docs

Flask behavior shifts between releases, as its Changes page records, so ground each answer in the live docs at <https://flask.palletsprojects.com/en/stable/>, not memory, and link the exact page behind every claim.

Route Django ORM, admin, migrations or URLconf questions to `django-docs`, and FastAPI dependencies, OpenAPI or Pydantic validation to `fastapi-docs`. Werkzeug, Jinja and third-party extensions belong to their own docs unless the question turns on Flask's documented integration or general extension patterns.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `flask.palletsprojects.com/en/stable` with the user's exact terms plus Flask vocabulary such as `Blueprint`, `application factory`, `g`, `session`, `test_client`, or `before_request`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version-specific changes: the Changes page.
- First steps: Quickstart and the Tutorial, before API reference pages.
- Recommended approaches: the user guide and Patterns pages; exact signatures: the API reference.
- Project structure: the Application Factories and Blueprints patterns.
- Context questions: tell the application context from the request context.
- Sessions: Sessions in Quickstart plus the sessions API reference.
- Errors: Handling Application Errors, before custom middleware.
- Security: Security Considerations.
- Async: Using async and await, including its note on when Quart may fit better.
- Deployment: Deploying to Production.

## Gotchas

- Flask has no built-in ORM, admin or migrations, unlike Django.
- Serve production traffic as Deploying to Production describes; the development server is for development.
- Use `current_app` and `g` only inside the context that provides them.
- Register blueprints and error handlers in the order and scope the docs specify.
- Check the async and Quart guidance before recommending Flask for heavy async workloads.
