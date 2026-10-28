---
name: aws-cli-docs
description: Official AWS CLI documentation, answered with links to the exact pages. Use for any AWS CLI question, including installing and configuring the CLI, credentials, profiles and SSO, output filtering and pagination, migrating from v1 to v2, or the syntax of a service command.
---

# AWS CLI Docs

AWS CLI answers drift with every release and v1 syntax still haunts memory, so ground each answer in the live docs at <https://docs.aws.amazon.com/cli/latest/userguide/>, not memory, and link the exact page behind every claim.

Route AWS SDK application code to the SDK's own docs unless the question is about shared CLI/SDK configuration or credentials; route infrastructure-as-code to `terraform-docs` or the CloudFormation/CDK docs unless it is about invoking AWS from the CLI; and route `kubectl`, `docker` or `redis-cli` to `kubernetes-docs`, `docker-docs` or `redis-docs`.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/cli/latest` with the user's exact terms plus AWS CLI vocabulary such as `--profile`, `--query`, `aws configure sso`, `credential_process`, or `--no-cli-pager`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Service command syntax: the service's page in the command reference at <https://docs.aws.amazon.com/cli/latest/reference/> (for example `aws s3`, `aws ec2`, `aws iam`), following its `aws <service> help` patterns.
- Concepts and workflows: the user guide, before the command reference.
- Install: the Getting Started install pages, before troubleshooting.
- Credentials: the configuration precedence pages.
- SSO: the SSO configuration pages, before access-key-only setup.
- Output: the output format and JMESPath `--query` filtering pages, before improvising `jq` pipelines.
- Scripting: the return codes, pagination (`--no-paginate`), and `--cli-read-timeout` pages.
- v1-to-v2 migration: the migration guide, before answering from v1 behavior.

## Gotchas

- Default to AWS CLI version 2 unless the user needs version 1, and keep v1 and v2 syntax and pagination behavior apart.
- Credentials resolve in order: command line, then environment, then credentials file, then config file.
- Keep secrets out of shell history with profiles, SSO, or `credential_process`, as the docs recommend.
- `--region` and `--profile` are global options shared by every service command.
- Offer a CLI equivalent of a console workflow only when the command reference documents one.
