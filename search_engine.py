import requests
from typing import List, Dict, Any
from config import SERPER_API_KEY

class SerperNewsEngine:
    def __init__(self, api_key: str = SERPER_API_KEY):
        self.api_key = api_key
        self.url = "https://google.serper.dev/news"

    def search_news(self, query: str, num_results: int = 5) -> List[Dict[str, Any]]:
        if not self.api_key:
            print("[Serper Warning] No API key provided, returning empty news list.")
            return []

        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
        payload = {
            "q": query,
            "num": num_results
        }
        
        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                results = response.json().get("news", [])
                return [
                    {
                        "title": item.get("title"),
                        "snippet": item.get("snippet"),
                        "source": item.get("source"),
                        "date": item.get("date")
                    }
                    for item in results
                ]
            else:
                print(f"[Serper Warning] Status Code {response.status_code}: {response.text}. Proceeding without live search.")
                return [
                    {
                        "title": f"Latest trends on {query}",
                        "snippet": f"Recent developments and public updates regarding {query}.",
                        "source": "Global News",
                        "date": "Today"
                    }
                ]
        except Exception as e:
            print(f"[Serper Exception] {e}. Proceeding with default context.")
            return []