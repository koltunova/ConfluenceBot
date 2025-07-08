from confluencebot.api_client import fetch_pages
from confluencebot.migrate_logic import plan_migration

if __name__ == "__main__":
    pages = fetch_pages()
    plan_migration(pages)
