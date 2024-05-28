from django.test import TestCase  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401
# Reverse é usado para meio que buscar a url que eu quero.


class NewsURLsTest(TestCase):
    def test_news_home_url_is_correct(self):
        url = reverse('news:home')
        self.assertEqual(url, '/')

    def test_news_detail_url_is_correct(self):
        url = reverse('news:detail', kwargs={'pk': 1})
        self.assertEqual(url, '/news/1/')

    def test_news_international_url_is_correct(self):
        url = reverse('news:international', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/international/1/')

    def test_news_economy_url_is_correct(self):
        url = reverse('news:economy', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/economy/1/')

    def test_news_technology_url_is_correct(self):
        url = reverse('news:technology', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/technology/1/')

    def test_news_health_url_is_correct(self):
        url = reverse('news:health', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/health/1/')

    def test_news_science_url_is_correct(self):
        url = reverse('news:science', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/science/1/')

    def test_news_sport_url_is_correct(self):
        url = reverse('news:sport', kwargs={'category_id': 1})
        self.assertEqual(url, '/news/sport/1/')
