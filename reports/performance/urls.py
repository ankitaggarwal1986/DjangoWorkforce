from . import views
from django.urls import path
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('api/projectreport/', views.ProjectReportList.as_view()),
    path('api/projectdetail/<int:pk>',views.ProjectReportDetail.as_view()),
    path('api/taskreport/', views.TaskReportList.as_view()),
    path('api/taskdetail/<int:pk>',views.TaskReportDetail.as_view()),
]
