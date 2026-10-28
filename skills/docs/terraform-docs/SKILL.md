---
name: terraform-docs
description: Official Terraform documentation, answered with links to the exact pages. Use for any Terraform question, including HCL configuration, providers and the Terraform Registry, modules, state and backends, or HCP Terraform and Terraform Enterprise.
---

# Terraform Docs

Terraform answers drift between language versions and provider releases, so ground each answer in the live docs at <https://developer.hashicorp.com/terraform/docs>, not memory, and link the exact page behind every claim.

Route AWS CLI commands to `aws-cli-docs`, Kubernetes YAML or `kubectl` usage to `kubernetes-docs`, and Helm chart templating or releases to `helm-docs`. Cloud consoles, Pulumi and CloudFormation belong to their own docs unless the question turns on Terraform behavior or a comparison with it.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `developer.hashicorp.com/terraform` with the user's exact terms plus Terraform vocabulary such as `terraform plan`, `backend "s3"`, `for_each`, `lifecycle`, `moved` block, or `required_providers`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and HCL or CLI examples only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Provider resource arguments: the Registry provider docs for the exact resource type, over the generic language docs.
- Language syntax: the Configuration Language docs, before CLI reference pages.
- Workflows and command flags: the CLI docs and tutorials.
- Modules: the Modules docs and the Registry module source, before inventing directory layouts.
- State: tell local state, remote backends and HCP Terraform state apart before recommending workarounds.
- Deprecated syntax or upgrades: the version-specific upgrade guides and provider changelogs.

## Gotchas

- Keep `terraform plan` output guarantees and `terraform apply` behavior apart, as the CLI docs describe each.
- Write current HCL2 patterns; Terraform 0.11 syntax differs.
- For team workflows, start from the remote backend guidance rather than local state.
- Provider docs examples show usage, not defaults that hold for every cloud account or org policy.
