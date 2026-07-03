---
name: aws-iam-docs
description: Use when users ask how to create, configure, secure, audit, or troubleshoot AWS IAM identities and permissions, including users, groups, roles, policies, trust policies, permission boundaries, IAM Identity Center, STS, MFA, access keys, service-linked roles, IAM Roles Anywhere, Access Analyzer, or cross-account access, especially when they need official AWS IAM documentation, exact links, or docs-grounded guidance.
---

AWS IAM questions are easy to answer from stale memory or overly broad `*` permissions. Use this skill to ground answers in the official AWS IAM documentation and return the closest authoritative page instead of improvising security policy advice.

## When to Use

Use this skill when the request is about:

- IAM concepts: principals, authentication, authorization, and policies
- IAM users, groups, roles, and identity federation
- Identity-based policies, resource-based policies, and permission boundaries
- Trust policies, assume-role, and cross-account access
- AWS STS temporary credentials and session policies
- IAM Identity Center (SSO) users, permission sets, and assignments
- MFA, access keys, and credential management best practices
- Service-linked roles and service roles
- IAM Access Analyzer, policy validation, and least-privilege guidance
- IAM Roles Anywhere and workload identity outside AWS
- Organizations SCPs when documented in IAM context (delegated admin, etc.)
- Troubleshooting access denied, implicit denies, and policy evaluation logic

Do not use this skill for:

- AWS CLI install, profiles, or `aws configure sso` syntax. Use `aws-cli-docs` instead.
- Service-specific resource configuration when the question is not about IAM permissions (for example S3 bucket lifecycle rules). Use the relevant service skill.
- Kubernetes RBAC on EKS. Use `kubernetes-docs` or `aws-eks-docs` for cluster RBAC; use this skill for AWS IAM side.
- Application code using AWS SDK credential providers unless the question is about IAM roles/policies documented in IAM guides.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Users, groups, and long-term credentials
- Roles, trust policies, and temporary credentials
- Policies: JSON structure, actions, resources, conditions
- IAM Identity Center and federation
- MFA and credential security
- Cross-account access and delegation
- Access Analyzer and policy tools
- Service-linked roles and AWS service permissions
- Troubleshooting access denied and policy simulation

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official AWS IAM docs first

- Treat `docs.aws.amazon.com/IAM/latest/UserGuide` as the source of truth for AWS IAM.
- Prefer the user guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/>.
- Prefer the API reference at <https://docs.aws.amazon.com/IAM/latest/APIReference/Welcome.html> for IAM API operations.
- Prefer STS docs at <https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html> for AssumeRole and temporary credentials.
- Search with the user's exact terms plus focused IAM phrases such as `trust policy`, `permission boundary`, `condition key`, `AssumeRole`, `Identity Center`, or `Access Analyzer`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For access denied errors, check policy evaluation logic docs before suggesting blanket `AdministratorAccess`.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For policy JSON, open the specific policy element reference when condition keys or resource ARNs matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact AWS IAM docs links, not just the docs homepage.
- Only provide policy JSON or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to AWS IAM docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example policy JSON or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is IAM? and how IAM works before policy reference pages.
- For role questions, distinguish trust policy (who can assume) from permissions policy (what they can do).
- For SSO questions, prefer IAM Identity Center docs over legacy SAML-only guides when applicable.
- For cross-account questions, check role trust and resource-based policies together.
- For least privilege, use Access Analyzer and policy validation docs before hand-waving "remove \*".
- For temporary credentials, check STS AssumeRole and session policy docs.
- For CLI syntax-only questions, cross-check `aws-cli-docs` for `aws iam` and `aws sts` commands.

## Common Mistakes

- Answering from memory without verifying the current AWS IAM docs
- Linking the IAM landing page when a narrower user guide or API page exists
- Recommending root user access keys or long-lived credentials against documented best practices
- Confusing identity-based policies with resource-based policies in access denied troubleshooting
- Adding `*` actions/resources without checking condition keys and permission boundaries
- Treating IAM user policies as interchangeable with role trust policies
- Ignoring IAM eventual consistency when policies were just created or updated

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live AWS IAM docs as the final authority.
