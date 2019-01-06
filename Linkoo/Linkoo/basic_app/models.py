from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=216, blank=False)
    key = models.CharField(max_length=216, unique=True, blank=False)
    url = models.URLField()

