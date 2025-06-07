from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase


class UserCreationFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            "username": "testuser",
            "password1": "Testpass123!",
            "password2": "Testpass123!",
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form_data = {
            "username": "testuser",
            "password1": "Testpass123!",
            "password2": "Mismatch123!",
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_blank_username(self):
        form_data = {
            "username": "",
            "password1": "Testpass123!",
            "password2": "Testpass123!",
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
