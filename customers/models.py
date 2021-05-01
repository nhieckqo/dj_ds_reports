from django.db import models
from django.db.models.base import Model

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='customers', default='no_picture.png')

    def __str__(self):
        return str(self.name)