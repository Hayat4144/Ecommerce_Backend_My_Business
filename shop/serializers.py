
from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category_name= serializers.CharField(source='categories')
    class Meta:
        model= Product
        fields = ('id','name','descriptions','regular_price','sales_price','image','available_colors','category_name')


class ProductSerializerByCategory(serializers.ModelSerializer):
    # category_name= serializers.CharField(source='categories')
    class Meta:
        model= Product
        fields = ('id','name','descriptions','regular_price','sales_price','image','available_colors')


