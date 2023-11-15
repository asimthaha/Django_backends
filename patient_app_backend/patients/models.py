from django.db import models

# Create your models here.
class PatientAdd(models.Model):
    """Model definition for PatientAdd."""

    name=models.CharField(max_length=100,default="")
    phone=models.CharField(default="", max_length=100)
    address=models.CharField(default="", max_length=100)
    email=models.CharField(default="", max_length=100)
    pincode=models.CharField(default="", max_length=100)

    class Meta:
        """Meta definition for PatientAdd."""

        verbose_name = 'PatientAdd'
        verbose_name_plural = 'PatientAdds'

    def __str__(self):
        """Unicode representation of PatientAdd."""
        pass
