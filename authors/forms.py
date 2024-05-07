from django import forms  # type: ignore # noqa: F401
from django.contrib.auth.models import User  # type: ignore # noqa: F401
from django.core.exceptions import ValidationError  # type: ignore # noqa: F401


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        })
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'E-mail',
            'password': 'Password',
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

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
