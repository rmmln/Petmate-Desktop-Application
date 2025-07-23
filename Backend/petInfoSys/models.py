from django.db import models

# Create your models here.
class basicInfo(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    detailedAddress = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    emergencyNumber = models.CharField(max_length=255)

class Pet(models.Model):
    owner = models.ForeignKey(
        basicInfo,
        on_delete=models.CASCADE,  # pag nabura owner, burahin din pets niya
        related_name='pets'       # para ma-access mo: owner.pets.all()
    )
    petName = models.CharField(max_length=255)
    petColor = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)   # pwede mo rin gawing choices kung gusto