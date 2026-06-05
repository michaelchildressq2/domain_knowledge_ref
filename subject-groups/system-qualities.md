# System Qualities

Pattern count: 40

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

## Analytical Column Storage

- `id`: `data.analytical-column-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/analytical-column-storage.md`
- `tags`: `data-systems`, `analytics`, `storage-engine`, `data-warehouse`, `performance`, `cloud-agnostic`
- `summary`: Use column-oriented storage for analytical workloads that scan many rows but only a subset of columns.

## Backpressure For Streams

- `id`: `data.backpressure-for-streams`
- `type`: `architecture-pattern`
- `source`: `patterns/backpressure-for-streams.md`
- `tags`: `data-systems`, `stream-processing`, `backpressure`, `reliability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Propagate overload signals through streaming systems so slow consumers do not cause unbounded queues or cascading failure.

## Cluster Per Environment

- `id`: `iac.cluster-per-environment`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-per-environment.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `environment-parity`, `high-availability`, `safe-change`
- `summary`: Use separate clusters when environment isolation, failure containment, or change independence outweighs shared-cluster efficiency.

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

## Coordinated Batch Aggregation

- `id`: `platform.coordinated-batch-aggregation`
- `type`: `architecture-pattern`
- `source`: `patterns/coordinated-batch-aggregation.md`
- `tags`: `platform-engineering`, `data-platform`, `data-consistency`, `scalability`, `operability`, `design-review`, `runtime-operations`, `testing`, `idempotency`, `batch-processing`, `aggregation`
- `summary`: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.

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

## Evolvable Data Systems

- `id`: `data.evolvable-data-systems`
- `type`: `architecture-pattern`
- `source`: `patterns/evolvable-data-systems.md`
- `tags`: `data-systems`, `maintainability`, `schema-evolution`, `modular-architecture`, `refactoring`, `cloud-agnostic`
- `summary`: Favor data models, schemas, interfaces, and processing boundaries that can change without coordinated rewrites.

## Hot Spot Aware Partitioning

- `id`: `data.hot-spot-aware-partitioning`
- `type`: `architecture-pattern`
- `source`: `patterns/hot-spot-aware-partitioning.md`
- `tags`: `data-systems`, `partitioning`, `scalability`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Partition data to distribute load while accounting for skew, range access, secondary indexes, and rebalancing.

## Index Cost Tradeoff

- `id`: `data.index-cost-tradeoff`
- `type`: `decision-guide`
- `source`: `patterns/index-cost-tradeoff.md`
- `tags`: `data-systems`, `indexing`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Add indexes deliberately because they speed reads but increase write cost, storage, and maintenance complexity.

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

## Load And Performance Characterization

- `id`: `data.load-and-performance-characterization`
- `type`: `decision-guide`
- `source`: `patterns/load-and-performance-characterization.md`
- `tags`: `data-systems`, `scalability`, `performance`, `capacity-planning`, `design-review`, `cloud-agnostic`
- `summary`: Describe scalability using workload dimensions, service-level expectations, and performance distributions before choosing scaling tactics.

## Log Structured Storage

- `id`: `data.log-structured-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/log-structured-storage.md`
- `tags`: `data-systems`, `storage-engine`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use append-oriented storage and compaction when write throughput and sequential I/O dominate the workload.

## Minimize Variation

- `id`: `iac.minimize-variation`
- `type`: `architecture-pattern`
- `source`: `patterns/minimize-variation.md`
- `tags`: `infrastructure-as-code`, `environment-parity`, `configuration-management`, `drift-prevention`, `operability`, `cloud-agnostic`
- `summary`: Keep instances that serve the same purpose as similar as possible to reduce drift, testing burden, and operational surprise.

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

## Operability First Systems

- `id`: `data.operability-first-systems`
- `type`: `architecture-pattern`
- `source`: `patterns/operability-first-systems.md`
- `tags`: `data-systems`, `operability`, `observability`, `runtime-operations`, `reliability`, `cloud-agnostic`
- `summary`: Design data systems so operators can observe, diagnose, repair, and safely change them.

## Partial Failure Design

- `id`: `data.partial-failure-design`
- `type`: `architecture-pattern`
- `source`: `patterns/partial-failure-design.md`
- `tags`: `data-systems`, `distributed-systems`, `reliability`, `failure-modes`, `design-review`, `cloud-agnostic`
- `summary`: Design distributed systems assuming some components can be slow, unreachable, or mistaken while others continue running.

## Partition Rebalancing

- `id`: `data.partition-rebalancing`
- `type`: `delivery-pattern`
- `source`: `patterns/partition-rebalancing.md`
- `tags`: `data-systems`, `partitioning`, `runtime-operations`, `scalability`, `safe-change`, `cloud-agnostic`
- `summary`: Plan partition movement as an operational workflow with bounded load, stable routing, and rollback or retry behavior.

## Reliability Scalability Maintainability

- `id`: `data.reliability-scalability-maintainability`
- `type`: `decision-guide`
- `source`: `patterns/reliability-scalability-maintainability.md`
- `tags`: `data-systems`, `reliability`, `scalability`, `maintainability`, `design-review`, `cloud-agnostic`
- `summary`: Evaluate data-system designs through reliability, scalability, and maintainability rather than a single technology preference.

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

## Reusable Work Queue Interface

- `id`: `platform.reusable-work-queue-interface`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-work-queue-interface.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `operability`, `modular-architecture`, `implementation-planning`, `runtime-operations`, `module-boundaries`, `idempotency`, `kubernetes`, `work-queue`
- `summary`: Build batch work queues from a generic queue manager, a versioned source interface, and worker containers launched by the orchestrator.

## Rolling Replacement

- `id`: `iac.rolling-replacement`
- `type`: `delivery-pattern`
- `source`: `patterns/rolling-replacement.md`
- `tags`: `infrastructure-as-code`, `zero-downtime`, `safe-change`, `high-availability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Change serving infrastructure by replacing a limited slice at a time while health checks protect availability.

## Scatter Gather Request Parallelism

- `id`: `platform.scatter-gather-request-parallelism`
- `type`: `architecture-pattern`
- `source`: `patterns/scatter-gather-request-parallelism.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `performance`, `design-review`, `runtime-operations`, `testing`, `kubernetes`, `scatter-gather`
- `summary`: Parallelize one request across many workers only when partial results can be merged and tail-latency, straggler, and availability costs are explicitly controlled.

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

## Storage Engine Fit

- `id`: `data.storage-engine-fit`
- `type`: `decision-guide`
- `source`: `patterns/storage-engine-fit.md`
- `tags`: `data-systems`, `storage-engine`, `database`, `performance`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage engines by write/read mix, update pattern, range-query needs, and compaction behavior.

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

## Transaction Boundary Fit

- `id`: `data.transaction-boundary-fit`
- `type`: `decision-guide`
- `source`: `patterns/transaction-boundary-fit.md`
- `tags`: `data-systems`, `transactions`, `consistency`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Use transactions where they simplify correctness, but keep boundaries aligned with invariants and operational cost.

## Trust But Verify Dataflows

- `id`: `data.trust-but-verify-dataflows`
- `type`: `governance-pattern`
- `source`: `patterns/trust-but-verify-dataflows.md`
- `tags`: `data-systems`, `data-quality`, `derived-data`, `observability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Continuously verify derived data against source facts to detect corruption, missed events, and broken assumptions.

## Workflow Queue Composition

- `id`: `platform.workflow-queue-composition`
- `type`: `architecture-pattern`
- `source`: `patterns/workflow-queue-composition.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `high-availability`, `modular-architecture`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `event-driven`, `workflow`
- `summary`: Compose multi-stage batch workflows with explicit copier, filter, splitter, sharder, and merger queue patterns backed by reliable pub/sub infrastructure.
