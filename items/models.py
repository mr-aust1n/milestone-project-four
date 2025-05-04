# items/models.py
from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    CATEGORY_CHOICES = [
        ("fashion", "Fashion"),
        ("electronics", "Electronics"),
        ("books", "Books"),
        ("home", "Home"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    date_posted = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title
