from django.urls import reverse, resolve  # type: ignore # noqa: F401
# Reverse é usado para buscar a url que eu quero.
# Resolve é usado para saber qual função esta sendo usando por uma url.
from news import views
from .test_news_base import NewsTestBase  # type: ignore # noqa: F401


class NewsCategoryViewsTest(NewsTestBase):
    def test_news_international_views_function_is_correct(self):
        view = resolve(
            reverse('news:international', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewIntenational)

    def test_news_international_template_loads_news(self):
        needed_title = 'This is a international page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:international', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_international_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:international', kwargs={'category_id': 1000}))
        self.assertIn('No international news found',
                      response.content.decode('utf-8'))

    def test_news_economy_views_function_is_correct(self):
        view = resolve(
            reverse('news:economy', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewEconomy)

    def test_news_economy_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:economy', kwargs={'category_id': 1000}))
        self.assertIn('No economy news found',
                      response.content.decode('utf-8'))

    def test_news_economy_template_loads_news(self):
        needed_title = 'This is a economy page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:economy', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_technology_views_function_is_correct(self):
        view = resolve(
            reverse('news:technology', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewTechnology)

    def test_news_technology_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:technology', kwargs={'category_id': 1000}))
        self.assertIn('No technology news found',
                      response.content.decode('utf-8'))

    def test_news_technology_template_loads_news(self):
        needed_title = 'This is a technology page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:technology', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_health_views_function_is_correct(self):
        view = resolve(
            reverse('news:health', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewHealth)

    def test_news_health_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:health', kwargs={'category_id': 1000}))
        self.assertIn('No health news found',
                      response.content.decode('utf-8'))

    def test_news_health_template_loads_news(self):
        needed_title = 'This is a health page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:health', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_science_views_function_is_correct(self):
        view = resolve(
            reverse('news:science', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewScience)

    def test_news_science_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:science', kwargs={'category_id': 1000}))
        self.assertIn('No science news found',
                      response.content.decode('utf-8'))

    def test_news_science_template_loads_news(self):
        needed_title = 'This is a science page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:science', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_news_sport_views_function_is_correct(self):
        view = resolve(
            reverse('news:sport', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.NewsListViewSport)

    def test_news_sport_views_returns_404_if_no_news_found(self):
        response = self.client.get(
            reverse('news:sport', kwargs={'category_id': 1000}))
        self.assertIn('No sport news found',
                      response.content.decode('utf-8'))

    def test_news_sport_template_loads_news(self):
        needed_title = 'This is a sport page'
        self.make_news(title=needed_title)

        response = self.client.get(
            reverse('news:sport', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
