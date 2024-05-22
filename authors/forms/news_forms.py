from django import forms  # type: ignore
from news.models import News


class AuthorNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = 'title', 'description', 'news_content', 'cover'
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span2'
                }
            )
        }
