from django.urls import path
from . import views

urlpatterns  = [

    path('api/create/address',views.create_address),
    path('api/update/address',views.update_address),
    path('api/get/address',views.get_address),
]