#!/usr/bin/env python3
"""Refresh the public Google Scholar snapshot used by the Research dashboard."""

import html
import json
import re
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

USER_ID = "F_aQcNMAAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en&pagesize=100"
OUTPUT = Path("data/scholar.json")


def text_only(markup: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", markup)).replace("\xa0", " ").strip()


def extract_stats(page: str) -> dict[str, int]:
    stats = {}
    for label, value in re.findall(
        r'<td class="gsc_rsb_sc1">.*?<a[^>]*>(.*?)</a>.*?</td>\s*<td class="gsc_rsb_std">(.*?)</td>',
        page,
        flags=re.S,
    ):
        name, number = text_only(label), text_only(value).replace(",", "")
        if name.lower() in {"citations", "h-index", "i10-index"} and number.isdigit():
            key = {"Citations": "citations", "h-index": "hIndex", "i10-index": "i10index"}[name]
            stats[key] = int(number)
    # Google Scholar's first values are all-time; recent values are in the second column.
    return stats


def extract_papers(page: str) -> list[dict]:
    papers = []
    for row in re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, flags=re.S):
        title_match = re.search(r'<a[^>]*class="gsc_a_at"[^>]*>(.*?)</a>', row, flags=re.S)
        if not title_match:
            continue
        title = text_only(title_match.group(1))
        citation_match = re.search(r'class="gsc_a_ac[^>]*>(.*?)</a>', row, flags=re.S)
        year_match = re.search(r'class="gsc_a_y[^"]*"[^>]*>\s*<span[^>]*>(\d{4})', row, flags=re.S)
        papers.append({
            "title": title,
            "citations": int(text_only(citation_match.group(1))) if citation_match and text_only(citation_match.group(1)).isdigit() else 0,
            "year": int(year_match.group(1)) if year_match else None,
        })
    return papers


TOPICS = {
    "Industrial anomaly diagnosis": ("anomal", "root cause", "fault", "diagnos", "process monitoring"),
    "Process safety & knowledge systems": ("safety risk", "hazop", "knowledge graph", "large language", "llm", "process industry"),
    "Autonomous driving verification": ("driver assistance", "adas", "autonomous driving", "vehicle", "verification"),
    "Time series & machine learning": ("time series", "autoencoder", "deep learning", "neural", "machine learning"),
    "Energy & battery systems": ("battery", "lithium", "energy storage"),
    "Remote sensing & environmental data": ("remote sensing", "river ice", "satellite", "environment"),
}


def main() -> None:
    request = urllib.request.Request(PROFILE_URL, headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchDashboard/1.0)"})
    with urllib.request.urlopen(request, timeout=30) as response:
        page = response.read().decode("utf-8", errors="replace")
    papers = extract_papers(page)
    if not papers:
        raise RuntimeError("Google Scholar returned no publications; keeping the existing snapshot")

    stats = extract_stats(page)
    yearly = Counter(paper["year"] for paper in papers if paper["year"])
    topics = []
    for topic, terms in TOPICS.items():
        count = sum(any(term in paper["title"].lower() for term in terms) for paper in papers)
        if count:
            topics.append({"name": topic, "count": count})
    topics.sort(key=lambda topic: (-topic["count"], topic["name"]))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "profileUrl": f"https://scholar.google.com/citations?user={USER_ID}&hl=zh-CN",
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "stats": stats,
        "papers": papers,
        "yearly": [{"year": year, "count": yearly[year]} for year in sorted(yearly)],
        "topics": topics,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {OUTPUT}: {len(papers)} papers, {len(topics)} inferred research areas")


if __name__ == "__main__":
    main()
