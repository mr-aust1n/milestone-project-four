# items / tests.py

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Item


class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_create_item(self):
        item = Item.objects.create(
            title="Test Item",
            description="A test description.",
            category="books",
            price=10.00,
            seller=self.user,
            quantity=5,
        )
        self.assertEqual(item.title, "Test Item")
        self.assertEqual(item.category, "books")
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.seller.username, "testuser")
