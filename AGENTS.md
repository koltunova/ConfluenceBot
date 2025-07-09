# Guidelines for Codex Agents

This repository contains Python scripts to manage Confluence spaces. When making changes, please follow the rules below.

## Coding Style

- Prefer standard Python 3.10+ features.
- Run `black` with default settings on all `.py` files before committing.
- Keep modules small and focused.

## Build and Tests

- Attempt `dotnet restore && dotnet build -c Release` even though the codebase is Python only. The commands may fail if .NET is not installed; include the failure logs in the PR description.
- Python code does not currently include automated tests. When you add tests under `Tests/`, run them with `pytest`.

## Documentation

- Update `docs/ARCHITECTURE.md` if architectural changes are introduced.
- Keep the root `README.md` concise and point to further docs in the `docs/` directory.

