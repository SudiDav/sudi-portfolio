# sudi-portfolio

Personal portfolio and blog for Sudi David — full-stack software engineer.
Built with [Astro](https://astro.build), plain CSS, and zero client-side
frameworks.

## Stack

- **Astro 7** — static site generation, `.astro` components
- **Vanilla CSS** — custom properties for theming, no CSS framework
- **Geist / Geist Mono / Inter** — typefaces, loaded from Google Fonts
- **Vanilla TypeScript** — small inline scripts for the theme toggle,
  mobile menu, and category filters

## Getting started

Requires Node.js 22.12 or newer.

```bash
npm install
```

```bash
npm run dev
```

The dev server runs at `http://localhost:4321`.

| Command           | Action                                    |
| ----------------- | ----------------------------------------- |
| `npm run dev`     | Start the dev server with hot reload       |
| `npm run build`   | Build the production site to `./dist/`     |
| `npm run preview` | Preview the production build locally       |

## Structure

```
src/
├── components/     Header, Footer, cards, badges, theme toggle
├── layouts/
│   └── Layout.astro    Base HTML shell, fonts, theme bootstrap
├── pages/
│   ├── index.astro     Home — intro, featured projects, latest articles
│   ├── work.astro      Project grid with category filters
│   ├── blog.astro      Article list with search and filters
│   └── about.astro     Bio, experience timeline, skills, contact
└── styles/
    ├── tokens.css      Design tokens (colors, theme variables)
    └── global.css      Resets and base element styles
public/
├── images/work/    Project banner screenshots
└── Sudi-David-Resume.pdf
scripts/
└── make_resume.py  Generates the resume PDF
```

## Theming

Colors live as CSS custom properties in `src/styles/tokens.css`, defined
once for `[data-theme="dark"]` (the default) and again for
`[data-theme="light"]`. The toggle in the header writes the choice to
`localStorage`, and an inline script in `Layout.astro` applies it before
first paint so there is no flash of the wrong theme.

Components should reference tokens (`var(--color-accent)`,
`var(--color-text-secondary)`) rather than hard-coded hex values, so both
themes stay in sync.

## Resume PDF

The downloadable resume linked from the About page is generated rather
than hand-maintained. Edit the content in `scripts/make_resume.py`, then:

```bash
python3 scripts/make_resume.py
```

This writes `public/Sudi-David-Resume.pdf`. Requires `reportlab`
(`pip install reportlab`).

## Content

Project entries live in the `projects` array in `src/pages/work.astro`,
and article entries in `src/pages/blog.astro` and `src/pages/index.astro`.
Blog posts mirror the published feed at
[sudi.dev/rss.xml](https://sudi.dev/rss.xml) and are updated by hand when
something new goes live.

## License

All rights reserved. The source is public for reference; the content,
branding, and imagery are not licensed for reuse.
