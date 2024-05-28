from django.contrib import admin  # type: ignore # noqa: F401
from django.urls import path, include  # type: ignore # noqa: F401
from django.conf.urls.static import static  # type: ignore # noqa: F401
from django.conf import settings  # type: ignore # noqa: F401


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('news.urls')),
    path('authors/', include('authors.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
