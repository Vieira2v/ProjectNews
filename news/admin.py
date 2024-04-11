from django.contrib import admin  # type: ignore # noqa: F401
from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
