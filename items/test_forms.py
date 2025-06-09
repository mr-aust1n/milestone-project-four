from django.test import TestCase

from items.forms import ItemForm


class ItemFormValidationTest(TestCase):

    def test_item_form_missing_required_fields(self):
        form_data = {
            "title": "",  # Assume this is a required field
            "price": "",  # Assume this is also required
        }
        form = ItemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("price", form.errors)
