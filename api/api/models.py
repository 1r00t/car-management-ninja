from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField(validators=[MinValueValidator(1886)])
    color = models.CharField(max_length=100)
    price = models.FloatField()

    def save(self, *args, **kwargs):
        if self.year < 1886:
            raise ValidationError("Cars were not invented yet!")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
