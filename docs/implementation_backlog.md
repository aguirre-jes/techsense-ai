# TechSense MVP Implementation Backlog

This backlog is intentionally limited to the MVP. Every item must remain compatible with the annual $500 budget and the serverless-first architecture.

## Priority 0: Foundation

| ID | Feature | Priority | Cost Impact | AI-Ready Task | Dependencies |
| --- | --- | --- | --- | --- | --- |
| TS-MVP-001 | Project bootstrap | High | Low | Create the initial Lambda-first project structure and config files. | AWS Lambda, DynamoDB, Bedrock, SES |
| TS-MVP-002 | Article schema contract | High | Low | Implement the Article object contract used across ingestion and scoring. | DynamoDB, AWS Lambda |
| TS-MVP-003 | Resource naming standard | High | Low | Apply naming and tagging rules to every MVP resource. | AWS Lambda, DynamoDB, SES, EventBridge |

## Priority 1: Core MVP Flow

| ID | Feature | Priority | Cost Impact | AI-Ready Task | Dependencies |
| --- | --- | --- | --- | --- | --- |
| TS-MVP-010 | RSS ingestion Lambda | High | Low | Fetch and normalize the three selected RSS feeds. | AWS Lambda, DynamoDB |
| TS-MVP-011 | Deduplication logic | High | Low | Prevent duplicate articles from entering the digest pipeline. | AWS Lambda, DynamoDB |
| TS-MVP-012 | Relevance scoring | High | Low to Medium | Rank incoming articles using lightweight heuristics and selective LLM calls. | AWS Lambda, Amazon Bedrock, DynamoDB |
| TS-MVP-013 | Weekly summary generation | High | Medium | Produce concise summaries for the top five articles. | AWS Lambda, Amazon Bedrock |
| TS-MVP-014 | Email delivery | High | Low | Deliver the Friday digest through a single email channel. | AWS Lambda, Amazon SES |
| TS-MVP-015 | Friday scheduler | High | Low | Trigger the workflow once per week. | Amazon EventBridge |

## Priority 2: Operational Safety

| ID | Feature | Priority | Cost Impact | AI-Ready Task | Dependencies |
| --- | --- | --- | --- | --- | --- |
| TS-MVP-020 | Ingestion failure runbook | Medium | Low | Keep the recovery steps short and serverless-first. | CloudWatch, DynamoDB |
| TS-MVP-021 | Scoring quality gates | Medium | Low | Add tests for duplicate filtering, JSON validity, and empty-feed handling. | AWS Lambda, Article schema |
| TS-MVP-022 | Logging and observability | Medium | Low | Emit structured logs that support low-cost troubleshooting. | AWS Lambda, CloudWatch |

## Deferred to Later Phases

- ECS Fargate worker migration.
- Multi-agent orchestration.
- SQS-based fan-out.
- OpenTelemetry tracing.
- Telegram support unless explicitly reintroduced.

## Backlog Rules

- Do not move a task into implementation unless its cost impact is still acceptable under the annual budget.
- Avoid adding services that create idle spend before the MVP proves value.
- Keep the data model stable so later migration to Fargate does not require a redesign.
- Prefer the smallest change that moves the weekly digest closer to working end-to-end.
