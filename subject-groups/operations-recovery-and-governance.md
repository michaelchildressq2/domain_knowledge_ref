# Operations Recovery And Governance

Pattern count: 55

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

## Apply Code Continuously

- `id`: `iac.apply-code-continuously`
- `type`: `delivery-pattern`
- `source`: `patterns/apply-code-continuously.md`
- `tags`: `infrastructure-as-code`, `drift-prevention`, `idempotency`, `runtime-operations`, `delivery-pipeline`, `cloud-agnostic`
- `summary`: Reapply infrastructure code regularly or on change to keep managed systems aligned with declared intent.

## Apply On Change

- `id`: `iac.apply-on-change-antipattern`
- `type`: `anti-pattern`
- `source`: `patterns/apply-on-change-antipattern.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `configuration-drift`, `runtime-operations`, `safe-change`, `cloud-agnostic`
- `summary`: Applying configuration only for selected changes lets unmanaged drift accumulate and makes future changes unpredictable.

## Backpressure For Streams

- `id`: `data.backpressure-for-streams`
- `type`: `architecture-pattern`
- `source`: `patterns/backpressure-for-streams.md`
- `tags`: `data-systems`, `stream-processing`, `backpressure`, `reliability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Propagate overload signals through streaming systems so slow consumers do not cause unbounded queues or cascading failure.

## Cloud Age Change Economics

- `id`: `iac.cloud-age-change-economics`
- `type`: `decision-guide`
- `source`: `patterns/cloud-age-change-economics.md`
- `tags`: `infrastructure-as-code`, `platform-engineering`, `safe-change`, `governance`, `design-review`, `cloud-agnostic`
- `summary`: Treat fast infrastructure change as a way to reduce risk through smaller, more frequent, better-tested changes.

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

## Conflict Free Domain Design

- `id`: `data.conflict-free-domain-design`
- `type`: `architecture-pattern`
- `source`: `patterns/conflict-free-domain-design.md`
- `tags`: `data-systems`, `replication`, `conflict-resolution`, `eventual-consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Shape replicated operations so concurrent updates commute or merge without losing user intent.

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

## Correctness Before Preservation

- `id`: `data.correctness-before-preservation`
- `type`: `decision-guide`
- `source`: `patterns/correctness-before-preservation.md`
- `tags`: `data-systems`, `correctness`, `maintainability`, `governance`, `design-review`, `cloud-agnostic`
- `summary`: Optimize data-system design for useful, correct outcomes rather than preserving existing mechanisms or local component uptime.

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

## Disposable Infrastructure

- `id`: `iac.disposable-infrastructure`
- `type`: `architecture-pattern`
- `source`: `patterns/disposable-infrastructure.md`
- `tags`: `infrastructure-as-code`, `immutability`, `reproducibility`, `high-availability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design replaceable infrastructure so failed or outdated parts can be rebuilt instead of nursed back to health.

## Event Driven Function Boundaries

- `id`: `platform.event-driven-function-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/event-driven-function-boundaries.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `operability`, `scalability`, `cost-management`, `design-review`, `implementation-planning`, `module-boundaries`, `testing`, `faas`, `event-driven`
- `summary`: Use FaaS for small stateless request transformations, asynchronous event handlers, and pipelines only when observability, cost, and state constraints fit.

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

## Immutable Server Image

- `id`: `iac.immutable-server-image`
- `type`: `architecture-pattern`
- `source`: `patterns/immutable-server-image.md`
- `tags`: `infrastructure-as-code`, `immutability`, `server-images`, `safe-change`, `runtime-operations`, `cloud-agnostic`
- `summary`: Prefer replacing servers from updated images over mutating long-lived servers when the platform and workload support it.

## Integration Registry Lookup

- `id`: `iac.integration-registry-lookup`
- `type`: `architecture-pattern`
- `source`: `patterns/integration-registry-lookup.md`
- `tags`: `infrastructure-as-code`, `configuration-management`, `registry`, `module-boundaries`, `platform-engineering`, `cloud-agnostic`
- `summary`: Use a general-purpose registry for cross-stack or cross-team integration values when stack-tool-specific coupling is too narrow.

## Leader Election Safety

- `id`: `data.leader-election-safety`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-election-safety.md`
- `tags`: `data-systems`, `coordination`, `leader-election`, `distributed-systems`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design leader election so only one effective leader can perform protected work at a time.

## Leader Follower Replication

- `id`: `data.leader-follower-replication`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-follower-replication.md`
- `tags`: `data-systems`, `replication`, `high-availability`, `database`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use leader-follower replication when one primary write path and multiple read or failover copies fit the consistency and availability needs.

## Lease Based Ownership Election

- `id`: `platform.lease-based-ownership-election`
- `type`: `architecture-pattern`
- `source`: `patterns/lease-based-ownership-election.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `data-consistency`, `operability`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `kubernetes`, `leader-election`
- `summary`: Elect one active owner among replicas with consensus-backed compare-and-swap, renewable leases, and fencing checks before protected actions.

## Linearizability When Needed

- `id`: `data.linearizability-when-needed`
- `type`: `decision-guide`
- `source`: `patterns/linearizability-when-needed.md`
- `tags`: `data-systems`, `consistency`, `linearizability`, `distributed-systems`, `design-review`, `cloud-agnostic`
- `summary`: Use linearizability for operations that require a single up-to-date view, and avoid paying its cost for data that can be stale or mergeable.

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

## Operability First Systems

- `id`: `data.operability-first-systems`
- `type`: `architecture-pattern`
- `source`: `patterns/operability-first-systems.md`
- `tags`: `data-systems`, `operability`, `observability`, `runtime-operations`, `reliability`, `cloud-agnostic`
- `summary`: Design data systems so operators can observe, diagnose, repair, and safely change them.

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

## Replicated Stateless Serving

- `id`: `platform.replicated-stateless-serving`
- `type`: `architecture-pattern`
- `source`: `patterns/replicated-stateless-serving.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `scalability`, `zero-downtime`, `design-review`, `runtime-operations`, `rollback`, `testing`, `kubernetes`, `load-balancing`
- `summary`: Run multiple interchangeable service replicas behind a load balancer with readiness checks, rollout controls, and optional replicated edge layers.

## Replication Lag Aware Reads

- `id`: `data.replication-lag-aware-reads`
- `type`: `architecture-pattern`
- `source`: `patterns/replication-lag-aware-reads.md`
- `tags`: `data-systems`, `replication`, `consistency`, `read-models`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design read paths around the user-visible anomalies created by asynchronous replication lag.

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

## Server Lifecycle As Code

- `id`: `iac.server-lifecycle-as-code`
- `type`: `architecture-pattern`
- `source`: `patterns/server-lifecycle-as-code.md`
- `tags`: `infrastructure-as-code`, `server-images`, `configuration-management`, `runtime-operations`, `reproducibility`, `cloud-agnostic`
- `summary`: Manage server build, configure, update, and retire phases as explicit coded lifecycle transitions.

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

## Snowflake System

- `id`: `iac.snowflake-system`
- `type`: `anti-pattern`
- `source`: `patterns/snowflake-system.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `configuration-drift`, `reproducibility`, `runtime-operations`, `cloud-agnostic`
- `summary`: A snowflake system is manually unique, hard to reproduce, and risky to change or recover.

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
