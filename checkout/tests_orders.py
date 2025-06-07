# checkout/tests_orders.py

from django.contrib.auth.models import User
from django.test import TestCase

from checkout.models import Order
from items.models import Item


class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="buyer", password="testpass")
        self.seller = User.objects.create_user(username="seller", password="testpass")
        self.item = Item.objects.create(
            title="Test Item",
            description="Description",
            category="other",
            price=50,
            quantity=5,
            seller=self.seller,
        )

    def test_order_creation_standard_purchase(self):
        """Order should correctly save non-offer purchases"""
        order = Order.objects.create(
            item=self.item, buyer=self.user, price=self.item.price, is_offer=False
        )
        self.assertEqual(order.item, self.item)
        self.assertEqual(order.buyer, self.user)
        self.assertEqual(order.price, 50)
        self.assertFalse(order.is_offer)

    def test_order_creation_offer_purchase(self):
        """Order should correctly save offers"""
        order = Order.objects.create(
            item=self.item,
            buyer=self.user,
            price=40,
            is_offer=True,
            offer_note="Testing offer",
        )
        self.assertTrue(order.is_offer)
        self.assertEqual(order.offer_note, "Testing offer")
