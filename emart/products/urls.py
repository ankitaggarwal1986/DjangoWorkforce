from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>', views.CustomerDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
    path('transection/', views.TransectionList.as_view()),
    path('transection/<int:pk>', views.TransectionDetail.as_view()),
]
