from django import forms  # type: ignore # noqa: F401


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        min_length=4, max_length=150,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
    )
