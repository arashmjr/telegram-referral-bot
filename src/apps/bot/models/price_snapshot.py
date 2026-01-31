from django.db import models


class PriceSnapshot(models.Model):
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)