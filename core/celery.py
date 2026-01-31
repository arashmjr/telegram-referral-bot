import os
from celery import Celery

# تنظیمات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# بارگذاری تنظیمات از settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# پیدا کردن task ها
app.autodiscover_tasks()



