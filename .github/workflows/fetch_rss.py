import feedparser
import json

FEED_URL = "https://example.com/rss"  # Replace with actual feed

feed = feedparser.parse(FEED_URL)
entries = []

for entry in feed.entries[:10]:  # Top 10 items
    entries.append({
        "title": entry.title,
        "link": entry.link,
        "published": entry.published,
        "summary": entry.summary,
    })

with open("rss_feed.json", "w") as f:
    json.dump(entries, f, indent=2)
