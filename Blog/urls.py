from django.urls import path
from .views import (
    ArticleUpdateView,
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # The keyword argument must be pk,
    # pk is defined by DetailView
    # pk is overwritten in def get_object of ArticleDetailView
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update')

]
