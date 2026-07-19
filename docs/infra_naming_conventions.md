# TechSense Infrastructure Naming Conventions

## Goals
The naming standard must support three objectives:

- Keep the MVP easy to operate.
- Make AWS cost tracking and ownership obvious.
- Keep resource names consistent across future AI-generated changes.

## Naming Pattern
Use this general pattern for all MVP resources:

`ts-mvp-<resource_type>-<purpose>-<region>`

### Examples
- `ts-mvp-lambda-ingest-us-east-1`
- `ts-mvp-lambda-score-us-east-1`
- `ts-mvp-lambda-summarize-us-east-1`
- `ts-mvp-lambda-deliver-us-east-1`
- `ts-mvp-dynamodb-articles-us-east-1`
- `ts-mvp-ses-email-us-east-1`
- `ts-mvp-eventbridge-friday-us-east-1`

## Naming Rules
- Use only lowercase letters, numbers, and hyphens.
- Keep names short but descriptive.
- Include the environment prefix `mvp` for all Phase 1 resources.
- Include the AWS region in the name when supported.
- Prefer one purpose per resource so cost attribution stays clear.
- Avoid ambiguous names such as `app`, `main`, or `service`.

## Resource-Type Abbreviations
- `lambda` for AWS Lambda functions.
- `dynamodb` for tables.
- `ses` for email delivery resources.
- `eventbridge` for schedules or rules.
- `logs` for log groups.
- `role` for IAM roles.
- `policy` for IAM policies.

## Cost-Tracking Guidance
The naming convention supports cost visibility by making it easy to identify MVP-only resources in billing reports, tags, and CloudWatch logs.

Recommended tags for every resource:

- `Project = TechSense`
- `Environment = mvp`
- `Owner = <team-or-person>`
- `CostCenter = aws-credits`
- `Workload = weekly-digest`

## AI-Ready Integration Schema
Use the following schema whenever future automation needs to add or rename infrastructure.

```json
{
  "feature_name": "infra_resource_naming",
  "priority": "medium",
  "cost_impact_estimated": 0.05,
  "ai_agent_task": "Generate AWS resource names and tags that remain consistent with the TechSense MVP naming standard.",
  "dependencies": ["AWS Lambda", "Amazon DynamoDB", "Amazon SES", "Amazon EventBridge"]
}
```
