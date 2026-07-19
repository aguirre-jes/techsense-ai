# ADR-002: IaC Validation Flow for TechSense

## Status
Accepted

## Context
TechSense is a small side project, not a long-running enterprise platform. The infrastructure workflow should stay lightweight, flexible, and easy to change without introducing unnecessary process overhead.

The team still needs enough structure to avoid drift and to keep infrastructure changes safe. The question is how to validate OpenTofu changes without forcing an enterprise-grade release process.

## Decision
Use a lightweight IaC workflow with local validation first, remote state always, and CI assistance where it adds value.

For the TechSense MVP:

- Run `tofu init`, `tofu fmt`, `tofu validate`, and `tofu plan` locally during development.
- Use remote state from the beginning so state is not tied to one laptop.
- Allow direct local `tofu apply` for small, well-understood changes while the project remains a solo side project.
- Use GitHub Actions later as a helper for validation and plan review when the repo becomes more active.

## Rationale
This approach fits the actual scale of the project.

- It keeps the workflow lightweight.
- It avoids unnecessary enterprise ceremony.
- It still provides safety through planning and remote state.
- It supports fast iteration when a change is small and low risk.
- It allows the process to mature later without redesigning the whole repo.

The goal is not to force every infrastructure change through a heavy approval chain. The goal is to keep the project controlled without slowing it down.

## What Happens During the Bootstrap Phase
The first bootstrap can be executed locally from the maintainer machine.

Typical bootstrap actions may include:

- initializing the OpenTofu working directory,
- creating the remote backend,
- creating the first storage or state resources,
- establishing the minimum IAM and support resources needed for the MVP.

This is acceptable because the project is still small and the maintainer is the only operator.

## What Happens After Bootstrap
After the base is in place, the default behavior should be:

- validate locally,
- keep state remote,
- review the plan before applying,
- decide whether the change is safe enough for local apply or should be moved to a more controlled flow.

If the project grows, GitHub Actions can take over more of the validation burden without forcing a full enterprise pipeline immediately.

## Why Not a Fully CI-Driven Apply from Day One
A fully automated apply pipeline would be heavier than necessary for TechSense at this stage.

It would add:

- extra setup work,
- extra maintenance,
- extra failure modes,
- more process than the project needs right now.

That said, the repo should remain ready for CI-based review when the scope expands.

## Consequences
Positive:

- Fast iteration for a solo maintainer.
- Lower overhead.
- Better fit for a side project.
- Remote state reduces drift risk.
- The workflow can grow later without rework.

Tradeoffs:

- Local applies require discipline.
- Manual review matters more when CI is lightweight.
- The repo must keep strong documentation to avoid confusion.

## Related MVP Feature Tasks
Use the existing AI-ready schema for future IaC-related automation or backlog items.

```json
{
  "feature_name": "iac_validation_flow",
  "priority": "high",
  "cost_impact_estimated": 0.1,
  "ai_agent_task": "Design a lightweight OpenTofu validation flow that keeps local development fast while preserving remote state and reviewability.",
  "dependencies": ["OpenTofu", "GitHub Actions", "Remote State"]
}
```
