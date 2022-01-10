from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('Employee/',views.EmployeeList.as_view()),
    path('Employee/<int:pk>',views.EmployeeDetail.as_view()),
    path('Tracking/',views.TrackingList.as_view()),
    path('Tracking/<int:pk>',views.TrackingDetail.as_view())

]