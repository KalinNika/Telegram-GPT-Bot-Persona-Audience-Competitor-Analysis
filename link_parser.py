import re
import requests
from bs4 import BeautifulSoup

def extract_metadata(url: str) -> str:
    """
    Универсальный парсер для Instagram/YouTube ссылок
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find("meta", property="og:title")
        description = soup.find("meta", property="og:description")

        title_text = title["content"] if title else "(без заголовка)"
        desc_text = description["content"] if description else "(без описания)"

        return f"Ссылка: {url}\nЗаголовок: {title_text}\nОписание: {desc_text}"
    
    except Exception as e:
        return f"⚠️ Не удалось извлечь информацию из ссылки: {url} (ошибка: {e})"

def find_links(text: str) -> list[str]:
    return re.findall(r'https?://\\S+', text)

def parse_links_in_text(text: str) -> str:
    links = find_links(text)
    if not links:
        return ""
    
    results = []
    for url in links:
        meta = extract_metadata(url)
        results.append(meta)

    return "\n\n".join(results)
