# Contributing to CapTrain

Thanks for your interest in contributing! CapTrain is an open, community-driven project building a unified ML/AI engineering layer that works for both humans (CLI) and AI agents (MCP).

We're in active early development, which means this is the perfect time to help shape the architecture, roadmap, and design. Every contribution counts — code, docs, tests, ideas, or a good question.

---

## Getting Started

Clone the repo and set up a local dev environment:

```bash
git clone https://github.com/masteryogo/captrain.git
cd captrain

# Sync dependencies (creates .venv with Python from .python-version)
uv sync --extra dev

# Run the test suite, linter, and type checks
uv run pytest
uv run ruff check .
uv run mypy src
```

## How to Contribute

1. **Check the roadmap** — see [README.md](./README.md#roadmap) for planned phases and open goals.
2. **Look for good first issues** — start with issues labeled `good-first-issue`.
3. **Open an issue first** for non-trivial changes to discuss design before writing code.
4. **Follow the branch workflow**:
   - `main` is protected. Always create a feature branch: `chore/xyz`, `feat/xyz`, or `fix/xyz`.
   - Keep changes focused and reviewable.
   - Open a Pull Request against `main`.

## Development Guidelines

- **Architecture first** — Core logic lives under `capmodels/src/captrain/core/`. CLI and MCP are thin wrappers over the core. No duplicated logic between interfaces.
- **Agent-friendly by design** — any new capability must expose structured output (JSON) for LLM consumption, not just human-readable text.
- **Write tests** — new functionality should ship with pytest tests under `capmodels/tests/`.
- **Keep it documented** — user-facing commands go in the README; complex decisions deserve a comment or docstring.

## Checklist Before Opening a PR

- [ ] Code follows the project structure (`core` central, CLI/MCP as thin wrappers)
- [ ] Tests pass locally (`pytest`)
- [ ] No secrets or credentials committed
- [ ] Public API changes reflected in the README
- [ ] Commits are concise and follow the repo style (conventional commit prefixes)

## Guidelines

- Be welcoming and respectful. We follow a code-of-conduct culture: assume good intent.
- Prefer small, incremental PRs over large monolithic ones.
- When in doubt, ask in the issue or PR thread — better safe than sorry.

## Getting Help

- Open a discussion in the [Issues](https://github.com/masteryogo/captrain/issues) tab.
- Reach out to maintainers for architecture or roadmap questions.

_This is a living document. If something feels off, contribute to improving it too!_
