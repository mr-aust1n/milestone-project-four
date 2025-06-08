from django.test import TestCase
from django.urls import reverse


class PermissionsTest(TestCase):

    def test_dashboard_redirects_for_anonymous_user(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, "/accounts/login/?next=/dashboard/")
