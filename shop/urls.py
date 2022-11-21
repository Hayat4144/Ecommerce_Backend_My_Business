from operator import imod
from django.urls import path 
from . import views

urlpatterns = [
    path('api/get_all_product', views.get_all_product),
    path('api/get_all_categories', views.get_all_categories),
    path('api/get_product_by_category/<str:name>/', views.get_product_by_category),
    path('api/get_product/<uuid:id>/', views.get_product_By_id),
    path('api/get_product/details/<uuid:id>/', views.get_product_details),
    path('api/add_to_cart_item', views.add_to_cart),
    path('api/get_cart_item', views.get_cart_item),
    # path('api/get_attribute', views.get_attribute),
    ]
