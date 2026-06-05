---
id: iac.terraform-team-delivery-workflow
title: Terraform Team Delivery Workflow
type: delivery-pattern
status: draft
summary: Make Terraform a team workflow with incremental adoption, version control, review, automated checks, controlled applies, and promotion paths for infrastructure changes.
tags:
  - infrastructure-as-code
  - terraform
  - team-workflow
  - ci-cd
  - code-review
  - adoption
  - delivery-pipeline
  - governance
aliases:
  - Terraform as a team
  - Terraform workflow
  - Terraform CI CD
  - infrastructure code review
  - Terraform adoption
  - Terraform pull request workflow
applies_when:
  - Terraform is moving from individual use to a shared team or organization workflow.
  - Infrastructure changes need review, testing, approval, apply control, and promotion.
avoid_when:
  - The user is running a one-person local experiment with no shared infrastructure.
  - The organization already has an equivalent managed workflow and only needs stack-specific configuration.
related:
  - iac.pipeline-delivered-infrastructure
  - iac.test-every-iac-change
  - iac.version-controlled-infrastructure
  - iac.safe-infrastructure-change
  - iac.team-workflow-metrics
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 10, How to Use Terraform as a Team."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Team Delivery Workflow

## Intent

Turn Terraform from a local operator tool into a disciplined team delivery process that preserves reviewability, safety, learning, and deployment flow.

## Use when

- Multiple people or teams change Terraform code.
- Infrastructure changes need pull requests, reviews, automated tests, and controlled applies.
- Terraform adoption requires cultural and process change, not just tool installation.
- Teams need to coordinate application deployment and infrastructure deployment workflows.
- Management, security, or operations stakeholders need evidence that Terraform reduces risk.

## Avoid when

- A lightweight local workflow is sufficient and formal process would only slow learning.
- The team has not yet agreed which infrastructure should be managed by Terraform.
- A central platform already enforces review, policy, state, and apply workflows.
- The process focuses on approvals but lacks automated evidence.

## Context and problem

Terraform works differently when one person runs it locally than when a team uses it to manage shared infrastructure. Team use introduces concurrent edits, code ownership, skills gaps, review expectations, credentials, state access, CI/CD, and production change control. Without a workflow, teams either keep applying manually from laptops or add process that slows delivery without improving safety.

Adoption is also a change-management problem. Infrastructure as code requires people to stop making direct manual changes and instead trust an indirect workflow: edit code, review, test, merge, and apply through automation.

## Forces

- IaC improves repeatability, but adoption has skill, tooling, mindset, and opportunity costs.
- Reviews improve safety, but reviewers need plan and test evidence to evaluate changes.
- Automated applies reduce laptop risk, but they require credentials, state, and policy controls.
- Incremental adoption delivers learning, but partial adoption can leave unmanaged drift.
- Infrastructure and application deployment workflows need coordination without becoming one giant release.

## Guidance

Adopt Terraform incrementally around concrete business and operational pain. Put all Terraform code in version control, require review for shared infrastructure, run automated checks on every change, and apply from a controlled pipeline or managed workflow rather than individual laptops.

Separate concerns in the workflow: developers propose changes, CI produces evidence, reviewers assess code and plan impact, and controlled automation applies approved changes with the right credentials. Teach the team how to read plans, recover from failed applies, and avoid manual drift.

## Implementation moves

- Start with a bounded use case that delivers visible value and manageable risk.
- Put Terraform code, examples, tests, and module versions in version control.
- Use pull requests or merge requests for infrastructure changes.
- Run format, validate, lint, policy, plan, and risk-based tests in CI.
- Show plan output in review while protecting secrets.
- Apply from CI/CD, Terraform Cloud, or another controlled runner with scoped credentials.
- Define who can approve and who can apply for each environment.
- Document break-glass and drift reconciliation procedures.
- Invest in onboarding so team members understand Terraform language, state, plans, and failure modes.

## Checks

- Can every production infrastructure change be traced to a reviewed commit?
- Do reviewers see plan and policy evidence before approval?
- Are applies performed by controlled automation rather than untracked laptops?
- Are credentials scoped by environment and stack?
- Is manual drift detected and reconciled back into code?
- Does the team have time and material to learn the new workflow?

## Failure modes

- Mandating Terraform everywhere before the team has skills, examples, and support.
- Keeping source in version control but applying manually with local credentials.
- Treating plan review as optional because the code review looks simple.
- Combining too many unrelated stacks into one approval and apply path.
- Measuring adoption by tool usage instead of safer, faster, more reliable delivery.

## Agent trigger hints

Use this pattern when the user says or implies:

- Terraform as a team
- Terraform workflow
- Terraform pull requests
- Terraform CI/CD
- who should run terraform apply
- infrastructure code review
- adopt Terraform incrementally
- Terraform governance

## Source notes

Synthesized from Chapter 10 of Terraform: Up & Running, third edition, including adoption guidance, version control, commit hooks, automated tests, infrastructure deployment workflow, and putting team practices together. No source excerpts are stored here.
