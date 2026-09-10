import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY", "your_serper_api_key_here")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")

GROQ_MODEL = "openai/gpt-oss-20b"

# FishAudio Settings
FISH_AUDIO_API_KEY = os.getenv("FISH_AUDIO_API_KEY", "your_fish_audio_api_key_here")
# Cloned Voice / Reference Model ID for the AI Radio Jockey
FISH_AUDIO_VOICE_ID = os.getenv("FISH_AUDIO_VOICE_ID", "your_cloned_voice_id_here")