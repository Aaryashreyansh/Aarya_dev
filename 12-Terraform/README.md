# 12. Terraform
Topics: providers, resources, variables, outputs, modules, state, plans, drift and remote state.

Safe workflow in a configured practice project:
    terraform fmt
    terraform validate
    terraform plan

Inspect the plan before any apply operation. Exercises: explain declarative infrastructure, protect state, create variables/outputs and compare plan/apply/destroy.

Never commit state files or credentials.