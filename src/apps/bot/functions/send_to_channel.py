import requests
from os import environ

TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_to_channel(text):
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Telegram bot token is not set in environment variables")
        
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": "@price_checker_channel",
        "text": text
    }
    response = requests.post(url, json=payload, timeout=5)


    # ارورهای HTTP (4xx / 5xx)
    response.raise_for_status()

    data = response.json()

    # ارورهای خود تلگرام
    if not data.get("ok"):
        error_code = data.get("error_code")
        description = data.get("description", "Unknown Telegram error")
        raise Exception(f"Telegram API error {error_code}: {description}")

    return data