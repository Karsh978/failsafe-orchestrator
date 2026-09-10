# D:\social_agent\test_all_agents.py
import os
from failsafe_agent import FailsafeMasterAgent

def run_full_failsafe_test():
    print("=== Testing Failsafe Master Orchestrator (Cyber + Legal/Corp + Social) ===\n")
    
    # Environment variable se OpenRouter Key uthayega
    openrouter_key = os.getenv("OPENROUTER_API_KEY", "your_openrouter_key_here")
    
    # Master Orchestrator Initialize
    agent = FailsafeMasterAgent(openrouter_api_key=openrouter_key)

    # 1. Test Strix Security Audit (Live Render Endpoint)
    print("[1/3] Testing Live Strix CyberSec Agent...")
    sec_result = agent.run_security_audit(target_url="https://example.com", scan_type="quick")
    print(f"-> Strix Response: {sec_result}\n")

    # 2. Test Legal & M&A Due Diligence Audit
    print("[2/3] Testing Legal & M&A Due Diligence Agent Suite...")
    sample_data_room = "Company A has $2M ARR, 1 pending UK labor law dispute, and 100% clean IP ownership."
    due_diligence_res = agent.legal_corp.run_due_diligence_audit(company_data_room=sample_data_room)
    print(f"-> Due Diligence Audit Response: {due_diligence_res}\n")

    # 3. Test Corporate Skills Execution
    print("[3/3] Testing Corporate AI Skill Execution...")
    skill_res = agent.legal_corp.execute_corporate_skill(role="Executive Leadership", task="Draft a 90-day GTM strategy")
    print(f"-> Corporate Skill Response: {skill_res}\n")

    print("=== All Master Orchestrator Tests Completed Successfully! ===")

if __name__ == "__main__":
    run_full_failsafe_test()