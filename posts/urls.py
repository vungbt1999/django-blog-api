from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api_views import PostListViewSet

router = DefaultRouter()
router.register(r'posts', PostListViewSet, basename='post')
urlpatterns = [
  path('', include(router.urls)),
]
