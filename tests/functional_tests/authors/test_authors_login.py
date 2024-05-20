from django.contrib.staticfiles.testing import StaticLiveServerTestCase  # type: ignore # noqa: E501
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from django.urls import reverse  # type: ignore
import pytest
import time


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div/form'
        )


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input').send_keys(
                'First Name'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input').send_keys(
                'Last Name'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[4]/input').send_keys(
                'Username'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[5]/input').send_keys(
                'anny@email.com'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[6]/input').send_keys(
                'Str@ngP@ssword1'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[7]/input').send_keys(
                'Str@ngP@ssword1'
            )

        form.submit()

        self.browser.get(self.live_server_url + '/authors/login/')
        form = self.get_form()

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input').send_keys(
                'Username'
            )

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input').send_keys(
                'Str@ngP@ssword1'
            )

        form.submit()

        self.assertIn('Your are logged in.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url +
                         reverse('authors:login_create'))
        self.assertIn('Not Found',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_login_invalid_credentials(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input').send_keys(
                'First Name'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input').send_keys(
                'Last Name'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[4]/input').send_keys(
                'Username'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[5]/input').send_keys(
                'anny@email.com'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[6]/input').send_keys(
                'Str@ngP@ssword1'
            )
        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[7]/input').send_keys(
                'Str@ngP@ssword1'
            )

        form.submit()

        self.browser.get(self.live_server_url + '/authors/login/')
        form = self.get_form()

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input').send_keys(
                'Usernamee'
            )

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input').send_keys(
                'Str@ngP@ssword1'
            )

        form.submit()

        self.assertIn('Invalid credentials.',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_login_invalid_username_or_password(self):
        self.browser.get(self.live_server_url + '/authors/login/')
        form = self.get_form()

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input').send_keys(
                ''
            )

        self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input').send_keys(
                ''
            )

        form.submit()

        self.assertIn('Invalid username or password.',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
