from selenium import webdriver
from chat.models import Message
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestChat(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)

        alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            'Sorry, you have no project. ---'
        )


