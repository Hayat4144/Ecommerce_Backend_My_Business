from rest_framework import serializers
from .models import WhishlistItem


class CartItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WhishlistItem
        fields = "__all__"