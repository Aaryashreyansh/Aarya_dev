# Phase 4 — Automation (Weeks 13–16)

**Outcome:** automate repeatable checks and understand infrastructure configuration workflows.

## Week 13 — CI/CD concepts and GitHub Actions
Learn CI vs Continuous Delivery vs Continuous Deployment; trigger, workflow, job, runner, step, action, artifact, environment and secret. Read workflow YAML carefully. Build a pipeline that checks out your own repository, sets up Python, installs test dependencies and runs tests on push and pull request.

## Week 14 — Jenkins
Learn controller/agent architecture, jobs, pipeline stages, Jenkinsfile, credentials store, plugins and build artifacts. Run Jenkins only in a local/disposable environment. Create a simple pipeline: checkout → test → package. Keep secrets in Jenkins credentials, not Jenkinsfile or repository.

## Week 15 — Terraform
1. Learn provider, resource, data source, variable, output and module.
2. Understand configuration files and declarative desired state.
3. Practise `terraform fmt`, `terraform init`, `terraform validate` and `terraform plan` in a local or disposable sandbox.
4. Understand state, drift, locking and remote state.
5. Read every plan before applying. Learn how destroy plans work before using them.
6. Keep state, tfvars containing secrets and credentials out of Git.

## Week 16 — Ansible and integrated pipeline
Learn inventory, ad-hoc command concept, module, playbook, task, handler, variable, template, role and idempotence. Start with localhost or a VM you own. Build a playbook that performs harmless configuration checks before attempting changes.

## Mini project — Push to image
Create a pipeline that checks out the project, runs tests, builds a Docker image and stores a build artifact or publishes to a registry you control. Use repository/environment secrets for credentials and least-privilege permissions. Do not deploy publicly by default.

## Exit checklist
- [ ] Push and pull request automatically run tests.
- [ ] Jenkinsfile stages are understood.
- [ ] Terraform plan is reviewed before any lab apply.
- [ ] Ansible playbook runs against an authorized test machine.
- [ ] Pipeline logs show a successful test and image build.
