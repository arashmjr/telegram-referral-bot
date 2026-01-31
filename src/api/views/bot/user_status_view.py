from django.shortcuts import get_object_or_404
from src.apps.bot.models import TelegramUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class UserStatusView(APIView):
    def get(self, request, telegram_id):
        try:
            user = get_object_or_404(
                TelegramUser,
                telegram_id=telegram_id
            )
        except Http404:
            return Response(
                {"detail": "User not found", "status": status.HTTP_404_NOT_FOUND},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "telegram_id": user.telegram_id,
            "referrer_telegram_id": (
                user.referrer.telegram_id
                if user.referrer else None
            ),
            "created_at": user.created_at
        })
