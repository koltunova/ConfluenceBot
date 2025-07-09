# Console UI

This document outlines the planned command-line interface (CLI) for ConfluenceBot. It will guide users through typical tasks without requiring them to remember individual scripts.

## Usage

Run the CLI entry point:

```bash
python -m confluencebot
```

A menu will appear offering actions such as fetching the current space structure, planning migrations and generating consolidated documents.

## Features

- **Fetch structure** – download pages from Confluence and display the hierarchy.
- **Plan migration** – analyze pages using AI and produce a recommended set of moves.
- **Apply migration** – execute the plan by calling the Confluence REST API.
- **Export document** – gather pages from a chosen branch and produce a single document.

For now these commands are mocked, but they describe the intended console experience.
