---
id: iac.ansible-molecule-role-quality-gate
title: Ansible Molecule Role Quality Gate
type: testing-practice
status: draft
summary: Use Molecule scenarios, linters, dependency installation, convergence, cleanup, and verifiers as the standard quality gate for reusable Ansible roles.
tags:
  - infrastructure-as-code
  - ansible
  - molecule
  - testing
  - ci-cd
  - linting
  - roles
aliases:
  - Molecule for Ansible roles
  - ansible-lint quality gate
  - molecule test
  - test Ansible roles
applies_when:
  - A role will be reused, shared, published, or relied on in production.
  - The team needs automated evidence that a role converges and produces expected host state.
  - Different platforms, drivers, or dependency sets need scenario coverage.
avoid_when:
  - The content is a tiny one-off playbook with no reusable role boundary.
  - The driver cannot represent the target behavior and a remote or sandbox test is required instead.
related:
  - iac.automated-iac-test-harness
  - iac.remote-iac-testing
  - iac.behavior-focused-iac-test-coverage
  - iac.ansible-role-capability-boundary
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 14, 22, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Molecule Role Quality Gate

## Intent

Make reusable Ansible roles testable units by running a predictable Molecule workflow that installs dependencies, lints content, converges fixtures, verifies outcomes, and cleans up.

## Use when

- A role changes packages, files, services, users, security posture, images, or application configuration.
- CI should test Ansible content before it is promoted or consumed by other projects.
- Role behavior needs to be checked across distributions, containers, VMs, cloud targets, or Windows hosts.
- Linters need to enforce YAML and Ansible style before runtime tests.
- Tests should prove both convergence and expected final state.

## Avoid when

- A static lint check is enough and runtime behavior is irrelevant.
- The role mutates a shared external system that Molecule cannot isolate.
- Credentials, cleanup, or cost controls are not ready for unattended scenario execution.
- A full-stack integration test is needed before role-level tests would add useful signal.

## Context and problem

Reusable roles can fail because of syntax, style, missing dependencies, unsupported platforms, incorrect idempotency, or wrong final state. Manual role testing is inconsistent and hard to reproduce. Generic CI can run commands, but Ansible roles benefit from a harness that understands role layouts, scenarios, drivers, dependency phases, converge phases, verifier phases, and cleanup.

The Ansible source presents Molecule as the role-oriented testing framework, with drivers, linting, dependencies, convergence, cleanup, and verifiers such as Ansible assertions, Goss, or TestInfra. This pattern specializes the broader automated IaC test harness for Ansible roles.

## Forces

- Fast lint feedback versus slower provisioned scenario tests.
- Container convenience versus realism for systemd, Windows, network, or cloud behavior.
- Multiple scenarios versus test maintenance cost.
- Ansible-native assertions versus external verifiers.
- CI automation versus local developer usability.

## Guidance

Make Molecule the standard entry point for role quality when a role is expected to be reused. Start with lint and a default converge scenario, then add scenarios for supported platforms, dependency modes, and high-risk behaviors. Use the driver that matches the risk: containers for fast Linux role checks, delegated or provider drivers for behavior that needs real hosts or cloud resources.

Verify outcomes, not only successful task execution. A passing converge phase should be paired with assertions or verifier tests that inspect packages, services, ports, files, users, and application endpoints.

## Implementation moves

- Initialize or maintain a Molecule scenario under the role.
- Configure dependency installation for required roles and collections.
- Run YAML and Ansible linters before convergence.
- Use `molecule converge` during development and `molecule test` in CI.
- Add verifier steps with Ansible assertions, Goss, TestInfra, or equivalent checks.
- Add cleanup and destroy behavior for resources created by the scenario.
- Run the same quality gate locally and in CI with pinned dependencies.
- Add separate scenarios for materially different platforms or topology.

## Checks

- Does the role have at least one scenario that converges from a clean fixture?
- Does the gate run linters before runtime tests?
- Are role and collection dependencies installed from checked-in manifests?
- Does verification inspect final state, not only task success?
- Is cleanup reliable after both success and failure?
- Are scenario drivers chosen based on the behavior being tested?

## Failure modes

- Treating `molecule converge` as the only test and never verifying outcomes.
- Running linters locally but not in CI.
- Using a container driver for behavior that only fails on a real VM, cloud host, or Windows target.
- Allowing test dependencies to float independently of project dependencies.
- Leaving created hosts, networks, volumes, or cloud resources after failed scenarios.

## Agent trigger hints

Use this pattern when the user says or implies:

- Molecule test
- test Ansible role
- ansible-lint
- yamllint
- Goss or TestInfra verifier
- role quality gate

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 14 on Molecule, linters, drivers, and verifiers; Chapter 22 on CI/CD for Ansible roles; and Chapter 24 on testing roles. No source excerpts are stored here.
