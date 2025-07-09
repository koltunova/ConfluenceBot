# ConfluenceBot Architecture

This document describes the current project structure and proposed high-level architecture for building an AI powered Confluence management tool.

## Goals

- Organize Confluence content using AI.
- Split one Confluence space into multiple spaces when needed.
- Move pages within the page tree.
- Generate documents from specific branches of the space tree.

## Current Code Overview

The project is a Python codebase with the following main components:

- **api_client.py** – wrappers around Confluence REST API calls (currently only page fetching).
- **page_model.py** – minimal `Page` class describing page attributes and hierarchy depth.
- **structure_builder.py** – utility to build a basic page tree from the API results.
- **migrate_logic.py** – placeholder for migration planning logic.
- **Scripts/** – small entry points for fetching data, building the structure and simulating migration.

A Visual Studio solution file (`ConfluenceBot.sln`) is included for convenience but the implementation is entirely Python.

## Proposed Functional Parts

1. **API Client**
   - Encapsulate all REST operations: fetching pages, creating spaces, moving pages, etc.
   - Handle pagination and authentication.

2. **Data Models**
   - Classes representing pages, spaces and other Confluence entities.
   - Provide helper methods to compute tree depth and relationships.

3. **AI Services**
   - Modules that call LLMs or local ML models to analyze page content.
   - Responsible for clustering pages or recommending moves to new spaces.

4. **Migration Planner**
   - Uses the AI services and existing page tree to plan how to split or reorganize spaces.
   - Produces actionable operations (move/create/delete) which can later be executed.

5. **Command Line Interface**
   - Entry points for common tasks like `fetch-structure`, `plan-migration`, `apply-migration`.
   - An interactive console UI will guide users through these commands. See [CONSOLE_UI.md](CONSOLE_UI.md) for an overview.

6. **Tests**
   - Unit tests for API wrappers and helper logic (to be created).

## Next Steps

- Expand the API client to include POST/PUT operations.
- Implement AI-driven clustering using an LLM provider.
- Flesh out the migration planner with real logic and tests.
- Provide examples of how to generate a consolidated document from a branch of the page tree.

