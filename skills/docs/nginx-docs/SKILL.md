---
name: nginx-docs
description: Official NGINX documentation, answered with links to the exact pages. Use for any NGINX question, including nginx.conf directives and location matching, reverse proxying and load balancing, SSL/TLS and HTTP/3, TCP/UDP stream proxying, or njs scripting.
---

# NGINX Docs

NGINX answers drift toward Apache-style configuration and misremembered directive semantics, so ground each answer in the live docs at <https://nginx.org/en/docs/>, not memory, and link the exact page behind every claim.

Route Kubernetes Ingress resources and `kubectl` usage to `kubernetes-docs`; NGINX Ingress Controller migration lives at kubernetes.nginx.org, as the NGINX docs reference it. HAProxy, Envoy, Traefik and application server code belong to their own docs unless the question turns on NGINX behavior, such as proxying to that backend. Link NGINX Plus commercial-only docs only when the user needs Plus.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `nginx.org/en/docs` with the user's exact terms plus NGINX vocabulary such as `proxy_pass`, `upstream`, `try_files`, `server_name`, `limit_req`, or `ssl_certificate`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and `nginx.conf` snippets only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Directive syntax: the module reference page for that exact directive; when the owning module is unclear, the alphabetical index of directives.
- Beginner questions: the Beginner's Guide and Admin's Guide, before module reference pages.
- Proxying: `ngx_http_proxy_module` and the upstream docs, before setting headers.
- TLS: Configuring HTTPS servers and `ngx_http_ssl_module`.
- `location` precedence: How nginx processes a request, before recommending `^~` or regex order.
- Stream (TCP/UDP): the stream module docs, not HTTP `proxy_pass` examples.

## Gotchas

- Write NGINX `rewrite` and `try_files`; Apache `.htaccess` and `mod_rewrite` patterns do not carry over.
- `proxy_pass` URI handling changes with and without a trailing slash; confirm it in `ngx_http_proxy_module`.
- Check the rewrite and request-processing docs before using `if` blocks for complex routing.
- Open source NGINX docs on nginx.org are separate from the NGINX Ingress Controller and NGINX Gateway Fabric docs.
- `stream` contexts follow the stream module docs, not HTTP `location` guidance.
