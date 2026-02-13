import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime

API_BASE = "https://api.semanticscholar.org/graph/v1"
S2_AUTHOR_ID = os.getenv("S2_AUTHOR_ID", "").strip()
API_KEY = os.getenv("S2_API_KEY", "").strip()

FIELDS = "papers.title,papers.year,papers.venue,papers.citationCount,papers.url,papers.authors"

def http_get(url: str) -> dict:
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "GiorgosPeikos-GitHubPages/1.0")
    if API_KEY:
        req.add_header("x-api-key", API_KEY)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def author_search(query: str) -> str:
    url = f"{API_BASE}/author/search?query={urllib.parse.quote(query)}&limit=5"
    data = http_get(url)
    for a in data.get("data", []):
        name = (a.get("name") or "").lower()
        if "peikos" in name:
            return str(a.get("authorId"))
    raise RuntimeError("Could not find an authorId in Semantic Scholar search results.")

def dump_yaml(top_cited, most_recent) -> str:
    def esc(s):
        return (s or "").replace('"', '\\"')

    def links_for(p):
        url = p.get("url") or ""
        if url:
            return f'    links:\n      - label: "Semantic Scholar"\n        url: "{esc(url)}"\n'
        return '    links: []\n'

    out = []
    out.append("top_cited:")
    for p in top_cited:
        authors = ", ".join([a.get("name","") for a in (p.get("authors") or [])][:6])
        out.append(f'  - title: "{esc(p.get("title"))}"')
        out.append(f'    authors: "{esc(authors)}"')
        out.append(f'    venue: "{esc(p.get("venue"))}"')
        out.append(f'    year: {int(p.get("year") or 0)}')
        out.append(f'    citations: {int(p.get("citationCount") or 0)}')
        out.append(links_for(p).rstrip("\n"))

    out.append("")
    out.append("most_recent:")
    for p in most_recent:
        authors = ", ".join([a.get("name","") for a in (p.get("authors") or [])][:6])
        out.append(f'  - title: "{esc(p.get("title"))}"')
        out.append(f'    authors: "{esc(authors)}"')
        out.append(f'    venue: "{esc(p.get("venue"))}"')
        out.append(f'    year: {int(p.get("year") or 0)}')
        out.append(links_for(p).rstrip("\n"))

    out.append("")
    out.append(f'# updated: {datetime.utcnow().isoformat()}Z')
    return "\n".join(out) + "\n"

def main():
    global S2_AUTHOR_ID
    if not S2_AUTHOR_ID:
        S2_AUTHOR_ID = author_search("Georgios Peikos")

    url = f"{API_BASE}/author/{S2_AUTHOR_ID}?fields={urllib.parse.quote(FIELDS)}"
    data = http_get(url)

    papers = data.get("papers") or []
    papers = [p for p in papers if p.get("title") and p.get("year")]

    top_cited = sorted(papers, key=lambda p: (p.get("citationCount") or 0, p.get("year") or 0), reverse=True)[:3]
    most_recent = sorted(papers, key=lambda p: (p.get("year") or 0, p.get("citationCount") or 0), reverse=True)[:3]

    os.makedirs("_data", exist_ok=True)
    with open("_data/publications.yml", "w", encoding="utf-8") as f:
        f.write(dump_yaml(top_cited, most_recent))

    print("Wrote _data/publications.yml")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
