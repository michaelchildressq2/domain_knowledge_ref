# Configuration And Contracts

Pattern count: 43

## Adapter Operability Normalization

- `id`: `platform.adapter-operability-normalization`
- `type`: `architecture-pattern`
- `source`: `patterns/adapter-operability-normalization.md`
- `tags`: `platform-engineering`, `sre`, `observability`, `operability`, `modular-architecture`, `runtime-operations`, `implementation-planning`, `module-boundaries`, `testing`, `kubernetes`, `adapter`
- `summary`: Use an adapter container to translate heterogeneous application interfaces into standard operational contracts for metrics, logs, health, or control planes.

## Ambassador Local Service Broker

- `id`: `platform.ambassador-local-service-broker`
- `type`: `architecture-pattern`
- `source`: `patterns/ambassador-local-service-broker.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `scalability`, `safe-change`, `migration`, `runtime-operations`, `module-boundaries`, `parameterization`, `kubernetes`, `service-discovery`, `ambassador`
- `summary`: Put service discovery, sharding, request splitting, or environment-specific brokering behind a local endpoint so application code can remain simple and portable.

## Apply On Change

- `id`: `iac.apply-on-change-antipattern`
- `type`: `anti-pattern`
- `source`: `patterns/apply-on-change-antipattern.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `configuration-drift`, `runtime-operations`, `safe-change`, `cloud-agnostic`
- `summary`: Applying configuration only for selected changes lets unmanaged drift accumulate and makes future changes unpredictable.

## Bounded Context Integrity

- `id`: `ddd.bounded-context-integrity`
- `type`: `architecture-pattern`
- `source`: `patterns/bounded-context-integrity.md`
- `tags`: `domain-driven-design`, `bounded-context`, `model-integrity`, `modular-architecture`, `module-boundaries`, `data-contracts`, `team-boundaries`, `integration`
- `summary`: Define where each model applies and keep that context internally consistent through language, ownership, integration, and tests.

## Compatible Schema Evolution

- `id`: `data.compatible-schema-evolution`
- `type`: `delivery-pattern`
- `source`: `patterns/compatible-schema-evolution.md`
- `tags`: `data-systems`, `schema-evolution`, `compatibility`, `delivery-pipeline`, `safe-change`, `cloud-agnostic`
- `summary`: Evolve encoded data with backward and forward compatibility so old and new code can coexist.

## Consensus For Coordination

- `id`: `data.consensus-for-coordination`
- `type`: `architecture-pattern`
- `source`: `patterns/consensus-for-coordination.md`
- `tags`: `data-systems`, `consensus`, `coordination`, `distributed-systems`, `reliability`, `cloud-agnostic`
- `summary`: Use consensus-backed coordination for leader election, membership, locks, and configuration that require agreement despite failures.

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

## Declarative Query Boundaries

- `id`: `data.declarative-query-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/declarative-query-boundaries.md`
- `tags`: `data-systems`, `query-languages`, `maintainability`, `modular-architecture`, `implementation-planning`, `cloud-agnostic`
- `summary`: Prefer declarative query interfaces when callers should state what data they need without encoding execution strategy.

## Define Everything As Code

- `id`: `iac.define-everything-as-code`
- `type`: `delivery-pattern`
- `source`: `patterns/define-everything-as-code.md`
- `tags`: `infrastructure-as-code`, `version-control`, `reproducibility`, `governance`, `implementation-planning`, `cloud-agnostic`
- `summary`: Define infrastructure, configuration, policies, and operational workflows as versioned code where they affect repeatability or change safety.

## Document Model Locality

- `id`: `data.document-model-locality`
- `type`: `architecture-pattern`
- `source`: `patterns/document-model-locality.md`
- `tags`: `data-systems`, `data-modeling`, `document-database`, `query-patterns`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use document storage when related data is usually read and written together as one aggregate.

## Evolvable Data Systems

- `id`: `data.evolvable-data-systems`
- `type`: `architecture-pattern`
- `source`: `patterns/evolvable-data-systems.md`
- `tags`: `data-systems`, `maintainability`, `schema-evolution`, `modular-architecture`, `refactoring`, `cloud-agnostic`
- `summary`: Favor data models, schemas, interfaces, and processing boundaries that can change without coordinated rewrites.

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

## Graph Relationship Modeling

- `id`: `data.graph-relationship-modeling`
- `type`: `architecture-pattern`
- `source`: `patterns/graph-relationship-modeling.md`
- `tags`: `data-systems`, `data-modeling`, `graph-database`, `query-patterns`, `design-review`, `cloud-agnostic`
- `summary`: Use graph modeling when relationships between entities are central, variable, and queried across multiple hops.

## Integration Registry Lookup

- `id`: `iac.integration-registry-lookup`
- `type`: `architecture-pattern`
- `source`: `patterns/integration-registry-lookup.md`
- `tags`: `infrastructure-as-code`, `configuration-management`, `registry`, `module-boundaries`, `platform-engineering`, `cloud-agnostic`
- `summary`: Use a general-purpose registry for cross-stack or cross-team integration values when stack-tool-specific coupling is too narrow.

## Message Passing Contracts

- `id`: `data.message-passing-contracts`
- `type`: `architecture-pattern`
- `source`: `patterns/message-passing-contracts.md`
- `tags`: `data-systems`, `messaging`, `schema-evolution`, `event-driven`, `implementation-planning`, `cloud-agnostic`
- `summary`: Design asynchronous messages as durable contracts with explicit schemas, idempotency, ordering assumptions, and compatibility rules.

## Minimize Variation

- `id`: `iac.minimize-variation`
- `type`: `architecture-pattern`
- `source`: `patterns/minimize-variation.md`
- `tags`: `infrastructure-as-code`, `environment-parity`, `configuration-management`, `drift-prevention`, `operability`, `cloud-agnostic`
- `summary`: Keep instances that serve the same purpose as similar as possible to reduce drift, testing burden, and operational surprise.

## Package Infrastructure Code

- `id`: `iac.package-infrastructure-code`
- `type`: `delivery-pattern`
- `source`: `patterns/package-infrastructure-code.md`
- `tags`: `infrastructure-as-code`, `delivery-pipeline`, `version-control`, `reproducibility`, `safe-change`, `cloud-agnostic`
- `summary`: Package or otherwise pin infrastructure code versions so pipelines apply the intended artifact consistently across environments.

## Polyglot Persistence Fit

- `id`: `data.polyglot-persistence-fit`
- `type`: `decision-guide`
- `source`: `patterns/polyglot-persistence-fit.md`
- `tags`: `data-systems`, `data-modeling`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage and query models based on access patterns, relationships, consistency needs, and evolution costs.

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

## Rollback Roll Forward Decision

- `id`: `iac.rollback-rollforward-decision`
- `type`: `decision-guide`
- `source`: `patterns/rollback-rollforward-decision.md`
- `tags`: `infrastructure-as-code`, `rollback`, `roll-forward`, `safe-change`, `incident-response`, `cloud-agnostic`
- `summary`: Decide whether to restore a previous version or move forward with a fix based on state, compatibility, and recovery speed.

## Safe Infrastructure Change

- `id`: `iac.safe-infrastructure-change`
- `type`: `decision-guide`
- `source`: `patterns/safe-infrastructure-change.md`
- `tags`: `infrastructure-as-code`, `safe-change`, `rollback`, `disaster-recovery`, `design-review`, `cloud-agnostic`
- `summary`: Choose a change strategy based on reversibility, blast radius, data risk, compatibility, and observability.

## Schema Registry Contracts

- `id`: `data.schema-registry-contracts`
- `type`: `governance-pattern`
- `source`: `patterns/schema-registry-contracts.md`
- `tags`: `data-systems`, `schema-evolution`, `governance`, `data-contracts`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Use a registry or equivalent governance point to validate shared data schemas and compatibility before producers publish changes.

## Secrets Out Of Source

- `id`: `iac.secrets-out-of-source`
- `type`: `governance-pattern`
- `source`: `patterns/secrets-out-of-source.md`
- `tags`: `infrastructure-as-code`, `secrets-management`, `security`, `governance`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Keep secret values out of source control while preserving coded references, access policy, and delivery flow.

## Server Lifecycle As Code

- `id`: `iac.server-lifecycle-as-code`
- `type`: `architecture-pattern`
- `source`: `patterns/server-lifecycle-as-code.md`
- `tags`: `infrastructure-as-code`, `server-images`, `configuration-management`, `runtime-operations`, `reproducibility`, `cloud-agnostic`
- `summary`: Manage server build, configure, update, and retire phases as explicit coded lifecycle transitions.

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

## Snowflake System

- `id`: `iac.snowflake-system`
- `type`: `anti-pattern`
- `source`: `patterns/snowflake-system.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `configuration-drift`, `reproducibility`, `runtime-operations`, `cloud-agnostic`
- `summary`: A snowflake system is manually unique, hard to reproduce, and risky to change or recover.

## Specification Business Rules

- `id`: `ddd.specification-business-rules`
- `type`: `architecture-pattern`
- `source`: `patterns/specification-business-rules.md`
- `tags`: `domain-driven-design`, `business-rules`, `specifications`, `query-patterns`, `domain-modeling`, `declarative-design`
- `summary`: Represent important predicates and selection rules as named, composable domain concepts instead of scattering conditionals.

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

## Storage Engine Fit

- `id`: `data.storage-engine-fit`
- `type`: `decision-guide`
- `source`: `patterns/storage-engine-fit.md`
- `tags`: `data-systems`, `storage-engine`, `database`, `performance`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage engines by write/read mix, update pattern, range-query needs, and compaction behavior.

## Supple Domain Design

- `id`: `ddd.supple-domain-design`
- `type`: `architecture-pattern`
- `source`: `patterns/supple-domain-design.md`
- `tags`: `domain-driven-design`, `software-design`, `code-readability`, `refactoring`, `testability`, `design-review`
- `summary`: Shape important domain code so intention, effects, assertions, and conceptual boundaries are obvious to client developers and maintainers.

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

## Terraform Remote State Backend

- `id`: `iac.terraform-remote-state-backend`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-remote-state-backend.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `remote-state`, `locking`, `reproducibility`, `security`
- `summary`: Store Terraform state in a shared remote backend with locking, encryption, versioning, and tightly scoped access instead of treating local state or version control as team-safe storage.

## Terraform Team Delivery Workflow

- `id`: `iac.terraform-team-delivery-workflow`
- `type`: `delivery-pattern`
- `source`: `patterns/terraform-team-delivery-workflow.md`
- `tags`: `infrastructure-as-code`, `terraform`, `team-workflow`, `ci-cd`, `code-review`, `adoption`, `delivery-pipeline`, `governance`
- `summary`: Make Terraform a team workflow with incremental adoption, version control, review, automated checks, controlled applies, and promotion paths for infrastructure changes.

## Version Controlled Infrastructure

- `id`: `iac.version-controlled-infrastructure`
- `type`: `delivery-pattern`
- `source`: `patterns/version-controlled-infrastructure.md`
- `tags`: `infrastructure-as-code`, `version-control`, `delivery-pipeline`, `governance`, `safe-change`, `cloud-agnostic`
- `summary`: Store infrastructure code in version control to make changes traceable, reviewable, recoverable, and deliverable through pipelines.
