---
id: iac.sandbox-iac-testing
title: Sandbox IaC Testing
type: testing-practice
status: draft
summary: Test infrastructure changes in isolated disposable environments so validation can create, update, and destroy resources without harming production or shared systems.
tags:
  - infrastructure-as-code
  - testing
  - sandbox
  - isolation
  - cost-control
  - safe-change
aliases:
  - sandbox testing
  - isolated infrastructure testing
  - disposable test environment
  - test environment isolation
applies_when:
  - IaC tests need to apply real changes, create resources, or destroy fixtures.
  - A failed or misconfigured test could update, delete, expose, or bill production-like infrastructure.
avoid_when:
  - The risk can be handled by a static check or plan-only validation.
  - The organization cannot yet provide isolated credentials, quotas, naming, or cleanup controls.
related:
  - iac.disposable-infrastructure
  - iac.remote-iac-testing
  - iac.cluster-per-environment
  - iac.safe-infrastructure-change
sources:
  - "paper: Hasan, Bhuiyan, and Rahman, Testing Practices for Infrastructure as Code, LANGETI 2020; Section 3, Sandbox Testing."
source_confidence: medium
last_reviewed: 2026-06-05
---

# Sandbox IaC Testing

## Intent

Allow IaC tests to exercise real provisioning behavior while containing blast radius, data exposure, and cost through isolated disposable environments.

## Use when

- Tests need to create, modify, or destroy infrastructure resources.
- The change touches networking, identity, storage, clusters, images, bootstrap, or managed services.
- A team wants stronger evidence than plan review without risking production.
- Multiple contributors or pull requests may run tests concurrently.
- The organization can create isolated subscriptions, accounts, projects, namespaces, resource groups, or ephemeral environments.

## Avoid when

- Sandbox setup would be more complex and risky than the infrastructure being tested.
- The test requires production-only data or connectivity that cannot be safely replicated.
- Cleanup is manual or unreliable.
- Shared quotas make concurrent sandbox creation disruptive.
- The test environment diverges so much from production that the result is misleading.

## Context and problem

IaC testing can be destructive by design: it may create resources, rotate configuration, change routes, or destroy fixtures to prove lifecycle behavior. If these tests run in the wrong place, a normal test failure can become an outage, data exposure, or cost event.

The paper identifies sandbox testing as a practice that isolates IaC test activity from production. The reusable pattern is to make isolation and disposal part of the test design, not a manual convention remembered by individual operators.

## Forces

- Real apply/destroy tests increase confidence, but they also increase blast radius.
- Sandboxes cost money and quota, but shared environments create hidden coupling and cleanup risk.
- A sandbox should resemble production enough to be meaningful while remaining cheap and disposable.
- Developers need self-service environments, but governance still needs guardrails.
- Cleanup must handle both successful and failed test runs.

## Guidance

Create dedicated sandbox targets for IaC tests. Keep them isolated by account, subscription, project, namespace, resource group, network boundary, credentials, and state backend as appropriate for the platform. Treat sandbox lifecycle as code: create, verify, tag, expire, and destroy.

Use production-like defaults only where they affect the behavior under test. Reduce size, retention, and availability settings where doing so does not invalidate the result. Every sandbox resource should carry enough metadata for ownership, cost attribution, expiration, and emergency cleanup.

## Implementation moves

- Define sandbox boundaries and name them explicitly in code and pipeline configuration.
- Use separate credentials with no production write access.
- Use separate state, locks, and backend keys for sandbox runs.
- Generate unique resource names for concurrent test runs.
- Apply TTL, owner, pull-request, commit, and cost-center tags to all supported resources.
- Destroy sandboxes automatically after tests, with periodic cleanup for abandoned resources.
- Block sandbox tests from running when the selected target is production or shared long-lived infrastructure.

## Checks

- Can a test accidentally target production with the same credentials or state backend?
- Are sandbox resources clearly tagged with owner and expiration?
- Does cleanup run on success, failure, cancellation, and timeout?
- Are quotas and budgets monitored for sandbox usage?
- Does the sandbox include the production-like behavior needed by the test?
- Can multiple runs execute without naming collisions or state-lock contention?

## Failure modes

- Leaving expensive resources running after tests finish or fail.
- Sharing a sandbox so heavily that tests influence each other.
- Using production credentials because sandbox credentials were inconvenient.
- Creating a sandbox that is too different from production to catch relevant defects.
- Forgetting that destructive tests need isolated state as well as isolated resources.

## Agent trigger hints

Use this pattern when the user says or implies:

- sandbox testing
- isolated IaC tests
- ephemeral infrastructure test environment
- avoid testing in production
- cleanup test resources
- resource cost after tests
- test apply and destroy safely

## Source notes

Synthesized from the LANGETI 2020 paper's Section 3 practice description for sandbox testing. The paper highlights isolation from production and cleanup/cost concerns; this pattern generalizes those concerns into lifecycle and guardrail guidance.
