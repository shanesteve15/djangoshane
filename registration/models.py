from django.db import models

class student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
# Create your models here.
