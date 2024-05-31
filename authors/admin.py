from django.contrib import admin  # type: ignore # noqa: F401
from authors.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
