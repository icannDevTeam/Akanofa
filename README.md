# Akanofa Website

Static, single-source-of-truth website. All HTML pages are generated from `build_pages.py`.

## Build

```bash
python3 build_pages.py
```

Generates `index.html`, `services.html`, `about.html`, `why-us.html`, `contact.html`.

## Local preview

```bash
python3 -m http.server 5500
```

Open http://localhost:5500

## Deploy to cPanel

Upload the following to `public_html/`:

```
.htaccess
index.html
services.html
about.html
why-us.html
contact.html
robots.txt
sitemap.xml
images/
```

Do **not** upload: `build_pages.py`, `README.md`, `.vscode/` — they are not needed in production (`.htaccess` already blocks `.py` / `.md` files from being served).

### After deploy

1. Update `https://akanofa.com` in `robots.txt` and `sitemap.xml` if your domain differs.
2. `.htaccess` enables: HTTPS redirect, clean URLs (`/services` instead of `/services.html`), gzip, long-term image caching, and basic security headers.
3. FormSubmit (Contact / Quote modal) requires a **one-time activation email** sent to `info@akanofa.com` after the very first form submission.

## File overview

| File | Purpose |
|---|---|
| `build_pages.py` | Source of truth — edit here, then rebuild |
| `images/Logo.png` | Brand logo (transparent PNG, 1024×1024) |
| `images/Office.jpg` | HQ photo, used on About page |
| `.htaccess` | Apache/cPanel rules: HTTPS, clean URLs, caching, gzip, security |
| `robots.txt` | Search-engine crawl directives |
| `sitemap.xml` | URL list for search engines |
---
title: DeepSite Project
colorFrom: red
colorTo: green
sdk: static
emoji: 🎨
tags:
  - deepsite-v4
---

# DeepSite Project

This project has been created with [DeepSite](https://deepsite.hf.co) AI Vibe Coding.
