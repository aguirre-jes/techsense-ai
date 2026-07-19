# ADR-001: Tech Stack for TechSense MVP

## Status
Accepted

## Context
TechSense Phase 1 is a weekly batch pipeline that ingests a small set of RSS feeds, ranks the items, summarizes the top five, and sends one email digest every Friday. The MVP has a hard annual budget cap of $500 USD and must stay serverless-first with low operational overhead.

The main architectural decision is whether the MVP should use AWS Lambda or ECS Fargate.

## Decision
Use AWS Lambda, Amazon DynamoDB, Amazon Bedrock, EventBridge Scheduler, and Amazon SES for the MVP.

## Rationale
Lambda is the better fit because the workload is periodic, short-lived, and low-volume. A weekly batch job does not need always-on containers, service discovery, or task orchestration. Lambda keeps costs aligned to actual executions, which is the safest way to stay within the $500/year budget.

This choice also matches the low-ops philosophy of the MVP:

- No container patching or cluster management.
- No idle compute cost.
- No baseline Fargate spend before product value is proven.
- Easy to start, easy to monitor, easy to replace later.

## Why Not Fargate for MVP
Fargate is a stronger choice only when the workload needs long-running workers, custom runtime packaging, or container-native scaling patterns. TechSense does not need those capabilities in Phase 1.

For the MVP, Fargate would add unnecessary cost and operational surface area without improving the user outcome. The workflow is a scheduled weekly digest, not a continuously running service.

## Consequences
Positive:

- Lower monthly spend.
- Faster MVP delivery.
- Easier maintenance.
- Better alignment with AWS free-tier-style usage.

Tradeoffs:

- The system must remain within Lambda execution limits.
- The architecture should avoid large in-memory processing.
- If the project evolves into continuous ingestion or multi-agent processing, a later migration to ECS Fargate may be justified.

## Related MVP Feature Tasks
Use this schema for future AI-assisted refinement of the MVP backlog.

```json
{
  "feature_name": "weekly_digest_pipeline",
  "priority": "high",
  "cost_impact_estimated": 0.75,
  "ai_agent_task": "Design the weekly Lambda-based RSS ingestion, scoring, summarization, and email delivery flow.",
  "dependencies": ["AWS Lambda", "Amazon DynamoDB", "Amazon Bedrock", "Amazon SES", "EventBridge Scheduler"]
}
```
