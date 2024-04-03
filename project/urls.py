from django.contrib import admin  # type: ignore # noqa: F401
from django.urls import path, include  # type: ignore # noqa: F401


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('notices.urls'))
]
