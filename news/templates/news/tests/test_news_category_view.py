from django.urls import reverse, resolve  # type: ignore # noqa: F401
# Reverse é usado para buscar a url que eu quero.
# Resolve é usado para saber qual função esta sendo usando por uma url.
from news import views
from .test_news_base import NewsTestBase  # type: ignore # noqa: F401


class NewsCategoryViewsTest(NewsTestBase):
    def test_news_international_views_function_is_correct(self):
        view = resolve(
            reverse('news:international', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.international)

    def test_news_international_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:international', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_international_template_loads_news(self):
        needed_title = 'This is a international page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:international', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_international_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:international',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)

    def test_news_economy_views_function_is_correct(self):
        view = resolve(
            reverse('news:economy', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.economy)

    def test_news_economy_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:economy', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_economy_template_loads_news(self):
        needed_title = 'This is a economy page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:economy', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_economy_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:economy',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)

    def test_news_technology_views_function_is_correct(self):
        view = resolve(
            reverse('news:technology', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.technology)

    def test_news_technology_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:technology', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_technology_template_loads_news(self):
        needed_title = 'This is a technology page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:technology', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_technology_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:technology',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)

    def test_news_health_views_function_is_correct(self):
        view = resolve(
            reverse('news:health', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.health)

    def test_news_health_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:health', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_health_template_loads_news(self):
        needed_title = 'This is a health page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:health', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_health_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:health',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)

    def test_news_science_views_function_is_correct(self):
        view = resolve(
            reverse('news:science', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.science)

    def test_news_science_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:science', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_science_template_loads_news(self):
        needed_title = 'This is a science page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:science', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_science_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:science',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)

    def test_news_sport_views_function_is_correct(self):
        view = resolve(
            reverse('news:sport', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.sport)

    def test_news_sport_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:sport', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_news_sport_template_loads_news(self):
        needed_title = 'This is a sport page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:sport', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_sport_template_dont_load_news_not_published(self):
        news = self.make_news(is_published=False)
        response = self.client.get(
            reverse('news:sport',
                    kwargs={'category_id': news.category.id}))
        self.assertEqual(response.status_code, 404)
