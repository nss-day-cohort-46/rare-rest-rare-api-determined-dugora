from django.db import models
from django.db.models.deletion import CASCADE

class Subscription(models.Model):
    follower_id=models.ForeignKey("RareUser", on_delete=CASCADE)
    author_id=models.ForeignKey("RareUser", on_delete=CASCADE)
    created_on=models.DateTimeField()
    ended_on=models.DateTimeField()