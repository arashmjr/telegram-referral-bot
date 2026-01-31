from src.errors.error_enum import ErrorEnum
from src.errors.exceptions import BadRequestException, NotFoundException
from src.apps.bot.models import TelegramUser
from rest_framework import serializers
from django.utils.translation import gettext as _


class ReferralCreateSerializer(serializers.Serializer):
    referrer_telegram_id = serializers.IntegerField()
    referred_telegram_id = serializers.IntegerField()

    def validate(self, data):
        referrer_id = data.get("referrer_telegram_id")
        referred_id = data.get("referred_telegram_id")
        error_messages = {}
        error_types = []
        if referrer_id == referred_id:
            error_messages["errors"] = _("referrer and referred cannot be the same.")
            error_types.append(ErrorEnum.Service.INVALID_REFERRER_AND_REFERRED)
            raise BadRequestException(
                error_type=error_types, message=error_messages
            )

        try:
            referred = TelegramUser.objects.get(
                telegram_id=data["referred_telegram_id"]
            )
        except TelegramUser.DoesNotExist:
            raise NotFoundException(
            message={"Referred user": _("Referred user does not exist")},
            error_type=[ErrorEnum.Service.INVALID_REFERRED_TELEGRAM_ID],
        )

        if referred.referrer is not None:
            error_messages["errors"] = _("referred_telegram_id that you entered is already has a referrer")
            error_types.append(ErrorEnum.Service.USER_ALREADY_HAS_A_REFERRER)
            raise BadRequestException(
                error_type=error_types, message=error_messages
            )
       

        return data

    def create(self, validated_data):
        referrer, _ = TelegramUser.objects.get_or_create(
            telegram_id=validated_data["referrer_telegram_id"]
        )
        referred = TelegramUser.objects.get(
            telegram_id=validated_data["referred_telegram_id"]
        )

        referred.referrer = referrer
        referred.save()
        return referred
