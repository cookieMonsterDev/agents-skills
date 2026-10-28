---
name: aws-ecs-docs
description: Official Amazon ECS documentation, answered with links to the exact pages. Use for any ECS question, including task definitions, services and deployments, Fargate, EC2 and Managed Instances capacity, networking and Service Connect, IAM roles, auto scaling, logging and ECS Exec, or ECS Anywhere.
---

# Amazon ECS Docs

ECS answers drift with every release and Kubernetes or Compose habits mislead them, so ground each answer in the live docs at <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/>, not memory, and link the exact page behind every claim.

Route Kubernetes or EKS cluster operations to `kubernetes-docs` or `aws-eks-docs`, Docker Engine or Compose without ECS context to `docker-docs`, AWS CLI install and global options to `aws-cli-docs`, Lambda container images to `aws-lambda-docs`, and IAM policy language to `aws-iam-docs`.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/AmazonECS/latest` with the user's exact terms plus ECS vocabulary such as `task definition`, `Fargate`, `capacity provider`, `Service Connect`, `task execution role`, or `awsvpc`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and task definition JSON, templates or commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- API parameters: the API reference at <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html>.
- Launch types: tell Fargate, EC2, and Managed Instances constraints apart; for Fargate limits, the Fargate platform version and networking pages, before EC2 assumptions.
- Networking: the `awsvpc` mode and security group pages, before guessing port mappings.
- Permission errors: the task execution role and task role pages, read separately.
- Scaling: tell service auto scaling from cluster capacity providers.
- Deployments: the rolling update and CodeDeploy blue/green pages.
- `aws ecs` syntax: cross-check `aws-cli-docs`.

## Gotchas

- The task execution role pulls images and writes logs; the task role grants the application's AWS API access.
- Fargate requires `awsvpc` networking; bridge networking defaults do not carry over.
- Fargate task sizes follow documented CPU and memory constraints.
- A service desired count change differs from a task definition update; check which fields are immutable.
- Keep EC2 capacity management patterns for EC2 capacity; Fargate-only workloads do not need them.
