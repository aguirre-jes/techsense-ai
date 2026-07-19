# TechSense Mingrammer Diagrams

This folder contains the minimal `diagrams` scripts for TechSense.

## Files

- `techsense_context.py`: C4-style context view for the MVP.
- `techsense_mvp_aws_flow.py`: AWS-focused flow diagram for the MVP runtime.

## Render Requirements

To render these diagrams locally, install:

- `diagrams`
- `graphviz`

Example:

```bash
pip install diagrams graphviz
python3 techsense_context.py
python3 techsense_mvp_aws_flow.py
```

Each script writes a PNG file in the same folder when executed.
