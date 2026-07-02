---
name: aws-cli-docs
description: Use when users ask how to install, configure, authenticate, script, filter output, troubleshoot, or run AWS CLI commands for AWS services, including profiles, credentials, SSO, IAM roles, regions, endpoints, JMESPath queries, output formats, pagination, retries, proxies, wizards, aliases, shell completion, or migration from AWS CLI v1 to v2, especially when they need official AWS CLI documentation, exact links, or docs-grounded command guidance.
---

AWS CLI questions are easy to answer from stale memory or v1 syntax. Use this skill to ground answers in the official AWS CLI documentation and return the closest authoritative page instead of guessing service-specific console steps.

## When to Use

Use this skill when the request is about:

- Installing, upgrading, or uninstalling AWS CLI version 2
- Configuring credentials, profiles, regions, and output formats
- Authentication with access keys, IAM roles, SSO, or external credential processes
- Command structure, parameters, pagination, filtering, and output control
- JMESPath `--query`, `--output`, and return codes
- Interactive features: command prompts, wizards, and aliases
- Retries, proxies, endpoints, and environment variables
- Shell completion and scripting patterns
- Migrating scripts from AWS CLI v1 to v2
- Troubleshooting install, configure, or runtime errors
- Service-specific CLI command syntax (via the command reference)

Do not use this skill for:

- AWS SDK application code unless the question is specifically about shared AWS CLI/SDK configuration or credentials.
- AWS Management Console UI walkthroughs when the user needs CLI commands instead.
- Infrastructure-as-code tools (CloudFormation, CDK, Terraform) unless the question is about invoking AWS via the CLI.
- Non-AWS command-line tools such as `kubectl`, `docker`, or `redis-cli`.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and installation
- Configuration, credentials, and profiles
- Command usage, parameters, and structure
- Output formatting, filtering, and pagination
- Authentication (SSO, roles, external processes)
- Interactive features and scripting helpers
- Migration from CLI v1 to v2
- Troubleshooting and return codes
- Service-specific command reference

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official AWS CLI docs first

- Treat `docs.aws.amazon.com/cli/latest` as the source of truth for AWS CLI.
- Prefer the user guide at <https://docs.aws.amazon.com/cli/latest/userguide/> for concepts and workflows.
- Prefer the command reference at <https://docs.aws.amazon.com/cli/latest/reference/> for service operation syntax.
- Search with the user's exact terms plus focused CLI phrases such as `--profile`, `--query`, `aws configure sso`, `credential_process`, or `--no-cli-pager`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For v1-to-v2 migration questions, check the migration guide before answering from v1 behavior.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For service commands, open the specific service page in the command reference (for example `aws s3`, `aws ec2`, `aws iam`).
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact AWS CLI docs links, not just the docs homepage.
- Only provide command examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to AWS CLI docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For install questions, prefer Getting Started and install pages before troubleshooting.
- For credential questions, check configuration precedence (command line > environment > credentials file > config file).
- For output questions, prefer output format and JMESPath filtering docs before improvising `jq` pipelines.
- For SSO questions, prefer SSO configuration docs over legacy access-key-only setup.
- For scripting questions, note return codes, pagination (`--no-paginate`), and `--cli-read-timeout` as documented.
- For service syntax questions, use `aws <service> help` patterns documented in the command reference.
- Default to AWS CLI version 2 unless the user explicitly needs version 1.

## Common Mistakes

- Answering from memory without verifying the current AWS CLI docs
- Linking the AWS CLI landing page when a narrower user guide or command reference page exists
- Mixing AWS CLI v1 and v2 syntax or pagination behavior
- Putting secrets in shell history when the docs recommend profiles, SSO, or `credential_process`
- Forgetting that `--region` and `--profile` are common global options across services
- Treating console-only workflows as CLI equivalents without checking the command reference

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live AWS CLI docs as the final authority.
