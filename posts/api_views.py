from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from blog_api.pagination import CustomPagination
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Q

class PostListViewSet(ModelViewSet):
  serializer_class = PostSerializer
  pagination_class = CustomPagination

  def list(self, request, *args, **kwargs):
    search_value = request.GET.get('q')

    posts = Post.objects.all()

    if search_value:
      posts = posts.filter(
          Q(name__icontains=search_value) | Q(content__icontains=search_value)
      )
      
    posts_paging = self.paginate_queryset(posts)
    serializer = self.get_serializer(posts_paging, many=True)
    posts_serializer = serializer.data
    response = self.get_paginated_response(posts_serializer)

    return response
