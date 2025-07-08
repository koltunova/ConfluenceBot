@echo off
setlocal
echo 🦔 Настройка проекта ConfluenceBot...

:: === Переход в директорию проекта ===
cd /d C:\Development\ConfluenceBot

:: === Создание базовых файлов ===
echo 📄 Создаю README.md...
(
    echo # ConfluenceBot
    echo Скрипты для работы с API Confluence
) > README.md

:: === settings.py ===
echo ⚙️ Создаю settings.py...
(
    echo # Конфигурация для подключения к Confluence
    echo BASE_URL = "https://your-domain.atlassian.net/wiki"
    echo API_TOKEN = "your_api_token_here"
    echo EMAIL = "your_email@domain.com"
    echo SPACE_KEY = "YOURSPACE"
) > settings.py

:: === confluence_fetch.py ===
echo 🧠 Создаю confluence_fetch.py...
(
    echo import requests
    echo from settings import BASE_URL, API_TOKEN, EMAIL, SPACE_KEY
    echo.
    echo def fetch_pages():
    echo     url = f"{BASE_URL}/rest/api/content?spaceKey={SPACE_KEY}^&expand=title"
    echo     auth = (EMAIL, API_TOKEN)
    echo     headers = {"Accept": "application/json"}
    echo     response = requests.get(url, auth=auth, headers=headers)
    echo.
    echo     if response.status_code == 200:
    echo         data = response.json()
    echo         for page in data.get("results", []):
    echo             print(f"- {page.get('title')}")
    echo     else:
    echo         print(f"Ошибка: {response.status_code}")
    echo.
    echo if __name__ == "__main__":
    echo     fetch_pages()
) > confluence_fetch.py

:: === Всё готово ===
echo ✅ Готово! Скрипты созданы в C:\Development\ConfluenceBot
pause
endlocal
