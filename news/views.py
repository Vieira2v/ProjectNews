from django.shortcuts import render  # type: ignore # noqa: F401
from news.models import News
from django.http import Http404  # type: ignore # noqa: F401
from utils.pagination import make_pagination
import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    news = News.objects.filter(
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    return render(request, 'news/pages/home.html', context={
        'news': page_obj,
        'pagination_range': pagination_range
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
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news:
        return render(request, 'news/pages/international.html', context={
            'news': None,
            'pagination_range': None,
            'title': 'No news International found - Category |'
        })

    return render(request, 'news/pages/international.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Category |'
    })


def economy(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news:
        return render(request, 'news/pages/economy.html', context={
            'news': None,
            'pagination_range': None,
            'title': 'No news Economy found - Category |'
        })

    return render(request, 'news/pages/economy.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Category |'
    })


def technology(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news:
        return render(request, 'news/pages/technology.html', context={
                'news': None,
                'pagination_range': None,
                'title': 'No news Technology found - Category |'
        })

    return render(request, 'news/pages/technology.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Technology |'
    })


def health(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news.exists():
        return render(request, 'news/pages/health.html', context={
            'news': None,
            'pagination_range': None,
            'title': 'No news Health found - Health |'
        })

    return render(request, 'news/pages/health.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Health |'
    })


def science(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news:
        return render(request, 'news/pages/science.html', context={
            'news': None,
            'pagination_range': None,
            'title': 'No news Science found - Category |'
        })

    return render(request, 'news/pages/science.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Science |'
    })


def sport(request, category_id):
    news = News.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, news, PER_PAGE)

    if not news:
        return render(request, 'news/pages/sport.html', context={
            'news': None,
            'pagination_range': None,
            'title': 'No news Sport found - Category |'
        })

    return render(request, 'news/pages/sport.html', context={
        'news': page_obj,
        'pagination_range': pagination_range,
        'title': f'{news.first().category.name} - Sport |'
    })
