from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

@api_view(["GET"])
def get_stock(request):
    return JsonResponse('djf',safe=False)