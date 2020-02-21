from django.urls import path
from .views import (
    CourseListView,
    CourseView,
    CourseCreateView,
    CourseUpdateView,
    my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', my_fbv, name='course-list')
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')

]
