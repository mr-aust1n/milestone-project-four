# orders/models.py
from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stripe_payment_intent = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.item.title}"
