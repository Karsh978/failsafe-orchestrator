from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List, Optional
import os
import uuid

from search_engine import SerperNewsEngine
from story_weaver import GroqStoryWeaver
from fish_audio import FishAudioTTSEngine

app = FastAPI(
    title="Arkham Social AI Agent Service",
    description="Unified API for dynamic quest generation, news integration, and AI Radio Jockey broadcast generation.",
    version="1.0.0"
)

# Initialize engines
search_engine = SerperNewsEngine()
story_weaver = GroqStoryWeaver()
tts_engine = FishAudioTTSEngine()

# Ensure audio output directory exists
AUDIO_DIR = "generated_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Request & Response Schemas
class QuestGenerationRequest(BaseModel):
    user_goal: str = Field(..., example="Launch a sustainable AI startup")
    celebrity: str = Field(..., example="Elon Musk")
    location: str = Field(..., example="Cybercity Underground Hub")
    user_mood: Optional[str] = Field("hyped", example="curious")
    generate_audio: Optional[bool] = Field(True, description="Whether to invoke FishAudio TTS")

class QuestResponse(BaseModel):
    request_id: str
    location: str
    quest_title: str
    radio_jockey_script: str
    narrative_snippet: str
    milestones: List[str]
    audio_url: Optional[str] = None


@app.get("/")
def health_check():
    return {"status": "ok", "service": "Arkham Social AI Agent"}


@app.post("/api/v1/generate-quest", response_model=QuestResponse)
def generate_quest(payload: QuestGenerationRequest):
    request_id = str(uuid.uuid4())[:8]
    
    # 1. Fetch live news via Serper
    news_items = search_engine.search_news(query=f"{payload.celebrity} latest news")
    
    # 2. Weave Quest & RJ Script via Groq
    try:
        quest_data = story_weaver.generate_quest(
            user_goal=payload.user_goal,
            celebrity=payload.celebrity,
            news_data=news_items,
            location=payload.location,
            user_mood=payload.user_mood
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Generation failed: {str(e)}")

    rj_script = quest_data.get("radio_jockey_script", "")
    audio_url = None

    # 3. Generate Audio via FishAudio (if requested)
    if payload.generate_audio and rj_script:
        audio_filename = f"rj_broadcast_{request_id}.mp3"
        audio_path = os.path.join(AUDIO_DIR, audio_filename)
        
        generated_path = tts_engine.generate_speech(
            text=rj_script,
            output_file=audio_path
        )
        if generated_path:
            audio_url = f"/api/v1/audio/{audio_filename}"

    return QuestResponse(
        request_id=request_id,
        location=quest_data.get("location", payload.location),
        quest_title=quest_data.get("quest_title", "Untitled Quest"),
        radio_jockey_script=rj_script,
        narrative_snippet=quest_data.get("narrative_snippet", ""),
        milestones=quest_data.get("milestones", []),
        audio_url=audio_url
    )


@app.get("/api/v1/audio/{filename}")
def stream_audio(filename: str):
    file_path = os.path.join(AUDIO_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
    return FileResponse(path=file_path, media_type="audio/mpeg", filename=filename)