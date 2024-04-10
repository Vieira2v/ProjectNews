from django.shortcuts import render  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401


def home(request):
    return render(request, 'news/pages/home.html')


def new(request, id):
    return render(request, 'news/pages/news-view.html')
