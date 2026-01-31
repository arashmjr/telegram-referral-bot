from rest_framework import serializers
from src.apps.bot.models import TelegramUser


class UserUpsertSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()

    def create(self, validated_data):
        user, _ = TelegramUser.objects.get_or_create(
            telegram_id=validated_data["telegram_id"]
        )
        return user

        