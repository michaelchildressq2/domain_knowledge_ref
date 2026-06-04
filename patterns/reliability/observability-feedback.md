---
id: platform.observability-feedback
title: Observability as Change Feedback
type: architecture-pattern
status: seed
summary: Treat observability as the feedback loop that proves infrastructure changes
  preserved or improved user-facing capability.
tags:
- platform-engineering
- sre
- observability
- safe-change
- runtime-operations
- delivery-pipeline
- incident-response
- design-review
- cloud-agnostic
- testing
aliases:
- change verification
- service health feedback
- post deploy checks
- operational telemetry
applies_when:
- The user asks how to know whether a platform or infrastructure change worked.
- Deployments succeed technically but users still experience errors or latency.
- A design needs signals for rollback, roll-forward, autoscaling, or incident response.
avoid_when:
- The system is a short-lived experiment with no operational commitment.
- Metrics are being used as a substitute for understanding business-critical behavior.
- The only need is static compliance evidence.
related:
- platform.safe-infrastructure-change
- platform.high-availability
- platform.iac-delivery
- platform.disaster-recovery
sources:
- synthesis: general sre, platform engineering, and continuous delivery practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: reliability
---

# Observability as Change Feedback

## Intent

Use runtime signals to determine whether infrastructure and platform changes preserved the capabilities users depend on.

## Use when

- An apply, deploy, migration, or failover needs success criteria beyond resource creation.
- The user asks about health checks, dashboards, alerts, SLOs, rollback signals, or post-deployment verification.
- Teams cannot tell whether a platform change improved or harmed the service.

## Avoid when

- The workload has no ongoing operational commitment.
- The requested evidence is purely static configuration compliance.
- The metrics available do not represent user capability and would create false confidence.

## Context and problem

Infrastructure tools report whether resources were created or modified, not whether users can complete their work. Agents should connect platform changes to service-level signals and operational feedback.

## Forces

- Signal quality versus implementation effort.
- User-level indicators versus low-level resource metrics.
- Fast rollback decisions versus noisy alerts.
- Standard platform dashboards versus service-specific behavior.

## Guidance

Define success and failure signals before the change. Use user-facing indicators where possible, then supporting infrastructure metrics to diagnose. Feed these signals into delivery pipelines, incident response, and design review.

## Implementation moves

- Identify the user capability or service objective affected by the change.
- Define success metrics, guardrail metrics, and rollback or roll-forward thresholds.
- Instrument requests, dependencies, saturation, errors, latency, and business-critical workflows.
- Add post-apply or post-deploy checks to the pipeline.
- Make dashboards and alerts environment-aware.
- Capture change events as annotations in observability tools.

## Checks

- What user-visible signal proves the change worked?
- What metric would trigger rollback or mitigation?
- Can operators correlate a symptom with the infrastructure change?
- Are health checks deep enough to detect dependency failure?
- Are alerts tied to action rather than noise?

## Failure modes

- Declaring success because the infrastructure apply completed.
- Monitoring only CPU, memory, or resource status while user requests fail.
- Dashboards that do not distinguish environment, version, or region.
- Alerts without owners or runbooks.
- Missing change annotations during incident analysis.

## Agent trigger hints

Use this pattern when the user says or implies:

- how do we know it worked
- post deploy validation
- infrastructure health checks
- observability for platform changes
- rollback signals
- slo impact
- change annotations

## Source notes

This is an original synthesis from SRE and continuous delivery practice. Link it to source-specific notes when a reading emphasizes feedback, testing, or operational verification.
