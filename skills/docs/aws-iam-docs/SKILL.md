---
name: aws-iam-docs
description: Official AWS IAM documentation, answered with links to the exact pages. Use for any AWS IAM question, including users, groups and roles, policies and permission boundaries, STS and cross-account access, IAM Identity Center, MFA and credentials, Access Analyzer, or troubleshooting access denied.
---

# AWS IAM Docs

IAM answers drift with every release and drift toward broad `*` permissions, so ground each answer in the live docs at <https://docs.aws.amazon.com/IAM/latest/UserGuide/>, not memory, and link the exact page behind every claim.

Route AWS CLI install, profiles and `aws configure sso` syntax to `aws-cli-docs`, service configuration that is not about permissions to that service's skill (for example `aws-s3-docs`), and Kubernetes RBAC on EKS to `aws-eks-docs` or `kubernetes-docs`; the AWS IAM side stays here. SDK credential provider code belongs to the SDK's docs unless the question turns on IAM roles or policies.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/IAM/latest` with the user's exact terms plus IAM vocabulary such as `trust policy`, `permission boundary`, `condition key`, `AssumeRole`, `Identity Center`, or `Access Analyzer`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and policy JSON or commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- IAM API operations: the API reference at <https://docs.aws.amazon.com/IAM/latest/APIReference/Welcome.html>.
- Temporary credentials: the STS `AssumeRole` and session policy pages, and the STS API reference at <https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html>.
- Policy JSON: the policy element reference when condition keys or resource ARNs matter.
- Access denied: the policy evaluation logic pages, before suggesting `AdministratorAccess`.
- Roles: tell the trust policy (who can assume) from the permissions policy (what they can do).
- Cross-account access: the role trust and resource-based policy pages together.
- SSO: the IAM Identity Center pages, before legacy SAML-only guides where they apply.
- Least privilege: the Access Analyzer and policy validation pages.
- `aws iam` and `aws sts` syntax: cross-check `aws-cli-docs`.

## Gotchas

- Follow the documented best practices for credentials: roles and temporary credentials, never root user access keys.
- Access denied troubleshooting needs both identity-based and resource-based policies, kept apart.
- Scope permissions with condition keys and permission boundaries in place of `*` actions or resources.
- IAM user policies and role trust policies do different jobs and are not interchangeable.
- IAM is eventually consistent: a policy just created or updated may not apply at once.
