from unittest import TestCase  # type: ignore # noqa: F401
from authors.forms import RegisterForm  # type: ignore # noqa: F401
from parameterized import parameterized  # type: ignore # noqa: F401


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
