from django.db import models
import datetime

class Comment(models.Model):
    post=models.ForeignKey("Post", on_delete=models.CASCADE)
    author=models.ForeignKey("Author", on_delete=models.CASCADE)
    content=models.CharField(max_length=50)
    created_on=models.DateTimeField(default=datetime.now())