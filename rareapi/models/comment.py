from django.db import models

class Comment(models.Model):
    post_id=models.ForeignKey("Post", on_delete=models.CASCADE)
    author_id=models.ForeignKey("Author", on_delete=models.CASCADE)
    content=models.CharField(max_length=50)
    created_on=models.DateTimeField()