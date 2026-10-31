# Aarya DevOps Academy: 26+ Week Roadmap

A practical, project-first path from Linux fundamentals to a cloud-deployed, monitored application. The schedule assumes steady part-time learning; spend more time when a concept needs practice. Do not rush ahead just to finish a week.

**Learning ratio:** aim for 70% hands-on practice and 30% theory. Push a small, meaningful commit regularly, and write questions or discoveries in `notes.md`.

---

## Phase 1: Foundation (Weeks 1–4)

| Folder | Focus |
|---|---|
| [01-Linux](01-Linux/README.md) | Commands, file permissions, users, processes, package managers |
| [02-Networking](02-Networking/README.md) | IP, DNS, ports, HTTP/HTTPS, firewalls, SSH |
| [03-Git-GitHub](03-Git-GitHub/README.md) | Commit, branch, merge, pull request, conflict resolution |

### Exit checklist
- [ ] I can run common Linux commands without looking them up every time.
- [ ] I have logged in to a server or VM using SSH in an authorized lab.
- [ ] I can manage my repository from the terminal.
- [ ] I understand basic IP, DNS, ports and HTTP/HTTPS.

**Mini project:** Create a branch, make a change, open a pull request, resolve a conflict if one occurs, and merge it. Do the workflow from the terminal wherever practical.

## Phase 2: Scripting (Weeks 5–8)

| Folder | Focus |
|---|---|
| [04-Python](04-Python/README.md) | Variables, loops, functions, files, error handling, APIs |
| [05-Bash-Scripting](05-Bash-Scripting/README.md) | Variables, conditions, loops, cron, automation |

### Exit checklist
- [ ] I have written 10 or more small Python programs.
- [ ] I can write a Bash script with arguments, conditions and clear exit behavior.
- [ ] I have scheduled a harmless test script with cron in my own Linux VM, or documented the equivalent scheduler on my OS.

**Mini project:** Build a backup or log-summary/cleanup script in Bash or Python. Test it on a dedicated sample folder first. Include a dry-run option and document what it will change before enabling any cleanup.

## Phase 3: Containers (Weeks 9–12)

| Folder | Focus |
|---|---|
| [06-Docker](06-Docker/README.md) | Images, containers, Dockerfile, volumes, networks, Compose |
| [07-Kubernetes](07-Kubernetes/README.md) | Pods, Deployments, Services, ConfigMaps, Secrets |

### Exit checklist
- [ ] I have written a Dockerfile for my own small app.
- [ ] I have run a multi-container setup with Docker Compose.
- [ ] I have deployed the app to a local Kubernetes cluster using kind or minikube.
- [ ] I can explain what configuration belongs in a Secret and why real secrets must not be committed.

**Mini project:** Package a simple app in Docker and run it on a local Kubernetes cluster. Add setup, test and cleanup instructions.

## Phase 4: Automation (Weeks 13–16)

| Folder | Focus |
|---|---|
| [08-CICD-Jenkins](08-CICD-Jenkins/README.md) | Pipelines, Jenkinsfile, GitHub Actions |
| [12-Terraform](12-Terraform/README.md) | Providers, resources, variables, state |
| [13-Ansible](13-Ansible/README.md) | Inventory, playbooks, roles |

### Exit checklist
- [ ] A push to my practice repository triggers an automated build and test.
- [ ] I have used Terraform plan/apply/destroy in a disposable lab and verified cleanup.
- [ ] I have used an Ansible playbook to configure a local VM or another authorized test host.

**Mini project:** Code push → automated tests → Docker image build. Keep credentials in the CI secret store, never in source code.

## Phase 5: Cloud (Weeks 17–22)

| Folder | Focus |
|---|---|
| [09-AWS](09-AWS/README.md) | EC2, S3, IAM, VPC, RDS concepts |
| [10-Azure](10-Azure/README.md) | Overview: VM, storage, resource groups |
| [11-GCP](11-GCP/README.md) | Overview: Compute Engine, Cloud Storage |

**Focus rule:** Learn one cloud deeply first. This roadmap uses AWS for the hands-on path; learn Azure and GCP concepts at overview level for now.

### Exit checklist
- [ ] I have reviewed AWS account security, pricing and current Free Tier eligibility, and configured billing alerts or budgets where available.
- [ ] I have launched a small EC2 lab instance and run a demo app, then stopped or deleted the resources.
- [ ] I understand IAM users, roles and policies at a conceptual level and use least privilege.
- [ ] I can explain the purpose of S3, VPC and RDS.

**Mini project:** Use Terraform to create a small EC2 lab, deploy a demo app, verify it works, and destroy all resources. Confirm in the cloud console that no billable resources were left behind.

> **Cloud cost warning:** Free Tier eligibility, quotas and prices change. Billing alerts are not always hard spending caps. Get the account owner's permission, check current pricing before provisioning, and verify cleanup afterwards.

## Phase 6: Monitoring + Database (Weeks 23–25)

| Folder | Focus |
|---|---|
| [14-Monitoring](14-Monitoring/README.md) | Prometheus, Grafana, logs, alerts |
| [15-SQL-NoSQL](15-SQL-NoSQL/README.md) | SQL queries, joins, indexes, MongoDB/Redis basics |

### Exit checklist
- [ ] I have built a Prometheus + Grafana dashboard in a local lab.
- [ ] I have configured and tested a simple alert rule.
- [ ] I have practised SQL joins and aggregations.
- [ ] I can explain the difference between metrics, logs and traces.

**Mini project:** Create a monitoring dashboard for the app built in Phase 3. Use sample or local test data and document what each panel tells you.

## Phase 7: Proof of Work (Week 26+)

| Folder | Focus |
|---|---|
| [16-Projects](16-Projects/README.md) | End-to-end projects |
| [17-Interview-Questions](17-Interview-Questions/README.md) | Questions and explained answers for each topic |
| [18-Cheat-Sheets](18-Cheat-Sheets/README.md) | Quick revision; update throughout every phase |

### Exit checklist
- [ ] I have completed at least two end-to-end projects.
- [ ] Every project has a README explaining what it does, why it exists and how to run it.
- [ ] I have revised the interview questions and can explain answers in my own words.
- [ ] My repositories contain no credentials, private keys or personal data.

**Capstone:** App → Docker → CI/CD pipeline → Terraform-based cloud deployment → monitoring. Add an architecture diagram, test evidence, security notes, estimated cost considerations and a reliable teardown guide.

---

## Weekly working rhythm

- Learn a concept, then practise it immediately.
- Keep a `notes.md` in the relevant folder for questions, errors and lessons learned.
- Push meaningful commits regularly; consistency matters more than empty contribution squares.
- At the end of each phase, push the mini project to GitHub as proof of work.
- If stuck, write down the exact error, what you expected, what happened and what you tried.

## Non-negotiable safety habits

- Use only machines, networks and cloud accounts you own or are explicitly authorized to use.
- Use a local VM/container for experiments whenever possible.
- Never commit passwords, API keys, SSH private keys, cloud credentials or real user data.
- Use least-privilege access and rotate any credential that is accidentally exposed.
- Review Terraform plans before applying; inspect what destroy will remove.
- Use dry-run modes and test folders for backup or cleanup scripts.
- Check cloud prices, quotas and account-owner permission before creating resources.
- After every cloud lab, verify resources are deleted. Do not assume stopping a VM removes every billable resource.

**Reminder:** The goal is not to tick every box quickly. The goal is to explain what you built, demonstrate it working, and safely reproduce it.
