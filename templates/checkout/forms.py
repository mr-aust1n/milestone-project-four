from django import forms


class OfferForm(forms.Form):
    offer_price = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Your Offer (£)"
    )
    note = forms.CharField(
        widget=forms.Textarea, required=False, label="Message (optional)"
    )
