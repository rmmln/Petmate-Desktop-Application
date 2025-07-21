from rest_framework import serializers
from .models import basicInfo

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = basicInfo
        fields = '__all__'
