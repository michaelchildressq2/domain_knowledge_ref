---
id: iac.terraform-test-strategy
title: Terraform Test Strategy
type: testing-pattern
status: draft
summary: Combine static, plan, unit, integration, and end-to-end Terraform tests so each risk is checked at the cheapest layer that can catch it.
tags:
  - infrastructure-as-code
  - terraform
  - testing
  - unit-testing
  - integration-testing
  - plan-testing
  - end-to-end-testing
  - ci-cd
aliases:
  - test Terraform code
  - Terraform testing pyramid
  - Terratest strategy
  - Terraform unit tests
  - Terraform integration tests
  - Terraform plan tests
applies_when:
  - Terraform code manages production-like infrastructure or reusable modules.
  - The team wants confidence beyond manual `terraform apply` and visual inspection.
avoid_when:
  - A disposable experiment has no shared, persistent, or production consequence.
  - The proposed test layer duplicates a cheaper check without catching additional risk.
related:
  - iac.risk-based-infrastructure-testing
  - iac.behavior-focused-iac-test-coverage
  - iac.sandbox-iac-testing
  - iac.test-every-iac-change
  - iac.terraform-production-module-design
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 9, How to Test Terraform Code."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Test Strategy

## Intent

Give Terraform changes credible safety evidence by matching test layers to the risks they can actually detect.

## Use when

- Terraform code is reviewed, shared, or promoted through CI/CD.
- Reusable modules need validation before consumers adopt a version.
- Manual testing is too slow, inconsistent, or risky.
- Changes can affect availability, security, cost, data, networking, or identity.
- The team needs a test plan for local development and automated pipelines.

## Avoid when

- The infrastructure is intentionally short-lived and the cost of defects is negligible.
- Every test would require full production-scale provisioning and no smaller fixture is possible.
- The team has not yet identified the behavior or risk each test should cover.
- Tests are written only to increase count, not confidence.

## Context and problem

Terraform tests can range from syntax checks to full end-to-end deployments. Teams often jump from no tests to expensive integration tests, then abandon the suite when it is slow or flaky. Others rely only on `plan`, which can catch many issues but cannot prove that real infrastructure and applications work together.

A good Terraform test strategy is layered. It uses static and plan checks for fast feedback, unit tests for module logic and contract behavior, integration tests for real infrastructure fixtures, and end-to-end tests for user-visible workflows where the extra cost is justified.

## Forces

- Fast tests are easy to run often, but they may miss provider and runtime behavior.
- Real apply tests catch more defects, but they need credentials, isolation, cleanup, time, and budget.
- Plan tests inspect intent before apply, but valid plans can still fail.
- End-to-end tests provide high confidence, but they are expensive and brittle if overused.
- Terraform modules are easier to test when designed with small contracts and examples.

## Guidance

Start every Terraform pipeline with cheap deterministic checks: formatting, validation, linting, static policy, and plan review. Add deeper tests only for risks those checks cannot catch. For modules, create examples or fixtures that can be applied in isolated environments. Use behavior-focused assertions over snapshots of incidental provider output.

Run expensive tests selectively by risk, schedule, or release boundary. Ensure any test that creates resources also owns cleanup, naming, retries, logging, and cost controls.

## Implementation moves

- Define the defect classes the test strategy must catch.
- Run `fmt`, `validate`, lint, and policy checks before any provider-backed test.
- Add plan tests for expected resources, forbidden changes, tags, encryption, IAM, and destructive actions.
- Add unit tests for module input validation, generated expressions, and contract behavior where feasible.
- Add integration tests that apply representative fixtures in isolated accounts, projects, or namespaces.
- Add end-to-end tests only for critical workflows that require full system behavior.
- Use unique names, TTL tags, and automated cleanup for apply-based tests.
- Publish test results and logs in CI without exposing secrets.

## Checks

- Does each test have a named risk it reduces?
- Are fast checks run before expensive infrastructure creation?
- Are integration fixtures smaller than production but realistic for the behavior under test?
- Does every apply-based test clean up on success, failure, and cancellation?
- Are destructive plan actions reviewed or blocked for protected resources?
- Are flaky tests fixed or quarantined with an owner rather than normalized?

## Failure modes

- Treating `terraform plan` as proof that the deployed system will work.
- Running full end-to-end tests for every small change until developers bypass them.
- Creating cloud resources in tests without reliable cleanup.
- Snapshot-testing noisy provider output instead of stable behavior.
- Writing tests after module design is fixed, then discovering the module is too monolithic to test.

## Agent trigger hints

Use this pattern when the user says or implies:

- how to test Terraform
- Terraform test strategy
- Terratest
- plan tests
- integration tests for Terraform
- end-to-end infrastructure tests
- Terraform CI checks
- valid plan can fail

## Source notes

Synthesized from Chapter 9 of Terraform: Up & Running, third edition, including manual tests, cleanup, automated tests, unit tests, integration tests, end-to-end tests, static analysis, and plan testing. No source excerpts are stored here.
