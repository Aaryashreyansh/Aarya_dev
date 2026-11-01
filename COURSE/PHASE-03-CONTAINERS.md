# Phase 3 — Containers (Weeks 9–12)

**Outcome:** package an application, run a multi-service local environment, and understand Kubernetes building blocks.

## Week 9 — Docker fundamentals
Learn container vs virtual machine, image vs container, registry, tag, layer, daemon/client and container lifecycle. Inspect Docker with `docker version`, `docker info`, `docker image ls` and `docker ps`. Run the official hello-world test if Docker is installed and available.

## Week 10 — Build and run an app
1. Create a tiny Python web app with a health endpoint.
2. Understand Dockerfile instructions: FROM, WORKDIR, COPY, RUN, ENV, EXPOSE and CMD.
3. Build an image with a meaningful tag.
4. Run it with an explicitly mapped local port.
5. Inspect logs, process status and exit code.
6. Understand bind mounts vs named volumes.
7. Learn container networks and service-to-service name resolution.

Use trusted base images, avoid running as root when practical, and never bake secrets into image layers.

## Week 11 — Docker Compose
Learn YAML indentation, services, images/build, ports, environment, volumes, networks, health checks and dependency behavior. Create a local app plus a database only with sample data. Use a local-only lab and document how to stop and remove the demo safely. Understand that persistent volumes may remain after containers are removed.

## Week 12 — Kubernetes foundations
1. Learn cluster, control plane, node, Pod and container runtime.
2. Understand Deployment and ReplicaSet; a Deployment declares the desired Pod state.
3. Learn Service types conceptually: ClusterIP, NodePort and LoadBalancer.
4. Learn Namespace, labels, selectors and annotations.
5. Learn ConfigMap for non-secret configuration and Secret for sensitive values; Kubernetes Secrets need appropriate access controls and encryption configuration.
6. Learn readiness, liveness and startup probes.
7. Learn requests/limits and why resource planning matters.
8. Use kind or minikube for a disposable local cluster. Practise `kubectl get`, `describe`, `logs`, `apply` and `delete` only in that lab.

## Mini project
Containerize the Phase 2 app, run it locally, then deploy it to a local kind/minikube cluster using a Deployment and Service. Add a README with architecture, build/run commands, tests, screenshots and teardown steps.

## Exit checklist
- [ ] Dockerfile builds a working app image.
- [ ] Compose starts the local multi-container demo.
- [ ] Local Kubernetes deployment reaches the expected state.
- [ ] You can inspect logs/events and explain a failed Pod.
- [ ] No credentials are stored in source, image or public manifests.


## Where to learn this phase
See [Resources Directory](RESOURCES.md): Docker → Docker Get Started and Compose quickstart; Kubernetes → official Kubernetes Basics tutorial; local cluster → kind or minikube documentation. Complete the beginner path before advanced configuration.
