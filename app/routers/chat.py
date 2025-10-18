from fastapi import APIRouter
from app.services.chat_ai import process_message

router = APIRouter()

@router.post("/")
async def chat(message: str):
    response = process_message(message)
    return {"response": response}