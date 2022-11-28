from django.urls import path
from .views import add_to_cart ,get_all_cart_item,delete_cart_item, update_cart_item

urlpatterns = [
    path('api/user/add_to_cart',add_to_cart),
    path('api/user/get_cart_item',get_all_cart_item),
    path('api/user/delete_cart_item',delete_cart_item),
    path('api/user/update_cart_item',update_cart_item),
]
