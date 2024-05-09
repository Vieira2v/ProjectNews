import re

from django import forms  # type: ignore # noqa: F401
from django.contrib.auth.models import User  # type: ignore # noqa: F401
from django.core.exceptions import ValidationError  # type: ignore # noqa: F401


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. The length should be'
            'at least 8 characters.'), code='Invalid')


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    first_name = forms.CharField(
        label='First name',
        error_messages={'required': 'Write your first name'},
    )

    last_name = forms.CharField(
        label='Last name',
        error_messages={'required': 'Write your last name'},
    )

    username = forms.CharField(
        label='Username',
        error_messages={
            'required':
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters.',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
            },
        min_length=4, max_length=150,
    )

    email = forms.CharField(
        label='E-mail',
        error_messages={'required': 'Email is required'},
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[strong_password],
        label='Password',
        error_messages={'required': 'Password must not be empty'}
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm password',
        error_messages={'required': 'Please, repeat your passsword'}
    )

    def clean(self):
        cleaned_data = super().clean()
        # Aqui estou chamando a classe pai do metodo clean, para
        # fazer a validação das minhas 2 senhas.

        password = cleaned_data.get('password')
        # Aqui estou acessando o valor digitado nas 2 password
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError({
                'password': 'Password and Confirm password must be equal',
                'confirm_password':
                    'Password and Confirm password must be equal'
            })
