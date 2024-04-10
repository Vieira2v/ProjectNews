from django.urls import path  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401
from . import views


urlpatterns = [
    path('', views.home),
    path('new/<int:id>/', views.new),
]
