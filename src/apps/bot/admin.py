from django.contrib import admin

# Register your models here.
from src.apps.bot.models.price_snapshot import PriceSnapshot
from src.apps.bot.models import TelegramUser



@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass

@admin.register(PriceSnapshot)
class PriceSnapshotAdmin(admin.ModelAdmin):
    pass