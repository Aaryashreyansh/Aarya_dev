# Aarya DevOps Academy — Complete Course Guide

Welcome! This is the main table of contents for a structured, practical DevOps course. Follow the phases in order. Each phase document contains lesson sequences, concepts, lab work, checkpoints and a mini-project.

## How to study each lesson
1. **Read:** understand the concept and the reason it exists.
2. **Explain:** write the idea in your own words in a `notes.md` file.
3. **Demonstrate:** run the lab in your own device, local VM or disposable container.
4. **Inspect:** compare actual output with expected behavior; read errors instead of blindly copying commands.
5. **Practise:** complete the exercise without looking at the solution.
6. **Prove:** save a screenshot, test output, diagram or short explanation in your project README.
7. **Review:** revisit the topic after one day and one week.

## Learning rules
- Target roughly 70% hands-on work and 30% reading.
- Do not mark a lesson complete just because you read it. Complete its exercise and explain what happened.
- Use a local lab first. Cloud resources can cost money.
- Only access systems you own or have explicit permission to administer.
- Never put passwords, tokens, private keys, personal data or production secrets in Git.
- Prefer read-only commands while learning. Understand a command before using one that changes or deletes data.
- Use placeholders such as `YOUR_HOST`, never copy an example as if it were a real host or credential.

## Phase map
| Phase | Timeline | Main skills | Guide |
|---|---:|---|---|
| 1. Foundation | Weeks 1–4 | Linux, networking, Git | [Phase 1](PHASE-01-FOUNDATION.md) |
| 2. Scripting | Weeks 5–8 | Python, Bash, scheduling | [Phase 2](PHASE-02-SCRIPTING.md) |
| 3. Containers | Weeks 9–12 | Docker, Compose, Kubernetes | [Phase 3](PHASE-03-CONTAINERS.md) |
| 4. Automation | Weeks 13–16 | CI/CD, Terraform, Ansible | [Phase 4](PHASE-04-AUTOMATION.md) |
| 5. Cloud | Weeks 17–22 | AWS deep dive, Azure/GCP overview | [Phase 5](PHASE-05-CLOUD.md) |
| 6. Monitoring + data | Weeks 23–25 | Prometheus, Grafana, SQL/NoSQL | [Phase 6](PHASE-06-MONITORING-DATA.md) |
| 7. Proof of work | Week 26+ | Portfolio, interviews, capstone | [Phase 7](PHASE-07-PROOF-OF-WORK.md) |

## Lesson completion template
Copy this into the relevant folder as `lesson-notes.md`:
- Topic:
- Date:
- What I understood:
- Commands/code I tested:
- Expected result:
- Actual result:
- Error and how I investigated it:
- Security/cost considerations:
- Exercise completed:
- What I still need to practise:

## Suggested folder layout for each project
```text
project-name/
├── README.md
├── docs/
│   ├── architecture.md
│   └── troubleshooting.md
├── src/
├── tests/
├── screenshots/
└── .gitignore
```

## What counts as finished?
You can explain the concept without memorized wording, reproduce the lab from a clean environment, identify a common failure, show evidence, and clean up safely. The weekly calendar is a guide, not a deadline.
