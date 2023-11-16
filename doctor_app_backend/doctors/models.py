from django.db import models

# Create your models here.
class DoctorAddModel(models.Model):
    """Model definition for DoctorAddModel."""

    name=models.CharField(max_length=100, default="")
    qualification=models.CharField(max_length=100, default="")
    specialization=models.CharField(max_length=100, default="")
    address=models.CharField(max_length=100, default="")
    department=models.CharField(max_length=100, default="")
    salary=models.CharField(max_length=100, default="")

    class Meta:
        """Meta definition for DoctorAddModel."""

        verbose_name = 'DoctorAddModel'
        verbose_name_plural = 'DoctorAddModels'

    def __str__(self):
        """Unicode representation of DoctorAddModel."""
        pass
