from django.db.models import fields
from . models import Product, Transection, Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields ='__all__'

class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transection
        fields ='__all__'