from django.shortcuts import render
from .models import address
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .serializers import AddressSerializer


@api_view(['POST'])
def create_address(request):
    address_data = json.loads(request.body)
    serializer = AddressSerializer(data=address_data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    else:
        return Response({'error': serializer.errors[0]})

@api_view(['GET'])
def get_address(request):
    address_data = address.objects.all()
    serializer = AddressSerializer(instance=address_data,many=True)
    return Response({"data":serializer.data})


@api_view(['POST'])
def update_address(request):
    address_data = json.loads(request.body)
    UserId = address.objects.get(user=address_data['user'])
    print(UserId)
    serializer = AddressSerializer(instance=UserId,data =address_data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data})
    else:
        return Response({"error":serializer.errors})