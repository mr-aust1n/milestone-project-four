# items/tests_views.py

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.item = Item.objects.create(
            title="Test Item",
            description="Test description",
            category="books",
            price=10.00,
            quantity=1,
            seller=self.user,
        )

    def test_home_page_accessible(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Latest Items")

    def test_item_detail_page(self):
        response = self.client.get(reverse("item_detail", args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.title)

    def test_add_item_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("add_item"))
        self.assertRedirects(response, f"/accounts/login/?next=/add/")

    def test_add_item_logged_in(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("add_item"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add")

    def test_edit_item_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("edit_item", args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.title)

    def test_delete_item_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("delete_item", args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete")
