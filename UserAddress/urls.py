
from django.urls import path
from  . import views

urlpatterns = [ 
            path('api/address', views.get_address),
            path('api/create/address',views.Save_address_data),
        ]
