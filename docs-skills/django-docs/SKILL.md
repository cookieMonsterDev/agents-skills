---
name: django-docs
description: Use when users ask how to build, explain, configure, model, query, secure, test, deploy, migrate, or troubleshoot Django web applications, including models, views, templates, forms, URLconfs, the admin, ORM, migrations, authentication, middleware, REST patterns, async views, caching, or management commands, especially when they need official Django 6.0 documentation, exact links, or docs-grounded Python guidance.
---

Django questions are easy to answer from stale memory or Flask/FastAPI assumptions. Use this skill to ground answers in the official Django documentation and return the closest authoritative page instead of generic Python web advice.

## When to Use

Use this skill when the request is about:

- Django concepts, project/app structure, settings, and the request/response cycle
- Models, fields, QuerySets, managers, and the ORM
- Migrations, schema changes, and database configuration
- Views, URLconfs, class-based views, and generic views
- Templates, template tags, filters, and context processors
- Forms, ModelForms, validation, and formsets
- Authentication, permissions, sessions, and the admin site
- Middleware, security (CSRF, XSS, clickjacking, CSP), and deployment
- Testing, fixtures, and the test client
- Management commands, signals, caching, and async support
- contrib apps: auth, admin, staticfiles, sessions, messages, postgres, etc.

Do not use this skill for:

- FastAPI path operations, dependencies, or OpenAPI-first APIs. Use `fastapi-docs` instead.
- Flask blueprints, WSGI-only patterns, or minimal microframework structure. Use `flask-docs` instead.
- Django REST Framework unless the question maps to core Django docs pages.
- Third-party packages not covered by Django's official documentation.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, installation, and tutorials
- Models, databases, and migrations
- Views, URLs, and class-based views
- Templates and forms
- Authentication, admin, and security
- Testing, deployment, and settings
- How-to guides and FAQ
- API reference (models, views, middleware, etc.)

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Django docs first

- Treat `docs.djangoproject.com/en/6.0` as the source of truth for Django 6.0.
- Prefer pages under <https://docs.djangoproject.com/en/6.0/>.
- If the user names a specific Django version, switch the docs version path when needed.
- Search with the user's exact terms plus focused Django phrases such as `QuerySet`, `ModelForm`, `path()`, `migrate`, `MIDDLEWARE`, or `class-based views`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For upgrade questions, check release notes and the deprecation timeline before answering from older versions.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- Distinguish topic guides, how-to guides, and API reference before recommending patterns.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Django docs links, not just the docs homepage.
- Only provide code examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Django docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example code, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer the tutorial and "Writing your first Django app" before API reference pages.
- For ORM questions, prefer Models and Making queries before inventing SQL.
- For migration questions, check Migrations and Operations reference before manual schema edits.
- For URL routing questions, prefer `path()`, `include()`, and URLconf docs over legacy `url()` patterns.
- For security questions, start with Security in Django and CSRF protection docs.
- For admin questions, prefer the admin site docs and FAQ: The admin.
- For async questions, check Asynchronous support and async view guidance.
- For deployment questions, prefer Deployment overview and the deployment checklist.

## Common Mistakes

- Answering from memory without verifying the current Django 6.0 docs
- Linking the Django docs homepage when a narrower topic or reference page exists
- Treating Django like Flask (no built-in ORM/admin unless explicitly using those layers)
- Using deprecated APIs without checking the deprecation timeline
- Confusing Django templates with Jinja-only Flask patterns
- Recommending raw SQL when the ORM docs cover the use case
- Mixing Django REST Framework patterns with core Django view/form docs without clarification

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Django docs as the final authority.
