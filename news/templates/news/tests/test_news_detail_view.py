from django.urls import reverse, resolve  # type: ignore # noqa: F401
# Reverse é usado para buscar a url que eu quero.
# Resolve é usado para saber qual função esta sendo usando por uma url.
from news import views
from .test_news_base import NewsTestBase  # type: ignore # noqa: F401


class NewsDetailViewsTest(NewsTestBase):
    def test_news_detail_views_function_is_correct(self):
        view = resolve(reverse('news:detail', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.NewsDetail)

    def test_news_detail_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:detail', kwargs={'pk': 1000}))

        self.assertEqual(response.status_code, 404)

    def test_news_detail_template_loads_the_correct_news(self):
        needed_title = 'This is a detail page - It load one news'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:detail', kwargs={'pk': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_detail_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:detail',
                    kwargs={'pk': news.pk}))
        self.assertEqual(response.status_code, 404)
