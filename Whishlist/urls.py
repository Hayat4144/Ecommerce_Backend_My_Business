from django.urls import path
from . import views

urlpatterns = [ 
    path('api/user/add_to_whishlist',views.add_to_whishlist)
]