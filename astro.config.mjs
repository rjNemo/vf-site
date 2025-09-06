// @ts-check
import { defineConfig } from "astro/config";

import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  i18n: {
    locales: ["fr", "en"],
    defaultLocale: "fr",
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: true,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
