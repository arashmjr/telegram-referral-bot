from django.shortcuts import get_object_or_404
from src.apps.bot.models import TelegramUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ReferralSummaryView(APIView):
    def get(self, request, referrer_telegram_id):
        referrer = get_object_or_404(
            TelegramUser,
            telegram_id=referrer_telegram_id
        )

        referrals_qs = referrer.referrals.order_by("-created_at")

        return Response({
            "count": referrals_qs.count(),
            "last_5_referrals": list(
                referrals_qs[:5].values_list("telegram_id", flat=True)
            )
        })
