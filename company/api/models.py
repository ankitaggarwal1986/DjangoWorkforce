from django.db import models
from django.db.models.fields import Field, IPAddressField

# Create your models here.
class Employee(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    #LastName = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)

    #class Meta:
     #   unique_together =(('Name','LastName'))

    def __str__(self):
        return self.Name

class Tracking(models.Model):
    EmpId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ActivityHours=models.PositiveIntegerField()
    IdleTime = models.PositiveIntegerField()

    def __int__(self):
        return self.EmpId

    #def TotalHours(self):
        #return (self.ActivityHours+self.IdleTime)                 
