from django.urls import reverse, resolve  # type: ignore # noqa: F401
# Reverse é usado para buscar a url que eu quero.
# Resolve é usado para saber qual função esta sendo usando por uma url.
from news import views
from .test_news_base import NewsTestBase  # type: ignore # noqa: F401


class NewsHomeViewsTest(NewsTestBase):
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
        self.assertIn('No news found here',
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
        self.make_news()
        response = self.client.get(reverse('news:home'))
        # Meu cliente fez acesso a minha home.
        content = response.content.decode('utf-8')
        # Minha home gerou um conteudo, e eu tive que decodificar.
        response_context_news = response.context['news']
        # Aqui estou pegando todas as receitas que teu no meu contexto.
        # No caso 1 pq eu só criei 1.
        self.assertIn('News Title', content)
        # E agora eu testei se tem as frase no conteudo.
        self.assertEqual(len(response_context_news), 1)

    def test_news_home_template_dont_load_news_not_published(self):
        self.make_news(is_published=False)
        response = self.client.get(reverse('news:home'))
        # Meu cliente fez acesso a minha home.
        self.assertIn('No news found here',
                      response.content.decode('utf-8'))
