from django.apps import AppConfig  # type: ignore # noqa: F401


class AuthorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authors"

    def ready(self, *args, **kwargs) -> None:
        import authors.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
