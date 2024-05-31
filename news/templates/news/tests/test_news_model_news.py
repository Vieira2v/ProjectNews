from .test_news_base import NewsTestBase, News
from django.core.exceptions import ValidationError  # type: ignore
from parameterized import parameterized  # type: ignore


class NewsModelsTest(NewsTestBase):
    def setUp(self) -> None:
        self.news = self.make_news()
        return super().setUp()
    # Todos os meus testes ja vão ter uma receita criada.

    def make_news_no_default(self):
        news = News(
            category=self.make_category(name='Test Category'),
            author=self.make_author(username='testuser'),
            title='Qualquer Coisa',
            description='News Description',
            slug='new-slug',
            news_content='News Content',
            # Criei uma nova receita para este teste.
        )
        news.full_clean()
        news.save()
        return news

    @parameterized.expand([
            ('title', 80),
            ('description', 180),
        ])
    def test_news_fields_max_length(self, field, max_length):
        setattr(self.news, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.news.full_clean()  # Aqui ocorre a validação.

    def test_news_content_html_is_false_by_default(self):
        news = self.make_news_no_default()
        self.assertFalse(news.news_content_is_html)
        # Aqui estou afirmando que news_content_is_html é False
        # Se la no meu model estiver que é True, este meu teste
        # falhará.

    def test_news_is_published_is_false_by_default(self):
        news = self.make_news_no_default()
        self.assertFalse(news.is_published)
        # Aqui estou afirmando que is_published é False
        # Se la no meu model estiver que é True, este meu teste
        # falhará.

    def test_news_string_representation(self):
        self.news.title = 'Testing Representation'
        self.news.full_clean()
        self.news.save()
        self.assertEqual(str(self.news), 'Testing Representation')
        # Este teste está verificando, se convertermos o objeto para
        # uma string(title), o resultado é a string esperada,
        # que neste caso é 'Testing Representation'.
