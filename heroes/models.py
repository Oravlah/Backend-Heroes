from django.db import models

# Create your models here.


class Heroes(models.Model):
    fullname = models.CharField(max_length=20)
    nombreheroe = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=100)
    power = models.CharField(max_length=100)