from unittest import TestCase  # type: ignore # noqa: F401
from django.test import TestCase as DjangoTestCase  # type: ignore # noqa: F401
from authors.forms import RegisterForm  # type: ignore # noqa: F401
from parameterized import parameterized  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('username', 'Username'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('confirm_password', 'Confirm password'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': 'Str0ngP@ssword1',
            'confirm_passsword': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name'),
        ('username',
         'Username must have letters, numbers or one of those @.+-_. '
         'The length should be between 4 and 150 characters.'),
        ('email', 'Email is required'),
        ('password', 'Password must not be empty'),
        ('confirm_password', 'Please, repeat your passsword'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        # Deixei o formulário todo em branco.
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        # Enviei um post para a url de cima, contendo o formulário vazio.
        self.assertIn(msg, response.content.decode('utf-8'))
        # E aqui estou testando se neste conteudo que enviei, tem a msg
        # This field must not be empty.

    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = 'joa'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Username must have at least 4 characters'
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = 'j' * 151
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Username must have less than 150 characters'
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_field_have_lower_upper_and_case_letters_and_numbers(self):  # noqa: E501
        self.form_data['password'] = 'abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = (
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. The length should be'
            'at least 8 characters.')
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_and_password_confirmation_are_equal(self):  # noqa: E501
        self.form_data['password'] = '@A123abc123'
        self.form_data['confirm_password'] = '@A123abc1235'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Password and Confirm password must be equal'
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_send_get_request_to_registration_create_view_returns_404(self):  # noqa: E501
        url = reverse('authors:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_form_valid(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['confirm_password'] = '@A123abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Your user is created, please log in.'
        self.assertIn(msg, response.content.decode('utf-8'))
