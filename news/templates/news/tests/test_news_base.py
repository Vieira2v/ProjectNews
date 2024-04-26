from django.test import TestCase  # type: ignore # noqa: F401
from news.models import Category, News
from django.contrib.auth.models import User  # type: ignore # noqa: F401


class NewsTestBase(TestCase):

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='1234567',
        email='user@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,)

    def make_news(
        self,
        category_data=None,
        author_data=None,
        title=None,
        description='News Description',
        slug='news-slug',
        news_content='News Content',
        news_content_is_html=False,
        is_published=True,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        if title is None:
            title = 'News Title'  # Título padrão se nenhum for especificado.

        return News.objects.create(  # noqa: F841
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            news_content=news_content,
            news_content_is_html=news_content_is_html,
            is_published=is_published,
            # Notícia criada.
            # Este trecho de código acima é para dar suporte há todos
            # os meus testes, todos os testes vão ter 1 notícia criada.
        )
