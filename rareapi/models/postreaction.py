from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

class PostReaction(models.Model):
    user_id=models.ForeignKey("RareUser", on_delete=CASCADE)
    post_id=models.ForeignKey("Post", on_delete=CASCADE)
    reaction_id=models.ForeignKey("Reaction", on_delete=DO_NOTHING)