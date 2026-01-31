from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from src.apps.bot.serializers.referral_create_serializer import ReferralCreateSerializer




class ReferralCreateView(APIView):
    def post(self, request):
        serializer = ReferralCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"status": "referral_created"},
            status=status.HTTP_201_CREATED
        )