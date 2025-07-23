from rest_framework import generics
from .models import basicInfo,Pet
from .serializers import BasicInfoSerializer, PetSerializer

# GET all & POST new patient
class BasicInfoListCreateView(generics.ListCreateAPIView):
    queryset = basicInfo.objects.all()
    serializer_class = BasicInfoSerializer

# GET / PUT / DELETE single patient by id
class BasicInfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = basicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class PetListCreateView(generics.ListCreateAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        owner_id = self.request.query_params.get('owner_id')
        if owner_id:
            return Pet.objects.filter(owner_id=owner_id)
        return Pet.objects.all()


class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer