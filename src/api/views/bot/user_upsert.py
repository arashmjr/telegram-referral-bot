from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from src.apps.bot.serializers.user_upsert_serializer import UserUpsertSerializer

class UserUpsertView(APIView):
    def post(self, request):
        serializer = UserUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "telegram_id": user.telegram_id,
            "created_at": user.created_at
        }, status=status.HTTP_201_CREATED)
