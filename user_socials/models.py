from django.db import models
import uuid
from users.models import User

# Create your models here.
class UserSocial(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='social')
  provider = models.JSONField(null=True)
  social_id = models.CharField(max_length=200)

  class Meta:
    db_table = 'user_socials'