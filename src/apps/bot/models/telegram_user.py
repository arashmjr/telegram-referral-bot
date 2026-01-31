from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    referrer = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="referrals"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.telegram_id)
