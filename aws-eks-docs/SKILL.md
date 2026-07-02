---
name: aws-eks-docs
description: Use when users ask how to create, configure, secure, scale, upgrade, network, or troubleshoot Amazon EKS clusters and workloads, including managed node groups, Fargate, EKS Auto Mode, add-ons, IRSA, EKS Capabilities, networking, storage, observability, eksctl, cluster access, or hybrid/Anywhere deployments, especially when they need official Amazon EKS documentation, exact links, or docs-grounded guidance.
---

Amazon EKS questions are easy to answer from stale memory or generic Kubernetes advice that ignores AWS-specific control plane, IAM, and networking. Use this skill to ground answers in the official Amazon EKS documentation and return the closest authoritative page instead of improvising cloud-provider steps.

## When to Use

Use this skill when the request is about:

- EKS concepts, architecture, and how EKS differs from self-managed Kubernetes
- Creating clusters, cluster IAM roles, and cluster endpoint access
- Managed node groups, self-managed nodes, and AWS Fargate profiles
- EKS Auto Mode and compute/storage automation
- Cluster add-ons (VPC CNI, CoreDNS, kube-proxy, EBS CSI, etc.)
- IAM Roles for Service Accounts (IRSA) and cluster access entries
- Networking: VPC, subnets, security groups, load balancers, and service mesh adjacency
- Storage on EKS: EBS, EFS, FSx, and S3 CSI drivers
- Observability: control plane logging, CloudWatch, Prometheus, and ADOT
- Upgrades, Kubernetes version lifecycle, and extended support
- EKS Capabilities (Argo CD, ACK, kro) and GitOps on EKS
- EKS Anywhere, hybrid nodes, and outpost deployments
- eksctl, CloudFormation, CDK, and Terraform patterns documented for EKS
- Troubleshooting cluster creation, node join, CNI, and API access errors

Do not use this skill for:

- Core Kubernetes API behavior with no EKS-specific context. Use `kubernetes-docs` instead.
- AWS CLI install or global CLI options. Use `aws-cli-docs` instead.
- General IAM policy language. Use `aws-iam-docs` for IAM fundamentals; use EKS docs for IRSA and access entries.
- ECS or Lambda deployment patterns. Use `aws-ecs-docs` or `aws-lambda-docs` instead.
- Helm chart authoring unless the question is about EKS add-ons or documented EKS integration paths.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and cluster creation
- Compute: node groups, Fargate, and Auto Mode
- Networking and load balancing
- Security, IAM, and access control
- Storage and persistent volumes
- Add-ons and platform components
- Observability and logging
- Upgrades and version lifecycle
- EKS Capabilities and integrations
- Hybrid, Anywhere, and advanced topologies
- Troubleshooting and known issues

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Amazon EKS docs first

- Treat `docs.aws.amazon.com/eks/latest/userguide` as the source of truth for Amazon EKS.
- Prefer the user guide at <https://docs.aws.amazon.com/eks/latest/userguide/>.
- Prefer the API reference at <https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html> for EKS API operations.
- Search with the user's exact terms plus focused EKS phrases such as `managed node group`, `Fargate profile`, `IRSA`, `access entry`, `EKS Auto Mode`, or `VPC CNI`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Kubernetes resource YAML, verify core behavior in `kubernetes-docs` when needed, but keep EKS-specific constraints from EKS docs.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API fields, open the specific EKS API reference page when operation parameters matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Amazon EKS docs links, not just the docs homepage.
- Only provide YAML, eksctl, or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Amazon EKS docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example YAML, eksctl config, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is Amazon EKS? and getting started before deep networking pages.
- For node issues, distinguish managed node groups, self-managed nodes, Fargate, and Auto Mode.
- For auth questions, check access entries and IRSA docs before legacy `aws-auth` ConfigMap-only guidance.
- For networking questions, check VPC CNI, security groups, and load balancer controller docs together.
- For storage questions, open the relevant CSI driver page (EBS, EFS, etc.) documented for EKS.
- For upgrade questions, check Kubernetes version lifecycle on EKS before generic kubectl upgrade advice.
- For CLI syntax-only questions, cross-check `aws-cli-docs` for `aws eks` commands.

## Common Mistakes

- Answering from generic Kubernetes memory without verifying EKS-specific docs
- Linking the EKS landing page when a narrower user guide or API page exists
- Treating EKS control plane management as identical to self-managed kubeadm clusters
- Confusing IRSA with node instance profile permissions
- Recommending `aws-auth` ConfigMap changes when access entries are the documented path
- Ignoring subnet tagging requirements for load balancers and VPC CNI
- Mixing Fargate networking constraints with standard node group behavior

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Amazon EKS docs as the final authority.
