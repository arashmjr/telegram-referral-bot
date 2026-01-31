from celery import shared_task
from src.apps.bot.models import PriceSnapshot
from src.apps.bot.functions import get_price
from src.apps.bot.functions import percent_change
from src.apps.bot.functions import send_to_channel

@shared_task(name='src.apps.bot.tasks.check_price')
def check_price():
    try:
        new_price = get_price()

        last = PriceSnapshot.objects.order_by("-created_at").first()
        if last:
            change = percent_change(last.price, new_price)

            if change is not None and abs(change) > 1:
                send_to_channel(
                    f"⚠️ Price Alert\n"
                    f"Old: {last.price}\n"
                    f"New: {new_price}\n"
                    f"Change: {change:.2f}%"
                )

        PriceSnapshot.objects.create(price=new_price)

    except Exception as e:
        print(f"❌ Price alert job failed: {e}")
