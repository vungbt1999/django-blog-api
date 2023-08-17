from django.db import models
import uuid

# Create your models here.
class User(models.Model):
  ADMIN = 'admin'
  NORMAL_USER = 'normal_user'
  RoleChoice = (
      (ADMIN, 'Admin'),
      (NORMAL_USER, 'Normal_User'),
  )
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  username = models.CharField(max_length=100, null=True, blank=False, unique=True)
  email = models.EmailField(unique=True)
  role = models.CharField(choices=RoleChoice, default=NORMAL_USER, max_length=36, db_index=True)
  password = models.CharField(max_length=100, null=False, blank=False)

  class Meta:
    db_table = 'users'