from django.views import View  # type: ignore # noqa: F401
from news.models import News
from django.http.response import Http404  # type: ignore # noqa: F401
from authors.forms.news_forms import AuthorNewsForm
from django.contrib import messages  # type: ignore # noqa: F401
from django.shortcuts import redirect, render  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401
from django.utils. decorators import method_decorator  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore


@method_decorator(
        login_required(login_url='authors:login', redirect_field_name='next'),
        name='dispatch'
    )
class DashboardNews(View):
    def get_news(self, id=None):
        news = None

        if id is not None:
            news = News.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not news:
                raise Http404()

        return news

    def render_news(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_news.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        news = self.get_news(id)
        form = AuthorNewsForm(instance=news)
        return self.render_news(form)

    def post(self, request, id=None):
        news = self.get_news(id)
        form = AuthorNewsForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=news
        )

        if form.is_valid():
            news = form.save(commit=False)

            news.author = request.user
            news.news_content_is_html = False
            news.is_published = False

            news.save()

            messages.success(request, 'Your news was saved successfully!')
            return redirect(reverse(
                'authors:dashboard_news_edit', args=(
                    news.id,)))

        return self.render_news(form)


@method_decorator(
        login_required(login_url='authors:login', redirect_field_name='next'),
        name='dispatch'
    )
class DashboardNewsDelete(DashboardNews):
    def post(self, *args, **kwargs):
        news = self.get_news(self.request.POST.get('id'))
        news.delete()
        messages.success(self.request, 'Deleted successfully')
        return redirect(reverse('authors:dashboard'))
