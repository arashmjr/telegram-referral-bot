from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import requests
from src.apps.bot.services import handle_start
from src.apps.bot.services import handle_my_status
from src.apps.bot.services import handle_ref_summary
from src.apps.bot.services import send_message


class TelegramWebhookView(APIView):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        print("ssssssssssssssssssss", data)
        message = data.get("message")

        if not message:
            return Response(
            data={"ok": True, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK
        )

        telegram_id = message["chat"]["id"]
        text = message.get("text", "")

        # تشخیص دستور
        if text.startswith("/start"):
            reply_text = handle_start(telegram_id, text)
        elif text == "/my_status":
            reply_text = handle_my_status(telegram_id)
        elif text == "/ref_summary":
            reply_text = handle_ref_summary(telegram_id)
        else:
            reply_text = "دستور نامعتبر است"

        print("aaaaaaaaaaaaaa", reply_text)
        res_data = send_message(telegram_id, reply_text)
        return Response(
            data={"ok": True,"data": res_data ,"status": status.HTTP_200_OK},
            status=status.HTTP_200_OK
         )




