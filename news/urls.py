from django.urls import path  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401
from . import views

app_name = "news"

urlpatterns = [
    path('', views.home, name="home"),
    path('new/category/<int:category_id>/', views.category, name="category"),
    path('new/<int:id>/', views.new, name="detail"),
    path('new/international/<int:category_id>/',
         views.international, name="international"),
    path('new/economy/<int:category_id>/',
         views.economy, name="economy"),
    path('new/technology/<int:category_id>/',
         views.technology, name="technology"),
    path('new/health/<int:category_id>/',
         views.health, name="health"),
    path('new/science/<int:category_id>/',
         views.science, name="science"),
    path('new/sport/<int:category_id>/',
         views.sport, name="sport"),
]
