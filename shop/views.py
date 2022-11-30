# from django.shortcuts import render
from itertools import product
from rest_framework.decorators import api_view
from .models import Category, Product, Product_item ,product_attribute
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductSerializerByCategory, CategorySerializer, ProductItemSerializer ,Product_attribute_Serializer 
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

@api_view(["POST"])
def productitem_attribute(request):
    renderer_classes = [JSONRenderer]
    client_data = json.loads(request.body)
    data = product_attribute.objects.filter(productItem__product_id=client_data['product_id'])
    serializer = Product_attribute_Serializer(instance=data ,many=True)
    return Response(serializer.data)