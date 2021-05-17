from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

class PostReaction(models.Model):
    user=models.ForeignKey("RareUser", on_delete=CASCADE)
    post=models.ForeignKey("Post", on_delete=CASCADE)
    reaction=models.ForeignKey("Reaction", on_delete=DO_NOTHING)
    