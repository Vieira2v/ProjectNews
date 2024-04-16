from django.shortcuts import render  # type: ignore # noqa: F401
from news.models import News
from django.http import Http404  # type: ignore # noqa: F401


def home(request):
    news = News.objects.filter(
        is_published=True,
    ).order_by('-id')
    return render(request, 'news/pages/home.html', context={
        'news': news,
    })


def category(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/category.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Category |'
    })


def new(request, id):
    new = News.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    return render(request, 'news/pages/news-view.html', context={
        'new': new,
        'is_detail_page': True,
    })


def search(request):
    return render(request, 'news/pages/search.html')
