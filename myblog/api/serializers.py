from django.contrib.auth.models import AbstractBaseUser, User
from rest_framework import serializers
from myblog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'id']
    
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'
    