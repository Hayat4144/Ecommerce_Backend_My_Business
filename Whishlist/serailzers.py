from rest_framework import serializers
from .models import WhishlistItem


class WhishlistItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WhishlistItem
        fields = "__all__"