# from django.shortcuts import render
from itertools import product
from rest_framework.decorators import api_view
from .models import Category, Product, Product_item
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductSerializerByCategory, CategorySerializer, ProductItemSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.http import JsonResponse
from account.models import User
import jwt
from Backend.settings import SECRET_KEY
import json


# Create your views here.


@api_view(['GET'])
def get_all_product(APIView):
    renderer_classes = [JSONRenderer]
    product_data = Product.objects.all()
    serialezer = ProductSerializer(instance=product_data, many=True)
    return Response(serialezer.data)


@api_view(['POST'])
def get_product_By_id(request, id):
    renderer_classes = [JSONRenderer]
    product_data = Product.objects.filter(id=id)
    print(product_data)
    serialzer = ProductSerializer(instance=product_data, many=True)
    return Response(serialzer.data)


@api_view(['GET'])
def get_all_categories(APIView):
    render_classes = [JSONRenderer]
    category_data = Category.objects.all()
    serializer = CategorySerializer(instance=category_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_category(request, name):
    renderer_classes = [JSONRenderer]
    product_data = Product.objects.filter(categories__name__istartswith=name)
    print(product_data)
    serializer = ProductSerializer(instance=product_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, id):
    render_classes = [JSONRenderer]
    product_item_data = Product_item.objects.filter(product_id=id)
    serialzer = ProductItemSerializer(instance=product_item_data, many=True)
    return Response(serialzer.data)


# @api_view(['POST'])
# def add_to_cart(request):
#     render_classess = [JSONRenderer]
#     token = request.headers.get('Authorization')
#     cart_data = json.loads(request.body)
#     UserId = jwt.decode(token.split()[1], SECRET_KEY, algorithms=['HS256'])['user_id']
#     checkUserValid = User.objects.filter(id=UserId).values()[0]['id']
#     if checkUserValid is None:
#         return Response({"error": "Invalid UUID"})

#     # fetch cart data if not created create it.
#     cart, created = shopping_cart.objects.get_or_create(user_id=checkUserValid)
#     # add product item to cart
#     # print(cart.id)
#     # CartItem = shopping_cart_item.objects.create(cart_id=cart.id,quantity=cart_data['quantity'],product_item_id=cart_data['product_item_id'])
#     print(cart_data['product_item_id'])
#     CartItem = shopping_cart_item.objects.create(product_item_id=cart_data['product_item_id'],quantity=cart_data['quantity'])
#     print(CartItem)
#     return JsonResponse({'data':f"The {CartItem} has been added successfully."})

# @api_view(['GET'])
# def get_cart_item(request):
#     render_classesss = [JSONRenderer]
#     token = request.headers.get('Authorization')
#     UserId = jwt.decode(token.split()[1],SECRET_KEY,algorithms=['HS256'])['user_id']
#     Cart_data = shopping_cart_item.objects.filter(cart__user=UserId)
#     print(Cart_data)
#     serializer = CartItemSerialzer(instance=Cart_data,many=True)
#     print(serializer.data)
#     return Response(serializer.data)


# @api_view(["POST"])
# def add_to_whishlist(request):
#     render_classess = [JSONRenderer]
#     whishlist_data = json.loads(request.body)
#     print(whishlist_data['product_item_id'])
#     token = request.headers.get('Authorization')
#     UserId = decode_token(token)
#     CheckValidUser = User.objects.filter(id=UserId).values()[0]['id']
#     if CheckValidUser is  None:
#         return JsonResponse({"error":"Usedr doesn't exist."})
#     whishlist,created = Whishlist.objects.get_or_create(user_id=UserId)
#     print(whishlist.get_whishlist_id())
#     print('hello')
#     return Response('hello')
#     # WhishlistItem = Whishlist_item.objects.create(whishlist_id=whishlist.get_whishlist_id(),product_item_id=whishlist_data['product_item_id'])
#     # return JsonResponse({"data":f"The {WhishlistItem} has been added to Wishlist Successfully."})