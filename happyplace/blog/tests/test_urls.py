from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import contact, login


class TestUrls(SimpleTestCase):

    def test_url_contact(self):
        url = reverse('blog-contact')
        print(resolve(url))
        self.assertEqual(resolve(url).func, contact)

    def test_url_login(self):
        url = reverse('blog-login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login)

