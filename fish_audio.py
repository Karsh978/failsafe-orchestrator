import os
import requests
from typing import Optional
from config import FISH_AUDIO_API_KEY, FISH_AUDIO_VOICE_ID

class FishAudioTTSEngine:
    def __init__(
        self, 
        api_key: Optional[str] = None, 
        default_reference_id: Optional[str] = None
    ):
        self.api_key = api_key or FISH_AUDIO_API_KEY
        self.default_reference_id = default_reference_id or FISH_AUDIO_VOICE_ID
        self.endpoint = "https://api.fish.audio/v1/tts"

    def generate_speech(
        self, 
        text: str, 
        output_file: str = "output_rj_speech.mp3",
        reference_id: Optional[str] = None,
        latency: str = "normal"
    ) -> Optional[str]:
        """
        Converts text (Radio Jockey script) into audio using FishAudio TTS / Voice Cloning.
        """
        if not self.api_key:
            print("[FishAudio Error] Missing API Key.")
            return None

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Reference ID corresponds to a cloned voice model on FishAudio
        voice_id = reference_id or self.default_reference_id

        payload = {
            "text": text,
            "format": "mp3",
            "reference_id": voice_id,
            "latency": latency
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                with open(output_file, "wb") as f:
                    f.write(response.content)
                print(f"[FishAudio Success] Audio saved to {output_file}")
                return output_file
            else:
                print(f"[FishAudio Error] Status {response.status_code}: {response.text}")
                return None

        except Exception as e:
            print(f"[FishAudio Exception] {e}")
            return None