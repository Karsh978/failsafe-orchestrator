# failsafe_agent.py
from typing import Dict, Any, Optional
from netryx_client import NetryxNovaClient
from cyber_agent import CyberSecAgentClient
from legal_corp_agent import LegalCorpAgentClient
from search_engine import SerperNewsEngine
from story_weaver import GroqStoryWeaver
from fish_audio import FishAudioTTSEngine

class FailsafeMasterAgent:
    def __init__(
        self, 
        strix_url: str = "https://strix-v8n1.onrender.com", 
        openrouter_api_key: Optional[str] = None
    ):
        # 1. Social AI Agent Pipeline
        self.news_engine = SerperNewsEngine()
        self.story_weaver = GroqStoryWeaver()
        self.tts_engine = FishAudioTTSEngine()
        
        # 2. Netryx Visual & MixedFace Intelligence
        self.netryx = NetryxNovaClient()

        # 3. CyberSec Pentesting Suite Client
        self.cyber_sec = CyberSecAgentClient(strix_url=strix_url)

        # 4. Legal & Corporate Suite Client
        self.legal_corp = LegalCorpAgentClient(openrouter_key=openrouter_api_key)

    def run_social_pipeline(self, user_goal: str, celebrity: str, location: str, user_mood: str = "hyped") -> Dict[str, Any]:
        news_data = self.news_engine.search_news(query=f"{celebrity} latest news")
        quest_data = self.story_weaver.generate_quest(user_goal, celebrity, news_data, location, user_mood)
        rj_script = quest_data.get("radio_jockey_script", "")
        audio_path = self.tts_engine.generate_speech(rj_script, f"generated_audio/failsafe_{user_mood}.mp3") if rj_script else None

        return {
            "status": "success",
            "quest": quest_data,
            "audio_broadcast": audio_path
        }

    def run_visual_audit(
        self, 
        file_bytes: bytes, 
        filename: str, 
        lat: float, 
        lon: float, 
        radius: Optional[float] = None, 
        engine: str = "default"
    ) -> Dict[str, Any]:
        return self.netryx.run_visual_search(
            file_bytes=file_bytes,
            filename=filename,
            lat=lat,
            lon=lon,
            radius=radius,
            engine=engine
        )

    def run_security_audit(self, target_url: str, scan_type: str = "quick") -> Dict[str, Any]:
        """Triggers Strix CyberSec pentesting scan on Render."""
        return self.cyber_sec.run_strix_scan(target_url=target_url)