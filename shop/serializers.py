
from rest_framework import serializers
from .models import Category, Product ,Produt_item


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

class ProductItemSerializer(serializers.ModelSerializer):  
    size_name = serializers.CharField(source ='size_id')
    colour_name = serializers.CharField(source ='colour_id')
    material_name = serializers.CharField(source ='material_id')
    product_name = serializers.CharField(source ='product_id')
    class Meta:
        model = Produt_item
        fields = ('id','sku','price','stock','size_name','colour_name','material_name' ,'product_name')
     