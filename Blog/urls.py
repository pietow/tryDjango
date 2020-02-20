from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail')
    # The keyword argument must be pk,
    # pk is defined by DetailView
    # pk is overwritten in def get_object of ArticleDetailView

]
