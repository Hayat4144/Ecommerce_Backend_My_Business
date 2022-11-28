from rest_framework import serializers
from .models import CartItem ,UserCart


class CartItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"