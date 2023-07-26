from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostSerializer

class PostViewSet(ModelViewSet):
  serializer_class = PostSerializer
  
  def get_queryset(self):
    return Post.objects.all()