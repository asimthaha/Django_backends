from django.db import models

# Create your models here.
class RecipeAddModel(models.Model):
    """Model definition for RecipeAddModel."""

    name= models.CharField(default='', max_length=100)
    author= models.CharField(default='', max_length=100)
    dateCreated= models.CharField(default='', max_length=100)
    ingredients= models.CharField(default='', max_length=100)
    description= models.CharField(default='', max_length=100)
    type= models.CharField(default='', max_length=100)

    class Meta:
        """Meta definition for RecipeAddModel."""

        verbose_name = 'RecipeAddModel'
        verbose_name_plural = 'RecipeAddModels'

    def __str__(self):
        """Unicode representation of RecipeAddModel."""
        pass
