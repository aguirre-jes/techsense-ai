# Contributing to TechSense AI

This repository is intentionally small and governed by `REPO_STANDARDS.md`. Even if you are the only contributor, follow the same process for every change so the project stays reviewable and easy to automate.

## Before You Start

- Read [REPO_STANDARDS.md](REPO_STANDARDS.md).
- Read the current [CHANGELOG.md](CHANGELOG.md).
- Check [docs/system_design.md](docs/system_design.md) and [project_requirements.md](project_requirements.md) for scope.

## Contribution Rules

- Keep changes aligned with the serverless-first MVP.
- Place files in the correct directory.
- Update `CHANGELOG.md` for every new code or feature addition.
- Prefer small, reviewable changes over broad rewrites.
- Keep AWS spend and operational complexity low.

## Suggested Workflow

1. Create a short-lived `feature/*` branch.
2. Make one focused change.
3. Add or update tests when behavior changes.
4. Update `CHANGELOG.md`.
5. Validate the change locally.
6. Merge into `develop`, then promote to `main` when ready.

## Code and Docs Standards

- Keep Lambda code modular under `src/`.
- Keep OpenTofu under `infra/`.
- Keep architecture and operational guidance under `docs/`.
- Keep tests under `tests/`.
- Keep reusable utilities under `scripts/`.

## Pull Request Guidance

Even for solo work, write changes as if they will be reviewed:

- Describe what changed.
- Explain why the change fits the MVP budget and architecture.
- Call out any new dependencies or cost impact.
- Link to any relevant docs or standards.
