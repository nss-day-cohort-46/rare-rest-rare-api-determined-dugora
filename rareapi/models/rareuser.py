from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import now

class RareUser(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE)
    bio=models.CharField(max_length=50)
    profile_image_url=models.ImageField()
    created_on=models.DateTimeField(default=now)
    active=models.BooleanField()
