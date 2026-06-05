# Pipelines Streams And Derived Data

Pattern count: 47

## Ansible Image Build Handoff

- `id`: `iac.ansible-image-build-handoff`
- `type`: `delivery-pattern`
- `source`: `patterns/ansible-image-build-handoff.md`
- `tags`: `infrastructure-as-code`, `ansible`, `image-building`, `packer`, `immutable-infrastructure`, `delivery-pipeline`, `reproducibility`
- `summary`: Use Ansible inside image-building workflows to configure base images once, then hand runtime variation to inventory, variables, and deployment automation.

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

## Backpressure For Streams

- `id`: `data.backpressure-for-streams`
- `type`: `architecture-pattern`
- `source`: `patterns/backpressure-for-streams.md`
- `tags`: `data-systems`, `stream-processing`, `backpressure`, `reliability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Propagate overload signals through streaming systems so slow consumers do not cause unbounded queues or cascading failure.

## Batch Derived Views

- `id`: `data.batch-derived-views`
- `type`: `architecture-pattern`
- `source`: `patterns/batch-derived-views.md`
- `tags`: `data-systems`, `batch-processing`, `derived-data`, `analytics`, `data-pipeline`, `cloud-agnostic`
- `summary`: Use batch processing to build reliable derived datasets when freshness can lag and complete input scans are acceptable.

## Compatible Schema Evolution

- `id`: `data.compatible-schema-evolution`
- `type`: `delivery-pattern`
- `source`: `patterns/compatible-schema-evolution.md`
- `tags`: `data-systems`, `schema-evolution`, `compatibility`, `delivery-pipeline`, `safe-change`, `cloud-agnostic`
- `summary`: Evolve encoded data with backward and forward compatibility so old and new code can coexist.

## Conflict Free Domain Design

- `id`: `data.conflict-free-domain-design`
- `type`: `architecture-pattern`
- `source`: `patterns/conflict-free-domain-design.md`
- `tags`: `data-systems`, `replication`, `conflict-resolution`, `eventual-consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Shape replicated operations so concurrent updates commute or merge without losing user intent.

## Coordinated Batch Aggregation

- `id`: `platform.coordinated-batch-aggregation`
- `type`: `architecture-pattern`
- `source`: `patterns/coordinated-batch-aggregation.md`
- `tags`: `platform-engineering`, `data-platform`, `data-consistency`, `scalability`, `operability`, `design-review`, `runtime-operations`, `testing`, `idempotency`, `batch-processing`, `aggregation`
- `summary`: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.

## Derived Data Over Distributed Transactions

- `id`: `data.derived-data-over-distributed-transactions`
- `type`: `decision-guide`
- `source`: `patterns/derived-data-over-distributed-transactions.md`
- `tags`: `data-systems`, `data-integration`, `distributed-workflow`, `derived-data`, `design-review`, `cloud-agnostic`
- `summary`: Prefer replayable derived dataflows over distributed transactions when integrating heterogeneous stores for read optimization.

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

## Eventual Consistency Boundaries

- `id`: `data.eventual-consistency-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/eventual-consistency-boundaries.md`
- `tags`: `data-systems`, `eventual-consistency`, `consistency`, `distributed-systems`, `design-review`, `cloud-agnostic`
- `summary`: Use eventual consistency only where product semantics, repair mechanisms, and user expectations can tolerate temporary divergence.

## Fencing Tokens

- `id`: `data.fencing-tokens`
- `type`: `architecture-pattern`
- `source`: `patterns/fencing-tokens.md`
- `tags`: `data-systems`, `distributed-systems`, `coordination`, `consistency`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use monotonically increasing fencing tokens to prevent stale leaders or lock holders from corrupting shared resources.

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

## Leader Election Safety

- `id`: `data.leader-election-safety`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-election-safety.md`
- `tags`: `data-systems`, `coordination`, `leader-election`, `distributed-systems`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design leader election so only one effective leader can perform protected work at a time.

## Materialized Conflict Constraints

- `id`: `data.materialized-conflict-constraints`
- `type`: `architecture-pattern`
- `source`: `patterns/materialized-conflict-constraints.md`
- `tags`: `data-systems`, `transactions`, `constraints`, `consistency`, `database`, `cloud-agnostic`
- `summary`: Materialize conflicts so the database can enforce invariants that would otherwise span predicate reads or missing rows.

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

## Repeatable Processes

- `id`: `iac.repeatable-processes`
- `type`: `delivery-pattern`
- `source`: `patterns/repeatable-processes.md`
- `tags`: `infrastructure-as-code`, `pipeline-automation`, `reproducibility`, `operability`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Automate any infrastructure process that must be run reliably more than once.

## Repository Boundaries

- `id`: `iac.repository-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/repository-boundaries.md`
- `tags`: `infrastructure-as-code`, `version-control`, `modular-architecture`, `delivery-pipeline`, `governance`, `cloud-agnostic`
- `summary`: Choose infrastructure repository boundaries based on ownership, delivery cadence, dependency management, and change isolation.

## Reusable Work Queue Interface

- `id`: `platform.reusable-work-queue-interface`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-work-queue-interface.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `operability`, `modular-architecture`, `implementation-planning`, `runtime-operations`, `module-boundaries`, `idempotency`, `kubernetes`, `work-queue`
- `summary`: Build batch work queues from a generic queue manager, a versioned source interface, and worker containers launched by the orchestrator.

## Risk Based Infrastructure Testing

- `id`: `iac.risk-based-infrastructure-testing`
- `type`: `delivery-pattern`
- `source`: `patterns/risk-based-infrastructure-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `safe-change`, `delivery-pipeline`, `design-review`, `cloud-agnostic`
- `summary`: Choose infrastructure tests based on the specific change risks they reduce, not on a desire to test every declaration.

## Saga With Compensation

- `id`: `data.saga-with-compensation`
- `type`: `architecture-pattern`
- `source`: `patterns/saga-with-compensation.md`
- `tags`: `data-systems`, `distributed-workflow`, `transactions`, `event-driven`, `implementation-planning`, `cloud-agnostic`
- `summary`: Coordinate multi-step business workflows with explicit state and compensating actions when one distributed transaction is not appropriate.

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

## Small Safe Changes

- `id`: `iac.small-safe-changes`
- `type`: `delivery-pattern`
- `source`: `patterns/small-safe-changes.md`
- `tags`: `infrastructure-as-code`, `safe-change`, `migration`, `roll-forward`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Use incremental, iterative, and walking-skeleton approaches to evolve infrastructure without betting on one large cutover.

## Stack Data Lookup

- `id`: `iac.stack-data-lookup`
- `type`: `architecture-pattern`
- `source`: `patterns/stack-data-lookup.md`
- `tags`: `infrastructure-as-code`, `stack-design`, `module-boundaries`, `configuration-management`, `implementation-planning`, `cloud-agnostic`
- `summary`: Let consumer stacks read provider outputs through the stack tool when stacks need explicit infrastructure dependencies.

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

## Terraform Team Delivery Workflow

- `id`: `iac.terraform-team-delivery-workflow`
- `type`: `delivery-pattern`
- `source`: `patterns/terraform-team-delivery-workflow.md`
- `tags`: `infrastructure-as-code`, `terraform`, `team-workflow`, `ci-cd`, `code-review`, `adoption`, `delivery-pipeline`, `governance`
- `summary`: Make Terraform a team workflow with incremental adoption, version control, review, automated checks, controlled applies, and promotion paths for infrastructure changes.

## Test Every IaC Change

- `id`: `iac.test-every-iac-change`
- `type`: `delivery-practice`
- `source`: `patterns/test-every-iac-change.md`
- `tags`: `infrastructure-as-code`, `testing`, `continuous-integration`, `delivery-pipeline`, `drift-detection`, `feedback`
- `summary`: Trigger an appropriate IaC test path for every infrastructure change, and supplement change-triggered tests with scheduled runs that catch environmental drift.

## Trust But Verify Dataflows

- `id`: `data.trust-but-verify-dataflows`
- `type`: `governance-pattern`
- `source`: `patterns/trust-but-verify-dataflows.md`
- `tags`: `data-systems`, `data-quality`, `derived-data`, `observability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Continuously verify derived data against source facts to detect corruption, missed events, and broken assumptions.

## Unbundled Derived Data

- `id`: `data.unbundled-derived-data`
- `type`: `architecture-pattern`
- `source`: `patterns/unbundled-derived-data.md`
- `tags`: `data-systems`, `derived-data`, `data-integration`, `event-driven`, `modular-architecture`, `cloud-agnostic`
- `summary`: Compose specialized storage and processing systems by deriving views from a durable source of truth instead of forcing one database to do everything.

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
