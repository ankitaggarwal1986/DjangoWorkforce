from django.db import models


# Create your models here.
class Project(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    ProjectOwner = models.CharField(max_length=100)
    EstimatedCost = models.FloatField()

    def __str__(self):
        return self.Name

class Task(models.Model):
    ProjectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    CreatedAt= models.DateField()
    Complete = models.BooleanField()

    def __int__(self):
        return self.ProjectId        