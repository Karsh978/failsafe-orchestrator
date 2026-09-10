import json
from groq import Groq
from typing import List, Dict, Any
from config import GROQ_API_KEY, GROQ_MODEL

class GroqStoryWeaver:
    def __init__(self, api_key: str = GROQ_API_KEY):
        self.client = Groq(api_key=api_key)

    def generate_quest(
        self, 
        user_goal: str, 
        celebrity: str, 
        news_data: List[Dict[str, Any]], 
        location: str,
        user_mood: str = "curious"
    ) -> Dict[str, Any]:
        
        news_text = "\n".join([f"- {item['title']}: {item['snippet']}" for item in news_data])
        
        system_prompt = (
            "You are an AI Radio Jockey and Immersive Quest Architect for 'Arkham Social', "
            "a taste-based social gaming platform. Always respond in valid JSON format."
        )

        user_prompt = f"""
        USER GOAL: {user_goal}
        PUBLIC FIGURE / CELEBRITY: {celebrity}
        CITY PLOT LOCATION: {location}
        CURRENT USER MOOD: {user_mood}
        
        LIVE NEWS DATA:
        {news_text}

        Task:
        1. Create a radio jockey script (engaging, radio host style, matching user's mood: '{user_mood}') introducing the quest.
        2. Weave the recent news about {celebrity} with the user's personal goal at {location}.
        3. Define 3 interactive milestones for the user to progress through the city location.

        Return ONLY a JSON object with this exact structure:
        {{
            "location": "{location}",
            "radio_jockey_script": "speech script text for audio generation",
            "quest_title": "title of the quest",
            "narrative_snippet": "story text weaving goal and news",
            "milestones": ["milestone 1", "milestone 2", "milestone 3"]
        }}
        """

        response = self.client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        return json.loads(content)