# cyber_agent.py
import requests
from typing import Dict, Any, Optional

class CyberSecAgentClient:
    def __init__(
        self, 
        strix_url: str = "https://strix-v8n1.onrender.com",
        shannon_url: Optional[str] = None,
        hexstrike_url: Optional[str] = None,
        pentagi_url: Optional[str] = None,
        phoneintel_url: Optional[str] = None
    ):
        self.strix_url = strix_url
        self.shannon_url = shannon_url or "http://localhost:8001"
        self.hexstrike_url = hexstrike_url or "http://localhost:8002"
        self.pentagi_url = pentagi_url or "http://localhost:8003"
        self.phoneintel_url = phoneintel_url or "http://localhost:8004"

    def run_strix_scan(self, target_url: str) -> Dict[str, Any]:
        endpoint = f"{self.strix_url}/api/v1/scan"
        payload = {"target_url": target_url}
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            return res.json() if res.status_code in [200, 201, 202] else {"status": "error", "detail": res.text}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

    # 2. Shannon Security Agent
    def run_shannon_scan(self, repo_url: str) -> Dict[str, Any]:
        endpoint = f"{self.shannon_url}/api/v1/analyze"
        payload = {"repo_url": repo_url}
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            return res.json() if res.status_code == 200 else {"status": "queued", "agent": "Shannon", "target": repo_url}
        except Exception as e:
            return {"status": "pending_deployment", "agent": "Shannon", "error": str(e)}

    # 3. HexStrike AI Agent
    def run_hexstrike_tool(self, target: str, tool_name: str = "nmap") -> Dict[str, Any]:
        endpoint = f"{self.hexstrike_url}/api/v1/execute"
        payload = {"target": target, "tool": tool_name}
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            return res.json() if res.status_code == 200 else {"status": "queued", "agent": "HexStrike", "target": target}
        except Exception as e:
            return {"status": "pending_deployment", "agent": "HexStrike", "error": str(e)}

    # 4. PentAGI Autonomous Agent
    def run_pentagi_task(self, target: str, task_description: str) -> Dict[str, Any]:
        endpoint = f"{self.pentagi_url}/api/v1/task"
        payload = {"target": target, "task": task_description}
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            return res.json() if res.status_code == 200 else {"status": "queued", "agent": "PentAGI", "target": target}
        except Exception as e:
            return {"status": "pending_deployment", "agent": "PentAGI", "error": str(e)}

    # 5. PhoneIntel OSINT Agent
    def run_phone_intel(self, phone_number: str) -> Dict[str, Any]:
        endpoint = f"{self.phoneintel_url}/api/v1/lookup"
        payload = {"phone": phone_number}
        try:
            res = requests.post(endpoint, json=payload, timeout=30)
            return res.json() if res.status_code == 200 else {"status": "queued", "agent": "PhoneIntel", "phone": phone_number}
        except Exception as e:
            return {"status": "pending_deployment", "agent": "PhoneIntel", "error": str(e)}