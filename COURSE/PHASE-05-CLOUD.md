# Phase 5 — Cloud (Weeks 17–22)

**Outcome:** understand cloud resource models and complete one carefully cost-controlled AWS lab. Learn Azure and GCP at overview level first.

## Weeks 17–18 — AWS foundations and account safety
Learn Regions, Availability Zones, shared responsibility, IAM users/roles/policies, least privilege, MFA, billing dashboards, budgets and alerts. Account creation and billing settings must be handled with the account owner's permission. Free Tier eligibility, quotas and prices change; alerts are not necessarily hard spending caps.

## Week 19 — Compute and storage
Learn EC2 instances, AMIs, instance families at a high level, key-pair concepts, security groups, EBS volumes and S3 buckets/objects. Understand that stopping an instance may not stop every charge; storage, addresses, snapshots and other resources may still cost money.

## Week 20 — Networking and databases
Learn VPC, subnet, route table, internet gateway, NAT concept, security group vs network ACL, public/private placement, RDS managed database concept and backup responsibility. Draw a network diagram before creating resources.

## Week 21 — AWS operations and app deployment
Understand secure access, patching, logs, monitoring, backups and how an application is exposed. Use a small demo app, minimal permissions and a short-lived lab. Never expose admin ports to the whole internet. Prefer managed secure access methods and remove temporary access after the lab.

## Week 22 — Terraform cloud lab and teardown
Plan a small lab with the account owner: create only the minimum required resources, inspect Terraform plan, deploy a demo, verify it, then destroy the lab. Check the cloud console and billing/resource inventory for leftovers such as disks, snapshots, IP addresses, load balancers and buckets.

## Azure overview
Learn tenant, subscription, resource group, region, virtual network, VM, storage account, identity and Azure Monitor. Compare these concepts with AWS rather than trying to master both clouds simultaneously.

## GCP overview
Learn organization/folder/project, IAM, region/zone, VPC, Compute Engine, Cloud Storage and Cloud Logging. Compare project organization and permissions with AWS/Azure.

## Mini project
Document an architecture for a small app on AWS, estimate costs using current official pricing, provision only with explicit account-owner approval, deploy, verify, destroy and verify cleanup.

## Exit checklist
- [ ] IAM least privilege and billing controls are understood.
- [ ] EC2, S3, VPC and RDS purposes can be explained.
- [ ] Azure and GCP core resource models can be compared.
- [ ] Lab teardown is verified, not merely assumed.


## Where to learn this phase
See [Resources Directory](RESOURCES.md): AWS → AWS Training and official service docs; Azure → Microsoft Learn; GCP → Google Cloud training. Use pricing calculators before labs and confirm account-owner permission. Training pages may include optional paid labs.
