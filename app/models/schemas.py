from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: int | None = None
    message: str

class ChatResponse(BaseModel):
    reply: str
