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


def new(request, id):
    new = News.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    if not new:
        raise Http404('Not found')

    return render(request, 'news/pages/news-view.html', context={
        'new': new,
        'is_detail_page': True,
    })


def international(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/international.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Category |'
    })


def economy(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/economy.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Category |'
    })


def technology(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/technology.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Technology |'
    })


def health(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/health.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Health |'
    })


def science(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/science.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Science |'
    })


def sport(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    if not news:
        raise Http404('Not found')

    return render(request, 'news/pages/sport.html', context={
        'news': news,
        'title': f'{news.first().category.name} - Sport |'
    })
