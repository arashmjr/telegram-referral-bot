from django.urls import include, path
from src.api.views.bot.referrals_summary import ReferralSummaryView
from src.api.views.bot.user_status_view import UserStatusView
from src.api.views.bot.referral_create import ReferralCreateView
from src.api.views.bot.user_upsert import UserUpsertView
from src.api.views.bot import TelegramWebhookView

bot_urlpatterns = [

    path("telegram-webhook/", TelegramWebhookView.as_view(), name="telegram_webhook"),
    path("users/upsert/", UserUpsertView.as_view(), name="users_upsert"),
    path("referrals/", ReferralCreateView.as_view(), name="referrals"),
    path("users/<int:telegram_id>/status/", UserStatusView.as_view(), name="users_status_view"),
    path("referrals/<int:referrer_telegram_id>/summary/", ReferralSummaryView.as_view(), name="referrals_summary_view"),

]

urlpatterns = [
    path("", include(bot_urlpatterns)),
]

