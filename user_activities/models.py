from django.db import models
import uuid
from users.models import User

class UserActivity(models.Model):
  SPIN = 'spin'
  ActivityChoice = (
      (SPIN, 'Spin'),
  )
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_activities')
  activity_name = models.CharField(choices=ActivityChoice, max_length=100)
  activity_date = models.DateField()
  result = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'user_activities'