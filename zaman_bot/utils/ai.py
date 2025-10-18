import os, requests

OPENAI_HUB_KEY = os.getenv("OPENAI_HUB_KEY")

def ask_gpt(prompt):
    headers = {"Authorization": f"Bearer {OPENAI_HUB_KEY}"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post("https://openai-hub.neuraldeep.tech/v1/chat/completions",
                         headers=headers, json=data)
    if resp.status_code == 200:
        return resp.json()["choices"][0]["message"]["content"]
    return "Sorry, I couldn't process that request right now."
