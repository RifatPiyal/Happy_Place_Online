from django.test import SimpleTestCase
from counselorchange.forms import ContactForm


class TestForms(SimpleTestCase):

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'name': 'rifat',
            'subject': 'account',
            'email': 'rifat@gmail.com',
            'message': 'change'

        })

        self.assertTrue(form.is_valid())

    def test_contact_form_no_data(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
