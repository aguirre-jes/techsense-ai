# TechSense AI

TechSense AI is a serverless-first AWS side project for curating high-signal technical news into a weekly Friday email digest. The MVP is intentionally constrained to keep the runtime small, the cost low, and the operational burden minimal.

## Project Intent

The goal is to reduce information overload by ingesting a small set of technical sources, filtering them with lightweight LLM reasoning, and delivering a top-five summary every week. The design is optimized to stay inside a strict $500/year budget and to evolve cleanly into later container-based phases if needed.

## High-Level Architecture

The MVP architecture follows the TechSense system design:

- Amazon EventBridge schedules the weekly run.
- AWS Lambda handles ingestion, scoring, summarization, and delivery.
- Amazon DynamoDB stores article state and deduplication metadata.
- Amazon Bedrock (Claude Haiku) provides concise reasoning and summarization.
- Amazon SES sends the weekly email digest.

This keeps the solution low-cost, low-ops, and compatible with AWS managed services.

## Repository Layout

- `src/` application source for Lambda functions.
- `infra/` OpenTofu infrastructure modules.
- `docs/` architecture, ADRs, schemas, runbooks, and standards.
- `tests/` unit and integration tests.
- `scripts/` helper automation scripts.
- `.github/workflows/` CI/CD workflows.

## Prerequisites

- AWS CLI
- OpenTofu
- Python 3.11 or newer
- Git

## Setup

1. Clone the repository.
2. Configure your AWS credentials with the AWS CLI.
3. Initialize the infrastructure workspace with OpenTofu.
4. Install Python dependencies for the Lambda and test environments.
5. Run the test suite before making changes.

## Documentation

Start with these files:

- [REPO_STANDARDS.md](REPO_STANDARDS.md)
- [project requirements](project_requirements.md)
- [docs/system_design.md](docs/system_design.md)
- [docs/README.md](docs/README.md)

## Governance

All new code and feature additions must follow the repository structure defined in `REPO_STANDARDS.md` and must add a matching entry to `CHANGELOG.md`.
