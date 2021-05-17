from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now


class Subscription(models.Model):
    follower=models.ForeignKey("RareUser", on_delete=CASCADE)
    author=models.ForeignKey("RareUser", on_delete=CASCADE, related_name="rare_author")
    created_on=models.DateTimeField(default=now)
    ended_on=models.DateTimeField(null=True)