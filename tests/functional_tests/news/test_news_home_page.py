from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase  # type: ignore # noqa: E501
from unittest.mock import patch
from utils.browser import make_chrome_browser
from news.templates.news.tests.test_news_base import NewsMixin
import time
import pytest


class NewsBaseFunctionalTest(StaticLiveServerTestCase, NewsMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)


@pytest.mark.functional_test
class NewsHomePageTest(NewsBaseFunctionalTest):
    @patch('news.views.PER_PAGE', new=3)
    def test_news_home_page_without_news_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No news found here', body.text)
