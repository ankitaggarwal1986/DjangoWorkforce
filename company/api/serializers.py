from django.db.models import fields
from rest_framework import serializers
from . models import Employee, Tracking

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = "__all__"        