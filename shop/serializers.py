
from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category_name= serializers.CharField(source='categories')
    class Meta:
        model= Product
        fields = ('id','name','descriptions','regular_price','image','category_name')


class ProductSerializerByCategory(serializers.ModelSerializer):
    # category_name= serializers.CharField(source='categories')
    class Meta:
        model= Product
        fields = ('id','name','descriptions','regular_price','sales_price','image','available_colors')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ('id','name')