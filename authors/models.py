from django.db import models  # type: ignore # noqa: F401
from django.contrib.auth import get_user_model  # type: ignore # noqa: F401

User = get_user_model()


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
