#!/usr/bin/env python3
"""Place the Jekyll blog below /homelab and publish the root blog directory."""

import html
import shutil
import sys
from pathlib import Path


site_dir = Path(sys.argv[1])
base_path = sys.argv[2]
if base_path != "/homelab":
    raise SystemExit(f"Unexpected Jekyll base path: {base_path!r}")

blog_dir = site_dir / base_path.lstrip("/")
if not (blog_dir / "index.html").is_file():
    raise SystemExit(f"Jekyll homepage missing: {blog_dir / 'index.html'}")

shutil.copytree("landing", site_dir, dirs_exist_ok=True)
shutil.copyfile("tools/unregister_homelab.js", blog_dir / "unregister.js")

# Old root-level post and section links should continue to reach their pages.
for page in blog_dir.rglob("index.html"):
    relative = page.relative_to(blog_dir)
    if relative == Path("index.html"):
        continue
    old_page = site_dir / relative
    old_page.parent.mkdir(parents=True, exist_ok=True)
    destination = "/homelab/" + relative.parent.as_posix().rstrip("/") + "/"
    escaped = html.escape(destination, quote=True)
    old_page.write_text(
        "<!doctype html>\n"
        '<html lang="en"><head><meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0; url={escaped}">'
        f'<link rel="canonical" href="https://peroty.github.io{escaped}">'
        '<title>Moved to Homelab</title></head><body>'
        f'<p>This page moved to <a href="{escaped}">{escaped}</a>.</p>'
        '</body></html>\n',
        encoding="utf-8",
    )

print(f"Prepared {site_dir} with Homelab at {base_path}/")
