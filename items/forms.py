# items/forms.py

from django import forms

from .models import Item, Message


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description", "category", "price", "image", "quantity"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["price"].min_value = 0.01


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


class MessageReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write your reply here...",
                    "aria-label": "Reply to buyer",
                }
            )
        }
