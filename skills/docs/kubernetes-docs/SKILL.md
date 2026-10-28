---
name: kubernetes-docs
description: Official Kubernetes documentation, answered with links to the exact pages. Use for any Kubernetes question, including workloads such as Pods and Deployments, Services and Ingress, storage, RBAC and Pod security, kubectl, or cluster setup with kubeadm.
---

# Kubernetes Docs

Kubernetes APIs are deprecated and removed between minor versions, so ground each answer in the live docs at <https://kubernetes.io/docs/home/>, not memory, and link the exact page behind every claim.

Route raw Docker Engine or Compose usage to `docker-docs`, Helm charts to `helm-docs`, EKS-specific operations to `aws-eks-docs`, and AWS CLI commands against EKS to `aws-cli-docs`. Argo CD, Istio and other third-party tools belong to their own docs unless the question turns on core Kubernetes resources or patterns.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `kubernetes.io/docs` with the user's exact terms plus Kubernetes vocabulary such as `PodDisruptionBudget`, `readinessProbe`, `server-side apply`, `kubeconfig`, `taints`, or `StorageClass`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and YAML manifests or `kubectl` commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Version: default to the current docs version (v1.37); when the user needs another supported version, say which version you are using and switch to its docs.
- Deprecated APIs or removed features: the deprecation guide, before older knowledge.
- Concepts: the Concepts pages, before Tasks or Reference.
- Cluster setup: Getting started and the kubeadm docs, before cloud-provider steps.
- API fields: the API reference page for that resource, such as Pod, Deployment or Ingress.
- `kubectl` flags or output format: the specific subcommand reference page.
- Debugging: Tasks > Troubleshooting.
- Security: RBAC and Pod Security Standards; PodSecurityPolicy guidance is legacy.
- Networking: Service types and the Ingress or Gateway API docs, before defaulting to NodePort.

## Gotchas

- Deployments run stateless workloads; StatefulSets add stable identity and storage.
- Persistent storage comes from PersistentVolume, PersistentVolumeClaim and StorageClass, kept apart, before any `hostPath` suggestion.
- Take container runtimes from the CRI docs; Docker and dockershim are not required runtimes.
- Namespaces isolate, labels select, and annotations carry metadata.
- Use current stable API versions: Ingress is `networking.k8s.io/v1`, since `extensions/v1beta1` was removed in v1.22.
- Check the security guidance before recommending `latest` image tags or default ServiceAccount permissions.
- Confirm Helm or operator behavior in their own docs; it is not built-in Kubernetes API behavior.
