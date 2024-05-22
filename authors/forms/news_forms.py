from django import forms  # type: ignore
from news.models import News
from collections import defaultdict
from django.core.exceptions import ValidationError  # type: ignore


class AuthorNewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._myerrors = defaultdict(list)

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

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if len(title) < 5:
            self._myerrors['title'].append('Must have at least 5 chars.')

        if title == description:
            self._myerrors['title'].append('Cannot be equal to description')
            self._myerrors['description'].append('Cannot be equal to title')

        if self._myerrors:
            raise ValidationError(self._myerrors)

        return super_clean

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            self._myerrors['title'].append('Must have at least 5 chars.')

        return title
