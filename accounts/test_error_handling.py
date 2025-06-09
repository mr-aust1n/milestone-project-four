from django.test import TestCase


class ErrorHandlingTest(TestCase):

    def test_404_error_on_invalid_url(self):
        response = self.client.get("/some-nonexistent-url/")
        self.assertEqual(response.status_code, 404)
