This directory vendors the minimal Ruff pre-commit hooks so that pre-commit can run without network access.
The scripts wrap `uv run ruff` and `uv run ruff format` to use the project's pinned Ruff.
