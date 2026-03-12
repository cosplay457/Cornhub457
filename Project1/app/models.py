from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    in_time = models.DateField()
    type = models.CharField(max_length=50)