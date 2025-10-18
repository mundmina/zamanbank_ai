import os
import requests

HUB_URL = "https://openai-hub.neuraldeep.tech/api"  # ✅ Your custom API endpoint
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def download_voice(file_id: str) -> str:
    """
    Download a Telegram voice message and save it locally.
    """
    file_info_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getFile?file_id={file_id}"
    file_info = requests.get(file_info_url).json()
    file_path = file_info["result"]["file_path"]

    file_url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_path}"
    voice_data = requests.get(file_url)

    os.makedirs("voices", exist_ok=True)
    local_path = os.path.join("voices", os.path.basename(file_path))
    with open(local_path, "wb") as f:
        f.write(voice_data.content)

    print(f"🎤 Downloaded voice message to {local_path}")
    return local_path


def handle_voice(file_id: str) -> str:
    """
    Send Telegram voice to the NeuralDeep OpenAI Hub for transcription.
    """
    try:
        local_path = download_voice(file_id)

        with open(local_path, "rb") as f:
            files = {"file": f}
            response = requests.post(f"{HUB_URL}/whisper", files=files)

        if response.status_code == 200:
            text = response.json().get("text", "")
            print(f"🗣️ Transcribed text: {text}")
            return text
        else:
            print("❌ Whisper API error:", response.text)
            return "Sorry, I couldn’t understand your voice message."

    except Exception as e:
        print("❌ Error in handle_voice:", e)
        return "Something went wrong while processing your voice message."
