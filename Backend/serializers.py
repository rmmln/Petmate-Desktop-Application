
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['owner_name', 'pet_name', 'species', 'breed', 'cell_No']
