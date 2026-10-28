---
name: django-docs
description: Official Django 6.1 documentation, answered with links to the exact pages. Use for any Django question, including models, the ORM and migrations, views, URLconfs and templates, forms, authentication and the admin, or testing and deployment.
---

# Django Docs

Django APIs move through a deprecation timeline with every release, so ground each answer in the live Django 6.1 docs at <https://docs.djangoproject.com/en/6.1/>, not memory, and link the exact page behind every claim.

Route FastAPI path operations, dependencies or OpenAPI-first APIs to `fastapi-docs`, and Flask blueprints or minimal microframework apps to `flask-docs`. Django REST Framework and third-party packages belong to their own docs unless the question turns on core Django behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.djangoproject.com/en/6.1` with the user's exact terms plus Django vocabulary such as `QuerySet`, `ModelForm`, `path()`, `migrate`, `MIDDLEWARE`, or `class-based views`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and code examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Another Django version: swap the version segment of the docs path to match the user's version.
- Upgrades: the release notes and the deprecation timeline.
- First steps: the tutorial, "Writing your first Django app", before API reference pages.
- Recommended patterns: the topic guides and how-to guides; exact signatures and options: the API reference.
- ORM: Models and Making queries.
- Migrations: Migrations and the Operations reference, before manual schema edits.
- URL routing: the URLconf docs for `path()` and `include()`.
- Security: Security in Django and the CSRF protection docs.
- Admin: the admin site docs and FAQ: The admin.
- Async: Asynchronous support and the async view guidance.
- Deployment: the Deployment overview and the deployment checklist.

## Gotchas

- Check the deprecation timeline before recommending an API; deprecated APIs are removed in later releases.
- Write URLconfs with `path()` and `include()`; `url()` is a legacy pattern.
- Use the ORM wherever the ORM docs cover the case, and raw SQL only beyond it.
- Django templates use the Django template language, distinct from Jinja-only Flask patterns.
- Label Django REST Framework patterns as DRF, separate from core Django view and form docs.
