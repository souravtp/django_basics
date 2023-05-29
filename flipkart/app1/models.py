from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=500)


class Cars(models.Model):
    model = models.CharField(max_length=250)
    make = models.CharField(max_length=250)
    year = models.IntegerField(validators=[MaxValueValidator(2023)])
