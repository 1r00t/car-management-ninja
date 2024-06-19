from django.db import models
from django.core.validators import MinValueValidator


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField(validators=[MinValueValidator(1886)])
    color = models.CharField(max_length=100)
    price = models.FloatField()
