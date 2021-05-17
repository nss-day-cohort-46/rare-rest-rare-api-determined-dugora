from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class DemotionQueue(models.Model):
    action=models.CharField(max_length=50)
    admin_id=ForeignKey("RareUser", on_delete=CASCADE)
    approver_one_id=ForeignKey("RareUser", on_delete=CASCADE)