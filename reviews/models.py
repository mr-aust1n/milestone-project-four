# reviews/models.py
from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()  # e.g., 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "reviewer",
            "item",
        )  # This will prevent multiple reviews per item by same user

    def __str__(self):
        return f"{self.reviewer.username}'s review of {self.item.title}"
