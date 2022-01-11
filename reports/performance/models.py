from django.db import models

from reports.settings import TIME_ZONE

# Create your models here.
class ProjectReport(models.Model):
    Id = models.IntegerField(primary_key=True)
    ProjectName = models.CharField(max_length=50)
    ProjectOwner = models.CharField(max_length=20)
    Task = models.CharField(max_length=50)
    AssignTo = models.CharField(max_length=20)
    EstimatedTime = models.TimeField()
    ProductiveTime = models.TimeField()
    Billing = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.ProjectName

class TaskReport(models.Model):
    Project_Id = models.ForeignKey(ProjectReport, on_delete=models.CASCADE)
    Tasks = models.CharField(max_length=100)
    TaskAssignTo = models.CharField(max_length=20)
    EstimatedTime = models.TimeField()
    ProductiveTime = models.TimeField()
    Billing = models.DecimalField(max_digits=6, decimal_places=2)    

    def __str__(self):
        return self.Tasks    
