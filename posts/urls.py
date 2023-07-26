from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api_views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns = [
  path('api/', include(router.urls)),
]