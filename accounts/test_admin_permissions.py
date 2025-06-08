from django.contrib.auth.models import User
from django.test import TestCase


class AdminPermissionsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser", password="testpass"
        )

    def test_admin_access_denied_for_non_admin(self):
        self.client.login(username="regularuser", password="testpass")
        response = self.client.get("/admin/")
        self.assertNotEqual(response.status_code, 200)
