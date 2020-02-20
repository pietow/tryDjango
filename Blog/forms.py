from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "your title"
    }))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "your title",
        "id": "text-id",
        "rows": 10,
        "cols": 10
    }))
   #
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
