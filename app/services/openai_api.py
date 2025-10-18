from openai import OpenAI
from fastapi import UploadFile

# Configure OpenAI client
client = OpenAI(
    base_url="https://openai-hub.neuraldeep.tech/v1",
    api_key="sk-roG3OusRr0TLCHAADks6lw"
)


def ask_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful banking AI assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def transcribe_audio(file: UploadFile) -> str:
    with file.file as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text
