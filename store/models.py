from django.db import models


# Create your models here.

class Product(models.Model):
      name = models.CharField(max_length=20)
      price = models.IntegerField(default=0)
      category = models.ForeignKey()
      des = models.CharField(max_length=200, default='')
      image = models.ImageField(upload_to='products/')


