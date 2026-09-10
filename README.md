# Failsafe Master Agent Orchestrator

Unified multi-agent orchestrator integrating CyberSecurity/OSINT, Legal/M&A, Financial, Biomedical, and Video Production AI services under a centralized OpenRouter pipeline.

## 🚀 Services Overview & Endpoints

| Service Name | Description | Key Endpoint | Method |
| :--- | :--- | :--- | :--- |
| **Strix CyberSec** | Autonomous Penetration Testing | `/api/v1/scan` | `POST` |
| **Legal & M&A Suite** | M&A Due Diligence & UK Co-Counsel | Internal LLM Wrapper | `Python API` |
| **AI Hedge Fund** | Portfolio Risk & Signal Analysis | `/api/v1/analyze-portfolio` | `POST` |
| **Aegis Forensics** | AI Forensic Evidence Audit | `/api/v1/audit` | `POST` |
| **Biomni** | Biomedical & Life Sciences Research | `/api/v1/analyze` | `POST` |
| **MoneyPrinterTurbo** | Async Video Generation & Rendering | `/api/v1/video/generate` | `POST` |

---

## 🛠️ How to Run All Microservices Locally

Start all background FastAPI microservices at once:

```bash
python run_all_servers.py
