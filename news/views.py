from django.shortcuts import render  # type: ignore # noqa: F401
from news.models import News
from django.http import Http404  # type: ignore # noqa: F401
from utils.pagination import make_pagination
from django.views.generic import ListView, DetailView  # type: ignore
from django.http import JsonResponse
from django.forms.models import model_to_dict  # type: ignore
import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


class NewsListViewBase(ListView):
    model = News
    context_object_name = 'news'
    ordering = ['-id']
    template_name = 'news/pages/home.html'

    # Manipulação de queryset, apenas noticias publicadas aparecerão.
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )
        return qs

    # Manipulação do contexto da pagina,
    # neste caso estou aplicando a minha, paginação.
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('news'),
            PER_PAGE
        )
        ctx.update(
            {'news': page_obj, 'pagination_range': pagination_range}
        )
        return ctx


class NewsListViewHome(NewsListViewBase):
    template_name = 'news/pages/home.html'


class NewsListViewHomeAPI(NewsListViewBase):
    template_name = 'news/pages/home.html'

    def render_to_response(self, context, **response_kwargs):
        news = self.get_context_data()['news']
        news_list = news.object_list.values()

        return JsonResponse(
            list(news_list),
            safe=False
            )


class NewsListViewIntenational(NewsListViewBase):
    template_name = 'news/pages/international.html'

    def get_queryset(self, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
            category__id=category_id,
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        news_queryset = self.get_queryset()

        page_obj, pagination_range = make_pagination(
            self.request,
            news_queryset,
            PER_PAGE
        )

        if news_queryset.exists():
            category_name = news_queryset.first().category.name
            title = f'{category_name} - Category |'
        else:
            title = 'No News - Category |'

        ctx.update(
            {'news': page_obj,
             'pagination_range': pagination_range,
             'title': title}
        )
        return ctx


class NewsListViewEconomy(NewsListViewIntenational):
    template_name = 'news/pages/economy.html'


class NewsListViewTechnology(NewsListViewIntenational):
    template_name = 'news/pages/technology.html'


class NewsListViewHealth(NewsListViewIntenational):
    template_name = 'news/pages/health.html'


class NewsListViewScience(NewsListViewIntenational):
    template_name = 'news/pages/science.html'


class NewsListViewSport(NewsListViewIntenational):
    template_name = 'news/pages/sport.html'


class NewsDetail(DetailView):
    model = News
    context_object_name = 'new'
    template_name = 'news/pages/news-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'is_detail_page': True,
        })

        return ctx


class NewsDetailAPI(NewsDetail):
    def render_to_response(self, context, **response_kwargs):
        news = self.get_context_data()['new']
        news_dict = model_to_dict(news)

        # Adicionando updated e created_at na API.
        news_dict['created_at'] = str(news.created_at)
        news_dict['updated_at'] = str(news.updated_at)

        # Json não responde há imagem, ent estou passando,
        # apenas a url da imagem.
        if news_dict.get('cover'):
            news_dict['cover'] = self.request.build_absolute_uri() + \
                news_dict['cover'].url[1:]
        else:
            ...

        # Deletando is_published e news_content_is_html da API.
        del news_dict['is_published']
        del news_dict['news_content_is_html']

        return JsonResponse(
            news_dict,
            safe=False
        )
