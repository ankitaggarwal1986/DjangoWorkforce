from django.contrib import admin
from . models import Project, Task

# Register your models here.
MyModels = [Project, Task]
admin.site.register(MyModels)
