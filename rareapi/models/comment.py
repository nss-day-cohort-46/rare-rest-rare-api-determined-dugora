from django.db import models
from django.utils.timezone import now

class Comment(models.Model):
    post=models.ForeignKey("Post", on_delete=models.CASCADE)
    author=models.ForeignKey("RareUser", on_delete=models.CASCADE)
    content=models.CharField(max_length=50)
    created_on=models.DateTimeField(default=now)