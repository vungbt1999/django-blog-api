from django.db import models
import uuid

from users.models import User

# Create your models here.
class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=224, null=False, blank=False)
  description = models.TextField(max_length=224, null=False, default=None, blank=False)
  content = models.TextField(null=False, blank=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='posts')
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.content

  class Meta:
    db_table = 'posts'