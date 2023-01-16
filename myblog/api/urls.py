from django.urls import path
from myblog.api import views


app_name = 'myblog'

urlpatterns = [
    path('', views.get_post, name="index"),
    path('post_detail',views.get_post_detail,name="detail"),
    path('delete_post',views.delete_post,name="delete"),
    path('create_post',views.create_post,name="create"),

]
