# items / tests_forms.py
from django.contrib.auth.models import User
from django.test import TestCase

from items.forms import ItemForm


class ItemFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="seller", password="testpass123")

    def test_valid_item_form(self):
        form_data = {
            "title": "Test Product",
            "description": "A very nice item.",
            "category": "fashion",
            "price": 50.00,
            "quantity": 3,
        }
        form = ItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_price_form(self):
        form_data = {
            "title": "Test Product",
            "description": "A very nice item.",
            "category": "fashion",
            "price": -20.00,  # Invalid price
            "quantity": 1,
        }
        form = ItemForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_missing_required_fields(self):
        form = ItemForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("price", form.errors)
