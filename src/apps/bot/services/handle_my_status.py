from src.apps.bot.models import TelegramUser




def handle_my_status(telegram_id):
    user = TelegramUser.objects.get(telegram_id=telegram_id)

    text = (
        f"Telegram ID: {user.telegram_id}\n"
        f"Registered At: {user.created_at}\n"
        f"Referral: {'Yes' if user.referrer else 'No'}"
    )

    if user.referrer:
        text += f"\nReferrer ID: {user.referrer.telegram_id}"

    return text
