# Chicago Fleet Wraps Sitemap

This repository hosts the complete sitemap for Chicago Fleet Wraps, automatically updated and served via GitHub Pages.

## Setup

1. Rename this repository to `chicagofleetwraps-sitemap`.
2. Go to **Settings > Pages**:
   - Source: **main** branch
   - Folder: **/docs**
3. Access your sitemap at:
   ```
   https://roywraps69.github.io/chicagofleetwraps-sitemap/sitemap-index.xml
   ```

## Structure

- `docs/`: Contains all sitemap XML files (`core-pages.xml`, `news-sitemap.xml`, etc., and `sitemap-index.xml`)
- `auto_update_sitemap.py`: Script regenerating sitemap-index.xml in `docs/`
- `.github/workflows/update-sitemaps.yml`: Workflow for daily automatic updates