# 07. Kubernetes ☸️
Topics: cluster, node, Pod, Deployment, ReplicaSet, Service, Namespace, ConfigMap, Secret, probes and resource requests/limits.

Use a disposable local cluster such as kind or minikube. Read installation and resource requirements first.

## Example Deployment manifest
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: hello
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: hello
      template:
        metadata:
          labels:
            app: hello
        spec:
          containers:
            - name: web
              image: nginx:stable
              ports:
                - containerPort: 80

Exercises: explain why Deployments manage Pods, inspect Pod events, expose a demo Service and compare readiness vs liveness probes.

Never paste real credentials into manifests or public repositories.