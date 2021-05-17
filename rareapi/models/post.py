from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

class Post(models.Model):
    user_id=models.ForeignKey("RareUser", on_delete=CASCADE)
    category_id=models.ForeignKey("Category", on_delete=DO_NOTHING)
    title=models.CharField(max_length=50)
    publication_date=models.DateField()
    image_url=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    approved=models.BooleanField()
