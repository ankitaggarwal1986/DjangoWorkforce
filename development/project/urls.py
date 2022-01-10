from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>',views.ProjectDetail.as_view()),
    path('task/',views.TaskList.as_view()),
    path('task/<int:pk>',views.TaskDetail.as_view()),

]