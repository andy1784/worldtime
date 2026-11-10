<div align="center">
<img width="1200" height="475" alt="World Time Sync Banner" src="https://worldtimessync.com/og-image.png" />
</div>

# World Time Sync

**🌐 [worldtimessync.com](https://worldtimessync.com)** — Free global time utility: 700+ cities, 67 countries, 60+ blog articles. Real-time world clock, meeting planner, time zone converter.

## Features

- **700+ Cities** — Current local time for major cities worldwide
- **Meeting Planner** — Find the best time for calls across multiple time zones
- **World Clock** — Live updating clock with city search
- **Time Zone Converter** — Convert time between any two cities
- **Daylight Saving Time** — Automatic DST adjustments for all supported regions
- **Country Pages** — Complete time zone guides for 67+ countries
- **Blog** — 60+ articles about time zones, DST, and remote work
- **WordPress Plugin** — Embeddable world clock for WordPress sites
- **No Ads on Core Tool** — Clean, fast, mobile-friendly interface

## Tech Stack

- **Frontend:** React 19, TypeScript, Vite 6, Tailwind CSS 4
- **Deployment:** Vercel (auto-deploy from this repo)
- **Analytics:** Google Analytics (GA4), Vercel Insights, Ahrefs Analytics
- **Ads:** Google AdSense

## SEO & Content

- ✅ 700+ city pages with unique human-written descriptions
- ✅ 67 country pages with time zone guides
- ✅ 60 blog articles about time zones and remote work
- ✅ Schema.org markup (WebApplication, Organization, FAQ, BreadcrumbList)
- ✅ Google Search Console verified
- ✅ Sitemap with 742+ URLs
- ✅ Open Graph and Twitter Card meta tags
- ✅ Multi-language support (8 languages via hreflang)

## WordPress Plugin

The repository includes a WordPress plugin (`/wp-plugin/`) that adds a world clock widget to any WordPress site.

## Run Locally

**Prerequisites:** Node.js 18+

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key (optional for local dev)

3. Run the app:
   ```bash
   npm run dev
   ```

## Build for Production

```bash
npm run build
```

The output will be in the `dist/` folder, ready for deployment.

## Project Structure

```
├── public/
│   ├── robots.txt        # Crawler instructions
│   ├── sitemap.xml       # XML sitemap
│   ├── ads.txt           # AdSense authorization
│   └── favicon.svg       # Site icon
├── src/
│   ├── App.tsx           # Main application component
│   ├── constants.ts      # City/timezone data
│   ├── components/       # React components
│   ├── index.tsx         # Entry point
│   └── index.css         # Global styles
├── index.html            # HTML template with SEO meta tags
├── vite.config.ts        # Vite configuration
└── package.json
```

## About

World Time Sync is a free, independent global time utility. No sign-up required, no API key needed — just search a city and get the current time.

Built and maintained by [Andy](https://github.com/andy1784).

## License

© 2026 World Time Sync. All rights reserved.