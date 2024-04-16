from django.urls import path  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401
from . import views

app_name = "news"

urlpatterns = [
    path('', views.home, name="home"),
    path('new/category/<int:category_id>/', views.category, name="category"),
    path('new/<int:id>/', views.new, name="detail"),
    path('new/search/', views.search, name="search"),
]
