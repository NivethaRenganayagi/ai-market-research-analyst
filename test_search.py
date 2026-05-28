from tools.web_search import search_web

results = search_web(
    "Top competitors of Notion"
)

for r in results:
    print("\nTITLE:", r["title"])
    print("URL:", r["url"])
    print("CONTENT:", r["content"])