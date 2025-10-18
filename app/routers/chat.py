from fastapi import APIRouter
from app.services.openai_api import ask_gpt
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat_with_ai(data: ChatRequest):
    reply = ask_gpt(data.message)
    return ChatResponse(reply=reply)
