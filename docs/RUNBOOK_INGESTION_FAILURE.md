# Runbook: RSS Ingestion Failure

## Purpose
This runbook describes the lowest-cost operational response when the TechSense ingestion Lambda fails to fetch or store RSS content.

## Scope
Applies to the MVP only. The architecture assumes serverless Lambda ingestion, DynamoDB persistence, and weekly Friday execution.

## Symptoms
- No new articles appear in DynamoDB.
- The ingestion Lambda returns an error or times out.
- The weekly email digest is empty or missing expected items.
- CloudWatch logs show RSS fetch failures, permission errors, or serialization issues.

## Immediate Checks
1. Open the CloudWatch logs for the ingestion Lambda.
2. Confirm whether the failure is source-specific or global.
3. Check whether the RSS source is reachable from a browser or curl request.
4. Verify that the function still has permission to write to DynamoDB.
5. Confirm the Lambda execution role can access any required AWS services.

## Triage Steps

### 1. Check Source Connectivity
- Verify the RSS URL is valid and returns XML.
- Confirm the source is not rate-limiting requests.
- Check whether the source changed its feed format or moved the endpoint.
- If a single source fails, mark it degraded and continue with the remaining feeds if possible.

### 2. Check Lambda Execution Logs
- Review the latest error message in CloudWatch.
- Look for HTTP status codes, timeout errors, parsing failures, or malformed XML.
- Confirm the function completed within the expected time window.

### 3. Verify DynamoDB Permissions
- Confirm the ingestion Lambda role can call `PutItem`, `UpdateItem`, and `BatchWriteItem` if used.
- Verify the table name and region still match the deployed configuration.
- Ensure the table exists and the partition key definition has not changed.

### 4. Verify Data Validation
- Confirm the ingestion Lambda is normalizing fields before writing records.
- Check whether required article fields are missing or empty.
- Make sure deduplication keys are stable across retries.

### 5. Re-run the Workflow
- If the issue is transient, rerun the ingestion Lambda manually.
- If only one source is broken, remove it temporarily from the weekly run and note the degradation.
- If the failure persists, stop at one retry and escalate the source or schema issue instead of adding operational complexity.

## Recovery Actions
- Restore the feed URL if it changed.
- Update parsing logic only if the feed format has legitimately changed.
- Fix IAM permissions if DynamoDB writes are failing.
- Re-deploy the Lambda only after the root cause is confirmed.
- Keep the solution simple and serverless-first; do not move the MVP to containers just to handle a feed issue.

## Prevention
- Keep feed URLs in configuration, not in code.
- Use small health checks for each source.
- Store structured errors in CloudWatch logs.
- Add unit tests for feed parsing and DynamoDB serialization.
- Keep the ingestion path minimal so failures are easier to isolate.

## AI-Ready Integration Schema
Use this structure when asking an AI agent to diagnose an ingestion failure.

```json
{
  "feature_name": "ingestion_failure_triage",
  "priority": "high",
  "cost_impact_estimated": 0.1,
  "ai_agent_task": "Analyze ingestion logs, source reachability, and DynamoDB permissions to isolate the failure cause.",
  "dependencies": ["AWS Lambda", "Amazon DynamoDB", "Amazon CloudWatch"]
}
```
