---
name: kubernetes-docs
description: Use when users ask how to install, configure, deploy, scale, secure, network, store, schedule, debug, or troubleshoot Kubernetes clusters and workloads, including pods, deployments, services, ingress, configmaps, secrets, RBAC, kubectl, kubeadm, Helm-adjacent core APIs, autoscaling, jobs, statefulsets, daemonsets, CRDs, or cluster administration, especially when they need official Kubernetes documentation, exact links, or docs-grounded guidance.
---

Kubernetes questions are easy to answer from stale memory or pre-dockershim patterns. Use this skill to ground answers in the official Kubernetes documentation and return the closest authoritative page instead of generic cloud-native advice.

## When to Use

Use this skill when the request is about:

- Kubernetes concepts, architecture, and cluster components
- Installing clusters with kubeadm, Minikube, or production setup paths
- Workloads: Pods, Deployments, StatefulSets, DaemonSets, Jobs, and CronJobs
- Services, Ingress, Gateway API, NetworkPolicy, and DNS
- Storage: PersistentVolumes, StorageClasses, CSI, and volume snapshots
- Configuration: ConfigMaps, Secrets, and resource requests/limits
- Security: RBAC, ServiceAccounts, Pod Security Standards, and admission control
- Scheduling: affinity, taints, tolerations, topology spread, and priority
- kubectl usage, kubeconfig, contexts, and imperative vs declarative management
- Kubernetes API resources, server-side apply, and CustomResourceDefinitions
- Monitoring, logging, debugging pods and nodes
- Upgrading clusters, feature gates, and version compatibility

Do not use this skill for:

- A different Kubernetes version when the user explicitly needs that version. Say which version you are using and offer to switch docs if needed.
- Raw Docker Engine or Compose usage without Kubernetes context. Use `docker-docs` instead.
- AWS EKS-specific console or CLI operations when the question is provider-specific rather than core Kubernetes behavior. Use `aws-cli-docs` for AWS CLI commands against EKS.
- Third-party tools (Helm charts, Argo CD, Istio) unless the question is about core Kubernetes resources or patterns documented on kubernetes.io.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started, concepts, and tutorials
- Cluster setup and administration (kubeadm, nodes, upgrades)
- Workloads and Pod configuration
- Services, networking, and ingress
- Storage and persistent data
- Security, RBAC, and policy
- Scheduling and resource management
- kubectl and API reference
- Debugging, monitoring, and troubleshooting
- Extending Kubernetes (CRDs, operators, webhooks)

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Kubernetes docs first

- Treat `kubernetes.io/docs` as the source of truth for Kubernetes.
- Prefer pages under <https://kubernetes.io/docs/home/>.
- Default to the current documentation version (v1.36) unless the user specifies another supported version.
- Search with the user's exact terms plus focused Kubernetes phrases such as `PodDisruptionBudget`, `readinessProbe`, `server-side apply`, `kubeconfig`, `taints`, or `StorageClass`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For deprecated APIs or removed features, check the deprecation guide before answering from older knowledge.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API fields, open the specific API reference page for the resource (for example Pod, Deployment, Ingress).
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Kubernetes docs links, not just the docs homepage.
- Only provide YAML manifests or kubectl examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Kubernetes docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example YAML or kubectl commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer Concepts before Tasks or Reference pages.
- For setup questions, prefer Getting started and kubeadm docs before guessing cloud-provider steps.
- For workload questions, distinguish Deployments (stateless) from StatefulSets (stable identity and storage).
- For networking questions, check Service types and Ingress/Gateway API docs before recommending NodePort as default.
- For storage questions, distinguish PersistentVolume, PersistentVolumeClaim, and StorageClass before suggesting hostPath.
- For security questions, start with RBAC and Pod Security Standards before legacy PodSecurityPolicy guidance.
- For debugging questions, prefer Tasks > Troubleshooting before generic log-grep advice.
- For kubectl questions, open the specific subcommand reference page when flags or output format matter.

## Common Mistakes

- Answering from memory without verifying the current Kubernetes docs
- Linking the Kubernetes docs homepage when a narrower Concepts, Tasks, or Reference page exists
- Assuming dockershim or Docker as the required container runtime without checking CRI docs
- Confusing namespaces (isolation) with labels (selection) or annotations (metadata)
- Mixing deprecated API versions (`extensions/v1beta1` Ingress) with current stable APIs
- Recommending `latest` image tags or default ServiceAccount permissions without checking security guidance
- Treating Helm or operator behavior as built-in Kubernetes API behavior without checking core docs

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Kubernetes docs as the final authority.
