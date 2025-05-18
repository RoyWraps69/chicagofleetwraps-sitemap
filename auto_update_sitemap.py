#!/usr/bin/env python3
"""
Automated Sitemap Generator for Chicago Fleet Wraps

Generates modular sitemaps and sitemap index in the docs/ folder for GitHub Pages.
"""

import os
import datetime

OUTPUT_DIR = "docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

today = datetime.date.today().isoformat()

# Define URL groups
core_pages = [
    {"loc": "https://www.chicagofleetwraps.com/", "changefreq": "weekly", "priority": 1.0},
    {"loc": "https://www.chicagofleetwraps.com/about", "changefreq": "yearly", "priority": 0.6},
    {"loc": "https://www.chicagofleetwraps.com/contact", "changefreq": "yearly", "priority": 0.5}
]
service_pages = [
    {"loc": "https://www.chicagofleetwraps.com/commercial-vehicle-wraps", "changefreq": "monthly", "priority": 0.95},
    {"loc": "https://www.chicagofleetwraps.com/color-change-wraps", "changefreq": "monthly", "priority": 0.90},
    {"loc": "https://www.chicagofleetwraps.com/ceramic-coating", "changefreq": "monthly", "priority": 0.85},
    {"loc": "https://www.chicagofleetwraps.com/window-tinting", "changefreq": "monthly", "priority": 0.85},
    {"loc": "https://www.chicagofleetwraps.com/wall-wraps", "changefreq": "monthly", "priority": 0.80},
    {"loc": "https://www.chicagofleetwraps.com/signs-and-graphics", "changefreq": "monthly", "priority": 0.80},
    {"loc": "https://www.chicagofleetwraps.com/apparel", "changefreq": "monthly", "priority": 0.80},
    {"loc": "https://www.chicagofleetwraps.com/wrap-removal", "changefreq": "monthly", "priority": 0.75}
]
blog_posts = [
    f"https://www.chicagofleetwraps.com/blog/{slug}" for slug in [
        "how-to-wrap-a-box-truck",
        "fleet-wrap-vs-paint-costs",
        "benefits-of-ceramic-coating",
        "chicago-vehicle-wrap-laws",
        "how-long-do-wraps-last"
    ]
]
local_pages = [
    f"https://www.chicagofleetwraps.com/vehicle-wraps-{town}" for town in [
        "naperville", "schaumburg", "oak-park", "evanston", "cicero",
        "berwyn", "elmhurst", "skokie", "arlington-heights", "aurora"
    ]
]
portfolio_pages = ["https://www.chicagofleetwraps.com/portfolio"]

# Combine entries
all_pages = []
for entry in core_pages + service_pages:
    all_pages.append(entry)
for url in blog_posts + local_pages + portfolio_pages:
    all_pages.append({"loc": url, "changefreq": "monthly", "priority": 0.7})

# Write unified sitemap
with open(os.path.join(OUTPUT_DIR, "sitemap-index.xml"), "w") as index_file:
    index_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    index_file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for e in all_pages:
        index_file.write(f'  <url>\n')
        index_file.write(f'    <loc>{e["loc"]}</loc>\n')
        index_file.write(f'    <lastmod>{today}</lastmod>\n')
        index_file.write(f'    <changefreq>{e["changefreq"]}</changefreq>\n')
        index_file.write(f'    <priority>{e["priority"]:.2f}</priority>\n')
        index_file.write('  </url>\n')
    index_file.write('</urlset>')
print("Sitemap index updated in docs/")