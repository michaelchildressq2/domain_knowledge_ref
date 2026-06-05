---
id: iac.test-every-iac-change
title: Test Every IaC Change
type: delivery-practice
status: draft
summary: Trigger an appropriate IaC test path for every infrastructure change, and supplement change-triggered tests with scheduled runs that catch environmental drift.
tags:
  - infrastructure-as-code
  - testing
  - continuous-integration
  - delivery-pipeline
  - drift-detection
  - feedback
aliases:
  - testing every iac change
  - test every infrastructure change
  - iac ci tests
  - scheduled infrastructure tests
applies_when:
  - IaC changes are reviewed through pull requests, merge requests, commits, or release branches.
  - Dependency, image, platform, or provider changes can break infrastructure even when source code changes look small.
avoid_when:
  - The repository is an abandoned prototype or non-shared experiment.
  - The only available tests are slow destructive checks and no progressive test path exists yet.
related:
  - iac.progressive-feedback
  - iac.pipeline-delivered-infrastructure
  - iac.apply-code-continuously
  - iac.safe-infrastructure-change
sources:
  - "paper: Hasan, Bhuiyan, and Rahman, Testing Practices for Infrastructure as Code, LANGETI 2020; Section 3, Testing Every IaC Change."
source_confidence: medium
last_reviewed: 2026-06-05
---

# Test Every IaC Change

## Intent

Ensure each infrastructure change receives timely validation, while scheduled test runs catch failures caused by environmental changes outside the repository.

## Use when

- IaC is delivered through CI/CD, pull requests, merge requests, or release pipelines.
- Small dependency or configuration changes can break provisioning, bootstrap, or runtime behavior.
- The team wants faster feedback on infrastructure defects before apply or promotion.
- IaC modules support multiple platforms, regions, environments, or versions.
- External dependencies such as base images, packages, provider APIs, or OS updates change independently.

## Avoid when

- Every available test requires expensive remote provisioning and would make normal development unusable.
- The test suite is flaky enough that triggering it on every change would reduce trust.
- A change affects only documentation and the pipeline cannot cheaply determine that.
- The organization has no owner for failed scheduled tests.

## Context and problem

IaC defects often surface after a change is merged or applied, when feedback is slow and expensive. Teams may test only large changes, release candidates, or manual deployment windows, which leaves dependency defects and cross-platform regressions undiscovered.

The paper identifies testing every IaC change as a recurring practice and also notes that periodic tests can catch environmental changes even when the IaC source has not changed. The resulting pattern is a two-trigger model: validate every source change with an appropriate test path, and run scheduled checks for dependency and environment drift.

## Forces

- Frequent tests improve feedback, but exhaustive tests can be too slow for every commit.
- IaC depends on external systems that change without source commits.
- Pull-request contributors need quick, actionable failures.
- Release managers need deeper confidence before promotion.
- Scheduled failures are useful only when someone owns triage and repair.

## Guidance

Build a progressive CI path for every IaC change. Start with fast deterministic checks, then run deeper plan, policy, sandbox, or remote tests based on risk and affected scope. Do not let expensive tests become an excuse for no per-change validation.

Add scheduled test runs for common usage scenarios, supported platforms, or critical modules. Scheduled runs should detect drift from provider changes, OS updates, dependency releases, image refreshes, and policy changes. Treat scheduled failures as real work, not background noise.

## Implementation moves

- Trigger fast checks on every pull request, merge request, and commit to protected branches.
- Use path filters or dependency mapping to select the relevant module and environment tests.
- Run formatting, validation, linting, policy, and plan checks before provisioning.
- Gate risky changes with sandbox or remote tests before apply or promotion.
- Schedule periodic tests for critical modules and supported platform combinations.
- Report failures with affected module, environment, provider, and dependency context.
- Track test duration and split slow checks into later pipeline stages when needed.

## Checks

- Does every IaC code path have at least one automatic check on change?
- Are high-risk changes routed to deeper tests before production impact?
- Are scheduled tests configured for dependencies that change outside source control?
- Can contributors see failures without needing deployment credentials?
- Is there an owner and service-level expectation for broken scheduled tests?
- Are documentation-only or metadata-only changes handled without wasting expensive test resources?

## Failure modes

- Running only slow full-environment tests until developers avoid the pipeline.
- Skipping small changes because they look harmless.
- Treating scheduled drift failures as optional alerts that no one owns.
- Using path filters that miss shared module dependencies.
- Allowing flaky tests to block every change without investing in stabilization.

## Agent trigger hints

Use this pattern when the user says or implies:

- test every IaC change
- CI for Terraform or Ansible
- validate every infrastructure pull request
- scheduled infrastructure tests
- catch dependency defects
- weekly IaC tests
- feedback on infrastructure changes

## Source notes

Synthesized from the LANGETI 2020 paper's Section 3 practice description for testing every IaC change and regular interval testing. The paper reports this as an observed practitioner practice; this file normalizes it into CI and scheduled-validation guidance.
