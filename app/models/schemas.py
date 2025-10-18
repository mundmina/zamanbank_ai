from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: int | None = None
    message: str

class ChatResponse(BaseModel):
    reply: str

class Goal(BaseModel):
    user_id: int
    title: str
    amount: float
    duration_months: int

class GoalResponse(BaseModel):
    message: str
