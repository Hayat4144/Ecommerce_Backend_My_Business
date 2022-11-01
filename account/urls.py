from django.urls import path
from . import views

urlpatterns = [
    path('api/signup', views.Signup),
    path('api/signin', views.Signin),
    path('api/forget/password' , views.ForgetPassword)
]