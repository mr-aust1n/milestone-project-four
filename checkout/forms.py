from django import forms
from django.core.validators import MinValueValidator


class OfferForm(forms.Form):
    offer_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Your Offer (£)",
        validators=[MinValueValidator(0.01)],
    )
    note = forms.CharField(
        widget=forms.Textarea, required=False, label="Message (optional)"
    )
