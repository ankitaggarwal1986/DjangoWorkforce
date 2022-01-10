from django.db import models

# Create your models here.
class Employee(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Tracking(models.Model):
    EmpId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ActivityHours=models.PositiveIntegerField()
    IdleTime = models.PositiveIntegerField()
    OfficeHours=models.PositiveIntegerField()

    def __int__(self):
        return self.EmpId

    #def TotalHours(self):
        #return (self.ActivityHours+self.IdleTime)                 
