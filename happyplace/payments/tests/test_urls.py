from django.test import SimpleTestCase
from django.urls import reverse, resolve
from payments.views import charge


class TestUrls(SimpleTestCase):

    def test_url(self):
        url = reverse('charge')
        print(resolve(url))
        self.assertEqual(resolve(url).func, charge)

