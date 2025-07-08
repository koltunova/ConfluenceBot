from confluencebot.api_client import fetch_pages
from confluencebot.structure_builder import build_structure

if __name__ == "__main__":
    pages = fetch_pages()
    build_structure(pages)
