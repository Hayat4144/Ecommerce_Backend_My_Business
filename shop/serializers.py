
from rest_framework import serializers
from .models import Category, Product, Product_item  ,product_attribute


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='categories')

    class Meta:
        model = Product
        fields = ('id', 'name', 'descriptions',
                  'regular_price', 'image', 'category_name')


class ProductSerializerByCategory(serializers.ModelSerializer):
    # category_name= serializers.CharField(source='categories')
    class Meta:
        model = Product
        fields = ('id', 'name', 'descriptions', 'regular_price',
                  'sales_price', 'image', 'available_colors')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductItemSerializer(serializers.ModelSerializer):
   
    product_name = serializers.CharField(source='product_id')

    class Meta:
        model = Product_item
        fields = ('id', 'sku', 'price','product_name')


class Product_attribute_Serializer(serializers.ModelSerializer):
  
    class Meta:
        model = product_attribute
        fields = '__all__'
        depth= 1
        