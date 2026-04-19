#!/usr/bin/env python3
"""Mixcloud APIからmixcloud.htmlを自動生成する"""

import urllib.request
import json

API_URL = "https://api.mixcloud.com/DJAKIO/cloudcasts/?limit=50"

with urllib.request.urlopen(API_URL) as res:
    data = json.loads(res.read())

items = data["data"]

cards = ""
for item in items:
    url = f"https://www.mixcloud.com{item['key']}"
    title = item["name"].replace("&", "&amp;")
    img = item.get("pictures", {}).get("extra_large", "")
    cards += f"""
      <div class="mix-item">
        <a href="{url}" target="_blank" rel="noopener">
          <div class="thumbnail"><img src="{img}" alt=""></div>
          <div class="mix-info">
            <p class="mix-title">{title}</p>
            <p class="mix-sub">Mixcloud</p>
          </div>
        </a>
      </div>
"""

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mixcloud — POND</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    :root {{
      --bg: #f4f1ec;
      --text: #1c1c1a;
      --text-dim: rgba(28,28,26,0.35);
    }}

    body {{
      background: var(--bg);
      color: var(--text);
      font-family: "Times New Roman", Times, serif;
      min-height: 100vh;
    }}

    .wrap {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 8vh 6vw;
    }}

    header {{
      display: flex;
      align-items: baseline;
      gap: 32px;
      margin-bottom: 10vh;
    }}

    .back {{
      font-size: 0.75rem;
      letter-spacing: 0.25em;
      color: var(--text-dim);
      text-decoration: none;
      text-transform: uppercase;
    }}

    .back:hover {{ color: var(--text); }}

    header h1 {{
      font-size: clamp(1rem, 2vw, 1.3rem);
      font-weight: normal;
      letter-spacing: 0.3em;
      text-transform: uppercase;
    }}

    .mix-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 48px 36px;
    }}

    .mix-item a {{
      display: block;
      text-decoration: none;
      color: var(--text);
    }}

    .thumbnail {{
      width: 100%;
      aspect-ratio: 1 / 1;
      overflow: hidden;
      background: #e8e4de;
    }}

    .thumbnail img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.85;
      filter: saturate(0.5) brightness(1.02);
      transition: opacity 0.6s, filter 0.6s;
      display: block;
    }}

    .mix-item a:hover .thumbnail img {{
      opacity: 1;
      filter: saturate(0.8) brightness(1.05);
    }}

    .mix-info {{ margin-top: 14px; }}

    .mix-title {{
      font-size: clamp(0.8rem, 1.3vw, 0.95rem);
      font-weight: normal;
      letter-spacing: 0.03em;
      line-height: 1.5;
    }}

    .mix-sub {{
      margin-top: 5px;
      font-size: 0.68rem;
      letter-spacing: 0.18em;
      color: var(--text-dim);
      text-transform: uppercase;
    }}

    footer {{
      margin-top: 12vh;
      font-size: 0.7rem;
      letter-spacing: 0.2em;
      color: var(--text-dim);
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <a class="back" href="index.html">← Pond</a>
      <h1>Mixcloud</h1>
    </header>
    <main class="mix-grid">
{cards}
    </main>
    <footer>© POND</footer>
  </div>
</body>
</html>
"""

with open("mixcloud.html", "w") as f:
    f.write(html)

print(f"Generated mixcloud.html with {len(items)} mixes")
