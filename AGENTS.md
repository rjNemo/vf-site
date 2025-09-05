# Repository Guidelines

## Project Structure & Modules

- `lib/`: static site generator code — `main.py` (entry point), `config.py`, `engine.py`.
- `pages/`: Jinja templates; layouts live in `pages/layouts/`.
- `data/`: page data in TOML; file name must match the template
  (e.g., `index.toml` → `index.html`).
- `assets/`: static files copied as‑is (`css/`, `js/`, `images/`, `webfonts/`).
- `dist/`: build output (generated, can be deleted/rebuilt).
- `config.toml`: required; at minimum `name = "VillaFleurie"`.

## Build, Test, and Development

- `make build`: renders templates into `dist/` (`pipenv run python -m lib.main`).
- `make run`: builds then serves `dist/` via `http.server`.
- `make lint`: format (`black`), lint/fix (`ruff`), and type‑check (`mypy`).
- Direct run: `pipenv run python -m lib.main`.
- Setup: `pipenv install --dev` (Python 3.11).

## Coding Style & Naming

- Python: formatted by `black` (120 cols), imports via `isort` (black profile),
  linted by `ruff`; type hints required (`mypy` with `disallow_untyped_defs`).
- Templates: Jinja; use inheritance with `pages/layouts/`. Prefer kebab‑case
  filenames (e.g., `t3-azur.html`).
- Data files: TOML mirroring template names (e.g., `t3-azur.toml`). Keep keys lower_snake_case.
- Modules: snake_case for Python files and identifiers.

## Testing Guidelines

- No formal test suite. Validate changes by:
  - Running `make lint` and fixing all issues.
  - Building with `make build` and visually checking pages in `dist/` (`make run`).
  - Verifying the correct data file is picked up for each template.

## Commit & Pull Requests

- Use Conventional Commits (seen in history):
  - Examples: `refactor(html): modernize header markup`,
    `feat(engine): add file watching`.
- PRs must:
  - Pass `make lint` and build cleanly.
  - Include a clear description, linked issues, and affected pages/files.
  - Add screenshots of visual changes (before/after) where relevant.
  - Stay focused and small; avoid mixed concerns.

## Revamp Spec & Branch

- Active branch: `revamp/website-spec`.
- Source of truth: `docs/spec/website-revamp-spec.md` (keep updated in PRs).
- Align changes to the agreed sitemap and CTAs defined in the spec.

## Configuration Tips

- Ensure `config.toml` exists at repo root; build fails without it.
- Do not commit generated `dist/` output.
