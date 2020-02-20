from django.urls import path
from .views import (
    CourseView,
    my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='home.html'), name='courses-list'),
    # path('', my_fbv, name='course-list')
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')

]
