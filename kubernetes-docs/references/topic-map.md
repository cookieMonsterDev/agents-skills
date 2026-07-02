# Kubernetes Topic Map

This reference is a compact routing aid derived from the Kubernetes documentation catalog. It is intentionally selective and deduplicated. Use it to find the right documentation neighborhood quickly, then verify against the live docs on `kubernetes.io`.

Base URL for all links below: <https://kubernetes.io/docs/>

Current documentation version: v1.36

## Documentation Home

- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Available Documentation Versions](https://kubernetes.io/docs/home/#available-documentation-versions)
- [Glossary](https://kubernetes.io/docs/reference/glossary/)

## Concepts

- [Concepts Overview](https://kubernetes.io/docs/concepts/overview/)
- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [Workloads and Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
- [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

## Setup and Administration

- [Getting Started](https://kubernetes.io/docs/setup/)
- [Learning Environment](https://kubernetes.io/docs/setup/learning-environment/)
- [Production Environment](https://kubernetes.io/docs/setup/production-environment/)
- [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Creating a Cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Upgrading kubeadm Clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
- [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

## Tasks

- [Tasks Overview](https://kubernetes.io/docs/tasks/)
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
- [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Assign CPU Resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
- [Assign Memory Resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
- [Configure a Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
- [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)
- [Run a Replicated Stateful Application](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/)
- [Use Port Forwarding to Access Applications](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
- [Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
- [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
- [Declarative Management with Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)
- [Declarative Management with Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)

## Tutorials

- [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)
- [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [StatefulSet Basics](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)

## kubectl Reference

- [kubectl Overview](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
- [kubectl Commands](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_commands/)
- [kubectl apply](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/)
- [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/)
- [kubectl describe](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/)
- [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
- [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/)
- [kubectl port-forward](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/)
- [kubectl rollout](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
- [JSONPath Support](https://kubernetes.io/docs/reference/kubectl/jsonpath/)
- [kubectl for Docker Users](https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/)

## API Reference

- [API Overview](https://kubernetes.io/docs/reference/kubernetes-api/)
- [Kubernetes API Concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
- [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/)
- [API Access Control](https://kubernetes.io/docs/reference/access-authn-authz/)
- [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/)
- [Feature Gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
- [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)

## Core API Resources

- [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)
- [Deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
- [StatefulSet](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
- [Service](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
- [Ingress](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/)
- [ConfigMap](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)
- [Secret](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
- [PersistentVolume](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
- [PersistentVolumeClaim](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
- [StorageClass](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/)
- [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)
- [CustomResourceDefinition](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/)

## Cluster Components

- [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
- [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
- [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
- [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
- [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)

## kubeadm Reference

- [kubeadm Overview](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
- [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/)
- [kubeadm join](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/)
- [kubeadm upgrade](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/)
