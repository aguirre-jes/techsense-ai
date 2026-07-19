# ADR-003: IaC as the Source of Truth for TechSense

## Status
Accepted

## Context
TechSense is a small side project, but it still needs a reliable way to manage AWS infrastructure without creating drift or hidden manual changes.

The question is whether AWS resources should be created ad hoc from the console or managed consistently through Infrastructure as Code.

## Decision
All AWS resources that belong to TechSense must be defined and managed through Infrastructure as Code using OpenTofu.

This includes, but is not limited to:

- Lambda functions
- DynamoDB tables
- EventBridge schedules
- IAM roles and policies
- SES resources
- state backend resources
- supporting infrastructure needed by the MVP

## Rationale
This decision keeps TechSense predictable and easy to maintain.

- The repo becomes the source of truth.
- Infrastructure changes remain reviewable.
- Drift is reduced because resources are not managed manually.
- The project can evolve without losing traceability.
- AI-generated changes can follow the same structure as human changes.

For a small side project, this is the right level of rigor: enough discipline to stay clean, but not so much ceremony that it slows development down.

## Bootstrap Exception
A very small bootstrap step may be needed at the beginning of the project, for example to establish the first remote state resources or other minimal support infrastructure.

That exception is allowed only when it is clearly documented and quickly brought back under IaC management.

The exception does not change the rule. It only helps initialize the system safely.

## Operational Rule
Any infrastructure change must follow this principle:

1. Define it in OpenTofu.
2. Review the plan.
3. Apply it through the agreed TechSense IaC flow.
4. Keep the code and the real infrastructure aligned.

Manual console changes are not the normal operating model for TechSense.

## Consequences
Positive:

- Less configuration drift.
- Better reproducibility.
- Clearer ownership.
- Easier collaboration with AI agents.
- Stronger alignment with the repository standards.

Tradeoffs:

- Initial setup takes a little more discipline.
- Small fixes must still be reflected in code.
- The repo must stay organized to avoid IaC sprawl.

## Related MVP Feature Tasks
Use the existing AI-ready schema for future automation or backlog items related to infrastructure governance.

```json
{
  "feature_name": "iac_source_of_truth",
  "priority": "high",
  "cost_impact_estimated": 0.1,
  "ai_agent_task": "Keep TechSense AWS resources defined in OpenTofu and prevent manual drift from the repository source of truth.",
  "dependencies": ["OpenTofu", "GitHub Actions", "Remote State"]
}
```
