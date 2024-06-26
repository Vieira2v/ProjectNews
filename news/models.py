from django.db import models  # type: ignore # noqa: F401
from django.contrib.auth.models import User  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401
from django.utils.text import slugify  # type: ignore # noqa: F401
from collections import defaultdict  # type: ignore  # noqa: F401
from django.forms import ValidationError  # type: ignore


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

    def get_absolute_url(self):
        return reverse("news:detail", args=(self.id,))
    # Função criada para criar um botão para redirecionar a receita,
    # vista na admin para o site, 'View on site'

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        return super().save(*args, **kwargs)
    # Função criada para criar uma slug de acordo o title da noticia.

    # Validação para n ter noticias com o msm titulo.
    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)

        news_from_db = News.objects.filter(
            title__iexact=self.title
        ).first()

        if news_from_db:
            if news_from_db.pk != self.pk:
                error_messages['title'].append(
                    'Found news with the same title'
                )

        if error_messages:
            raise ValidationError(error_messages)
