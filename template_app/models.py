from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()
