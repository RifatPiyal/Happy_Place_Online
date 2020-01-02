from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import profile


class TestUrls(SimpleTestCase):

    def test_url(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

