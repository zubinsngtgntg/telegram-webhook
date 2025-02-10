from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("7602960350:AAEoW-756QqOqJiTGETlSbfhXBYb4Z_myW4")
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.post("/telegram-webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        response_text = f"Lo bilang: {text}"
        async with httpx.AsyncClient() as client:
            await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": response_text})

    return {"status": "ok"}
