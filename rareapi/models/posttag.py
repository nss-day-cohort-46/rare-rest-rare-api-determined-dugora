from django.db import models
from django.db.models.deletion import CASCADE

class PostTag(models.Model):
    tag=models.ForeignKey("Tag", on_delete=CASCADE)
    post=models.ForeignKey("Post", on_delete=CASCADE)