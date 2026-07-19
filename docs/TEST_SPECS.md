# TechSense Test Specs

## Purpose
Define the minimum quality gates for the MVP scoring Lambda. The goal is to keep the system reliable while preserving the low-cost, low-ops architecture.

## Quality Gate 1: Duplicate Filtering
### Requirement
The scoring Lambda must filter out duplicate articles before ranking them.

### Acceptance Criteria
- Duplicate items with the same content hash are not counted twice.
- If the same URL appears in multiple feeds, only one canonical article survives.
- The scoring output marks duplicates clearly or excludes them from the final candidate set.

### Why It Matters
Duplicate suppression protects the weekly email from noise and keeps Bedrock usage under control.

## Quality Gate 2: Valid JSON Output
### Requirement
The scoring Lambda must return valid JSON that conforms to the Article schema in `docs/DATA_SCHEMAS.json`.

### Acceptance Criteria
- The function response parses successfully as JSON.
- Required fields are present for each returned article.
- Field types match the schema expectations.
- Invalid or partial records are rejected before downstream processing.

### Why It Matters
Structured output is required for reliable handoff between ingestion, scoring, summarization, and delivery.

## Quality Gate 3: Empty Feed Handling
### Requirement
The scoring Lambda must handle empty RSS feeds gracefully.

### Acceptance Criteria
- No exception is thrown when a feed returns zero items.
- The function returns an empty candidate list or an explicit no-data status.
- The workflow can continue without failing the weekly digest.
- CloudWatch logs clearly indicate that the source was empty rather than broken.

### Why It Matters
A quiet feed should not break the MVP or force unnecessary retries.

## Test Notes
- Prefer fast unit tests over heavy integration tests for the MVP.
- Mock RSS input and DynamoDB writes.
- Keep test fixtures small and deterministic.
- Run tests in a way that does not require always-on infrastructure.

## AI-Ready Integration Schema
Use this schema when future AI agents generate or refine test cases.

```json
{
  "feature_name": "scoring_lambda_quality_gates",
  "priority": "high",
  "cost_impact_estimated": 0.15,
  "ai_agent_task": "Generate unit and contract tests that validate duplicate filtering, JSON correctness, and empty-feed behavior for the scoring Lambda.",
  "dependencies": ["AWS Lambda", "Amazon DynamoDB", "Article schema"]
}
```
