from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from checkout.models import Order
from items.models import Item


class CheckoutViewsTest(TestCase):

    def setUp(self):
        self.seller = User.objects.create_user(username="seller", password="testpass")
        self.buyer = User.objects.create_user(username="buyer", password="testpass")
        self.item = Item.objects.create(
            title="Test Item",
            description="Test Description",
            category="fashion",
            price=10.00,
            seller=self.seller,
            quantity=1,
        )
        self.client.login(username="buyer", password="testpass")

    def test_make_offer_get(self):
        """Check that offer page loads correctly for buyer."""
        url = reverse("make_offer", args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Offer")

    def test_make_offer_post_valid(self):
        """Submit valid offer and check it's created."""
        url = reverse("make_offer", args=[self.item.id])
        response = self.client.post(url, {"offer_price": 8.00, "note": "Test offer"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/offer_submitted.html")
        self.assertTrue(Order.objects.filter(buyer=self.buyer, item=self.item).exists())

    def test_make_offer_redirect_if_invalid(self):
        """Test redirect if trying to offer on sold item."""
        self.item.is_sold = True
        self.item.save()
        url = reverse("make_offer", args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
