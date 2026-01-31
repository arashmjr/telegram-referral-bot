from core.settings import get_env
from src.errors import BadRequestException, SerializerErrors
import requests
from os import environ


TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(
            url,
            json=payload,
            timeout=10
        )

    # ارورهای HTTP (4xx / 5xx)
    response.raise_for_status()

    data = response.json()

    # ارورهای خود تلگرام
    if not data.get("ok"):
        error_code = data.get("error_code")
        description = data.get("description", "Unknown Telegram error")
        raise Exception(f"Telegram API error {error_code}: {description}")

    return data  # موفقیت


# def create_bank_account(data, user_id):
#     data["user"] = user_id
#     serializer = CreateBankAccountSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return serializer.data
#     errors = serializer.errors
#     error_types = []
#     for error in errors.keys():
#         error_type = SerializerErrors.CreateBankAccountSerializer.errors.get(
#             error
#         )
#         error_types.append(error_type)
#     raise BadRequestException(message=errors, error_type=error_types)
