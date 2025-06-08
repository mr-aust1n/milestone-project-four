from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_login_page_loads(self):
        response = self.client.post(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_signup_page_loads(self):
        response = self.client.post(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign Up")

    def test_logout_redirects(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(reverse("logout"))
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to homepage after logout
