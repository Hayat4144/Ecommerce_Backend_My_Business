
from rest_framework import serializers
from .models import Category, Product, Product_item


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
    size_name = serializers.CharField(source='size_id')
    colour_name = serializers.CharField(source='colour_id')
    material_name = serializers.CharField(source='material_id')
    product_name = serializers.CharField(source='product_id')

    class Meta:
        model = Product_item
        fields = ('id', 'sku', 'price', 'size_name',
                  'colour_name', 'material_name', 'product_name')


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = shopping_cart
#         fields = "__all__"


# class CartItemSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = shopping_cart_item
#         fields = "__all__"

# class WhislistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Whishlist
#         fields = "__all__"

# class WishListItemsSeriailizer(serializers.ModelSerializer):
#     class Meta:
#         model = Whishlist_item
#         fields = "__all__"

        