from fastapi import FastAPI, Request
import requests, os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

user_state = {}

# ---------- Helper functions ----------
def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(f"{BASE_URL}/sendMessage", json=data)

def answer_callback(callback_id, text=""):
    requests.post(f"{BASE_URL}/answerCallbackQuery",
                  json={"callback_query_id": callback_id, "text": text})

# ---------- Keyboards ----------
def main_menu():
    return {
        "inline_keyboard": [
            [{"text": "🏦 Online Banking", "callback_data": "banking"}],
            [{"text": "🤖 AI Assistant", "callback_data": "ai"}],
        ]
    }

def banking_menu():
    return {
        "inline_keyboard": [
            [{"text": "💰 View Balance", "callback_data": "check_balance"}],
            [{"text": "💳 Open Deposit", "callback_data": "open_deposit"}],
            [{"text": "📤 Transfer Money", "callback_data": "transfer"}],
            [{"text": "🏠 Main Menu", "callback_data": "main"}],
        ]
    }

def ai_menu():
    return {
        "inline_keyboard": [
            [{"text": "💬 Ask a Question", "callback_data": "ask_ai"}],
            [{"text": "📘 What can you do?", "callback_data": "ai_help"}],
            [{"text": "🏠 Main Menu", "callback_data": "main"}],
        ]
    }

def back_to_menu():
    """Keyboard that always brings back the main menu"""
    return {"inline_keyboard": [[{"text": "🏠 Main Menu", "callback_data": "main"}]]}

# ---------- Webhook route ----------
@app.post("/")
async def webhook(req: Request):
    data = await req.json()
    print("📩 Incoming:", data)

    # ---------- Button handling ----------
    if "callback_query" in data:
        cq = data["callback_query"]
        chat_id = cq["message"]["chat"]["id"]
        cb_id = cq["id"]
        choice = cq["data"]
        user_state.setdefault(chat_id, {"mode": "main"})
        answer_callback(cb_id)

        if choice == "banking":
            send_message(chat_id, "🏦 Welcome to *Online Banking*!\nSelect an option below:", reply_markup=banking_menu())
            user_state[chat_id]["mode"] = "banking"

        elif choice == "ai":
            send_message(chat_id, "🤖 I’m your *AI Assistant*.\nAsk questions or get help:", reply_markup=ai_menu())
            user_state[chat_id]["mode"] = "ai"

        elif choice == "check_balance":
            send_message(chat_id, "💰 Your balance is *120,000₸*.\n\nWould you like to do something else?", reply_markup=banking_menu())
            user_state[chat_id]["mode"] = "banking"

        elif choice == "open_deposit":
            send_message(chat_id, "💳 To open a deposit, please confirm the amount (demo):\n\nRecommended: *50,000₸*", reply_markup=banking_menu())
            user_state[chat_id]["mode"] = "banking"

        elif choice == "transfer":
            send_message(chat_id, "📤 Transfer service (demo):\nWho would you like to send money to?", reply_markup=back_to_menu())
            user_state[chat_id]["mode"] = "transfer"

        elif choice == "ask_ai":
            send_message(chat_id, "💬 Great! Just type your question below — I’ll answer right away.")
            user_state[chat_id]["mode"] = "ai_chat"

        elif choice == "ai_help":
            send_message(chat_id,
                         "🧠 I can help with:\n• Financial tips\n• Bank product info\n• General knowledge questions\n\nAsk me anything!",
                         reply_markup=ai_menu())
            user_state[chat_id]["mode"] = "ai"

        elif choice == "main":
            send_message(chat_id, "🏠 Back to main menu:", reply_markup=main_menu())
            user_state[chat_id]["mode"] = "main"

        return {"ok": True}

    # ---------- Normal message handling ----------
    if "message" in data:
        msg = data["message"]
        chat_id = msg["chat"]["id"]
        text = msg.get("text", "")
        user_state.setdefault(chat_id, {"mode": "main"})
        mode = user_state[chat_id]["mode"]

        # Start command
        if text == "/start":
            send_message(chat_id, "👋 Hello! I’m *Zaman AI Assistant*.\nHow can I help you today?", reply_markup=main_menu())
            return {"ok": True}

        # AI chat mode
        if mode == "ai_chat":
            # Here you will connect to NeuralDeep or OpenAI later
            reply = f"🤖 (AI demo) You said: *{text}*.\n\nI’m here to help with your questions!"
            send_message(chat_id, reply, reply_markup=ai_menu())
            user_state[chat_id]["mode"] = "ai"
            return {"ok": True}

        # Transfer simulation
        if mode == "transfer":
            send_message(chat_id, f"✅ (Demo) Transfer to *{text}* completed successfully!\n\nWhat would you like to do next?",
                         reply_markup=banking_menu())
            user_state[chat_id]["mode"] = "banking"
            return {"ok": True}

        # Fallback
        send_message(chat_id, "Please use the menu below 👇", reply_markup=main_menu())
        return {"ok": True}

    return {"ok": True}
