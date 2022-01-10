from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework import generics
from . serializers import ProjectSerializer, TaskSerializer
from . models import Project, Task

# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project
    serializer_class = ProjectSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task
    serializer_class = TaskSerializer           