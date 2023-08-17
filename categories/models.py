from django.db import models
import uuid

from foods.models import Foot

# Create your models here.
class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  foot = models.ForeignKey(Foot, on_delete=models.CASCADE)
  name = models.CharField(max_length=224, null=False, blank=False)
  description = models.TextField(max_length=224, null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'categories'

