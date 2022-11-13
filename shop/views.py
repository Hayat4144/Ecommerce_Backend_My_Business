# from django.shortcuts import render
from itertools import product
from rest_framework.decorators import api_view
from .models import Category, Product
from rest_framework.response import Response
from .serializers import ProductSerializer , ProductSerializerByCategory ,CategorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
# Create your views here.




@api_view(['GET'])
def get_all_product(APIView):
    renderer_classes = [JSONRenderer]
    product_data = Product.objects.all()
    serialezer = ProductSerializer(instance=product_data , many=True)
    return Response(serialezer.data)



@api_view(['GET'])
def get_all_categories(APIView):
    render_classes = [JSONRenderer]
    category_data = Category.objects.all() 
    serializer = CategorySerializer(instance = category_data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_by_category(request,name):
    renderer_classes = [JSONRenderer]
    print('ok')
    print(name)
    product_data = Product.objects.filter(categories__name__istartswith=name)
    serializer = ProductSerializer(instance=product_data, many=True)
    return Response(serializer.data)
