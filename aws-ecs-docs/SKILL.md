---
name: aws-ecs-docs
description: Use when users ask how to create, configure, deploy, scale, network, secure, or troubleshoot Amazon ECS clusters, task definitions, services, and tasks, including Fargate, EC2 launch types, ECS Managed Instances, Service Connect, auto scaling, IAM roles, ECR integration, ECS Anywhere, or capacity providers, especially when they need official Amazon ECS documentation, exact links, or docs-grounded guidance.
---

Amazon ECS questions are easy to answer from stale memory or Kubernetes patterns that do not apply to ECS task definitions and services. Use this skill to ground answers in the official Amazon ECS documentation and return the closest authoritative page instead of generic container orchestration advice.

## When to Use

Use this skill when the request is about:

- ECS concepts: clusters, task definitions, tasks, services, and capacity
- Creating clusters, task definitions, and running tasks or services
- Launch types: AWS Fargate, EC2, and ECS Managed Instances
- Networking: awsvpc, bridge, host modes, security groups, and Service Connect
- IAM roles: task execution role, task role, and permissions boundaries
- Container images, ECR integration, and private registry authentication
- Load balancing with ALB/NLB and service discovery (Cloud Map)
- Auto scaling for services and capacity providers
- ECS Exec, logging (awslogs, FireLens), and observability
- ECS Anywhere and external instance registration
- Blue/green and rolling deployments with CodeDeploy
- Troubleshooting task placement, health checks, and stopped tasks

Do not use this skill for:

- Kubernetes or EKS cluster operations. Use `kubernetes-docs` or `aws-eks-docs` instead.
- Docker Engine or Compose without ECS context. Use `docker-docs` instead.
- AWS CLI install or global CLI options. Use `aws-cli-docs` instead.
- Lambda container image deployment. Use `aws-lambda-docs` for Lambda-specific constraints.
- General IAM policy language. Use `aws-iam-docs` for IAM fundamentals.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Task definitions and container definitions
- Clusters, capacity, and launch types
- Services, deployments, and scheduling
- Networking and Service Connect
- Security, IAM roles, and secrets
- Storage, volumes, and EFS/EBS integration
- Auto scaling and capacity providers
- Logging, monitoring, and ECS Exec
- ECS Anywhere and hybrid capacity
- Troubleshooting stopped tasks and placement failures

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Amazon ECS docs first

- Treat `docs.aws.amazon.com/AmazonECS/latest/developerguide` as the source of truth for Amazon ECS.
- Prefer the developer guide at <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/>.
- Prefer the API reference at <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html> for operation-level details.
- Search with the user's exact terms plus focused ECS phrases such as `task definition`, `Fargate`, `capacity provider`, `Service Connect`, `task execution role`, or `awsvpc`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For Fargate-specific limits, check Fargate platform version and networking docs before answering from EC2 assumptions.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API fields, open the specific ECS API reference page when parameters matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Amazon ECS docs links, not just the docs homepage.
- Only provide task definition JSON, CloudFormation, or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Amazon ECS docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example task definition, service config, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is Amazon ECS? and getting started before API reference pages.
- For launch type questions, distinguish Fargate, EC2, and Managed Instances constraints.
- For networking questions, check `awsvpc` mode and security group rules before guessing port mappings.
- For permission errors, check task execution role vs task role docs separately.
- For scaling questions, distinguish service auto scaling from cluster capacity providers.
- For deployment questions, check rolling update and CodeDeploy blue/green docs.
- For CLI syntax-only questions, cross-check `aws-cli-docs` for `aws ecs` commands.

## Common Mistakes

- Answering from Kubernetes or Docker Compose memory without verifying ECS docs
- Linking the ECS landing page when a narrower developer guide or API page exists
- Confusing task execution role (pull image, logs) with task role (application AWS API access)
- Applying bridge networking defaults when Fargate requires `awsvpc`
- Ignoring CPU/memory platform constraints documented for Fargate task sizes
- Treating service desired count changes as equivalent to task definition immutable field updates
- Recommending EC2 capacity management patterns for Fargate-only workloads

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Amazon ECS docs as the final authority.
