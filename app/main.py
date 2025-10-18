from fastapi import FastAPI
from app.routers import chat, speech, products

app = FastAPI(title="Zaman AI Assistant Backend")

app.include_router(chat.router)
app.include_router(speech.router)
app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "Zaman AI Assistant Backend is running successfully."}
