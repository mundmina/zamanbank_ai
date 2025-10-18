from fastapi import FastAPI
from app.routers import chat, user

app = FastAPI(title="Chat AI Assistant")

# Include routers
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(user.router, prefix="/user", tags=["User"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat AI Assistant API"}