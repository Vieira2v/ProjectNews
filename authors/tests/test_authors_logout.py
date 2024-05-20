from django.test import TestCase  # type: ignore # noqa: F401
from django.contrib.auth.models import User  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401


class AuthorLogoutTest(TestCase):
    def test_user_tries_to_logout(self):
        User.objects.create_user(username='username', password='p@ssword')
        self.client.login(username='username', password='p@ssword')

        response = self.client.post(
            reverse('authors:logout'),
            follow=True
        )

        self.assertIn('Logout realized with success!',
                      response.content.decode('utf-8'))
