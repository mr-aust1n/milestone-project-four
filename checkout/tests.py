# checkout / tests.py
from django.contrib.auth.models import User
from django.test import TestCase

from checkout.models import Order
from items.models import Item


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="buyer", password="testpass123")
        self.seller = User.objects.create_user(
            username="seller", password="testpass456"
        )
        self.item = Item.objects.create(
            title="Test Item",
            description="Test Description",
            category="books",
            price=20.00,
            quantity=5,
            seller=self.seller,
        )

    def test_create_order(self):
        order = Order.objects.create(
            item=self.item, buyer=self.user, price=self.item.price
        )
        self.assertEqual(order.price, 20.00)
        self.assertEqual(order.buyer.username, "buyer")
        self.assertEqual(order.item.title, "Test Item")
