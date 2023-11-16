from django.db import models

# Create your models here.
class MovieAdd(models.Model):
    """Model definition for MovieAdd."""

    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

