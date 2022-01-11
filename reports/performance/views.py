from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from . serializers import ProjectReportSerializer, TaskReportSerializer
from . models import ProjectReport, TaskReport

# Create your views here.
class ProjectReportList(generics.ListCreateAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer

class ProjectReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectReport
    serializer_class = ProjectReportSerializer    

class TaskReportList(generics.ListCreateAPIView):
    queryset = TaskReport.objects.all()
    serializer_class = TaskReportSerializer

class TaskReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskReport
    serializer_class = TaskReportSerializer    



