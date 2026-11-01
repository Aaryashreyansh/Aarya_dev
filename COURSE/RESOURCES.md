# Aarya DevOps Academy — Learning Resources Directory

This directory answers: **Where can I learn and practise each topic?** Start with the beginner resource, use official documentation as the reference, then practise in a personal/local lab.

## How to use these links
1. Read the beginner guide first.
2. Open the official documentation for accurate details and command references.
3. Complete the hands-on lab in your own device, local VM, or disposable environment.
4. Write notes and save evidence in your project README.

**Access labels**
- **Official** means documentation or training from the technology's maintainers/provider.
- **Practice** means a learning playground or interactive exercise platform.
- **Community** means a third-party guide; check its date and accuracy against official docs.

Most documentation links are free to read. Some learning platforms offer optional paid plans, accounts, or limited free labs. Availability and pricing can change. This directory does not promise that every external lab is unlimited or free.

---

## Phase 1 — Foundation (Weeks 1–4)

### 01. Linux
| Resource | What to learn | Link |
|---|---|---|
| Ubuntu command-line tutorial — Official | Terminal basics, folders, files, commands, safe use of administrator privileges | https://ubuntu.com/tutorials/command-line-for-beginners |
| Ubuntu Desktop Linux tutorial — Official | Step-by-step beginner command-line practice | https://ubuntu.com/desktop/docs/en/latest/tutorial/the-linux-command-line-for-beginners/ |
| Ubuntu Server tutorial — Official | Server basics, terminal, software management and administration | https://ubuntu.com/server/docs/tutorial/ |
| Linux Journey — Community | Linux concepts arranged in beginner-friendly lessons | https://linuxjourney.com/ |
| GNU Coreutils manual — Official | Reference for common file and text commands | https://www.gnu.org/software/coreutils/manual/coreutils.html |

**Recommended order:** Ubuntu command-line tutorial → Linux Journey → practise commands in your own Termux/Linux VM → use Coreutils manual when you need command details.

### 02. Networking
| Resource | What to learn | Link |
|---|---|---|
| Cloudflare Learning Center — DNS | DNS, resolvers and domain-name lookup concepts | https://www.cloudflare.com/learning/dns/what-is-dns/ |
| MDN HTTP overview — Reference | HTTP requests, responses, methods, headers and status codes | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview |
| MDN HTTPS — Reference | HTTPS and secure web communication | https://developer.mozilla.org/en-US/docs/Glossary/HTTPS |
| OpenSSH manual — Official | SSH client/server command reference | https://www.openssh.com/manual.html |
| Ubuntu OpenSSH Server guide — Official | SSH server setup and administration | https://ubuntu.com/server/docs/how-to/security/openssh-server/ |
| Ubuntu UFW guide — Community documentation | Basic host firewall concepts and UFW | https://help.ubuntu.com/community/UFW |

**Recommended order:** IP/private-public address and ports → DNS → HTTP/HTTPS → SSH concepts → firewall basics. Practise only against your own device, local VM or explicitly authorized host.

### 03. Git and GitHub
| Resource | What to learn | Link |
|---|---|---|
| Pro Git book — Official project book | Git from basics through branching, merging, remotes and internals | https://git-scm.com/book/en/v2 |
| GitHub Get Started — Official | GitHub repositories, workflow and collaboration | https://docs.github.com/en/get-started |
| GitHub Hello World — Official hands-on | Repository, branch, commit, pull request and merge | https://docs.github.com/en/get-started/using-github/hello-world |
| GitHub Skills — Official interactive courses | Guided GitHub practice with automated feedback | https://skills.github.com/ |
| GitHub flow — Official | Branch-based contribution workflow | https://docs.github.com/en/get-started/using-github/github-flow |

**Recommended order:** Pro Git chapters 1–3 → GitHub Hello World → GitHub Skills → complete the Phase 1 terminal-only mini-project.

---

## Phase 2 — Scripting (Weeks 5–8)

### 04. Python
| Resource | What to learn | Link |
|---|---|---|
| Python Tutorial — Official | Language basics, control flow, functions, data structures, files and exceptions | https://docs.python.org/3/tutorial/ |
| Python setup and usage — Official | Interpreter and environment basics | https://docs.python.org/3/using/index.html |
| Python standard library — Official | Files, paths, JSON, logging, command-line arguments and testing tools | https://docs.python.org/3/library/ |
| Exercism Python track — Practice | Small coding exercises and practice problems | https://exercism.org/tracks/python |

**Recommended order:** Python Tutorial sections 3–8 → files/JSON/exceptions → virtual environments → 10 small programs → log-summary mini-project.

### 05. Bash scripting and cron
| Resource | What to learn | Link |
|---|---|---|
| GNU Bash manual — Official | Shell syntax, variables, conditions, loops, functions and expansions | https://www.gnu.org/software/bash/manual/bash.html |
| Bash reference manual — Official | Full Bash language reference | https://www.gnu.org/software/bash/manual/ |
| ShellCheck — Tool | Find common shell-script mistakes | https://www.shellcheck.net/ |
| Ubuntu Server documentation — Official | Server administration and scheduled task context | https://ubuntu.com/server/docs/ |

**Recommended order:** shell basics → quoting and variables → conditions/loops/functions → exit codes and redirection → ShellCheck → schedule a harmless test script in your own Linux VM. Android app environments may not provide a normal cron service.

---

## Phase 3 — Containers (Weeks 9–12)

### 06. Docker and Compose
| Resource | What to learn | Link |
|---|---|---|
| Docker Get Started — Official | Beginner Docker path | https://docs.docker.com/get-started/ |
| Docker container learning path — Official | Images, containers, volumes and Compose | https://docs.docker.com/learn/paths/get-started-with-docker-containers/ |
| Docker Compose quickstart — Official | Multi-container app with a database | https://docs.docker.com/compose/gettingstarted/ |
| Docker Python guide — Official | Containerize a Python application and use Compose | https://docs.docker.com/guides/python/ |
| Docker guides — Official | Additional hands-on labs and app guides | https://docs.docker.com/guides/ |

**Recommended order:** run first container → understand image/container → Dockerfile → volumes/networks → Compose quickstart → containerize your own small app.

### 07. Kubernetes
| Resource | What to learn | Link |
|---|---|---|
| Kubernetes Basics — Official interactive tutorial | Deploy, scale, update and debug an app | https://kubernetes.io/docs/tutorials/kubernetes-basics/ |
| Kubernetes tutorials — Official | Pods, Services, configuration, workloads and security | https://kubernetes.io/docs/tutorials/ |
| Kubernetes concepts — Official | Cluster architecture and core objects | https://kubernetes.io/docs/concepts/ |
| Minikube — Official | Run Kubernetes locally | https://minikube.sigs.k8s.io/docs/start/ |
| kind — Official | Run local Kubernetes clusters using containers | https://kind.sigs.k8s.io/ |

**Recommended order:** Kubernetes Basics → Pods and Deployments → Services → ConfigMaps/Secrets → probes/resources → deploy the Dockerized mini-project to kind or minikube.

---

## Phase 4 — Automation (Weeks 13–16)

### 08. CI/CD and Jenkins
| Resource | What to learn | Link |
|---|---|---|
| GitHub Actions getting started — Official | Workflows, jobs, runners, steps and triggers | https://docs.github.com/en/actions/get-started |
| GitHub Actions Python CI — Official | Build and test a Python project automatically | https://docs.github.com/en/actions/tutorials/build-and-test-code/python |
| GitHub Actions security — Official | Permissions and secure workflow practices | https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions |
| Jenkins tutorials — Official | Guided Jenkins and Pipeline tutorials | https://www.jenkins.io/doc/tutorials/ |
| Jenkins Pipeline — Official | Jenkinsfile and pipeline syntax | https://www.jenkins.io/doc/book/pipeline/ |

**Recommended order:** GitHub Actions quickstart → Python test workflow → secure secrets/permissions → Jenkins guided tour → Jenkinsfile. Do not commit credentials into workflow files.

### 12. Terraform
| Resource | What to learn | Link |
|---|---|---|
| Terraform tutorials — Official | Step-by-step infrastructure-as-code tutorials | https://developer.hashicorp.com/terraform/tutorials |
| Terraform AWS getting started — Official | Create, manage and destroy AWS lab infrastructure | https://developer.hashicorp.com/terraform/tutorials/aws-get-started |
| Terraform language docs — Official | Providers, resources, variables, outputs and modules | https://developer.hashicorp.com/terraform/language |
| Terraform CLI docs — Official | init, plan, apply, state and destroy commands | https://developer.hashicorp.com/terraform/cli |

**Recommended order:** Terraform get started → variables/outputs → state → plan review → disposable lab. Always inspect plans and verify cleanup; never commit state files or credentials.

### 13. Ansible
| Resource | What to learn | Link |
|---|---|---|
| Ansible Getting Started — Official | Installation, inventory and first playbook | https://docs.ansible.com/projects/ansible/latest/getting_started/index.html |
| Start automating with Ansible — Official | Build an automation project and Hello World playbook | https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_ansible.html |
| Ansible playbooks — Official | Playbook structure and tasks | https://docs.ansible.com/projects/ansible/latest/playbook_guide/ |
| Red Hat Ansible learning — Official | Beginner paths and guided learning | https://developers.redhat.com/products/ansible/getting-started |

**Recommended order:** inventory → modules → first playbook → variables/handlers → roles → idempotence. Practise on localhost or a VM you own.

---

## Phase 5 — Cloud (Weeks 17–22)

### 09. AWS — primary cloud for this roadmap
| Resource | What to learn | Link |
|---|---|---|
| AWS Training and Certification — Official | Beginner cloud courses and role-based learning | https://aws.amazon.com/training/ |
| AWS Skill Builder — Official | Self-paced digital training and labs; check which items are free | https://skillbuilder.aws/ |
| AWS documentation — Official | EC2, S3, IAM, VPC, RDS and other service references | https://docs.aws.amazon.com/ |
| AWS EC2 documentation — Official | Virtual server concepts and operations | https://docs.aws.amazon.com/ec2/ |
| AWS S3 documentation — Official | Object storage concepts and tasks | https://docs.aws.amazon.com/s3/ |
| AWS IAM documentation — Official | Users, roles, policies and access control | https://docs.aws.amazon.com/iam/ |
| AWS VPC documentation — Official | Virtual networking, subnets and routing | https://docs.aws.amazon.com/vpc/ |
| AWS Pricing Calculator — Official | Estimate costs before creating resources | https://calculator.aws/ |

**Recommended order:** cloud fundamentals → IAM and security → VPC concepts → EC2 → S3 → RDS overview → Terraform lab. Get account-owner permission, review current prices and set budget alerts before provisioning. Free-tier terms and prices can change; alerts may not be hard spending limits.

### 10. Azure — overview only
| Resource | What to learn | Link |
|---|---|---|
| Azure training — Official | Azure Fundamentals learning paths | https://learn.microsoft.com/en-us/training/azure |
| Azure cloud concepts learning path — Official | Cloud models and shared responsibility | https://learn.microsoft.com/en-us/training/paths/azure-fundamentals/ |
| Azure documentation — Official | VM, storage, networking and resource groups | https://learn.microsoft.com/en-us/azure/ |
| Azure pricing calculator — Official | Estimate resource costs | https://azure.microsoft.com/en-us/pricing/calculator/ |

### 11. Google Cloud — overview only
| Resource | What to learn | Link |
|---|---|---|
| Google Cloud training — Official | Courses, learning paths and labs | https://cloud.google.com/learn/training |
| Google Cloud documentation — Official | Compute Engine, Cloud Storage, IAM and VPC | https://cloud.google.com/docs |
| Google Cloud Skills Boost — Official | Guided cloud learning and labs; check access terms | https://www.cloudskillsboost.google/ |
| Google Cloud pricing calculator — Official | Estimate cloud costs | https://cloud.google.com/products/calculator |

---

## Phase 6 — Monitoring and databases (Weeks 23–25)

### 14. Monitoring: Prometheus and Grafana
| Resource | What to learn | Link |
|---|---|---|
| Prometheus first steps — Official | Install, configure, scrape metrics and query | https://prometheus.io/docs/introduction/first_steps/ |
| Prometheus getting started — Official | Targets, queries, graphs and rules | https://prometheus.io/docs/prometheus/latest/getting_started/ |
| PromQL basics — Official | Query language for metrics | https://prometheus.io/docs/prometheus/latest/querying/basics/ |
| Grafana learning hub — Official | Guided learning journeys and paths | https://grafana.com/docs/learning-hub/ |
| Grafana getting started — Official | Data sources and first dashboard | https://grafana.com/docs/grafana/latest/fundamentals/getting-started/ |

**Recommended order:** metrics concepts → run Prometheus locally → scrape a sample target → learn PromQL basics → connect Grafana → create panels → test one alert.

### 15. SQL and NoSQL
| Resource | What to learn | Link |
|---|---|---|
| PostgreSQL tutorial — Official | Tables, queries, joins, aggregates and transactions | https://www.postgresql.org/docs/current/tutorial.html |
| SQLBolt — Interactive practice | SQL lessons and exercises in the browser | https://sqlbolt.com/ |
| MongoDB manual — Official | Document database concepts and tutorials | https://www.mongodb.com/docs/manual/ |
| MongoDB University — Official learning | Self-paced MongoDB courses | https://learn.mongodb.com/ |
| Redis documentation — Official | Redis data structures and getting started | https://redis.io/docs/latest/ |
| Redis getting started — Official | First steps with Redis | https://redis.io/docs/latest/develop/get-started/ |

**Recommended order:** SELECT/WHERE → GROUP BY/aggregates → JOIN → indexes/transactions → MongoDB documents → Redis key/value and expiry. Use sample data and parameterized queries.

---

## Phase 7 — Proof of Work (Week 26+)

### 16. Projects
- GitHub Skills: https://skills.github.com/
- Docker guides and hands-on labs: https://docs.docker.com/guides/
- Kubernetes tutorials: https://kubernetes.io/docs/tutorials/
- HashiCorp Terraform tutorials: https://developer.hashicorp.com/terraform/tutorials
- Grafana learning hub: https://grafana.com/docs/learning-hub/

### 17. Interview preparation
- Linux command reference: https://www.gnu.org/software/coreutils/manual/coreutils.html
- Git reference book: https://git-scm.com/book/en/v2
- Kubernetes concepts: https://kubernetes.io/docs/concepts/
- Docker docs: https://docs.docker.com/
- AWS training: https://aws.amazon.com/training/

For every answer practise: **definition → why it matters → example → trade-off**. Do not memorize one-line answers only.

### 18. Cheat sheets
- Git reference: https://git-scm.com/docs
- Python library reference: https://docs.python.org/3/library/
- Bash manual: https://www.gnu.org/software/bash/manual/bash.html
- Docker CLI reference: https://docs.docker.com/reference/cli/docker/
- kubectl reference: https://kubernetes.io/docs/reference/kubectl/
- Terraform CLI: https://developer.hashicorp.com/terraform/cli
- Ansible documentation: https://docs.ansible.com/ansible/latest/

---

## Browser-based practice options
These are supplementary practice sites, not substitutes for official documentation. Review their current access limits and privacy terms before creating an account.

- AkOps Labs playground: https://akopslabs.com/playground — browser-based guided Linux, Git, Docker, CI/CD, Kubernetes and Terraform exercises.
- LabEx learning: https://labex.io/learn — hands-on Linux, Docker, Kubernetes, Git, Python and cloud practice; free access may be limited by plan.
- Killercoda: https://killercoda.com/ — browser-based interactive technical scenarios; availability varies by scenario.

## Resource quality and safety checklist
- Prefer the official documentation for exact commands, version behavior and security guidance.
- Check the page's version and publication/update date.
- Never run a command from a tutorial without understanding its effect.
- Use sample folders, local VMs and disposable clusters for experiments.
- Do not share credentials, API keys, SSH private keys or personal data with learning sites.
- Cloud accounts and labs may incur charges. Review pricing and permissions first, then verify cleanup.
- If a link moves, search the provider's official documentation by the exact product/topic rather than trusting a random download mirror.
