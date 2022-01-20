from os import access
from django.shortcuts import render
#from django.db.models.query import QuerySet
#from rest_framework import serializers
#from rest_framework.serializers import Serializer
from rest_framework import generics
from . serializers import EmployeeSerializer, TrackingSerializer 
from . models import Employee, Tracking
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("request")
        return Response({'success': "Hurray you are authenticated"})
'''
class Demodetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'success': "yes you are authenticated"})
'''
class RegisterdView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "status":"success", 
                'user_id':user.id,
                'refresh':str(refresh), 
                'access':str(refresh.access_token)
                        
            })        

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
