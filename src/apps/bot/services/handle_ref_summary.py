from src.apps.bot.models import TelegramUser



def handle_ref_summary(telegram_id):
    user = TelegramUser.objects.get(telegram_id=telegram_id)
    referrals = user.referrals.order_by("-created_at")

    if not referrals.exists():
        return "شما زیرمجموعه‌ای ندارید"

    text = f"Total Referrals: {referrals.count()}\n\nLast 5:\n"

    for ref in referrals[:5]:
        text += f"- {ref.telegram_id} | {ref.created_at}\n"

    return text
