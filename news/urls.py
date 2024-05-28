from django.urls import path  # type: ignore # noqa: F401
from . import views

app_name = "news"

urlpatterns = [
    path('', views.NewsListViewHome.as_view(), name="home"),
    path('news/api/v1/',
         views.NewsListViewHomeAPI.as_view(),
         name="home_api_v1"),
    path('news/<int:pk>/', views.NewsDetail.as_view(), name="detail"),
    path('news/api/v1/<int:pk>/',
         views.NewsDetailAPI.as_view(),
         name="detail_api_v1"),
    path('news/international/<int:category_id>/',
         views.NewsListViewIntenational.as_view(), name="international"),
    path('news/economy/<int:category_id>/',
         views.NewsListViewEconomy.as_view(), name="economy"),
    path('news/technology/<int:category_id>/',
         views.NewsListViewTechnology.as_view(), name="technology"),
    path('news/health/<int:category_id>/',
         views.NewsListViewHealth.as_view(), name="health"),
    path('news/science/<int:category_id>/',
         views.NewsListViewScience.as_view(), name="science"),
    path('news/sport/<int:category_id>/',
         views.NewsListViewSport.as_view(), name="sport"),
]
