from django.shortcuts import render  # type: ignore # noqa: F401
from utils.news.factory import make_news


def home(request):
    return render(request, 'news/pages/home.html', context={
        'news': [make_news() for _ in range(10)],
    })


def new(request, id):
    return render(request, 'news/pages/news-view.html', context={
        'new': make_news(),
    })
