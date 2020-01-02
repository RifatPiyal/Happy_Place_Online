from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chat.views import room, index


class TestUrls(SimpleTestCase):

    def test_urls(self):
        url = reverse('room', args=['some-slug'])
        print(resolve(url))


