#!/usr/bin/env python3
"""Refresh data/substack.json from The Tabular Guy RSS feed.

Substack's Cloudflare protection blocks GitHub Actions, so the site can't fetch
the feed at build time. Run this locally after publishing a post; with --push it
also commits and pushes the change (on main, that triggers a deploy).
"""
import html
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://thetabularguy.substack.com/feed"
OUT = Path(__file__).resolve().parent.parent / "data" / "substack.json"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"


def clean(text):
    text = html.unescape(re.sub(r"<[^>]+>", "", text or ""))
    return re.sub(r"Thanks for reading .*$", "", text).strip()


def fetch_posts():
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        channel = ET.fromstring(resp.read()).find("channel")
    return [
        {
            "title": clean(item.findtext("title")),
            "link": item.findtext("link"),
            "date": parsedate_to_datetime(item.findtext("pubDate")).isoformat(),
            "description": clean(item.findtext("description")),
        }
        for item in channel.findall("item")
    ]


def main():
    posts = fetch_posts()
    if not posts:
        sys.exit("Feed returned no posts; leaving data/substack.json unchanged.")

    new = json.dumps(posts, indent=2, ensure_ascii=False) + "\n"
    old = OUT.read_text() if OUT.exists() else ""
    if new == old:
        print(f"No new posts ({len(posts)} in feed).")
        return

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(new)
    print(f"Updated data/substack.json: {len(posts)} posts, latest: {posts[0]['title']}")

    if "--push" in sys.argv:
        repo = OUT.parent.parent
        subprocess.run(["git", "-C", repo, "add", OUT], check=True)
        subprocess.run(["git", "-C", repo, "commit", "-m", "Update Substack posts", "--", OUT], check=True)
        subprocess.run(["git", "-C", repo, "push"], check=True)


if __name__ == "__main__":
    main()
