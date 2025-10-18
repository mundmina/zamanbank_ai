# app/services/openai_api.py
import os
from typing import List, Optional
from openai import OpenAI
from openai.openai_object import OpenAIObject
from app.core.config import settings

# Load configuration from environment or constants
client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_BASE_URL
)

# You might define system prompt for your banking assistant
SYSTEM_PROMPT = (
    "You are a helpful financial assistant for a user of Zaman Bank. "
    "You help them set savings goals, analyze spending, "
    "and recommend halal banking products in a friendly conversational tone."
)

def ask_gpt(
    user_id: Optional[int],
    user_message: str,
    history: Optional[List[dict]] = None,
    temperature: float = 0.7,
    max_tokens: int = 512,
) -> str:
    """
    Send a chat request to GPT model and return the text reply.
    You can pass conversation history if you implement memory.
    """
    messages = []
    # add system prompt
    messages.append({"role": "system", "content": SYSTEM_PROMPT})
    # optionally add history if you keep tracked chat
    if history:
        for msg in history:
            messages.append(msg)
    # add current user message
    messages.append({"role": "user", "content": user_message})

    response: OpenAIObject = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    # Extract assistant reply
    reply = response.choices[0].message.content
    return reply

def transcribe_audio(file) -> str:
    """
    Accepts a file-like object for audio, sends it to Whisper model and returns the transcript.
    """
    # The API may require binary file upload
    # The openai library may accept file path or file object.
    # We'll assume file is a fastapi UploadFile.
    audio_file = file.file  # file is UploadFile
    response: OpenAIObject = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
    )
    transcript = response.text
    return transcript
