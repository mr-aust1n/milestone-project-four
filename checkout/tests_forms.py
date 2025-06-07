# checkout/tests_forms.py

from django.test import TestCase

from checkout.forms import OfferForm


class OfferFormTests(TestCase):
    def test_valid_offer_form(self):
        """Form is valid with positive price and optional note."""
        form_data = {"offer_price": 25.50, "note": "Please accept my offer."}
        form = OfferForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_valid_offer_form_without_note(self):
        """Form is valid with only price, no note."""
        form_data = {"offer_price": 15.00}
        form = OfferForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_offer_price(self):
        """Form invalid if price is missing."""
        form_data = {"note": "Missing price"}
        form = OfferForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("offer_price", form.errors)

    def test_invalid_negative_offer_price(self):
        """Form invalid if price is zero or negative."""
        form_data = {"offer_price": 0, "note": "Invalid price"}
        form = OfferForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("offer_price", form.errors)
