import requests
from typing import Dict, Any, Optional

class NetryxNovaClient:
    def __init__(self):
        self.render_base = "https://netryx-nova.onrender.com"
        self.modal_base = "https://varanasirithulram--netryx-nova-worker-fastapi-app.modal.run"

    def run_visual_search(
        self, 
        file_bytes: bytes, 
        filename: str,
        lat: float, 
        lon: float, 
        radius: Optional[float] = None, 
        engine: str = "default"
    ) -> Dict[str, Any]:
        
        files = {'file': (filename, file_bytes)}
        data = {'lat': str(lat), 'lon': str(lon), 'engine': engine}
        if radius is not None:
            data['radius'] = str(radius)

        # Try Render (increased timeout to 60s for cold starts)
        try:
            print("[Netryx] Sending request to Render instance...")
            response = requests.post(f"{self.render_base}/api/v1/search/run", files=files, data=data, timeout=60)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"[Netryx Render Timeout/Error]: {e}. Attempting direct Modal worker...")

        # Fallback to Modal worker directly if Render times out
        try:
            response = requests.post(f"{self.modal_base}/api/v1/search/run", files=files, data=data, timeout=60)
            if response.status_code == 200:
                return response.json()
            return {"status": "error", "detail": f"Modal status: {response.status_code}"}
        except Exception as e:
            return {"status": "failed", "error": f"Both instances failed: {e}"}