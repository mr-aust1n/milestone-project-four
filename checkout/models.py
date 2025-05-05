from django.conf import settings
from django.db import models

from items.models import Item


class Order(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="checkout_orders"
    )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_offer = models.BooleanField(default=False)
    offer_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.item.title} by {self.buyer.username}"
