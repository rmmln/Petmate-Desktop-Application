from django.urls import path
from .views import BasicInfoListCreateView, BasicInfoRetrieveUpdateDestroyView

urlpatterns = [
    path('patients/', BasicInfoListCreateView.as_view(), name='patients-list-create'),
    path('patients/<int:pk>/', BasicInfoRetrieveUpdateDestroyView.as_view(), name='patients-detail'),
]
