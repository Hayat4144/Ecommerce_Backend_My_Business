from django.urls import path
from . import views

urlpatterns = [
    path('api/stock',views.get_stock)
]