from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField()
