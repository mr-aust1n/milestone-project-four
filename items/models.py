# items/models.py
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
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
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    image = CloudinaryField("image")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    date_posted = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    @property
    def secure_image_url(self):
        return self.image.build_url(secure=True)


class Message(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender.username} → {self.receiver.username} on {self.item.title}"
