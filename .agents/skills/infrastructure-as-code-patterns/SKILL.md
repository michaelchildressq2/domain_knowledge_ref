---
name: infrastructure-as-code-patterns
description: Agent reference skill for Infrastructure as Code patterns, anti-patterns, principles, delivery practices, and decision guides synthesized from iac2 chapter text. Use for platform engineering, cloud architecture, safe infrastructure change, stack design, testing, governance, configuration, server images, clusters, and drift questions.
metadata:
  tags:
    - infrastructure-as-code
    - platform-engineering
    - cloud-architecture
    - safe-change
    - configuration-drift
    - reusable-stacks
    - environment-parity
    - testing
    - governance
    - secrets-management
    - modular-architecture
    - server-images
    - clusters
    - delivery-pipeline
---

# Infrastructure As Code Patterns

Use this skill when a user asks for guidance, critique, planning, or review related to Infrastructure as Code and platform engineering. Load only the relevant reference files; do not load the whole library unless the user asks for broad synthesis.

## How To Use

1. Start with `references/tags.md` when the request names a concept such as drift, reusable stacks, secrets, testing, governance, server images, clusters, rollback, or safe change.
2. Use `references/index.md` to browse patterns grouped by concern.
3. Load the specific files under `references/patterns/` that match the user's problem.
4. Apply the pattern guidance pragmatically. Check `Use when`, `Avoid when`, `Failure modes`, and `Checks` before recommending an approach.

## High-Value Entry Points

- Safe changes and rollout risk: `iac.safe-infrastructure-change`, `iac.reduce-change-scope`, `iac.rollback-rollforward-decision`.
- Stack and module design: `iac.reusable-stack`, `iac.component-boundaries`, `iac.monolithic-stack`, `iac.service-stack`.
- Drift and reproducibility: `iac.apply-code-continuously`, `iac.snowflake-system`, `iac.reproducible-infrastructure`.
- Testing and delivery: `iac.progressive-feedback`, `iac.risk-based-infrastructure-testing`, `iac.pipeline-delivered-infrastructure`.
- Configuration and secrets: `iac.externalized-configuration`, `iac.simple-stack-parameters`, `iac.secrets-out-of-source`.
- Servers and clusters: `iac.server-image-pipeline`, `iac.immutable-server-image`, `iac.cluster-as-code`.

## Source Policy

This skill contains original synthesized guidance and source pointers only. Do not reproduce long passages from the source chapter text.
