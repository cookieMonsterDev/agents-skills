---
name: flask-docs
description: Use when users ask how to build, explain, configure, route, secure, test, deploy, or troubleshoot Flask web applications, including blueprints, application factories, request/response objects, templates, sessions, error handling, CLI commands, extensions, WSGI middleware, async views, or production deployment, especially when they need official Flask documentation, exact links, or docs-grounded Python guidance.
---

Flask questions are easy to answer from stale memory or Django/FastAPI assumptions. Use this skill to ground answers in the official Flask documentation and return the closest authoritative page instead of generic Python web advice.

## When to Use

Use this skill when the request is about:

- Flask concepts, application objects, routing, and the request lifecycle
- Blueprints, application factories, and modular project structure
- Request and response handling, sessions, and cookies
- Templates (Jinja), static files, and context processors
- Error handling, debugging, and logging
- Configuration, instance folders, and environment variables
- Testing with the test client and CLI runner
- Class-based views, signals, and the CLI
- Security considerations (XSS, CSRF, headers)
- Deployment, WSGI servers, and async/gevent support
- Flask extensions and extension development patterns

Do not use this skill for:

- Django ORM, admin, migrations, or URLconf. Use `django-docs` instead.
- FastAPI dependencies, OpenAPI, or Pydantic validation. Use `fastapi-docs` instead.
- Werkzeug or Jinja internals unless the question is about Flask's documented integration.
- Third-party Flask extensions not covered by Flask docs unless the question is about general extension patterns.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, installation, and quickstart
- Routing, requests, responses, and sessions
- Templates, static files, and blueprints
- Configuration, application context, and request context
- Error handling, debugging, and logging
- Testing and CLI
- Patterns, security, and deployment
- API reference

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Flask docs first

- Treat `flask.palletsprojects.com/en/stable` as the source of truth for Flask.
- Prefer pages under <https://flask.palletsprojects.com/en/stable/>.
- Search with the user's exact terms plus focused Flask phrases such as `Blueprint`, `application factory`, `g`, `session`, `test_client`, or `before_request`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For version-specific changes, check the Changes page before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish user guide patterns from API reference before recommending approaches.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Flask docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Flask docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Quickstart and the Tutorial before API reference pages.
- For structure questions, prefer Application Factories and Blueprints patterns.
- For context questions, distinguish application context from request context.
- For session questions, check Sessions in quickstart and the sessions API reference.
- For error questions, prefer Handling Application Errors before custom middleware.
- For security questions, start with Security Considerations.
- For async questions, check Using async and await and note when Quart may be more appropriate.
- For deployment questions, prefer Deploying to Production over development server advice.

## Common Mistakes

- Answering from memory without verifying the current Flask docs
- Linking the Flask homepage when a narrower guide or API page exists
- Treating Flask like Django (built-in ORM, admin, or migrations)
- Using the development server in production without checking deployment docs
- Confusing `current_app`/`g` usage outside the proper context
- Registering blueprints or error handlers in the wrong order or scope
- Recommending Flask for heavy async workloads without checking async/Quart guidance

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Flask docs as the final authority.
