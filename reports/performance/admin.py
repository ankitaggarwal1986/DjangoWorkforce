from django.contrib import admin

from performance.models import ProjectReport, TaskReport

# Register your models here.
MyModels=[ProjectReport, TaskReport]
admin.site.register(MyModels)