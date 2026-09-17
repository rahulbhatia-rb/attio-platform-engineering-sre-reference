# Platform SRE Reference — Attio application

A compact, testable reference for treating a platform as a product: explicit service objectives, error-budget policy, safe deployment gating, and an auditable infrastructure boundary. Prepared by Rahul H Bhatia for Attio’s Platform Engineer role. It is an independent portfolio project, not an Attio system or production deployment.

## Reviewer guide

| Attio theme | Evidence | Scope |
| --- | --- | --- |
| SLOs, error budgets and reliability culture | `app/slo.py` calculates availability/error-budget state with clear validation; `docs/reliability.md` defines operational use | Implemented logic, not a live telemetry integration |
| Fast, safe CI/CD | `app/release_gate.py` blocks release when reliability policy or artifact identity fails; CI exercises unit tests | A reference gate, not Attio’s pipeline |
| Incident response and post-mortems | `docs/reliability.md` provides triage and blameless learning-loop guidance | No real incident data or SLO values claimed |
| Terraform, Kubernetes and GCP | `terraform/platform.tf` declares a GCP project-input, log sink destination and workload service account pattern | GCP design adaptation; no claim of production GCP experience or deployed resources |
| Product mindset | Outputs explain the reason for a decision, not only pass/fail state | Example interface, not a complete platform product |

## Run

```bash
python -m unittest discover -s tests -v
terraform -chdir=terraform init
terraform -chdir=terraform validate
```

The test suite makes no cloud or model calls. CI does not apply Terraform. An actual implementation needs Attio-owned SLO targets, data sources, alert routing, IAM model, VPC/service design, Terraform state, policy review, capacity tests and staged rollout. Do not infer an Attio infrastructure design from these examples.

## Background alignment

Rahul’s hands-on background includes AWS/GCP-adjacent cloud platform work, Terraform/CloudFormation, Kubernetes/EKS, CI/CD/GitOps, observability, cost optimization and production incident ownership. The reference deliberately does not claim production GCP operations, Datadog/Splunk ownership, a specific number of years, or an Attio deployment.

## Contact

Rahul H Bhatia · +91 9884541449 · rahulbhatia1998@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
