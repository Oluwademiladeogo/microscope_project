from django.db import models


# Create your models here.
class Specimen(models.Model):
    username = models.CharField(max_length=100)
    specimen_name = models.CharField(max_length=100)
    microscope_size = models.FloatField()
    magnification = models.FloatField()
    actual_size = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.specimen_name} by {self.username}"

    def calculate_actual_size(self):
        """Calculate actual size from microscope size and magnification"""
        return self.microscope_size / self.magnification
