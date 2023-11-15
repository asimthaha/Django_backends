from django.db import models

# Create your models here

class StudentModel(models.Model):
    """Model definition for StudentModel."""

    name=models.CharField(max_length=100, default="")
    admno=models.CharField(max_length=100, default="")
    rollno=models.CharField(max_length=100, default="")
    college=models.CharField(max_length=100, default="")

    class Meta:
        """Meta definition for StudentModel."""

        verbose_name = 'StudentModel'
        verbose_name_plural = 'StudentModels'

    def __str__(self):
        """Unicode representation of StudentModel."""
        pass
