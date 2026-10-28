---
name: aws-eks-docs
description: Official Amazon EKS documentation, answered with links to the exact pages. Use for any EKS question, including cluster creation and upgrades, managed node groups, Fargate and Auto Mode, add-ons, cluster access and IRSA, networking and storage, observability, EKS Capabilities, or hybrid and EKS Anywhere deployments.
---

# Amazon EKS Docs

EKS answers drift with every release and generic Kubernetes advice skips its AWS-specific control plane, IAM and networking, so ground each answer in the live docs at <https://docs.aws.amazon.com/eks/latest/userguide/>, not memory, and link the exact page behind every claim.

Route core Kubernetes API behavior with no EKS angle to `kubernetes-docs`, AWS CLI install and global options to `aws-cli-docs`, IAM policy language to `aws-iam-docs` (IRSA and access entries stay here), ECS or Lambda deployments to `aws-ecs-docs` or `aws-lambda-docs`, and Helm chart authoring to `helm-docs` unless it concerns EKS add-ons.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/eks/latest` with the user's exact terms plus EKS vocabulary such as `managed node group`, `Fargate profile`, `IRSA`, `access entry`, `EKS Auto Mode`, or `VPC CNI`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and YAML, eksctl configs or commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- API parameters: the API reference at <https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html>.
- Node issues: tell managed node groups, self-managed nodes, Fargate, and Auto Mode apart.
- Auth: the access entries and IRSA pages, before legacy `aws-auth` ConfigMap guidance.
- Networking: the VPC CNI, security group, and load balancer controller pages together.
- Storage: the EKS page for the relevant CSI driver (EBS, EFS, FSx, or S3).
- Upgrades: the Kubernetes version lifecycle on EKS, before generic kubectl upgrade advice.
- Kubernetes resource YAML: verify core behavior with `kubernetes-docs`, keeping EKS-specific constraints from these docs.
- `aws eks` syntax: cross-check `aws-cli-docs`.

## Gotchas

- EKS manages the control plane; self-managed kubeadm cluster procedures do not apply to it.
- IRSA grants pods permissions through their service account, separate from the node instance profile.
- Access entries are the documented path for cluster access, ahead of `aws-auth` ConfigMap changes.
- Load balancers and the VPC CNI depend on the documented subnet tagging.
- Fargate has its own networking constraints; keep them apart from node group behavior.
