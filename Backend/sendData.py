import os
import django
import sys

# Add Backend to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Set Django settings and initialize
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from petInfoSys.models import basicInfo

def save_data_to_db(firstName, lastname, phoneNumber, province, city, barangay, detailedAddress, email, emergencyNumber):
    new_entry = basicInfo(
        firstName=firstName,
        lastname=lastname,
        phoneNumber=phoneNumber,
        province=province,
        city=city,
        barangay=barangay,
        detailedAddress=detailedAddress,
        email=email,
        emergencyNumber=emergencyNumber
    )
    new_entry.save()
