# Website Revamp Specification (WIP)

- Branch: `revamp/website-spec`
- Business Goal: Improve design to attract more customers and increase conversion
  rate.
- Primary Conversion: Submit a reservation request (inquiry form).
- Secondary Actions: Highlight availability on Booking.com and Airbnb with badges/links.
  - Booking.com: <https://www.booking.com/hotel/gp/villafleurie.fr.html>
  - Airbnb (T2): <https://airbnb.fr/h/villafleurie-t2>
  - Airbnb (T3): <https://airbnb.fr/h/villafleurie-t3>
- Availability Flow: Inquiry form via Netlify Forms; manual confirmation
  (no live calendar sync).
- Audience: Small families and couples.
- Languages: French and English (FR/EN).

## Internationalization

- URL structure: folder-based `/fr/...` and `/en/...`.
- Default language: FR. Root `/` redirects to `/fr/`.
- Language toggle: visible in navbar; links to the sibling page
  (`/fr/x` ↔ `/en/x`), fallback to home if missing.
- SEO: set `<html lang>`, `hreflang` alternates, localized titles/descriptions;
  separate sitemap entries per locale.
- Tech note: update generator to support nested templates
  (e.g., `pages/fr/*.html`, `pages/en/*.html`) and preserve subdirectories in `dist/`.

## Sitemap

- Home: Hero, value proposition, lead form (primary CTA), Booking/Airbnb badges.
- Apartments (overview): Grid of units with quick facts and CTAs.
  - T2 Corail: Details, amenities, gallery, inquiry CTA.
  - T3 Azur: Details, amenities, gallery, inquiry CTA.
- Gallery
- Reviews
- Location & Access: Map, parking, nearby attractions.
- Rates & Availability: Pricing explainer; links to Booking/Airbnb for instant booking.
- FAQ
- Contact: Inquiry form (primary CTA).
- Footer: Language toggle (FR/EN), Privacy, Terms.

## Tech Stack

- Framework: Astro (static output).
- Styling: Tailwind CSS (utility-first); map brand tokens in config.
- JS: Vanilla JS only (no jQuery). Use lightweight, dependency-free components.
- Components: reuse existing HTML/CSS/JS where useful; migrate to `.astro` with
  Tailwind classes.
- Libraries: no Bootstrap, no Magnific. Static hero (no Swiper). Lightweight
  lightbox for gallery (vanilla, no jQuery).
- Hosting: Netlify (static deploys).
- Forms: Netlify Forms for reservation inquiries.

## Analytics & Events

- Provider: Plausible (domain: `villafleuriegp.com`).
- Primary events: `booking_request_submitted`, `click_airbnb`, `click_booking`.
- Secondary events: `click_call`, `click_email`.
- Event properties: `locale` (fr/en), `page` (e.g., home, apartment),
  `apartment` (t2/t3/na), `position` (navbar/hero/footer/section).

- Implementation: use `plausible("event", {props})` on CTA clicks and after
  successful form submit; retain outbound-link tracking for platform links.

## Release Plan

- Phase 1 (FR Core): Home, Appartements (T2/T3 pages), Reviews, Location & Access,
  Contact (inquiry form), Rates (flat pricing + links), footer legal links pointing
  to placeholders.
- Phase 2 (EN + Media): EN translations for all Phase 1 pages, Gallery (standalone

- per‑apartment mini‑galleries), translated reviews on EN pages.

- Phase 3 (Policies + Analytics + Perf): French policy pages (Terms, Privacy,
  Cancellation, House Rules), Plausible custom events, image optimizations
  (WebP/srcset), Lighthouse/perf pass, optional consent banner.
- Deploy: Netlify with preview deploys per PR; production on main branch.

## Timeline

- Phase 1 target: next week (FR core launch).
- Milestones: content freeze (T‑3), design QA + accessibility (T‑2), copy/links
  final check (T‑1), deploy + smoke test (T‑0).

## Branding

- Logo: `/assets/images/logo.png`
- Primary color: `#1EBBCE`
- Fonts: `/assets/webfonts` (use existing webfonts; confirm final pairing). Current
  template references Open Sans + PT Serif.
- Secondary color: `#138A9A`
- Border radius: `rounded-lg` (0.5rem)

## Contact & CTAs

- Phone: `+33 6 58 96 12 79` (click‑to‑call link).
- Email: `location.villafleurie@gmail.com` (site‑wide contact and form notifications).
- Navbar: show a prominent call button (icon + number) on mobile/desktop.
- Footer: repeat phone and booking email.
- Primary CTA label:
  - FR: "Envoyer une demande"
  - EN: "Send a Request"

## Apartments

### T2 Corail

- Max occupancy: 2–3 guests
- Ideal for: couples and small families (2–3)
- Size: 45 m²
- Beds: 1 queen-sized bed, 1 sofa-bed
- Key amenities: AC, Wi‑Fi, kitchen, crib on demand, secured parking space
- House rules: no smoking, no parties
- Minimum stay: 3 nights
- Check-in/out: 14:00 / 11:00
- Highlight photos: TBD (6–10 featured images) — use placeholders until final selection
- Description FR: Idéal pour les couples, appartement chaleureux et cosy, à
  proximité des plages et des commerces.
- Description EN: Ideal for couples, a cozy and warm apartment close to beaches
  and shops.

### T3 Azur

- Max occupancy: up to 4 guests
- Ideal for: couples and small families (up to 4)
- Size: 55 m²
- Beds: 2 queen-sized beds
- Key amenities: same as T2 Corail
- House rules: same as T2 Corail
- Minimum stay: 3 nights
- Check-in/out: 14:00 / 11:00
- Highlight photos: TBD (6–10 featured images) — use placeholders until final
  selection
- Description FR: Idéal pour les familles, appartement spacieux avec deux lits
  queen, proche des plages et des commerces.
- Description EN: Perfect for families, a spacious apartment with two queen beds,
  close to beaches and shops.

## Reservation Inquiry Form

- Required fields: full_name, email, arrival_date, departure_date, apartment (T2/T3),
  guests_adults, guests_children, consent_privacy.
- Optional fields: phone, message.
- Validation: basic required checks, email format, arrival < departure.
- i18n: localized field labels and validation messages (FR/EN).

## Form Notifications & Auto-Reply

- Owner notifications: send all submissions to `location.villafleurie@gmail.com`.
- Auto-reply: enabled; send localized confirmation (FR/EN based on page locale).
- Auto-reply content: brief thank you, submitted details (dates, apartment, guests),
  expected reply time, and links to Booking.com/Airbnb for instant booking.
- Implementation: Netlify Forms + serverless email (provider TBD, recommendation:
  Resend) via submission-created function.
- Email details (TBD): sender name, from address (e.g., `noreply@villafleuriegp.com`),
  subject lines per locale.
- Post-submit redirect: Yes — `/fr/merci` and `/en/thank-you` with confirmation
  and next steps (Booking/Airbnb CTAs).

## Booking Description / Rates Page

- Purpose: explain pricing model and availability options, then drive inquiry or
  instant booking.
- Content blocks:
  - Pricing explainer (flat nightly rate per apartment; no seasonal pricing).
  - Secondary CTAs: Booking.com and Airbnb links.
  - Booking terms section with policy links (French only):
    - Terms of Service (FR)
    - Privacy Policy (FR)
    - Cancellation Policy (FR)
    - House Rules (FR)
- Placement: terms section appears below pricing and CTAs as a concise block with
  1‑line summaries + links.
- URLs: TBD — define `/fr/...` pages only; English will link to the French policies.

### Pricing Details

- Model: Flat nightly rate per apartment (no seasonal pricing).
- T2 Corail nightly rate: 59 €.
- T3 Azur nightly rate: 79 €.
- Cleaning fee: 20 € if left dirty; free otherwise (per stay).
- Security deposit: none.
- Cancellation summary: 50% late cancellation fee (define late window in policy);
  link to full French policy.
- Cancellation summary: 50% fee for cancellations within 14 days of check‑in;
  link to full French policy. No‑show treated as late cancellation.

## Legal & Policies (FR only)

- Pages to create under FR namespace:
  - Conditions Générales d’Utilisation (CGU) / de Vente (CGV) — Terms
  - Politique de Confidentialité — Privacy
  - Politique d’Annulation — Cancellation
  - Règlement Intérieur — House Rules
- Links: from Rates page and footer.
- Include: owner/legal entity details, address, contact email/phone, hosting provider
  (Netlify), analytics (Plausible) note, data rights (RGPD), and effective date.
- Drafting: assistant to provide concise templates tailored to current rules once
  legal details are confirmed.

### Legal Entity Details

- Legal name: VillaFleurie (Jacques Gordien)
- Contact: <location.villafleurie@gmail.com>, +33 6 58 96 12 79
- Jurisdiction: France
- Hosting provider: Netlify
- Analytics: Plausible (privacy‑friendly, no cookies by default)
- Company ID: SIRET/SIREN — TBD (provide if applicable)

## Home Page Copy (Initial)

- FR Headline: Séjours confortables au Gosier pour couples et petites familles
- FR Subheadline: Deux appartements lumineux, près des plages. Envoyez une demande
  ou réservez instantanément.
- EN Headline: Comfortable stays in Le Gosier for couples and small families
- EN Subheadline: Two bright apartments near the beaches. Send a request or book
  instantly.

## Home Description Copy

- FR: Villa est un lieu de vacances unique situé sur le magnifique archipel de
  la Guadeloupe, prête à accueillir des touristes en quête de tranquillité
  tout au long de l'année.
- EN: Villa is a unique holiday retreat in the beautiful Guadeloupe archipelago,
  ready to welcome tranquility‑seeking guests all year round.
- Images: `/assets/images/villafleurie_t2_salon_1_wl81yXI.jpg`,
  `/assets/images/villafleurie_t3_chambre.jpg`, `/assets/images/villafleurie_t2_terrasse.jpg`.

## Home Hero

- Type: static image (no carousel).
- Image: `/assets/images/villafleurie_t2_salon_1_wl81yXI.jpg` (shared FR/EN).
- Overlay: localized headline, subheadline, primary CTA (inquiry), secondary
  Booking/Airbnb badges.
- Performance: responsive sizes, WebP preferred, lazy‑load below the fold.

## Home Page Sections (Order)

1. Description: brief intro copy (FR/EN) and 2–3 supporting images.
2. Facilities: showcase key amenities (icons + short labels).
3. Rooms Overview: cards for T2 Corail and T3 Azur with quick facts and CTAs.
4. Reviews: 6–8 curated quotes with star ratings and attribution.
5. Location & Access: map embed + address/GPS + parking note.
6. Footer: contact, quick links, legal.

## Navigation

- Language toggle in navbar; legal links in footer.
- FR order: Accueil, Appartements, Galerie, Avis, Accès, Tarifs & Disponibilités,
  FAQ, Contact
- EN order: Home, Apartments, Gallery, Reviews, Location & Access, Rates & Availability,
  FAQ, Contact

## SEO

- Title format: "[Page Title] · VillaFleurie" (localized).
- Meta descriptions: custom per page (120–160 chars), localized FR/EN.
- Open Graph/Twitter: default OG image at `/assets/images/og-default.jpg`; custom
  OG for Home and each Apartment.
- Hreflang: cross-link FR/EN counterparts; `<html lang>` set per locale.
- Sitemap: include both locales; mark FR as default.

## Gallery

- Standalone page: lightbox grid of curated photos (20–30 images max).
- Per‑apartment mini‑galleries: 6–10 highlight photos on each apartment page.
- Captions: Yes — localized FR/EN; concise (3–6 words), only when helpful.
- Attribution: optional small note when photos feature platform badges.

## Images & Performance

- Formats: generate WebP with JPG fallback.
- Responsive: provide `srcset` and appropriate `sizes` for hero, cards, and lightbox.
- Hero: prefetch/prioritize hero image; lazy‑load below‑the‑fold assets.
- Naming: keep existing filenames; add `-webp` variants on build if we add a pipeline.

## FAQ

- Format: concise Q&A; FR primary, EN translated.
- Items (FR → EN to translate):
  - Parking: « Parking gratuit et sécurisé sur place. »
  - Plage: « Plage à 10 minutes à pied. »
  - Règles: « Non‑fumeur, pas de fêtes, pas d’animaux. »
  - Langues: « Nous parlons français, anglais et allemand. »
  - Lit bébé: « Lit bébé sur demande. »
  - Commerces: « Commerces à 2 minutes à pied. »
  - Arrivée/Départ: « Arrivée 14:00 / Départ 11:00. »
  - Séjour minimum: « 3 nuits minimum. »
  - Wi‑Fi: « Wi‑Fi rapide et stable. »
  - Annulation: « Annulation tardive: 50% dans les 14 jours avant l’arrivée. »

### FAQ — EN Translations

- Parking: Free and secure parking on site.
- Beach: Beach 10 minutes' walk away.
- Rules: No smoking, no parties, no pets.
- Languages: We speak French, English and German.
- Crib: Crib available on request.
- Shops: Shops 2 minutes' walk away.
- Check-in/Check-out: Check-in 14:00 / Check-out 11:00.
- Minimum stay: 3 nights minimum.
- Wi‑Fi: Fast, reliable Wi‑Fi.
- Cancellation: Late cancellation: 50% fee within 14 days of arrival.

## Facilities (Icons & Labels)

- AC
  - Icon: `fa-solid fa-snowflake`
  - FR: "Climatisation"
  - EN: "Air conditioning"
- Fast Wi‑Fi
  - Icon: `fa-solid fa-wifi`
  - FR: "Wi‑Fi rapide"
  - EN: "Fast Wi‑Fi"
- Equipped Kitchen
  - Icon: `fa-solid fa-kitchen-set` (fallback: `fa-solid fa-utensils`)
  - FR: "Cuisine équipée"
  - EN: "Equipped kitchen"
- Crib On Demand
  - Icon: `fa-solid fa-baby`
  - FR: "Lit bébé sur demande"
  - EN: "Crib on demand"
- Secured Parking
  - Icon: `fa-solid fa-square-parking`
  - FR: "Parking sécurisé"
  - EN: "Secured parking"
- Near Beaches
  - Icon: `fa-solid fa-umbrella-beach`
  - FR: "Près des plages"
  - EN: "Near the beaches"
- Quiet Neighborhood
  - Icon: `fa-solid fa-house`
  - FR: "Quartier calme"
  - EN: "Quiet neighborhood"
- Family‑Friendly
  - Icon: `fa-solid fa-people-roof`
  - FR: "Adapté aux familles"
  - EN: "Family‑friendly"

## Location & Access

- Map: Google Maps embed iframe using provided URL.
  - Embed src: <https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3831.2598078323063!2d-61.48991482394046!3d16.20707768449259!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c134f148764f5d5%3A0x981bb218cee8b16c!2sVillaFleurie!5e0!3m2!1sfr!2sde!4v1685258248016!5m2!1sfr!2sde>
- Address: 4 rue Gerty Archimède, 97190 Le Gosier (localized FR/EN label).
- GPS: 16.207078, -61.489915 (rounded from embed URL) — display optionally.
- Parking: secured onsite parking (align copy with amenities).

### Badge Labels

- FR: "Réserver sur Booking.com", "Réserver sur Airbnb (T2)", "Réserver sur Airbnb (T3)"
- EN: "Book on Booking.com", "Book on Airbnb (T2)", "Book on Airbnb (T3)"

## Notes

- Keep one primary CTA per page; Booking/Airbnb links as secondary actions.
- This document will evolve iteratively as we refine requirements.

## Reviews

- Source: curated from Booking.com; raw dataset captured at `docs/spec/data/reviews-raw.txt`.
- Display: show 6–10 highlight quotes with name, country, date, rating (converted to 5-star), short excerpt, and “from Booking.com” attribution.
- i18n: Translate reviews on EN pages; show originals on FR pages. Include a small “translated from {language}” note where applicable. Prefer curated/manual translations for accuracy.

## Apartments Overview Cards

- Each card shows: size (m²), max guests, bed setup, 3–4 key amenity icons, nightly rate (shown), and primary CTA.
- Currency: EUR (€).
- T2 Corail quick facts: 45 m²; 2–3 guests; 1 queen + sofa‑bed; AC, Wi‑Fi, kitchen, parking; 59 €/night.
- T3 Azur quick facts: 55 m²; up to 4 guests; 2 queen beds; AC, Wi‑Fi, kitchen, parking; 79 €/night.
