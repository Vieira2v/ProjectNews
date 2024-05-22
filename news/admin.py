from django.contrib import admin  # type: ignore # noqa: F401
from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'is_published']
    list_display_links = ['title', 'created_at']
    search_fields = ['id', 'title', 'description', 'slug', 'news_content']
    list_filter = ['category', 'author', 'is_published',
                   'news_content_is_html']
    list_per_page = 10
    list_editable = ['is_published',]
    ordering = ['-id']
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Category, CategoryAdmin)
