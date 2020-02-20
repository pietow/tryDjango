from django.shortcuts import render
from .forms import ArticleForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)

from .models import Article

class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all() #blog/<modelname>_list.html