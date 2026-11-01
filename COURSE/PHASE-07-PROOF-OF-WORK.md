# Phase 7 — Proof of Work (Week 26+)

**Outcome:** demonstrate skills through reproducible projects, readable documentation and clear technical explanations.

## Portfolio minimum
Complete at least two end-to-end projects. Recommended choices:
1. **Automated Python service:** Python app + tests + GitHub Actions + Docker.
2. **Local cloud-native lab:** Docker Compose or local Kubernetes + Prometheus/Grafana + operational README.
3. **Infrastructure automation demo:** Terraform plan in a disposable sandbox + Ansible configuration of a local VM.

## Every project README should answer
- What problem does it solve?
- Why did you choose this design?
- What are the prerequisites?
- How do I set it up and run it?
- How do I test it?
- What does the architecture diagram show?
- What can fail, and how do I troubleshoot it?
- What security controls are present?
- What could cost money?
- How do I clean up and verify cleanup?
- What did you learn and what would you improve?

## Interview preparation method
For each question answer in four parts: definition → why it matters → concrete example → trade-off/limitation. Practise explaining Linux processes, DNS, TCP/UDP, Git merge conflicts, Docker images/containers, Kubernetes Deployments/Services, CI/CD, Terraform state, IAM least privilege, metrics/logs/traces and SQL joins.

## Capstone — application to monitored deployment
1. Build a small app with tests.
2. Track it in Git and use a feature-branch/PR workflow.
3. Build a Docker image.
4. Run automated tests and image build in CI.
5. Define infrastructure using Terraform in an approved sandbox.
6. Deploy the app using a documented and secure approach.
7. Add monitoring, dashboard and an actionable alert.
8. Document architecture, assumptions, risks, cost estimate and teardown.
9. Destroy temporary infrastructure and verify no billable resources remain.

## Final assessment
A project is complete only when another person can follow the README, reproduce the result, run tests, understand the architecture and clean up the lab safely. A green contribution calendar is not a substitute for working evidence.
