import json
from search_engine import SerperNewsEngine
from story_weaver import GroqStoryWeaver
from fish_audio import FishAudioTTSEngine

def run_social_agent():
    search_engine = SerperNewsEngine()
    story_weaver = GroqStoryWeaver()
    tts_engine = FishAudioTTSEngine()

    # Inputs
    celebrity = "Elon Musk"
    user_goal = "Launch an AI startup"
    location = "Cybercity Underground Hub"
    user_mood = "energetic"

    print("1. Fetching news...")
    news = search_engine.search_news(query=f"{celebrity} latest news")

    print("2. Generating quest & Radio Jockey script...")
    quest = story_weaver.generate_quest(
        user_goal=user_goal,
        celebrity=celebrity,
        news_data=news,
        location=location,
        user_mood=user_mood
    )

    rj_script = quest.get("radio_jockey_script", "")
    print(f"\n[RJ Script]: {rj_script}\n")

    print("3. Generating voice output via FishAudio...")
    audio_path = tts_engine.generate_speech(
        text=rj_script,
        output_file="rj_broadcast.mp3"
    )

    if audio_path:
        print(f"Pipeline Complete! Audio broadcast ready at: {audio_path}")

if __name__ == "__main__":
    run_social_agent()