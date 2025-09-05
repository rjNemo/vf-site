export type Locale = 'fr' | 'en';

export type RouteKey =
  | 'home'
  | 'apartments'
  | 'apartment_t2'
  | 'apartment_t3'
  | 'reviews'
  | 'location'
  | 'rates'
  | 'contact'
  | 'thank_you'
  | 'terms'
  | 'privacy'
  | 'cancellation'
  | 'house_rules';

export const routes: Record<RouteKey, Record<Locale, string>> = {
  home: { fr: '/fr/', en: '/en/' },
  apartments: { fr: '/fr/appartements/', en: '/en/apartments/' },
  apartment_t2: { fr: '/fr/appartements/t2-corail/', en: '/en/apartments/t2-corail/' },
  apartment_t3: { fr: '/fr/appartements/t3-azur/', en: '/en/apartments/t3-azur/' },
  reviews: { fr: '/fr/avis/', en: '/en/reviews/' },
  location: { fr: '/fr/acces/', en: '/en/location-access/' },
  rates: { fr: '/fr/tarifs-disponibilites/', en: '/en/rates-availability/' },
  contact: { fr: '/fr/contact/', en: '/en/contact/' },
  thank_you: { fr: '/fr/merci/', en: '/en/thank-you/' },
  terms: { fr: '/fr/politiques/conditions/', en: '/en/policies/terms/' },
  privacy: { fr: '/fr/politiques/confidentialite/', en: '/en/policies/privacy/' },
  cancellation: { fr: '/fr/politiques/annulation/', en: '/en/policies/cancellation/' },
  house_rules: { fr: '/fr/politiques/reglement/', en: '/en/policies/house-rules/' },
};

const normalize = (p: string) => {
  if (!p) return '/';
  let out = p.startsWith('/') ? p : `/${p}`;
  if (!out.endsWith('/')) out = `${out}/`;
  return out;
};

export function keyForPath(pathname: string): RouteKey | null {
  const n = normalize(pathname);
  for (const key of Object.keys(routes) as RouteKey[]) {
    const localizations = routes[key];
    if (n === localizations.fr || n === localizations.en) return key;
  }
  return null;
}

export function siblingPath(pathname: string, locale: Locale): string {
  const key = keyForPath(pathname);
  if (key) return routes[key][locale];
  return routes.home[locale];
}

export function hrefFor(key: RouteKey, locale: Locale): string {
  return routes[key][locale];
}

export function navFor(locale: Locale): Array<{ label: string; href: string }> {
  return locale === 'en'
    ? [
        { label: 'Apartments', href: routes.apartments.en },
        { label: 'Reviews', href: routes.reviews.en },
        { label: 'Location & Access', href: routes.location.en },
        { label: 'Rates', href: routes.rates.en },
      ]
    : [
        { label: 'Appartements', href: routes.apartments.fr },
        { label: 'Avis', href: routes.reviews.fr },
        { label: 'Accès', href: routes.location.fr },
        { label: 'Tarifs', href: routes.rates.fr },
      ];
}

export function ctaLabelFor(locale: Locale): string {
  return locale === 'en' ? 'Send a Request' : 'Envoyer une demande';
}
