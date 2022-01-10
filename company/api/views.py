from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework import generics
from . serializers import EmployeeSerializer, TrackingSerializer 
from . models import Employee, Tracking

# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer

class TrackingList(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

class TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracking
    serializer_class = TrackingSerializer    
