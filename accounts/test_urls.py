from django.test import SimpleTestCase
from django.urls import resolve, reverse

from items.views import dashboard


class UrlResolutionTest(SimpleTestCase):
    def test_dashboard_url_resolves(self):
        url = reverse("dashboard")
        self.assertEqual(resolve(url).func, dashboard)
