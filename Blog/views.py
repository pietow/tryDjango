from django.shortcuts import render, get_object_or_404
from .forms import ArticleModelForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)

from .models import Article


class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()  # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'

    # queryset = Article.objects.all()
    # queries through our article table

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

