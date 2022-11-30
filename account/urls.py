from django.urls import path
from . import views

urlpatterns = [
    path('api/signup', views.Signup),
    path('api/user/reset/password',views.reset_password),
    path('api/Change/password' , views.ChangePassword),
    path('api/user/reset/password/done',views.password_reset_done),
]