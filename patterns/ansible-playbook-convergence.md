---
id: iac.ansible-playbook-convergence
title: Ansible Playbook Convergence
type: delivery-pattern
status: draft
summary: Write Ansible playbooks as readable desired-state workflows that can be re-run safely, report real changes, and avoid unnecessary imperative shell logic.
tags:
  - infrastructure-as-code
  - ansible
  - idempotency
  - desired-state
  - configuration-management
  - drift-prevention
  - operability
aliases:
  - idempotent Ansible playbooks
  - Ansible desired state
  - playbook convergence
  - changed status in Ansible
applies_when:
  - Playbooks configure packages, files, services, users, cloud resources, or application state repeatedly.
  - Operators need to rerun automation after partial failure or drift.
  - Handlers, check mode, and change reporting drive downstream behavior.
avoid_when:
  - The task is intentionally a one-time migration with nonrepeatable side effects.
  - An external orchestrator owns state and Ansible is only invoking a controlled command.
related:
  - iac.idempotent-automation
  - iac.apply-code-continuously
  - iac.ansible-debugging-feedback-loop
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 1, 3, 7, 8, 19, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Playbook Convergence

## Intent

Make repeated Ansible runs converge systems toward the desired state without duplicating work, hiding drift, or reporting false changes.

## Use when

- A playbook will be run more than once against the same host or environment.
- Automation may be interrupted and resumed.
- Tasks notify handlers, trigger restarts, or gate later deployment steps based on changed status.
- The playbook replaces manual configuration procedures.
- Operators need check mode or diff mode to reason about expected changes.

## Avoid when

- The operation is inherently non-idempotent and should be wrapped in a purpose-built module or workflow.
- A migration requires explicit once-only tracking and rollback planning.
- Shell commands are safer because the target system lacks a reliable module and the command is carefully guarded.

## Context and problem

Ansible executes tasks top to bottom, which can make playbooks feel like scripts. But Ansible modules are most valuable when they describe desired state and return accurate change information. If a task uses raw shell commands without guards, always reports changed, or fails to handle existing state, reruns become risky and handlers fire unnecessarily.

The Ansible source presents idempotency as a core desired-state property and links it to check mode, module behavior, handlers, and best practices. This pattern narrows the generic idempotent automation principle to Ansible playbook construction.

## Forces

- Simple task order versus safe repeated convergence.
- Shell flexibility versus module-level state awareness.
- Accurate changed status versus shortcuts that always mutate.
- Readable playbooks versus too much conditional scaffolding.
- Fast local fixes versus durable operational reruns.

## Guidance

Prefer Ansible modules that model state over shell commands that perform actions. Make each task safe to repeat, and make changed status meaningful. Use handlers for changes that require restarts or reloads, but ensure the notifying tasks only report changed when the underlying state actually changed. Use check mode and assertions where they expose risk before mutation.

When a command is unavoidable, add `creates`, `removes`, `changed_when`, `failed_when`, explicit state checks, or a custom module so the playbook still behaves like convergent automation.

## Implementation moves

- Use modules with `state` parameters for packages, services, files, users, cloud resources, and templates.
- Guard command and shell tasks with idempotency checks.
- Set `changed_when` and `failed_when` deliberately for commands and probes.
- Use handlers for restart and reload actions caused by configuration changes.
- Support check mode for custom modules and critical tasks where practical.
- Add assertions for prerequisites and unsafe variable combinations.
- Run playbooks twice in test environments and expect the second run to report no changes except intentional probes.

## Checks

- Can the playbook be rerun after success without creating additional changes?
- Can the playbook be rerun after partial failure without manual cleanup?
- Do changed results correspond to actual desired-state changes?
- Are handlers triggered only by meaningful changes?
- Do shell and command tasks explain why a state-aware module was not used?
- Does check mode give useful evidence for high-risk changes?

## Failure modes

- Treating playbooks as procedural scripts and losing convergence.
- Using shell commands for state that Ansible modules already model.
- Letting every command report changed and causing unnecessary restarts.
- Hiding errors with broad `ignore_errors` instead of modeling expected state.
- Assuming a custom module is safe without implementing check mode and accurate changed results.

## Agent trigger hints

Use this pattern when the user says or implies:

- idempotent Ansible
- playbook reports changed every time
- Ansible handler keeps restarting service
- check mode support
- avoid shell module
- rerun playbook safely

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 1 on Ansible's desired-state model, Chapter 3 on tasks and handlers, Chapter 7 on application deployment, Chapter 8 on check mode and debugging, Chapter 19 on module changed results and check mode, and Chapter 24 on desired state. No source excerpts are stored here.
