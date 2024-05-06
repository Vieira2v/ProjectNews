from django.shortcuts import render  # type: ignore # noqa: F401
from .forms import RegisterForm
from django.http import Http404  # type: ignore # noqa: F401


def register_view(request):
    form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm(request.POST)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
