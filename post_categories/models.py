from django.db import models
import uuid
from posts.models import Post

# Create your models here.
class PostCategory(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  name = models.CharField(max_length=224, null=False, blank=False)
  description = models.TextField(max_length=224, null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'post_categories'
