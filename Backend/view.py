# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentList(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
