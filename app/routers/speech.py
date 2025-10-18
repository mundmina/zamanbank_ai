from fastapi import APIRouter, UploadFile, File
from app.services.openai_api import transcribe_audio

router = APIRouter(prefix="/speech", tags=["Speech"])

@router.post("/")
async def speech_to_text(file: UploadFile = File(...)):
    text = transcribe_audio(file)
    return {"text": text}
