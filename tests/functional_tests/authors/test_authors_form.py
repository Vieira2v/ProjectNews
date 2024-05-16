from django.contrib.staticfiles.testing import StaticLiveServerTestCase  # type: ignore # noqa: E501
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


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
class AuthorsRegisterTest(AuthorsBaseTest):
    def test_empty_first_name_error_message(self):
        # Acessei a url de registro e selecionei o meu form.
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        # Fields = todos os meus INPUTS
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

        # Selecionei o input First Name,
        # no caso o primeiro input do form para dar inicio.
        first_name_field = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[2]/input')
        # Como o email n da para ter só espaços em branco,
        # tive que digitar um email qualquer.
        form.find_element(By.NAME, 'email').send_keys('anny@email.com')
        first_name_field.send_keys(Keys.ENTER)

        # E por fim, tive que selecionar o form denovo, pq dei enter,
        # e recarregou a página.
        form = self.get_form()

        # E aqui qro saber se esta aparecendo esta mensagem de erro,
        # ao enviar o form incorreto.
        self.assertIn('Write your first name', form.text)

    def test_empty_last_name_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

        last_name_field = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[3]/input')

        form.find_element(By.NAME, 'email').send_keys('anny@email.com')
        last_name_field.send_keys(Keys.ENTER)

        form = self.get_form()

        self.assertIn('Write your last name', form.text)

    def test_invalid_username_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

        username_field = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[4]/input')

        form.find_element(By.NAME, 'email').send_keys('anny@email.com')
        username_field.send_keys(Keys.ENTER)

        form = self.get_form()

        self.assertIn(
            'Username must have letters, numbers or one of those @.+-_.'
            ' The length should be between 4 and 150 characters.', form.text)

    def test_invalid_email_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

        email_field = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[5]/input')

        form.find_element(By.NAME, 'email').send_keys('anny@emailcom')
        email_field.send_keys(Keys.ENTER)

        form = self.get_form()

        self.assertIn('Enter a valid email address.', form.text)

    def test_passwords_do_not_match(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

        password = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[6]/input')

        confirm_password = self.browser.find_element(
            By.XPATH, '/html/body/main/div/form/div/div[7]/input')

        confirm_password.send_keys('AAaa')

        form.find_element(By.NAME, 'email').send_keys('anny@email.com')
        password.send_keys(Keys.ENTER)

        form = self.get_form()

        self.assertIn('Password and Confirm password must be equal', form.text)

    def test_user_valid_data_register_successfully(self):
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

        self.assertIn('Your user is created, please log in.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )
