import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "sk-roG3OusRr0TLCHAADks6lw")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://openai-hub.neuraldeep.tech/v1")
    MODEL_NAME: str = "gpt-4o-mini"
    WHISPER_MODEL: str = "whisper-1"

settings = Settings()
