# items / forms.py
from django import forms

from .models import Item, Message


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description", "category", "price", "image", "quantity"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Ask the seller a question about this item...",
                    "aria-label": "Message to seller",
                }
            )
        }
