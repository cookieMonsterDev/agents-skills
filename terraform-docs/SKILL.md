---
name: terraform-docs
description: Use when users ask how to install, configure, write, plan, apply, import, destroy, test, secure, or troubleshoot Terraform infrastructure as code, including HCL syntax, providers, modules, state, workspaces, backends, variables, outputs, data sources, provisioners, HCP Terraform, Terraform Enterprise, or the Terraform Registry, especially when they need official HashiCorp Terraform documentation, exact links, or docs-grounded guidance.
---

Terraform questions are easy to answer from stale memory or provider-specific assumptions. Use this skill to ground answers in the official HashiCorp Terraform documentation and return the closest authoritative page instead of generic IaC advice.

## When to Use

Use this skill when the request is about:

- Terraform concepts, architecture, and adoption patterns
- Terraform configuration language (HCL), resources, data sources, variables, outputs, and locals
- Terraform CLI commands: init, plan, apply, destroy, import, state, workspace, and fmt
- Providers, modules, and the Terraform Registry
- Remote state, backends, locking, and drift detection
- HCP Terraform and Terraform Enterprise workflows
- Provider development and module publishing
- Testing, validation, policy, and security for Terraform code
- Upgrading Terraform versions and provider version constraints

Do not use this skill for:

- Raw cloud console operations when the question is provider UI rather than Terraform behavior. Use `aws-cli-docs` for AWS CLI commands.
- Kubernetes workload YAML or kubectl usage without Terraform context. Use `kubernetes-docs` instead.
- Helm chart templating or release management. Use `helm-docs` instead.
- Pulumi, CloudFormation, or other IaC tools unless the user explicitly asks for comparison with Terraform docs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Introduction, concepts, and use cases
- Configuration language and HCL syntax
- Terraform CLI workflows and commands
- Providers and the Terraform Registry
- Modules and reusable configuration
- State, backends, and workspaces
- HCP Terraform and Terraform Enterprise
- Plugin and provider development
- Testing, policy, and security

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Terraform docs first

- Treat `developer.hashicorp.com/terraform` as the source of truth for Terraform.
- Prefer pages under <https://developer.hashicorp.com/terraform/docs>.
- For provider-specific resource arguments, prefer the provider docs on the Terraform Registry over generic language docs.
- Search with the user's exact terms plus focused Terraform phrases such as `terraform plan`, `backend "s3"`, `for_each`, `lifecycle`, `moved` block, or `required_providers`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For deprecated syntax or removed features, check the upgrade guides before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For resource arguments, open the specific provider resource page on the Registry when available.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Terraform docs links, not just the docs homepage.
- Only provide HCL examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Terraform docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example HCL or CLI commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For language syntax questions, prefer Configuration Language docs before CLI reference pages.
- For workflow questions, prefer CLI docs and tutorials before guessing command flags.
- For provider resource questions, open the Registry provider docs for the exact resource type.
- For state questions, distinguish local state, remote backends, and HCP Terraform state before recommending workarounds.
- For module questions, prefer the Modules docs and Registry module source before inventing directory layouts.
- For upgrade questions, check version-specific upgrade guides and provider changelogs.

## Common Mistakes

- Answering from memory without verifying the current Terraform docs
- Linking the Terraform docs homepage when a narrower Language, CLI, or Registry page exists
- Confusing `terraform apply` behavior with `terraform plan` output guarantees
- Mixing Terraform 0.11 syntax with current HCL2 patterns
- Recommending local state for team workflows without checking remote backend guidance
- Treating provider docs examples as guaranteed defaults for every cloud account or org policy

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Terraform docs as the final authority.
