from logging import raiseExceptions
from django.shortcuts import render
from rest_framework.response import Response
from .admin import user_address, Country, address
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import  AdressSerializer
import json
from rest_framework import status
from django.utils.html import escape

# Create your views here

@api_view(['GET'])
def get_address(APIView):
    renderer_classes = [JSONRenderer]
    text = "hello <p>your Name </p> ;' '</script>9"
    encoded_html= escape(text)
    address_data = address.objects.all()
    serializer = AdressSerializer(instance = address_data,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def Save_address_data(request):
    renderer_classes = [JSONRenderer]
    address_data = json.loads(request.body)
    # escape html characters to prevent xss
    for key, value,in address_data.items():
        address_data[key] = escape(value)
    
    serializer = AdressSerializer(data= address_data)
    serializer.is_valid(raise_exception =True)
    serializer.save()
    return Response(serializer.data, status= status.HTTP_200_OK)
