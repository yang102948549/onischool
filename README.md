# Oni School website

Static HTML product directory and product tours for https://onischool.net.

- `index.html`: ecosystem hub. Hero, app directory (every app with status and links to its tour), what the apps share, about and contact. No per-app demos or data tables here; those live on each app page.
- `oni-class/index.html`: Oni Class tour, download and storage details.
- `oni-record/index.html`: Oni Record tour (intro, API key prerequisite, workflow, annotated screen, writing by record type, Assist, Check, NEIS, checklist, data). Follows the Figma sales detail page; screenshots in `assets/record/` are cropped from that file and use pseudonyms.
- `assets/site.css`: shared design tokens and base styles.
- `assets/class-tour.css`, `assets/site.js`: home and Oni Class layouts, demo tabs, copy-email button.
- `assets/record-tour.css`: Oni Record tour layout.

## Cloudflare Pages

Use Git integration with `yang102948549/onischool`, production branch `main`, no framework, no build command, output directory `.`. Enable automatic production deployments. Changes pushed to `main` then produce a new production deployment. Cloudflare must have access to this private repository through its GitHub app.

The original `onischool` project uses Direct Upload and cannot be converted in place. Migration target: `onischool-git`. Verify its Git deployment before moving `onischool.net`. Preserve the original project for rollback; only the website CNAME and Pages domain attachment need changing. Email DNS records must remain intact.

## Content evidence (2026-10-09)

- Oni Class source: `yang102948549/oni-class-source`, branch `oni-class`, commit `ca1e225087e2be2ec2e0d90b157b29c030281f0f`. UI follows `src/App.tsx`, `src/notion.css`, `src/theme.css` and the student/attendance/submission components. Demonstrations are re-created HTML with fictional data, not live app screenshots.
- Class storage: `src/records.ts` defines `mobileCloudKinds`: entries, attendance, surveys, timetable, mobileRoster. Detailed student data, enrollments, notes, seating, memos, progress, settings and import history stay local in this flow. `src-tauri/src/main.rs` stores protected payloads and backups in SQLite. Legacy records and installed releases can differ; local-only behavior does not imply historical cloud data was deleted.
- Class downloads: public GitHub release `v0.1.1-beta.9` and its Windows x64 EXE were verified. Source documentation mentions a later beta, so the page deliberately calls beta.9 the verified public installer rather than the latest version.
- Record storage: `yang102948549/oni-record-source`, `src/lib/store.js` and `electron/main.cjs`: main/check JSON stores, an OS-protected API key when safeStorage is available (the current code has a plaintext fallback otherwise), no reviewed account sheet-sync path. `electron/gemini-client.cjs` sends prompts and selected content to Google's API. API key encryption does not encrypt work JSON.
- Proctor, Time and Enrollment storage is not claimed until their deployment implementation is reviewed.

No analytics, tracking or submission forms were added. Contact uses mailto and an optional clipboard button. Demo state is in memory only.

## Validation

Headless Edge checks covered the home, Class and Record pages at 1280, 390 and 320 CSS pixels, body overflow, fragment targets, JavaScript errors and Class demo mouse/keyboard tab navigation. Light and dark screenshots were inspected. External download URLs were taken from the public release API.
