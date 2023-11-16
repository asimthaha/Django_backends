from django.db import models

# Create your models here.
class AssignmentAddModel(models.Model):
    """Model definition for AssignmentAddModel."""

    name=models.CharField(max_length=100,default="")
    subject=models.CharField(max_length=100,default="")
    teacher=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    fileType=models.CharField(max_length=100,default="")
    lastDate=models.CharField(max_length=100,default="")

    class Meta:
        """Meta definition for AssignmentAddModel."""

        verbose_name = 'AssignmentAddModel'
        verbose_name_plural = 'AssignmentAddModels'

    def __str__(self):
        """Unicode representation of AssignmentAddModel."""
        pass

    