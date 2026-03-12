from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    area = models.CharField(max_length=100, default="大陆")
    type = models.ForeignKey(Type,on_delete=models.DO_NOTHING)

