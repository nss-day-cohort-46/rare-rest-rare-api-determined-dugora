from django.db import models
from django.db.models.deletion import CASCADE

class RareUser(models.Model):
    user_id=models.ForeignKey("RareUser", on_delete=CASCADE)
    bio=models.CharField(max_length=50)
    profile_image_url=models.CharField(max_length=50)
    created_on=models.DateTimeField()
    active=models.BooleanField()
    