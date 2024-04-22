from django.test import TestCase  # type: ignore # noqa: F401
from django.urls import reverse, resolve  # type: ignore # noqa: F401
# Reverse é usado para buscar a url que eu quero.
# Resolve é usado para saber qual função esta sendo usando por uma url.
from news import views
from news.models import Category, News
from django.contrib.auth.models import User  # type: ignore # noqa: F401


class NewsViewsTest(TestCase):
    def test_news_home_views_function_is_correct(self):
        view = resolve(reverse('news:home'))
        self.assertIs(view.func, views.home)
        # view.func é a função retornada pelo resolve na variavel view.

    def test_news_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('news:home'))
        # O método GET é usado para pedir dados de um servidor,
        # como solicitar uma página da web.
        self.assertEqual(response.status_code, 200)

    def test_news_home_view_loads_correct_template(self):
        response = self.client.get(reverse('news:home'))
        # O cliente solicitou a minha url home a cima.
        self.assertTemplateUsed(response, 'news/pages/home.html')
        # E agora eu testei se minha url home esta carregando o template certo.

    def test_news_home_template_shows_no_news_found_if_no_news(self):
        response = self.client.get(reverse('news:home'))
        self.assertIn('No recipes found here',
                      response.content.decode('utf-8'))
        # self.assertIn('No recipes found here', ...)
        # está sendo usado para verificar se a string 'No recipes found here'
        # está presente no objeto que está sendo testado.
        # response.content é usado para acessar o conteúdo da
        # resposta de uma solicitação HTTP.
        # response.content é uma sequência de bytes (bytes object),
        # não uma string diretamente utilizável.
        # Portanto, response.content.decode('utf-8') é utilizado
        # para decodificar essa sequência de bytes em uma string legível.

    def test_news_home_template_loads_news(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='1234567',
            email='user@email.com',)
        news = News.objects.create(  # noqa: F841
            category=category,
            author=author,
            title='News Title',
            description='News Description',
            slug='news-slug',
            news_content='News Content',
            news_content_is_html=False,
            is_published=True,
            # Notícia criada.
            # Este trecho de código acima é para dar suporte ao meu código,
            # chamado de fixtures.
        )
        response = self.client.get(reverse('news:home'))
        # Meu cliente fez acesso a minha home.
        content = response.content.decode('utf-8')
        # Minha home gerou um conteudo, e eu tive que decodificar.
        response_context_news = response.context['news']
        # Aqui estou pegando todas as receitas que teu no meu contexto.
        # No caso 1 pq eu só criei 1.
        self.assertIn('News Title', content)
        self.assertIn('News Description', content)
        # E agora eu testei se tem as frase no conteudo.
        self.assertEqual(len(response_context_news), 1)

    def test_news_category_views_function_is_correct(self):
        view = resolve(reverse('news:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_news_category_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_detail_views_function_is_correct(self):
        view = resolve(reverse('news:detail', kwargs={'id': 1}))
        self.assertIs(view.func, views.new)

    def test_news_detail_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:detail', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_international_views_function_is_correct(self):
        view = resolve(
            reverse('news:international', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.international)

    def test_news_international_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:international', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_economy_views_function_is_correct(self):
        view = resolve(
            reverse('news:economy', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.economy)

    def test_news_economy_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:economy', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_technology_views_function_is_correct(self):
        view = resolve(
            reverse('news:technology', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.technology)

    def test_news_technology_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:technology', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_health_views_function_is_correct(self):
        view = resolve(
            reverse('news:health', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.health)

    def test_news_health_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:health', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_science_views_function_is_correct(self):
        view = resolve(
            reverse('news:science', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.science)

    def test_news_science_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:science', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_sport_views_function_is_correct(self):
        view = resolve(
            reverse('news:sport', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.sport)

    def test_news_sport_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:sport', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)
