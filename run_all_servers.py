# D:\social_agent\run_all_servers.py
import subprocess
import time
import sys

def start_services():
    print("Starting all microservice FastAPI servers...")
    
    p1 = subprocess.Popen([sys.executable, "deployed_agents/ai-hedge-fund/server.py"])
    p2 = subprocess.Popen([sys.executable, "deployed_agents/AegisForensics/server.py"])
    p3 = subprocess.Popen([sys.executable, "deployed_agents/MoneyPrinterTurbo/server.py"])
    p4 = subprocess.Popen([sys.executable, "deployed_agents/Biomni/server.py"])

    print("Waiting 3 seconds for servers to spin up...")
    time.sleep(3)
    return [p1, p2, p3, p4]

if __name__ == "__main__":
    processes = start_services()
    print("All servers running in background! Press Ctrl+C to stop.")
    try:
        for p in processes:
            p.wait()
    except KeyboardInterrupt:
        print("\nStopping all servers...")
        for p in processes:
            p.terminate()