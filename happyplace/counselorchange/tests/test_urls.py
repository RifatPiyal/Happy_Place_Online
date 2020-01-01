from django.test import SimpleTestCase
from django.urls import reverse, resolve
from counselorchange.views import contact_us


class TestUrls(SimpleTestCase):

    def test_url(self):
        url = reverse('ch-contactus')
        print(resolve(url))
        self.assertEqual(resolve(url).func, contact_us)

