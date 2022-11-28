from django.urls import path
from . import views

urlpatterns = [ 
    path('api/user/add_to_whishlist',views.add_to_whishlist),
    path('api/user/get_all_whishlist',views.get_all_wishlistItem),
    path('api/user/delete_whishlist',views.delete_wishlistItem),
]