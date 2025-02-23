
from django.db import models

class Appointment(models.Model):
    owner_name = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    cell_No = models.CharField(max_length=255)

    def __str__(self):
        return self.owner_name
