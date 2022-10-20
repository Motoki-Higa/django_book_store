from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# https://docs.djangoproject.com/en/4.1/ref/models/fields/


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    # Below is to customise how the data is displayed in <QuerySet> in console

    def __str__(self):
        return f'{self.title} ({self.ratings})'
