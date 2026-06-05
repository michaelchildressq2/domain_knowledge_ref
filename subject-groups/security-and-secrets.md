# Security And Secrets

Pattern count: 17

## Cluster Per Environment

- `id`: `iac.cluster-per-environment`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-per-environment.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `environment-parity`, `high-availability`, `safe-change`
- `summary`: Use separate clusters when environment isolation, failure containment, or change independence outweighs shared-cluster efficiency.

## Copy Paste Environments

- `id`: `iac.copy-paste-environments`
- `type`: `anti-pattern`
- `source`: `patterns/copy-paste-environments.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `environment-parity`, `configuration-drift`, `stack-design`, `cloud-agnostic`
- `summary`: Duplicating stack source per environment creates short-term isolation but long-term drift and delivery overhead.

## Isolation Level Explicitness

- `id`: `data.isolation-level-explicitness`
- `type`: `decision-guide`
- `source`: `patterns/isolation-level-explicitness.md`
- `tags`: `data-systems`, `transactions`, `isolation-levels`, `consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Choose isolation levels by the anomalies the application can tolerate, not by database defaults or ACID labels.

## Offline Stack Testing

- `id`: `iac.offline-stack-testing`
- `type`: `delivery-pattern`
- `source`: `patterns/offline-stack-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `delivery-pipeline`, `policy-as-code`, `safe-change`, `cloud-agnostic`
- `summary`: Run static, syntactic, policy, and unit-like checks before applying stack changes to real infrastructure.

## Policy As Code Guardrails

- `id`: `iac.policy-as-code-guardrails`
- `type`: `governance-pattern`
- `source`: `patterns/policy-as-code-guardrails.md`
- `tags`: `infrastructure-as-code`, `policy-as-code`, `governance`, `security`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Encode repeatable governance, security, and compliance rules as automated checks in the infrastructure delivery flow.

## Repository Boundaries

- `id`: `iac.repository-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/repository-boundaries.md`
- `tags`: `infrastructure-as-code`, `version-control`, `modular-architecture`, `delivery-pipeline`, `governance`, `cloud-agnostic`
- `summary`: Choose infrastructure repository boundaries based on ownership, delivery cadence, dependency management, and change isolation.

## Reusable Stack

- `id`: `iac.reusable-stack`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-stack.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `environment-parity`, `parameterization`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use one stack code project with simple parameters to create consistent instances across environments or tenants.

## Sandbox IaC Testing

- `id`: `iac.sandbox-iac-testing`
- `type`: `testing-practice`
- `source`: `patterns/sandbox-iac-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `sandbox`, `isolation`, `cost-control`, `safe-change`
- `summary`: Test infrastructure changes in isolated disposable environments so validation can create, update, and destroy resources without harming production or shared systems.

## Secrets Out Of Source

- `id`: `iac.secrets-out-of-source`
- `type`: `governance-pattern`
- `source`: `patterns/secrets-out-of-source.md`
- `tags`: `infrastructure-as-code`, `secrets-management`, `security`, `governance`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Keep secret values out of source control while preserving coded references, access policy, and delivery flow.

## Server Image Pipeline

- `id`: `iac.server-image-pipeline`
- `type`: `delivery-pattern`
- `source`: `patterns/server-image-pipeline.md`
- `tags`: `infrastructure-as-code`, `server-images`, `delivery-pipeline`, `security`, `testing`, `cloud-agnostic`
- `summary`: Build, test, publish, and promote server images through automation before using them in infrastructure stacks.

## Shared Cluster Boundary

- `id`: `iac.shared-cluster-boundary`
- `type`: `decision-guide`
- `source`: `patterns/shared-cluster-boundary.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `governance`, `security`, `cost-management`, `design-review`
- `summary`: Share clusters only when isolation, ownership, capacity, and change-management boundaries are explicit and enforceable.

## Sidecar Application Augmentation

- `id`: `platform.sidecar-application-augmentation`
- `type`: `architecture-pattern`
- `source`: `patterns/sidecar-application-augmentation.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `operability`, `security`, `migration`, `implementation-planning`, `module-boundaries`, `parameterization`, `kubernetes`, `sidecar`
- `summary`: Add tightly coupled auxiliary behavior beside an application container when shared local resources let the helper improve the app without changing its code.

## Terraform Provider Topology

- `id`: `iac.terraform-provider-topology`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-provider-topology.md`
- `tags`: `infrastructure-as-code`, `terraform`, `providers`, `multi-account`, `multi-region`, `aliases`, `versioning`, `module-boundaries`
- `summary`: Model Terraform provider source, version, aliases, accounts, regions, and module injection explicitly so multi-provider infrastructure stays reviewable and least-privilege.

## Terraform Remote State Backend

- `id`: `iac.terraform-remote-state-backend`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-remote-state-backend.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `remote-state`, `locking`, `reproducibility`, `security`
- `summary`: Store Terraform state in a shared remote backend with locking, encryption, versioning, and tightly scoped access instead of treating local state or version control as team-safe storage.

## Terraform Secret State Minimization

- `id`: `iac.terraform-secret-state-minimization`
- `type`: `security-pattern`
- `source`: `patterns/terraform-secret-state-minimization.md`
- `tags`: `infrastructure-as-code`, `terraform`, `secrets-management`, `state-management`, `plan-files`, `oidc`, `security`
- `summary`: Keep secrets out of Terraform source while also minimizing secret exposure through variables, state, plan files, logs, provider credentials, and remote-state outputs.

## Terraform State Isolation Layout

- `id`: `iac.terraform-state-isolation-layout`
- `type`: `architecture-pattern`
- `source`: `patterns/terraform-state-isolation-layout.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `environments`, `blast-radius`, `file-layout`, `stack-design`
- `summary`: Split Terraform state by environment and component using explicit file layout and backend keys so failures, permissions, plans, and dependencies stay bounded.

## Timeout Retry Backoff

- `id`: `data.timeout-retry-backoff`
- `type`: `delivery-pattern`
- `source`: `patterns/timeout-retry-backoff.md`
- `tags`: `data-systems`, `distributed-systems`, `resilience`, `runtime-operations`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use timeouts, retries, backoff, and idempotency together so transient faults do not become overload or duplicate side effects.
