from django.contrib import admin
from . models import Customer, Product, Transection

# Register your models here.
MyModels = [Customer, Product, Transection]
admin.site.register(MyModels)
