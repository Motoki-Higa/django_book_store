from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# https://docs.djangoproject.com/en/4.1/ref/models/fields/


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1


    # absolute url
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])


    # overwrite save() to use title for slug
    def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs) # this makes sure that Django's built-in save() method is still called


    # Below is to customise how the data is displayed in <QuerySet> in console
    def __str__(self):
        return f'{self.title} ({self.ratings})'
