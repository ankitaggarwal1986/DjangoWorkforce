from django.db import models

# Create your models here.
class Customer(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    ContactNumber = models.IntegerField()

    def __str__(self):
        return self.Name

class Product(models.Model):
    P_Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()

    def __str__(self):
        return self.Name

class Transection(models.Model):
    CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    SalePrice = models.IntegerField()

    def __int__(self):
        return self.SalePrice
            
