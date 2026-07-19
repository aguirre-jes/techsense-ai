# TechSense Documentation Index

This folder is the source of truth for the TechSense MVP (Phase 1). All future implementation work should stay aligned with the $500/year budget cap and the serverless-first architecture.

## Read Order

1. [project requirements](../project_requirements.md) - business goals, roadmap, source shortlist, and budget framing.
2. [system design](./system_design.md) - MVP architecture, C4 views, cost controls, and AI-ready integration schema.
3. [ADR-001-TechStack](./ADR-001-TechStack.md) - why Lambda is the right MVP foundation.
4. [data schemas](./DATA_SCHEMAS.json) - Article contract between ingestion and scoring.
5. [infra naming conventions](./INFRA_NAMING_CONVENTIONS.md) - AWS resource naming and tagging rules.
6. [runbook ingestion failure](./RUNBOOK_INGESTION_FAILURE.md) - operational guidance for feed or write failures.
7. [test specs](./TEST_SPECS.md) - quality gates for the scoring Lambda.

## Source of Truth Rules

- Do not introduce infrastructure that violates the serverless-first MVP plan without a documented decision.
- Keep every proposed feature inside the low-cost, low-ops operating model.
- Prefer AWS managed services already present in the MVP design.
- Use the AI-ready integration schema from the system design for future backlog items.

## Document Map

- Requirements: what the product must do.
- System design: how the MVP is built.
- ADR: why the core tech stack was selected.
- Data schema: what flows between Lambdas.
- Naming conventions: how AWS resources are labeled.
- Runbook: what to do when ingestion fails.
- Test specs: how quality is enforced before release.
