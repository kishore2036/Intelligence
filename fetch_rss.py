import feedparser
import json
import os
from datetime import datetime

# Configuration
FEED_URL = "https://feeds.feedburner.com/TheHackersNews"  # Replace with actual feed
BASE_DIR = "Intelligence"

# Current date components
today = datetime.utcnow()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%Y-%m-%d")

# Output directory and file path
output_dir = os.path.join(BASE_DIR, year, month)
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"{day}.json")

# Fetch RSS feed
feed = feedparser.parse(FEED_URL)
entries = []

for entry in feed.entries[:10]:
    entries.append({
        "title": entry.title,
        "link": entry.link,
        "published": entry.get("published", ""),
        "summary": entry.get("summary", ""),
    })

# Save feed to file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
