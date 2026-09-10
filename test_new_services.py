# D:\social_agent\test_new_services.py
import requests

def test_endpoints():
    print("=== Testing Newly Created Services local endpoints ===")
    
    # 1. Hedge Fund
    try:
        res = requests.get("http://localhost:8001/health", timeout=3)
        print(f"Hedge Fund Health: {res.json()}")
    except Exception as e:
        print(f"Hedge Fund Offline: {e}")

    # 2. Aegis Forensics
    try:
        res = requests.get("http://localhost:8002/health", timeout=3)
        print(f"Aegis Forensics Health: {res.json()}")
    except Exception as e:
        print(f"Aegis Forensics Offline: {e}")

    # 3. MoneyPrinter Video
    try:
        res = requests.get("http://localhost:8003/health", timeout=3)
        print(f"Video Agent Health: {res.json()}")
    except Exception as e:
        print(f"Video Agent Offline: {e}")

if __name__ == "__main__":
    test_endpoints()