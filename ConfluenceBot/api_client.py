import requests
from .settings import BASE_URL, EMAIL, API_TOKEN, SPACE_KEY

def fetch_pages():
    url = f"{BASE_URL}/rest/api/content"
    params = {
        "spaceKey": SPACE_KEY,
        "expand": "title,ancestors",
        "limit": 100,
        "start": 0
    }

    auth = (EMAIL, API_TOKEN)
    headers = {"Accept": "application/json"}
    pages = []

    while True:
        response = requests.get(url, headers=headers, auth=auth, params=params)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}: {response.text}")
            break

        data = response.json()
        pages.extend(data.get("results", []))
        if "_links" in data and "next" in data["_links"]:
            params["start"] += params["limit"]
        else:
            break

    return pages
