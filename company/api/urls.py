from django.urls import path
#from django.urls.resolvers import URLPattern
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('employee/',views.EmployeeList.as_view()),
    path('employee/<int:pk>',views.EmployeeDetail.as_view()),
    path('tracking/',views.TrackingList.as_view()),
    path('tracking/<int:pk>',views.TrackingDetail.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='create_token'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('demoview/', views.DemoView.as_view()),
    path('register/',views.RegisterdView.as_view())
    #path('demodetail/', views.Demodetail.as_view()),

]