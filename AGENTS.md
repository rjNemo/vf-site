# Repository Guidelines

## Project Structure & Modules

- `src/`: Astro app — `pages/` (locale folders: `fr/`, `en/`), `layouts/`, `styles/`.
- `src/i18n/routes.ts`: central route manifest (`hrefFor`, `siblingPath`) for FR/EN slugs.
- `public/`: static assets and redirects (`_redirects`, `assets/images`, `webfonts`, etc.).
- `docs/spec/website-revamp-spec.md`: product/UX spec and release plan (source of truth).
- Legacy: `lib/`, `pages/`, `data/` (Python generator) — deprecated; do not modify.

## Build, Test, and Development

- Setup: `corepack enable && pnpm i` (uses `pnpm@10`).
- Dev server: `pnpm dev` (Astro). Build: `pnpm build`. Preview: `pnpm preview`.
- Deploy: Netlify (static). Redirects in `public/_redirects` (root → `/fr/`).
- Analytics: Plausible (`plausible("event", {props})`).

## Coding Style & Conventions

- UI: Tailwind CSS v4 (brand tokens: `--color-brand`, `--color-brand-600`).
- Icons: `lucide-astro` inline SVGs; use `text-brand` for accent.
- JS: vanilla only (no jQuery). Prefer lightweight patterns (e.g., scrollBy carousels).
- i18n: prefer `getRelativeLocaleUrl()` from `astro:i18n` for links; use `siblingPath()` for toggles when slugs differ.
- Content slugs differ by locale (e.g., FR `avis` ↔ EN `reviews`) — never hardcode.

## Testing Guidelines

- Sanity: `pnpm build` must succeed. Then `pnpm preview` for visual QA.
- Check: FR/EN toggles, redirects (`/ → /fr/`), forms (Netlify), and analytics events.
- Accessibility: keyboard nav for mobile menu; color contrast for brand accents.

## Commit & Pull Requests

- Conventional Commits (examples): `feat(home): hero CTA`, `fix(i18n): toggle sibling path`.
- PRs should include: build passing, screenshots (FR/EN), and spec updates when needed.
- Keep focused and small; avoid mixing refactors with features.

## Revamp Spec & Phases

- Branch: `revamp/website-spec`. Spec: `docs/spec/website-revamp-spec.md`.
- Phase 1 (current): FR core pages, inquiry form, i18n scaffolding.
- Phase 2: EN pages + gallery, translated reviews.
- Phase 3: Policies, analytics KPIs, performance polish (WebP/srcset, Lighthouse).

## Notes

- Do not commit `dist/`. Assets live in `public/assets/...`.
- Use the route manifest for any new pages/links; add entries for new slugs.
