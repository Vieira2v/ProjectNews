from django.urls import path  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401
from . import views

app_name = "news"

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<int:id>/', views.new, name="detail"),
    path('news/international/<int:category_id>/',
         views.international, name="international"),
    path('news/economy/<int:category_id>/',
         views.economy, name="economy"),
    path('news/technology/<int:category_id>/',
         views.technology, name="technology"),
    path('news/health/<int:category_id>/',
         views.health, name="health"),
    path('news/science/<int:category_id>/',
         views.science, name="science"),
    path('news/sport/<int:category_id>/',
         views.sport, name="sport"),
]
