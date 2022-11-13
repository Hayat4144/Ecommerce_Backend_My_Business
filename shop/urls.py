from operator import imod
from django.urls import path 
from . import views

urlpatterns = [
    path('api/get_all_product', views.get_all_product),
    path('api/get_all_categories', views.get_all_categories),
    path('api/get_product_by_category/<str:name>/', views.get_product_by_category),
    # path('api/get_attribute', views.get_attribute),
    ]
