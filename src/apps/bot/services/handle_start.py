from src.apps.bot.models import TelegramUser




def handle_start(telegram_id, text):
    print("cccccccccc", text)
    parts = text.split()
    print("dddddddddd", parts)
    referral_code = None

    if len(parts) > 1 and parts[1].startswith("ref_"):
        referral_code = parts[1].replace("ref_", "")

    user, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id
    )
    print("bbbbbbbbbbbbb", referral_code)
    
    if created and referral_code:
        referrer = TelegramUser.objects.filter(
            telegram_id=referral_code
        ).first()

        if referrer and referrer.telegram_id != telegram_id:
            user.referrer = referrer
            user.save()

    return "ثبت‌نام با موفقیت انجام شد"