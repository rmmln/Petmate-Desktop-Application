from rest_framework import generics
from .models import basicInfo
from .serializers import BasicInfoSerializer

# GET all & POST new patient
class BasicInfoListCreateView(generics.ListCreateAPIView):
    queryset = basicInfo.objects.all()
    serializer_class = BasicInfoSerializer

# GET / PUT / DELETE single patient by id
class BasicInfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = basicInfo.objects.all()
    serializer_class = BasicInfoSerializer
