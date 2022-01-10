from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from . serializers import CustomerSerializer,ProductSerializer,TransectionSerializer
from . models import Product, Customer, Transection
# Create your views here.

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer
    serializer_class = CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer

class TransectionList(generics.ListCreateAPIView):
    queryset = Transection.objects.all()
    serializer_class = TransectionSerializer

class TransectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transection
    serializer_class = TransectionSerializer
            
        