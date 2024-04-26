from django.db import models  # type: ignore # noqa: F401
from django.contrib.auth.models import User  # type: ignore # noqa: F401


# Uma tabela. MySQL
class Category(models.Model):
    name = models.CharField(max_length=85)

# Função criada para aparecer o nome da categoria la na admin
    def __str__(self):
        return self.name


# Outra tabela. MySQL
class News(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    news_content = models.TextField()
    news_content_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='news/covers/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True, default=None)

# Função criada para aparecer o titulo da noticia la na admin
    def __str__(self):
        return self.title
