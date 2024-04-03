from django.shortcuts import render  # type: ignore # noqa: F401
from django.http import HttpResponse  # type: ignore # noqa: F401


def home(request):
    return render(request, 'notices/pages/home.html')
