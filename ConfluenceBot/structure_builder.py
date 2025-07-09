from .page_model import Page


def build_structure(pages_json):
    pages = [Page(p["id"], p["title"], p.get("ancestors", [])) for p in pages_json]
    pages.sort(key=lambda p: p.depth())

    for page in pages:
        print(page)
