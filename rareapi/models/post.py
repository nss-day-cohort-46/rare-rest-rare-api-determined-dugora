from rareapi.models.posttag import PostTag
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
import datetime

class Post(models.Model):
    user=models.ForeignKey("RareUser", on_delete=CASCADE)
    category=models.ForeignKey("Category", on_delete=DO_NOTHING)
    title=models.CharField(max_length=50)
    publication_date=models.DateTimeField(default=datetime.now())
    image_url=models.ImageField()
    content=models.CharField(max_length=50)
    approved=models.BooleanField()
    tags=models.ManyToManyField("Tag", through="PostTag", related_name="posts")
    reactions=models.ManyToManyField("Reaction", through="PostReaction", related_name="posts")
