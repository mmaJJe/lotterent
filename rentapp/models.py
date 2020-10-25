from django.db import models
from userapp.models import CustomUser

class rent(models.Model):
    machine = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    inventory = models.IntegerField()
    provider = models.ManyToManyField(CustomUser)