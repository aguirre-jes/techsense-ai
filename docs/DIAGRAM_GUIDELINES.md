# TechSense Diagram Guidelines

## Purpose

These guidelines define the minimum set of diagrams required to explain TechSense clearly without adding unnecessary documentation overhead.

TechSense is a small side project, so the diagram set should stay lightweight, useful, and easy to maintain.

## Minimum Diagram Set

### 1. C4 Context Diagram
Use this to show:

- who uses the system,
- what sources feed into it,
- what external services it depends on.

This diagram answers the question: "What is TechSense and what surrounds it?"

### 2. C4 Container Diagram
Use this to show:

- the main Lambda functions,
- DynamoDB,
- Bedrock,
- SES,
- EventBridge,
- how the MVP pieces connect.

This diagram answers the question: "How is the MVP broken down at a high level?"

## Optional Diagram Types

### AWS Component Diagram
Use an AWS-focused component diagram only when it adds real clarity.

This is useful when you want to explain internal service relationships or the flow inside the AWS implementation with more detail than a C4 Container diagram provides.

Recommended tool:

- `diagrams.mingrammer.com`

Use it when you want a clean AWS architecture drawing for:

- ingestion flow,
- scoring flow,
- delivery flow,
- OpenTofu-managed infrastructure layout.

### When Not to Add More Diagrams
Do not add extra diagrams if they only repeat information already covered by the context and container views.

For TechSense, avoid diagram sprawl. The documentation should stay small enough to be maintained by one person and by AI agents without friction.

## Recommended Visual Set for TechSense

1. C4 Context
2. C4 Container
3. Optional AWS component diagram for the MVP runtime flow
4. Optional IaC diagram if OpenTofu structure becomes more complex later

## Maintenance Rule

Every diagram must earn its place.

If a diagram does not improve understanding, reduce ambiguity, or help implementation, it should not be added.
