# VillaFleurie Website (Astro + Tailwind)

This site is built with Astro and Tailwind, with FR/EN locales. The legacy Python generator remains for reference but is deprecated — new work happens in `src/`.

## Quick Start

- Requirements: Node 18+, Corepack enabled (`pnpm`). Then:
  - `corepack enable`
  - `pnpm install`
- Dev server: `pnpm dev` → open `http://localhost:4321/fr/` (root redirects to `/fr/`).
- Build: `pnpm build` → static output in `dist/`. Preview: `pnpm preview`.

## Structure

- `src/pages/fr|en/`: localized pages (Home, Apartments, Reviews, Rates, Contact, Policies).
- `src/layouts/`: shared layout with sticky header, language toggle, footer.
- `src/styles/global.css`: Tailwind v4 with brand tokens (`--color-brand`, `--color-brand-600`).
- `src/i18n/routes.ts`: route manifest (`siblingPath`, CTA label helper).
- `public/`: static assets + `_redirects` (root → `/fr/`).
- Spec: `docs/spec/website-revamp-spec.md` (goals, sitemap, copy, release plan).

## i18n & Navigation

- Folder-based locales with different slugs (e.g., FR `avis` ↔ EN `reviews`).
- Always use the route helpers for links and the language toggle; don’t hardcode cross‑locale paths.

## Forms & Analytics

- Netlify Forms on `/fr/contact/` and `/en/contact/`, with localized thank‑you pages.
- Plausible events: `booking_request_submitted` (primary), `click_airbnb`, `click_booking`, etc.

## Contributing

- Use Conventional Commits. Include screenshots (FR/EN) for UI changes.
- Keep the spec updated when requirements change.
- See `AGENTS.md` for contributor guidelines and the current phase plan.

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
