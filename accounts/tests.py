# accounts / tests.py
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# accounts/tests.py


class AccountTests(TestCase):

    def test_signup_page_loads(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Your ReLuvd Account")

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_user_creation(self):
        user = User.objects.create_user(
            username="testuser", password="testpass123", email="test@example.com"
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass123"))
