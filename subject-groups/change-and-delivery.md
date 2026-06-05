# Change And Delivery

Pattern count: 79

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

## Ansible Collection Dependency Manifest

- `id`: `iac.ansible-collection-dependency-manifest`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-collection-dependency-manifest.md`
- `tags`: `infrastructure-as-code`, `ansible`, `collections`, `dependency-management`, `versioning`, `modules`, `packaging`
- `summary`: Use Ansible collections and dependency manifests to package modules, roles, plugins, and playbooks as versioned content with explicit fully qualified dependencies.

## Ansible Control Node Dependency Isolation

- `id`: `iac.ansible-control-node-dependency-isolation`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-control-node-dependency-isolation.md`
- `tags`: `infrastructure-as-code`, `ansible`, `dependency-management`, `reproducibility`, `python`, `ci-cd`, `platform-engineering`
- `summary`: Isolate Ansible, Python, collection, and control-node dependencies per project so playbook behavior is reproducible across contributors and automation runners.

## Ansible Custom Module Boundary

- `id`: `iac.ansible-custom-module-boundary`
- `type`: `design-pattern`
- `source`: `patterns/ansible-custom-module-boundary.md`
- `tags`: `infrastructure-as-code`, `ansible`, `modules`, `extensibility`, `idempotency`, `testing`, `api-integration`
- `summary`: Create a custom Ansible module when desired-state behavior, validation, check mode, and change reporting are too important or complex for shell tasks or roles.

## Ansible Debugging Feedback Loop

- `id`: `iac.ansible-debugging-feedback-loop`
- `type`: `operational-practice`
- `source`: `patterns/ansible-debugging-feedback-loop.md`
- `tags`: `infrastructure-as-code`, `ansible`, `debugging`, `observability`, `runtime-operations`, `testing`, `feedback-loop`
- `summary`: Diagnose Ansible failures by narrowing the failing assumption with inventory inspection, verbosity, check mode, tags, debug output, and direct remote verification.

## Ansible Image Build Handoff

- `id`: `iac.ansible-image-build-handoff`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-image-build-handoff.md`
- `tags`: `infrastructure-as-code`, `ansible`, `image-building`, `packer`, `immutable-infrastructure`, `delivery-pipeline`, `reproducibility`
- `summary`: Use Ansible inside image-building workflows to configure base images once, then hand runtime variation to inventory, variables, and deployment automation.

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

## Ansible Progressive Orchestration

- `id`: `iac.ansible-progressive-orchestration`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-progressive-orchestration.md`
- `tags`: `infrastructure-as-code`, `ansible`, `orchestration`, `progressive-delivery`, `runtime-operations`, `high-availability`, `delivery-pipeline`
- `summary`: Use host patterns, serial batches, delegation, tags, blocks, and handlers to make multi-host Ansible changes staged, inspectable, and recoverable.

## Ansible Role Capability Boundary

- `id`: `iac.ansible-role-capability-boundary`
- `type`: `design-pattern`
- `source`: `patterns/ansible-role-capability-boundary.md`
- `tags`: `infrastructure-as-code`, `ansible`, `roles`, `module-boundaries`, `composability`, `versioning`, `testing`
- `summary`: Design Ansible roles as small, documented, versioned capabilities with clear defaults, dependencies, handlers, and test scenarios.

## Apply Code Continuously

- `id`: `iac.apply-code-continuously`
- `type`: `delivery-pattern`
- `source`: `patterns/apply-code-continuously.md`
- `tags`: `infrastructure-as-code`, `drift-prevention`, `idempotency`, `runtime-operations`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Reapply infrastructure code regularly or on change to keep managed systems aligned with declared intent.

## Apply From The Start

- `id`: `iac.apply-from-start`
- `type`: `delivery-pattern`
- `source`: `patterns/apply-from-start.md`
- `tags`: `infrastructure-as-code`, `delivery-pipeline`, `safe-change`, `reproducibility`, `roll-forward`, `cloud-agnostic`
- `summary`: When a pipeline fails, fix source and rerun from the beginning instead of patching later stages by hand.

## Apply On Change

- `id`: `iac.apply-on-change-antipattern`
- `type`: `anti-pattern`
- `source`: `patterns/apply-on-change-antipattern.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `configuration-drift`, `runtime-operations`, `safe-change`, `cloud-agnostic`
- `summary`: Applying configuration only for selected changes lets unmanaged drift accumulate and makes future changes unpredictable.

## Automated IaC Test Harness

- `id`: `iac.automated-iac-test-harness`
- `type`: `testing-practice`
- `source`: `patterns/automated-iac-test-harness.md`
- `tags`: `infrastructure-as-code`, `testing`, `automation`, `test-harness`, `ci-cd`, `tool-selection`
- `summary`: Use an automated IaC-specific test harness to provision fixtures, run checks, and clean up consistently instead of relying on manual validation.

## Batch Derived Views

- `id`: `data.batch-derived-views`
- `type`: `architecture-pattern`
- `source`: `patterns/batch-derived-views.md`
- `tags`: `data-systems`, `batch-processing`, `derived-data`, `analytics`, `data-pipeline`, `cloud-agnostic`
- `summary`: Use batch processing to build reliable derived datasets when freshness can lag and complete input scans are acceptable.

## Behavior Focused IaC Test Coverage

- `id`: `iac.behavior-focused-iac-test-coverage`
- `type`: `testing-practice`
- `source`: `patterns/behavior-focused-iac-test-coverage.md`
- `tags`: `infrastructure-as-code`, `testing`, `coverage`, `behavior-driven-testing`, `verification`, `safe-change`
- `summary`: Measure IaC test coverage by expected infrastructure behavior and observable state, not by the number of declarations or files touched by tests.

## Cloud Age Change Economics

- `id`: `iac.cloud-age-change-economics`
- `type`: `decision-guide`
- `source`: `patterns/cloud-age-change-economics.md`
- `tags`: `infrastructure-as-code`, `platform-engineering`, `safe-change`, `governance`, `design-review`, `cloud-agnostic`
- `summary`: Treat fast infrastructure change as a way to reduce risk through smaller, more frequent, better-tested changes.

## Cluster Per Environment

- `id`: `iac.cluster-per-environment`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-per-environment.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `environment-parity`, `high-availability`, `safe-change`
- `summary`: Use separate clusters when environment isolation, failure containment, or change independence outweighs shared-cluster efficiency.

## Compatible Schema Evolution

- `id`: `data.compatible-schema-evolution`
- `type`: `delivery-pattern`
- `source`: `patterns/compatible-schema-evolution.md`
- `tags`: `data-systems`, `schema-evolution`, `compatibility`, `delivery-pipeline`, `safe-change`, `cloud-agnostic`
- `summary`: Evolve encoded data with backward and forward compatibility so old and new code can coexist.

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

## Coordinated Batch Aggregation

- `id`: `platform.coordinated-batch-aggregation`
- `type`: `architecture-pattern`
- `source`: `patterns/coordinated-batch-aggregation.md`
- `tags`: `platform-engineering`, `data-platform`, `data-consistency`, `scalability`, `operability`, `design-review`, `runtime-operations`, `testing`, `idempotency`, `batch-processing`, `aggregation`
- `summary`: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.

## Copy Paste Environments

- `id`: `iac.copy-paste-environments`
- `type`: `anti-pattern`
- `source`: `patterns/copy-paste-environments.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `environment-parity`, `configuration-drift`, `stack-design`, `cloud-agnostic`
- `summary`: Duplicating stack source per environment creates short-term isolation but long-term drift and delivery overhead.

## Data Continuity Strategy

- `id`: `iac.data-continuity-strategy`
- `type`: `architecture-pattern`
- `source`: `patterns/data-continuity-strategy.md`
- `tags`: `infrastructure-as-code`, `data-continuity`, `disaster-recovery`, `safe-change`, `database`
- `summary`: Handle persistent data explicitly when changing or replacing infrastructure, using segregation, replication, reload, or a deliberate mix.

## Define Everything As Code

- `id`: `iac.define-everything-as-code`
- `type`: `delivery-pattern`
- `source`: `patterns/define-everything-as-code.md`
- `tags`: `infrastructure-as-code`, `version-control`, `reproducibility`, `governance`, `implementation-planning`, `cloud-agnostic`
- `summary`: Define infrastructure, configuration, policies, and operational workflows as versioned code where they affect repeatability or change safety.

## Event Driven Function Boundaries

- `id`: `platform.event-driven-function-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/event-driven-function-boundaries.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `operability`, `scalability`, `cost-management`, `design-review`, `implementation-planning`, `module-boundaries`, `testing`, `faas`, `event-driven`
- `summary`: Use FaaS for small stateless request transformations, asynchronous event handlers, and pipelines only when observability, cost, and state constraints fit.

## Event Log As Source

- `id`: `data.event-log-as-source`
- `type`: `architecture-pattern`
- `source`: `patterns/event-log-as-source.md`
- `tags`: `data-systems`, `event-log`, `stream-processing`, `event-driven`, `data-pipeline`, `cloud-agnostic`
- `summary`: Use an append-only event log as a durable integration backbone when consumers need replayable ordered facts.

## Evolvable Data Systems

- `id`: `data.evolvable-data-systems`
- `type`: `architecture-pattern`
- `source`: `patterns/evolvable-data-systems.md`
- `tags`: `data-systems`, `maintainability`, `schema-evolution`, `modular-architecture`, `refactoring`, `cloud-agnostic`
- `summary`: Favor data models, schemas, interfaces, and processing boundaries that can change without coordinated rewrites.

## Idempotent Automation

- `id`: `iac.idempotent-automation`
- `type`: `delivery-pattern`
- `source`: `patterns/idempotent-automation.md`
- `tags`: `infrastructure-as-code`, `idempotency`, `drift-prevention`, `reproducibility`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design infrastructure automation so repeated application converges safely instead of duplicating work or causing drift.

## Idempotent Event Processing

- `id`: `data.idempotent-event-processing`
- `type`: `delivery-pattern`
- `source`: `patterns/idempotent-event-processing.md`
- `tags`: `data-systems`, `stream-processing`, `idempotency`, `event-driven`, `runtime-operations`, `cloud-agnostic`
- `summary`: Make event consumers safe under duplicate delivery, retries, restarts, and replay.

## Immutable Server Image

- `id`: `iac.immutable-server-image`
- `type`: `architecture-pattern`
- `source`: `patterns/immutable-server-image.md`
- `tags`: `infrastructure-as-code`, `immutability`, `server-images`, `safe-change`, `runtime-operations`, `cloud-agnostic`
- `summary`: Prefer replacing servers from updated images over mutating long-lived servers when the platform and workload support it.

## Knowledge Crunching Loop

- `id`: `ddd.knowledge-crunching-loop`
- `type`: `practice`
- `source`: `patterns/knowledge-crunching-loop.md`
- `tags`: `domain-driven-design`, `domain-modeling`, `requirements-discovery`, `collaboration`, `iterative-design`, `feedback`, `testing`, `design-review`
- `summary`: Iterate with domain experts until terminology, scenarios, code, and model structure expose useful domain knowledge.

## Lease Based Ownership Election

- `id`: `platform.lease-based-ownership-election`
- `type`: `architecture-pattern`
- `source`: `patterns/lease-based-ownership-election.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `data-consistency`, `operability`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `kubernetes`, `leader-election`
- `summary`: Elect one active owner among replicas with consensus-backed compare-and-swap, renewable leases, and fencing checks before protected actions.

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

## Package Infrastructure Code

- `id`: `iac.package-infrastructure-code`
- `type`: `delivery-pattern`
- `source`: `patterns/package-infrastructure-code.md`
- `tags`: `infrastructure-as-code`, `delivery-pipeline`, `version-control`, `reproducibility`, `safe-change`, `cloud-agnostic`
- `summary`: Package or otherwise pin infrastructure code versions so pipelines apply the intended artifact consistently across environments.

## Partition Rebalancing

- `id`: `data.partition-rebalancing`
- `type`: `delivery-pattern`
- `source`: `patterns/partition-rebalancing.md`
- `tags`: `data-systems`, `partitioning`, `runtime-operations`, `scalability`, `safe-change`, `cloud-agnostic`
- `summary`: Plan partition movement as an operational workflow with bounded load, stable routing, and rollback or retry behavior.

## Pipeline Delivered Infrastructure

- `id`: `iac.pipeline-delivered-infrastructure`
- `type`: `delivery-pattern`
- `source`: `patterns/pipeline-delivered-infrastructure.md`
- `tags`: `infrastructure-as-code`, `delivery-pipeline`, `pipeline-automation`, `safe-change`, `governance`, `cloud-agnostic`
- `summary`: Deliver infrastructure code through pipelines that build, test, promote, apply, and record evidence for every change.

## Policy As Code Guardrails

- `id`: `iac.policy-as-code-guardrails`
- `type`: `governance-pattern`
- `source`: `patterns/policy-as-code-guardrails.md`
- `tags`: `infrastructure-as-code`, `policy-as-code`, `governance`, `security`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Encode repeatable governance, security, and compliance rules as automated checks in the infrastructure delivery flow.

## Production Change Monitoring

- `id`: `iac.production-change-monitoring`
- `type`: `delivery-pattern`
- `source`: `patterns/production-change-monitoring.md`
- `tags`: `infrastructure-as-code`, `observability`, `safe-change`, `runtime-operations`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Use monitoring as part of the testing strategy for risks that only appear during or after live infrastructure change.

## Progressive Feedback Pipeline

- `id`: `iac.progressive-feedback`
- `type`: `delivery-pattern`
- `source`: `patterns/progressive-feedback.md`
- `tags`: `infrastructure-as-code`, `testing`, `delivery-pipeline`, `safe-change`, `implementation-planning`, `cloud-agnostic`
- `summary`: Arrange checks so infrastructure changes get fast, useful feedback first and deeper risk checks before production impact.

## Reduce Change Scope

- `id`: `iac.reduce-change-scope`
- `type`: `delivery-pattern`
- `source`: `patterns/reduce-change-scope.md`
- `tags`: `infrastructure-as-code`, `safe-change`, `modular-architecture`, `delivery-pipeline`, `design-review`, `cloud-agnostic`
- `summary`: Make infrastructure changes smaller by splitting systems, sequencing work, and limiting each change to one coherent intent.

## Remote IaC Testing

- `id`: `iac.remote-iac-testing`
- `type`: `testing-practice`
- `source`: `patterns/remote-iac-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `remote-testing`, `integration-testing`, `cloud`, `provider-behavior`
- `summary`: Run selected IaC tests against remote or provider-backed environments when local execution cannot reveal provider, platform, or runtime integration defects.

## Repeatable Processes

- `id`: `iac.repeatable-processes`
- `type`: `delivery-pattern`
- `source`: `patterns/repeatable-processes.md`
- `tags`: `infrastructure-as-code`, `pipeline-automation`, `reproducibility`, `operability`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Automate any infrastructure process that must be run reliably more than once.

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

## Reproducible Infrastructure

- `id`: `iac.reproducible-infrastructure`
- `type`: `architecture-pattern`
- `source`: `patterns/reproducible-infrastructure.md`
- `tags`: `infrastructure-as-code`, `reproducibility`, `disaster-recovery`, `safe-change`, `runtime-operations`, `cloud-agnostic`
- `summary`: Ensure infrastructure and runtime parts can be rebuilt from known inputs without manual decisions.

## Risk Based Infrastructure Testing

- `id`: `iac.risk-based-infrastructure-testing`
- `type`: `delivery-pattern`
- `source`: `patterns/risk-based-infrastructure-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `safe-change`, `delivery-pipeline`, `design-review`, `cloud-agnostic`
- `summary`: Choose infrastructure tests based on the specific change risks they reduce, not on a desire to test every declaration.

## Rollback Roll Forward Decision

- `id`: `iac.rollback-rollforward-decision`
- `type`: `decision-guide`
- `source`: `patterns/rollback-rollforward-decision.md`
- `tags`: `infrastructure-as-code`, `rollback`, `roll-forward`, `safe-change`, `incident-response`, `cloud-agnostic`
- `summary`: Decide whether to restore a previous version or move forward with a fix based on state, compatibility, and recovery speed.

## Rolling Replacement

- `id`: `iac.rolling-replacement`
- `type`: `delivery-pattern`
- `source`: `patterns/rolling-replacement.md`
- `tags`: `infrastructure-as-code`, `zero-downtime`, `safe-change`, `high-availability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Change serving infrastructure by replacing a limited slice at a time while health checks protect availability.

## Safe Infrastructure Change

- `id`: `iac.safe-infrastructure-change`
- `type`: `decision-guide`
- `source`: `patterns/safe-infrastructure-change.md`
- `tags`: `infrastructure-as-code`, `safe-change`, `rollback`, `disaster-recovery`, `design-review`, `cloud-agnostic`
- `summary`: Choose a change strategy based on reversibility, blast radius, data risk, compatibility, and observability.

## Sandbox IaC Testing

- `id`: `iac.sandbox-iac-testing`
- `type`: `testing-practice`
- `source`: `patterns/sandbox-iac-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `sandbox`, `isolation`, `cost-control`, `safe-change`
- `summary`: Test infrastructure changes in isolated disposable environments so validation can create, update, and destroy resources without harming production or shared systems.

## Scatter Gather Request Parallelism

- `id`: `platform.scatter-gather-request-parallelism`
- `type`: `architecture-pattern`
- `source`: `patterns/scatter-gather-request-parallelism.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `performance`, `design-review`, `runtime-operations`, `testing`, `kubernetes`, `scatter-gather`
- `summary`: Parallelize one request across many workers only when partial results can be merged and tail-latency, straggler, and availability costs are explicitly controlled.

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

## Sidecar Application Augmentation

- `id`: `platform.sidecar-application-augmentation`
- `type`: `architecture-pattern`
- `source`: `patterns/sidecar-application-augmentation.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `operability`, `security`, `migration`, `implementation-planning`, `module-boundaries`, `parameterization`, `kubernetes`, `sidecar`
- `summary`: Add tightly coupled auxiliary behavior beside an application container when shared local resources let the helper improve the app without changing its code.

## Small Safe Changes

- `id`: `iac.small-safe-changes`
- `type`: `delivery-pattern`
- `source`: `patterns/small-safe-changes.md`
- `tags`: `infrastructure-as-code`, `safe-change`, `migration`, `roll-forward`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Use incremental, iterative, and walking-skeleton approaches to evolve infrastructure without betting on one large cutover.

## Spaghetti Module

- `id`: `iac.spaghetti-module`
- `type`: `anti-pattern`
- `source`: `patterns/spaghetti-module.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `module-boundaries`, `modular-architecture`, `testing`, `cloud-agnostic`
- `summary`: A spaghetti module has too many modes, branches, and responsibilities to be safely reused or tested.

## Stream Derived Views

- `id`: `data.stream-derived-views`
- `type`: `architecture-pattern`
- `source`: `patterns/stream-derived-views.md`
- `tags`: `data-systems`, `stream-processing`, `derived-data`, `event-driven`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use stream processing to maintain derived data incrementally when low-latency updates matter.

## Team Workflow Metrics

- `id`: `iac.team-workflow-metrics`
- `type`: `governance-pattern`
- `source`: `patterns/team-workflow-metrics.md`
- `tags`: `infrastructure-as-code`, `governance`, `operability`, `delivery-pipeline`, `safe-change`, `cloud-agnostic`
- `summary`: Use delivery and reliability metrics together to evaluate whether infrastructure workflow changes improve outcomes.

## Terraform Production Module Design

- `id`: `iac.terraform-production-module-design`
- `type`: `design-pattern`
- `source`: `patterns/terraform-production-module-design.md`
- `tags`: `infrastructure-as-code`, `terraform`, `modules`, `production-readiness`, `composability`, `testing`, `versioning`, `platform-engineering`
- `summary`: Build production Terraform modules as small, composable, testable, and versioned units backed by explicit production-readiness checks.

## Terraform Stable Resource Addressing

- `id`: `iac.terraform-stable-resource-addressing`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-stable-resource-addressing.md`
- `tags`: `infrastructure-as-code`, `terraform`, `refactoring`, `for-each`, `count`, `lifecycle`, `zero-downtime`, `safe-change`
- `summary`: Use stable keys, lifecycle-aware refactors, and cautious conditionals so Terraform does not replace resources merely because list order, count indexes, or addresses changed.

## Terraform Team Delivery Workflow

- `id`: `iac.terraform-team-delivery-workflow`
- `type`: `delivery-pattern`
- `source`: `patterns/terraform-team-delivery-workflow.md`
- `tags`: `infrastructure-as-code`, `terraform`, `team-workflow`, `ci-cd`, `code-review`, `adoption`, `delivery-pipeline`, `governance`
- `summary`: Make Terraform a team workflow with incremental adoption, version control, review, automated checks, controlled applies, and promotion paths for infrastructure changes.

## Terraform Test Strategy

- `id`: `iac.terraform-test-strategy`
- `type`: `testing-pattern`
- `source`: `patterns/terraform-test-strategy.md`
- `tags`: `infrastructure-as-code`, `terraform`, `testing`, `unit-testing`, `integration-testing`, `plan-testing`, `end-to-end-testing`, `ci-cd`
- `summary`: Combine static, plan, unit, integration, and end-to-end Terraform tests so each risk is checked at the cheapest layer that can catch it.

## Test Code Antipattern Linting

- `id`: `iac.test-code-antipattern-linting`
- `type`: `testing-practice`
- `source`: `patterns/test-code-antipattern-linting.md`
- `tags`: `infrastructure-as-code`, `testing`, `linting`, `maintainability`, `technical-debt`, `quality-gates`
- `summary`: Lint IaC test code and supporting scripts so the tests that protect infrastructure do not become a separate source of defects and maintenance drag.

## Test Every IaC Change

- `id`: `iac.test-every-iac-change`
- `type`: `delivery-practice`
- `source`: `patterns/test-every-iac-change.md`
- `tags`: `infrastructure-as-code`, `testing`, `continuous-integration`, `delivery-pipeline`, `drift-detection`, `feedback`
- `summary`: Trigger an appropriate IaC test path for every infrastructure change, and supplement change-triggered tests with scheduled runs that catch environmental drift.

## Timeout Retry Backoff

- `id`: `data.timeout-retry-backoff`
- `type`: `delivery-pattern`
- `source`: `patterns/timeout-retry-backoff.md`
- `tags`: `data-systems`, `distributed-systems`, `resilience`, `runtime-operations`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use timeouts, retries, backoff, and idempotency together so transient faults do not become overload or duplicate side effects.

## Trust But Verify Dataflows

- `id`: `data.trust-but-verify-dataflows`
- `type`: `governance-pattern`
- `source`: `patterns/trust-but-verify-dataflows.md`
- `tags`: `data-systems`, `data-quality`, `derived-data`, `observability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Continuously verify derived data against source facts to detect corruption, missed events, and broken assumptions.

## Version Controlled Infrastructure

- `id`: `iac.version-controlled-infrastructure`
- `type`: `delivery-pattern`
- `source`: `patterns/version-controlled-infrastructure.md`
- `tags`: `infrastructure-as-code`, `version-control`, `delivery-pipeline`, `governance`, `safe-change`, `cloud-agnostic`
- `summary`: Store infrastructure code in version control to make changes traceable, reviewable, recoverable, and deliverable through pipelines.

## Workflow Queue Composition

- `id`: `platform.workflow-queue-composition`
- `type`: `architecture-pattern`
- `source`: `patterns/workflow-queue-composition.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `high-availability`, `modular-architecture`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `event-driven`, `workflow`
- `summary`: Compose multi-stage batch workflows with explicit copier, filter, splitter, sharder, and merger queue patterns backed by reliable pub/sub infrastructure.
