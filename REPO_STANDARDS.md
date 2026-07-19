# TechSense Repository Governance & Structure Standards

## Purpose

This document defines the repository conventions for TechSense so future implementation work stays consistent, reviewable, and easy for AI agents to navigate. The standards are optimized for a small AWS serverless project with a strict $500/year budget and a low-ops operating model.

## 1. Repository Principles

- Keep the repository modular and predictable.
- Separate application code, infrastructure, documentation, tests, scripts, and CI/CD concerns.
- Prefer explicit file ownership and narrow directories over shared catch-all folders.
- Treat documentation as part of the product, not as an afterthought.
- Keep every addition compatible with the MVP serverless-first architecture.

## 2. Canonical Directory Structure

The repository must follow this top-level layout:

```text
techsense/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
├── REPO_STANDARDS.md
├── src/
│   ├── ingest/
│   ├── score/
│   ├── summarize/
│   └── deliver/
├── infra/
│   ├── modules/
│   ├── environments/
│   └── state/
├── docs/
│   ├── ADR-001-TechStack.md
│   ├── DATA_SCHEMAS.json
│   ├── INFRA_NAMING_CONVENTIONS.md
│   ├── RUNBOOK_INGESTION_FAILURE.md
│   ├── system_design.md
│   └── TEST_SPECS.md
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/
│   ├── bash/
│   └── python/
└── .github/
    └── workflows/
```

## 3. Directory Responsibilities

### `src/`
All application source code lives here. For TechSense MVP, this means AWS Lambda function code only. Each Lambda should have its own bounded module so the ingestion, scoring, summarization, and delivery paths remain isolated.

### `infra/`
All OpenTofu configuration lives here. Use reusable modules, environment-specific definitions, and separate state management concerns. The infrastructure layer must remain aligned with the serverless-first design in `docs/system_design.md`.

### `docs/`
All architecture and governance documents live here. This includes ADRs, schemas, runbooks, test specs, and system design references. The docs folder is the repository-level source of truth for future AI-generated changes.

### `tests/`
All test suites live here. Keep unit tests separate from integration tests so the MVP can validate business logic quickly without requiring full cloud deployment for every check.

### `scripts/`
Reusable automation scripts live here. Use this folder for local helpers, build support, cleanup utilities, and repository automation that should not be embedded inside application code.

### `.github/`
CI/CD workflows live here. Use GitHub Actions to automate linting, testing, packaging, and infrastructure validation.

## 4. Standard Root Files

The repository must always contain the following root files:

- `README.md` for setup, architecture summary, and day-one usage.
- `CONTRIBUTING.md` for feature submission, code review, and documentation rules.
- `CHANGELOG.md` for project history and visible evolution.
- `.gitignore` for Python, OpenTofu, AWS, and local environment artifacts.
- `REPO_STANDARDS.md` for governance, layout, and repo-level conventions.

## 5. Branching Strategy

Use a lightweight Git-Flow model suitable for a side project:

- `main`: Always stable and release-ready.
- `develop`: Integration branch for work that is nearly complete.
- `feature/*`: Short-lived branches for one change at a time.

### Branch Rules

- Merge feature branches into `develop` first.
- Merge `develop` into `main` only when a versioned release is ready.
- Avoid long-lived branches that drift from the current architecture.
- Keep branch names descriptive and scoped to one task.

### Example Branch Names

- `feature/rss-ingestion-lambda`
- `feature/dynamodb-article-schema`
- `feature/email-digest-delivery`
- `feature/infra-tofu-bootstrap`

## 6. Change Governance

Every new code or feature addition must satisfy both of these rules:

1. Add or update the corresponding entry in `CHANGELOG.md`.
2. Place the change in the correct directory according to this document.

No feature should bypass the directory structure or appear as an untracked ad hoc file at the repository root.

## 7. AI-Governance Rule

Any AI-generated code must follow the repository structure and must include a matching changelog entry before it is considered complete.

This rule exists to prevent invisible drift and to keep AI-generated changes reviewable, traceable, and easy to audit.

### Required AI Metadata Pattern

When an AI agent proposes a new feature, it should be mapped to the existing TechSense AI-ready schema pattern from `docs/system_design.md`.

```json
{
  "feature_name": "string",
  "priority": "low|medium|high",
  "cost_impact_estimated": "float",
  "ai_agent_task": "string",
  "dependencies": ["list_of_services"]
}
```

## 8. Python, OpenTofu, and AWS Hygiene

### Python
- Keep virtual environments out of source control.
- Ignore `__pycache__`, `.pytest_cache`, `.mypy_cache`, and build artifacts.

### OpenTofu
- Ignore local state, crash logs, and temporary plan files.
- Never commit generated state or secrets.

### AWS and Environment Secrets
- Ignore local `.env` files and credentials.
- Never commit access keys, session tokens, or deployment secrets.

## 9. Why This Structure Helps AI Agents

This structure makes AI agents more effective because each responsibility has a predictable home.

- Narrow directories reduce context switching.
- Clear file names make retrieval and modification safer.
- Separate docs, infra, source, and tests let an agent scope its reasoning correctly.
- The changelog requirement forces every change to be documented, which improves traceability.
- The branching model reduces ambiguity about what is stable, what is in progress, and what is isolated.
- The repo becomes easier to map into small tasks, which is exactly what AI-assisted development needs.

## 10. Compliance Summary

A TechSense change is compliant only if it:

- Follows the directory structure in this document.
- Keeps the MVP serverless-first and cost-aware.
- Updates `CHANGELOG.md` for any new code or feature.
- Remains consistent with `docs/system_design.md` and `project_requirements.md`.
