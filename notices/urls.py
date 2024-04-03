from django.urls import path  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401
from notices.views import home


urlpatterns = [
    path('', home),
]
