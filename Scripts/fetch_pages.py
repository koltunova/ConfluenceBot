from confluencebot.api_client import fetch_pages

if __name__ == "__main__":
    pages = fetch_pages()
    print(f"✅ Получено {len(pages)} страниц")
