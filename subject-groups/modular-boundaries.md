# Modular Boundaries

Pattern count: 53

## Adapter Operability Normalization

- `id`: `platform.adapter-operability-normalization`
- `type`: `architecture-pattern`
- `source`: `patterns/adapter-operability-normalization.md`
- `tags`: `platform-engineering`, `sre`, `observability`, `operability`, `modular-architecture`, `runtime-operations`, `implementation-planning`, `module-boundaries`, `testing`, `kubernetes`, `adapter`
- `summary`: Use an adapter container to translate heterogeneous application interfaces into standard operational contracts for metrics, logs, health, or control planes.

## Aggregate Lifecycle Boundary

- `id`: `ddd.aggregate-lifecycle-boundary`
- `type`: `architecture-pattern`
- `source`: `patterns/aggregate-lifecycle-boundary.md`
- `tags`: `domain-driven-design`, `aggregates`, `consistency`, `transactions`, `data-modeling`, `lifecycle-management`
- `summary`: Use aggregate roots to define consistency, reference, transaction, creation, retrieval, and deletion boundaries for domain objects.

## Ambassador Local Service Broker

- `id`: `platform.ambassador-local-service-broker`
- `type`: `architecture-pattern`
- `source`: `patterns/ambassador-local-service-broker.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `scalability`, `safe-change`, `migration`, `runtime-operations`, `module-boundaries`, `parameterization`, `kubernetes`, `service-discovery`, `ambassador`
- `summary`: Put service discovery, sharding, request splitting, or environment-specific brokering behind a local endpoint so application code can remain simple and portable.

## Ansible Collection Dependency Manifest

- `id`: `iac.ansible-collection-dependency-manifest`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-collection-dependency-manifest.md`
- `tags`: `infrastructure-as-code`, `ansible`, `collections`, `dependency-management`, `versioning`, `modules`, `packaging`
- `summary`: Use Ansible collections and dependency manifests to package modules, roles, plugins, and playbooks as versioned content with explicit fully qualified dependencies.

## Ansible Custom Module Boundary

- `id`: `iac.ansible-custom-module-boundary`
- `type`: `design-pattern`
- `source`: `patterns/ansible-custom-module-boundary.md`
- `tags`: `infrastructure-as-code`, `ansible`, `modules`, `extensibility`, `idempotency`, `testing`, `api-integration`
- `summary`: Create a custom Ansible module when desired-state behavior, validation, check mode, and change reporting are too important or complex for shell tasks or roles.

## Ansible Molecule Role Quality Gate

- `id`: `iac.ansible-molecule-role-quality-gate`
- `type`: `testing-practice`
- `source`: `patterns/ansible-molecule-role-quality-gate.md`
- `tags`: `infrastructure-as-code`, `ansible`, `molecule`, `testing`, `ci-cd`, `linting`, `roles`
- `summary`: Use Molecule scenarios, linters, dependency installation, convergence, cleanup, and verifiers as the standard quality gate for reusable Ansible roles.

## Ansible Playbook Convergence

- `id`: `iac.ansible-playbook-convergence`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-playbook-convergence.md`
- `tags`: `infrastructure-as-code`, `ansible`, `idempotency`, `desired-state`, `configuration-management`, `drift-prevention`, `operability`
- `summary`: Write Ansible playbooks as readable desired-state workflows that can be re-run safely, report real changes, and avoid unnecessary imperative shell logic.

## Ansible Role Capability Boundary

- `id`: `iac.ansible-role-capability-boundary`
- `type`: `design-pattern`
- `source`: `patterns/ansible-role-capability-boundary.md`
- `tags`: `infrastructure-as-code`, `ansible`, `roles`, `module-boundaries`, `composability`, `versioning`, `testing`
- `summary`: Design Ansible roles as small, documented, versioned capabilities with clear defaults, dependencies, handlers, and test scenarios.

## Ansible Vault Secret Boundary

- `id`: `iac.ansible-vault-secret-boundary`
- `type`: `security-pattern`
- `source`: `patterns/ansible-vault-secret-boundary.md`
- `tags`: `infrastructure-as-code`, `ansible`, `secrets-management`, `ansible-vault`, `least-privilege`, `configuration-management`, `security`
- `summary`: Keep Ansible secrets separate from ordinary inventory and encrypt or externally source them so credentials stay reviewable, scoped, and usable in automation.

## Anti-Corruption Layer

- `id`: `ddd.anti-corruption-layer`
- `type`: `architecture-pattern`
- `source`: `patterns/anti-corruption-layer.md`
- `tags`: `domain-driven-design`, `anti-corruption-layer`, `integration`, `legacy-modernization`, `bounded-context`, `modular-architecture`
- `summary`: Protect a clean domain model from external or legacy models by translating at an explicit boundary.

## Bounded Context Integrity

- `id`: `ddd.bounded-context-integrity`
- `type`: `architecture-pattern`
- `source`: `patterns/bounded-context-integrity.md`
- `tags`: `domain-driven-design`, `bounded-context`, `model-integrity`, `modular-architecture`, `module-boundaries`, `data-contracts`, `team-boundaries`, `integration`
- `summary`: Define where each model applies and keep that context internally consistent through language, ownership, integration, and tests.

## Cluster As Code

- `id`: `iac.cluster-as-code`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-as-code.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `cluster-management`, `platform-engineering`, `implementation-planning`
- `summary`: Define application clusters and their supporting services as code, including the platform dependencies around the cluster itself.

## Cluster Per Environment

- `id`: `iac.cluster-per-environment`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-per-environment.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `environment-parity`, `high-availability`, `safe-change`
- `summary`: Use separate clusters when environment isolation, failure containment, or change independence outweighs shared-cluster efficiency.

## Component Boundaries

- `id`: `iac.component-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/component-boundaries.md`
- `tags`: `infrastructure-as-code`, `modular-architecture`, `module-boundaries`, `safe-change`, `design-review`, `cloud-agnostic`
- `summary`: Split infrastructure into components with low coupling, high cohesion, and clear responsibility for change.

## Component Testability

- `id`: `iac.component-testability`
- `type`: `architecture-pattern`
- `source`: `patterns/component-testability.md`
- `tags`: `infrastructure-as-code`, `testing`, `module-boundaries`, `modular-architecture`, `implementation-planning`, `cloud-agnostic`
- `summary`: Design infrastructure components small enough and explicit enough to test quickly and meaningfully.

## Container Contracts for Reuse

- `id`: `platform.container-contracts-for-reuse`
- `type`: `architecture-pattern`
- `source`: `patterns/container-contracts-for-reuse.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `operability`, `design-review`, `implementation-planning`, `module-boundaries`, `parameterization`, `version-control`, `kubernetes`, `container-contracts`
- `summary`: Treat reusable containers as callable components with explicit parameters, stable APIs, documented behavior, and compatibility checks.

## Copy Paste Environments

- `id`: `iac.copy-paste-environments`
- `type`: `anti-pattern`
- `source`: `patterns/copy-paste-environments.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `environment-parity`, `configuration-drift`, `stack-design`, `cloud-agnostic`
- `summary`: Duplicating stack source per environment creates short-term isolation but long-term drift and delivery overhead.

## Core Domain Distillation

- `id`: `ddd.core-domain-distillation`
- `type`: `decision-guide`
- `source`: `patterns/core-domain-distillation.md`
- `tags`: `domain-driven-design`, `core-domain`, `subdomains`, `prioritization`, `architecture-strategy`, `module-boundaries`, `maintainability`, `design-review`
- `summary`: Concentrate design talent and model clarity on the parts of the domain that create strategic advantage.

## Correctness Before Preservation

- `id`: `data.correctness-before-preservation`
- `type`: `decision-guide`
- `source`: `patterns/correctness-before-preservation.md`
- `tags`: `data-systems`, `correctness`, `maintainability`, `governance`, `design-review`, `cloud-agnostic`
- `summary`: Optimize data-system design for useful, correct outcomes rather than preserving existing mechanisms or local component uptime.

## Declarative Query Boundaries

- `id`: `data.declarative-query-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/declarative-query-boundaries.md`
- `tags`: `data-systems`, `query-languages`, `maintainability`, `modular-architecture`, `implementation-planning`, `cloud-agnostic`
- `summary`: Prefer declarative query interfaces when callers should state what data they need without encoding execution strategy.

## Event Driven Function Boundaries

- `id`: `platform.event-driven-function-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/event-driven-function-boundaries.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `operability`, `scalability`, `cost-management`, `design-review`, `implementation-planning`, `module-boundaries`, `testing`, `faas`, `event-driven`
- `summary`: Use FaaS for small stateless request transformations, asynchronous event handlers, and pipelines only when observability, cost, and state constraints fit.

## Eventual Consistency Boundaries

- `id`: `data.eventual-consistency-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/eventual-consistency-boundaries.md`
- `tags`: `data-systems`, `eventual-consistency`, `consistency`, `distributed-systems`, `design-review`, `cloud-agnostic`
- `summary`: Use eventual consistency only where product semantics, repair mechanisms, and user expectations can tolerate temporary divergence.

## Externalized Configuration

- `id`: `iac.externalized-configuration`
- `type`: `architecture-pattern`
- `source`: `patterns/externalized-configuration.md`
- `tags`: `infrastructure-as-code`, `configuration-management`, `parameterization`, `environment-parity`, `cloud-agnostic`
- `summary`: Separate reusable code from environment-specific values so the same code can safely create multiple stack instances.

## Facade Module

- `id`: `iac.facade-module`
- `type`: `architecture-pattern`
- `source`: `patterns/facade-module.md`
- `tags`: `infrastructure-as-code`, `module-boundaries`, `modular-architecture`, `terraform`, `implementation-planning`
- `summary`: Use a facade module to hide repetitive low-level resource details behind a simpler domain-specific interface.

## Integration Registry Lookup

- `id`: `iac.integration-registry-lookup`
- `type`: `architecture-pattern`
- `source`: `patterns/integration-registry-lookup.md`
- `tags`: `infrastructure-as-code`, `configuration-management`, `registry`, `module-boundaries`, `platform-engineering`, `cloud-agnostic`
- `summary`: Use a general-purpose registry for cross-stack or cross-team integration values when stack-tool-specific coupling is too narrow.

## Lease Based Ownership Election

- `id`: `platform.lease-based-ownership-election`
- `type`: `architecture-pattern`
- `source`: `patterns/lease-based-ownership-election.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `data-consistency`, `operability`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `kubernetes`, `leader-election`
- `summary`: Elect one active owner among replicas with consensus-backed compare-and-swap, renewable leases, and fencing checks before protected actions.

## Model Driven Design

- `id`: `ddd.model-driven-design`
- `type`: `architecture-pattern`
- `source`: `patterns/model-driven-design.md`
- `tags`: `domain-driven-design`, `domain-modeling`, `software-design`, `implementation-planning`, `module-boundaries`, `maintainability`, `refactoring`, `design-review`
- `summary`: Keep the core design and implementation closely mapped to the domain model so analysis and code evolve together.

## Monolithic Stack

- `id`: `iac.monolithic-stack`
- `type`: `anti-pattern`
- `source`: `patterns/monolithic-stack.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `stack-design`, `modular-architecture`, `safe-change`, `cloud-agnostic`
- `summary`: A monolithic stack manages too many unrelated resources, making changes slow, risky, and hard to test independently.

## Multiheaded Stack

- `id`: `iac.multiheaded-stack`
- `type`: `anti-pattern`
- `source`: `patterns/multiheaded-stack.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `stack-design`, `environment-parity`, `safe-change`, `cloud-agnostic`
- `summary`: A multiheaded stack uses one code project to manage unrelated environments or components with complex branches and high blast radius.

## Offline Stack Testing

- `id`: `iac.offline-stack-testing`
- `type`: `delivery-pattern`
- `source`: `patterns/offline-stack-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `delivery-pipeline`, `policy-as-code`, `safe-change`, `cloud-agnostic`
- `summary`: Run static, syntactic, policy, and unit-like checks before applying stack changes to real infrastructure.

## Partial Failure Design

- `id`: `data.partial-failure-design`
- `type`: `architecture-pattern`
- `source`: `patterns/partial-failure-design.md`
- `tags`: `data-systems`, `distributed-systems`, `reliability`, `failure-modes`, `design-review`, `cloud-agnostic`
- `summary`: Design distributed systems assuming some components can be slow, unreachable, or mistaken while others continue running.

## Replicated Stateless Serving

- `id`: `platform.replicated-stateless-serving`
- `type`: `architecture-pattern`
- `source`: `patterns/replicated-stateless-serving.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `scalability`, `zero-downtime`, `design-review`, `runtime-operations`, `rollback`, `testing`, `kubernetes`, `load-balancing`
- `summary`: Run multiple interchangeable service replicas behind a load balancer with readiness checks, rollout controls, and optional replicated edge layers.

## Repository Boundaries

- `id`: `iac.repository-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/repository-boundaries.md`
- `tags`: `infrastructure-as-code`, `version-control`, `modular-architecture`, `delivery-pipeline`, `governance`, `cloud-agnostic`
- `summary`: Choose infrastructure repository boundaries based on ownership, delivery cadence, dependency management, and change isolation.

## Resource Matching

- `id`: `iac.resource-matching`
- `type`: `architecture-pattern`
- `source`: `patterns/resource-matching.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `configuration-management`, `module-boundaries`, `cloud-agnostic`
- `summary`: Discover dependency resources by matching supported names or tags when loose coupling is more useful than direct stack outputs.

## Reusable Stack

- `id`: `iac.reusable-stack`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-stack.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `environment-parity`, `parameterization`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use one stack code project with simple parameters to create consistent instances across environments or tenants.

## Reusable Work Queue Interface

- `id`: `platform.reusable-work-queue-interface`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-work-queue-interface.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `operability`, `modular-architecture`, `implementation-planning`, `runtime-operations`, `module-boundaries`, `idempotency`, `kubernetes`, `work-queue`
- `summary`: Build batch work queues from a generic queue manager, a versioned source interface, and worker containers launched by the orchestrator.

## Scatter Gather Request Parallelism

- `id`: `platform.scatter-gather-request-parallelism`
- `type`: `architecture-pattern`
- `source`: `patterns/scatter-gather-request-parallelism.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `performance`, `design-review`, `runtime-operations`, `testing`, `kubernetes`, `scatter-gather`
- `summary`: Parallelize one request across many workers only when partial results can be merged and tail-latency, straggler, and availability costs are explicitly controlled.

## Separate Declarative And Imperative Concerns

- `id`: `iac.declarative-imperative-separation`
- `type`: `architecture-pattern`
- `source`: `patterns/declarative-imperative-separation.md`
- `tags`: `infrastructure-as-code`, `modular-architecture`, `declarative`, `imperative`, `testing`, `cloud-agnostic`
- `summary`: Use declarative code for desired resource state and imperative code for procedural workflows, rather than mixing both in one tangled abstraction.

## Server Image Pipeline

- `id`: `iac.server-image-pipeline`
- `type`: `delivery-pattern`
- `source`: `patterns/server-image-pipeline.md`
- `tags`: `infrastructure-as-code`, `server-images`, `delivery-pipeline`, `security`, `testing`, `cloud-agnostic`
- `summary`: Build, test, publish, and promote server images through automation before using them in infrastructure stacks.

## Service Stack

- `id`: `iac.service-stack`
- `type`: `architecture-pattern`
- `source`: `patterns/service-stack.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `module-boundaries`, `delivery-pipeline`, `safe-change`, `cloud-agnostic`
- `summary`: Group infrastructure around a service or independently delivered capability when that boundary matches ownership and change cadence.

## Sharded Service Routing

- `id`: `platform.sharded-service-routing`
- `type`: `architecture-pattern`
- `source`: `patterns/sharded-service-routing.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `data-consistency`, `design-review`, `runtime-operations`, `module-boundaries`, `testing`, `kubernetes`, `sharding`
- `summary`: Split stateful serving across shards with deterministic routing, careful shard-key design, consistent hashing, and targeted replication for hot or critical shards.

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

## Simple Stack Parameters

- `id`: `iac.simple-stack-parameters`
- `type`: `architecture-pattern`
- `source`: `patterns/simple-stack-parameters.md`
- `tags`: `infrastructure-as-code`, `parameterization`, `configuration-management`, `stack-design`, `implementation-planning`, `cloud-agnostic`
- `summary`: Keep stack parameters simple, explicit, and limited to values that should vary across instances.

## Spaghetti Module

- `id`: `iac.spaghetti-module`
- `type`: `anti-pattern`
- `source`: `patterns/spaghetti-module.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `module-boundaries`, `modular-architecture`, `testing`, `cloud-agnostic`
- `summary`: A spaghetti module has too many modes, branches, and responsibilities to be safely reused or tested.

## Stack Data Lookup

- `id`: `iac.stack-data-lookup`
- `type`: `architecture-pattern`
- `source`: `patterns/stack-data-lookup.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `module-boundaries`, `configuration-management`, `implementation-planning`, `cloud-agnostic`
- `summary`: Let consumer stacks read provider outputs through the stack tool when stacks need explicit infrastructure dependencies.

## Stack Parameter Registry

- `id`: `iac.stack-parameter-registry`
- `type`: `architecture-pattern`
- `source`: `patterns/stack-parameter-registry.md`
- `tags`: `infrastructure-as-code`, `configuration-management`, `parameterization`, `registry`, `environment-parity`, `cloud-agnostic`
- `summary`: Use a registry for shared stack parameters when direct manual inputs become fragile or duplicated.

## Terraform Module Contract

- `id`: `iac.terraform-module-contract`
- `type`: `design-pattern`
- `source`: `patterns/terraform-module-contract.md`
- `tags`: `infrastructure-as-code`, `terraform`, `modules`, `reuse`, `contracts`, `inputs`, `outputs`, `versioning`
- `summary`: Design Terraform modules as explicit contracts with inputs, outputs, provider expectations, path-safe internals, and versioned consumption rather than copied environment code.

## Terraform Production Module Design

- `id`: `iac.terraform-production-module-design`
- `type`: `design-pattern`
- `source`: `patterns/terraform-production-module-design.md`
- `tags`: `infrastructure-as-code`, `terraform`, `modules`, `production-readiness`, `composability`, `testing`, `versioning`, `platform-engineering`
- `summary`: Build production Terraform modules as small, composable, testable, and versioned units backed by explicit production-readiness checks.

## Terraform Provider Topology

- `id`: `iac.terraform-provider-topology`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-provider-topology.md`
- `tags`: `infrastructure-as-code`, `terraform`, `providers`, `multi-account`, `multi-region`, `aliases`, `versioning`, `module-boundaries`
- `summary`: Model Terraform provider source, version, aliases, accounts, regions, and module injection explicitly so multi-provider infrastructure stays reviewable and least-privilege.

## Terraform State Isolation Layout

- `id`: `iac.terraform-state-isolation-layout`
- `type`: `architecture-pattern`
- `source`: `patterns/terraform-state-isolation-layout.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `environments`, `blast-radius`, `file-layout`, `stack-design`
- `summary`: Split Terraform state by environment and component using explicit file layout and backend keys so failures, permissions, plans, and dependencies stay bounded.

## Transaction Boundary Fit

- `id`: `data.transaction-boundary-fit`
- `type`: `decision-guide`
- `source`: `patterns/transaction-boundary-fit.md`
- `tags`: `data-systems`, `transactions`, `consistency`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Use transactions where they simplify correctness, but keep boundaries aligned with invariants and operational cost.

## Version Controlled Infrastructure

- `id`: `iac.version-controlled-infrastructure`
- `type`: `delivery-pattern`
- `source`: `patterns/version-controlled-infrastructure.md`
- `tags`: `infrastructure-as-code`, `version-control`, `delivery-pipeline`, `governance`, `safe-change`, `cloud-agnostic`
- `summary`: Store infrastructure code in version control to make changes traceable, reviewable, recoverable, and deliverable through pipelines.
