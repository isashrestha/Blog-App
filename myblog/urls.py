from .import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name = 'index'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name = 'post_detail'),
]