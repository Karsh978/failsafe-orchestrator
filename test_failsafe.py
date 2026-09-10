import os
from failsafe_agent import FailsafeMasterAgent

def run_failsafe_test():
    print("=== Testing Failsafe Master Agent Pipelines ===\n")
    
    agent = FailsafeMasterAgent()

    # 1. Test Social AI Pipeline
    print("[1/2] Testing Social AI Pipeline...")
    social_result = agent.run_full_pipeline(
        user_goal="Launch an autonomous AI startup",
        celebrity="Elon Musk",
        location="Cybercity Underground Hub",
        mood="hyped"
    )
    print(f"-> Quest Status: {social_result.get('status')}")
    print(f"-> Audio Generated: {social_result.get('broadcast_audio')}\n")

    # 2. Test Netryx Visual Search Endpoint
    print("[2/2] Testing Netryx Nova Visual Search...")
    
    # Dummy file/image simulation for test
    dummy_filename = "test_image.jpg"
    with open(dummy_filename, "wb") as f:
        f.write(b"fake image byte data for testing endpoint")

    with open(dummy_filename, "rb") as f:
        file_bytes = f.read()

    visual_result = agent.netryx.run_visual_search(
        file_bytes=file_bytes,
        filename=dummy_filename,
        lat=28.6139,
        lon=77.2090,
        radius=5.0,
        engine="default"
    )
    
    print(f"-> Visual Search Response: {visual_result}\n")

    # Clean up dummy test file
    if os.path.exists(dummy_filename):
        os.remove(dummy_filename)

    print("=== Test Complete! ===")

if __name__ == "__main__":
    run_failsafe_test()