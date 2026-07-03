---
name: nginx-docs
description: Use when users ask how to install, configure, proxy, load-balance, secure, reload, or troubleshoot NGINX as a web server, reverse proxy, mail proxy, or TCP/UDP stream proxy, including nginx.conf syntax, server blocks, location matching, upstreams, SSL/TLS, HTTP/2, HTTP/3, QUIC, rewrite rules, rate limiting, caching, FastCGI, WebSocket proxying, njs scripting, or module directives, especially when they need official NGINX documentation, exact links, or docs-grounded guidance.
---

NGINX questions are easy to answer from stale memory or Apache-style configuration assumptions. Use this skill to ground answers in the official NGINX documentation and return the closest authoritative page instead of generic reverse-proxy advice.

## When to Use

Use this skill when the request is about:

- NGINX architecture, master/worker processes, and request processing
- Installing, building, starting, stopping, and reloading NGINX
- Configuration file structure: `http`, `server`, `location`, and `stream` contexts
- Serving static content, reverse proxying, and load balancing
- Upstreams, health checks, and connection distribution methods
- HTTPS, TLS certificates, HTTP/2, HTTP/3, and QUIC
- Rewrite rules, redirects, and URL mapping
- Rate limiting, access control, and request filtering
- FastCGI, uWSGI, SCGI, gRPC, and WebSocket proxying
- Stream (TCP/UDP) proxying and SSL preread
- Mail proxy modules (IMAP, POP3, SMTP)
- njs scripting and dynamic configuration
- Module directives, variables, and logging

Do not use this skill for:

- Kubernetes Ingress resources or `kubectl` usage without NGINX-specific context. Use `kubernetes-docs` instead; for NGINX Ingress Controller migration, check kubernetes.nginx.org as referenced in NGINX docs.
- HAProxy, Envoy, or Traefik configuration unless the user asks for comparison with NGINX docs.
- Application server code (Node.js, PHP-FPM app logic) unless the question is about NGINX proxying to that backend per NGINX docs.
- NGINX Plus commercial-only features unless the user explicitly needs Plus docs linked from nginx.org.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Installation, build, and process control
- HTTP server configuration and static content
- Reverse proxy, upstreams, and load balancing
- TLS, HTTPS, HTTP/2, and HTTP/3
- Rewrites, redirects, and WebSocket proxying
- Stream (TCP/UDP) and mail proxying
- Rate limiting, access control, and logging
- njs scripting and advanced modules
- Directive and variable reference

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official NGINX docs first

- Treat `nginx.org/en/docs` as the source of truth for open source NGINX.
- Prefer pages under <https://nginx.org/en/docs/>.
- Search with the user's exact terms plus focused NGINX phrases such as `proxy_pass`, `upstream`, `try_files`, `server_name`, `limit_req`, `ssl_certificate`, or `stream`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For directive syntax, prefer the module reference page for the exact directive before answering from memory.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For `location` matching questions, open How nginx processes a request before guessing precedence rules.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact NGINX docs links, not just the docs homepage.
- Only provide `nginx.conf` snippets when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to NGINX docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example `nginx.conf` snippets, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer Beginner's Guide and Admin's Guide before module reference pages.
- For proxy questions, open `ngx_http_proxy_module` and upstream docs before inventing header settings.
- For TLS questions, prefer Configuring HTTPS servers and `ngx_http_ssl_module`.
- For `location` precedence questions, read How nginx processes a request before recommending `^~` or regex order.
- For stream/TCP questions, use stream module docs rather than HTTP `proxy_pass` examples.
- For directive lookup, use the alphabetical index of directives before guessing module ownership.

## Common Mistakes

- Answering from memory without verifying the current NGINX docs
- Linking the NGINX docs homepage when a narrower module or guide page exists
- Mixing Apache `.htaccess` or `mod_rewrite` patterns with NGINX `rewrite` or `try_files`
- Misunderstanding `proxy_pass` URI behavior with and without trailing slashes
- Recommending `if` blocks for complex routing without checking rewrite and request-processing docs
- Confusing open source NGINX docs with NGINX Ingress Controller or NGINX Gateway Fabric docs
- Applying HTTP `location` guidance to `stream` contexts without checking stream module docs

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live NGINX docs as the final authority.
